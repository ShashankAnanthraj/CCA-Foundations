"""MCP client bridge — adapt external MCP-server tools into the vendor-neutral tool loop.

Purpose:    Connect (client-side) to one or more MCP servers, discover their tools, and expose each
            as a `core.tools.ToolSpec` + a synchronous handler — so ANY provider's `run_tools` loop
            (Topic 05) can call GitHub / filesystem / docs / deploy / query-opt MCP tools with zero
            changes to the kernel. This is the piece that turns "we host an MCP server" (Topic 06/07)
            into "our agents USE external MCP servers."

Placement:  Lives in `core/` — next to the `ToolSpec` / `run_tools` contract it bridges — and NOT in
            the repo's `mcp/` folder. Reason: `mcp/` holds servers we AUTHOR; adding an
            `mcp/__init__.py` there would make the repo dir a regular package that SHADOWS the
            installed `mcp` SDK on `sys.path`. The `mcp` SDK is the open-protocol library, not a
            vendor LLM SDK, so importing it here does not violate ADR 0001 — and it is imported
            LAZILY so `import core` never pulls it in.

Design:     The MCP SDK is async; `run_tools` is synchronous. We run each session on a dedicated
            background event-loop thread and keep it open for the client's lifetime (so stdio
            subprocesses / stateful servers stay alive). Handlers marshal each call onto that loop
            via `run_coroutine_threadsafe` and block for the result — a clean async→sync boundary.

Usage:      with MCPClient.from_manifest(["filesystem"]) as mc:
                agent = Agent("dev", provider, system, tools=mc.tools, handlers=mc.handlers)
                agent.run("List the files and summarize the README.")

Depends on: mcp (`pip install -e ".[mcp]"`). stdlib: asyncio, threading, os, re, json, pathlib.
Security:   Least privilege — pass an `allow` filter to expose only the tools a role needs; secrets
            come from env via `${VAR}` expansion in the manifest, never inline (Constitution).
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable

from core.tools import ToolSpec

# Default manifest location (repo `mcp/`). `servers.json` is git-ignored (may reference secrets);
# `servers.example.json` is the committed template used as a fallback.
_MCP_DIR = Path(__file__).resolve().parents[1] / "mcp"
DEFAULT_MANIFEST = _MCP_DIR / "servers.json"
EXAMPLE_MANIFEST = _MCP_DIR / "servers.example.json"

_ENV_RE = re.compile(r"\$\{([A-Z0-9_]+)\}")
_TOOL_NAME_RE = re.compile(r"[^a-zA-Z0-9_-]")


# --------------------------------------------------------------------------- #
# Manifest → server specs
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class ServerSpec:
    """One MCP server declaration (a normalized row of the manifest)."""

    name: str
    transport: str = "stdio"  # "stdio" (local subprocess) | "http" (remote streamable HTTP)
    command: str | None = None
    args: list[str] = field(default_factory=list)
    env: dict[str, str] = field(default_factory=dict)
    url: str | None = None
    headers: dict[str, str] = field(default_factory=dict)
    note: str | None = None
    #: env vars referenced via ${VAR} in the manifest that were unset/empty at load time.
    missing_env: tuple[str, ...] = ()

    @property
    def startable(self) -> bool:
        """True if this repo can actually connect: has a command/url, and no unresolved ${ENV}.

        A ${VAR} that expanded to empty (e.g. AI_OS_TARGET_DIR unset) leaves a blank command/arg/url
        that would launch a broken server — treat that as NOT startable so callers fail loudly with
        a clear message (see `missing_env`) instead of spawning a doomed subprocess.
        """
        if self.missing_env:
            return False
        if self.transport == "stdio":
            return bool(self.command) and all(bool(a) for a in self.args)
        if self.transport == "http":
            return bool(self.url) and self.url.startswith(("http://", "https://"))
        return False


def _expand(value):
    """Recursively expand `${ENV_VAR}` references using the process environment."""
    if isinstance(value, str):
        return _ENV_RE.sub(lambda m: os.environ.get(m.group(1), ""), value)
    if isinstance(value, list):
        return [_expand(v) for v in value]
    if isinstance(value, dict):
        return {k: _expand(v) for k, v in value.items()}
    return value


def load_manifest(path: str | Path | None = None) -> dict[str, ServerSpec]:
    """Load the MCP server manifest → {name: ServerSpec}, expanding `${ENV}` placeholders.

    Falls back to `servers.example.json` when `servers.json` is absent. Raises if neither exists.
    """
    p = Path(path) if path else (DEFAULT_MANIFEST if DEFAULT_MANIFEST.exists() else EXAMPLE_MANIFEST)
    if not p.exists():
        raise FileNotFoundError(f"no MCP manifest at {p} (copy servers.example.json to servers.json)")
    raw = json.loads(p.read_text(encoding="utf-8"))
    servers = raw.get("mcpServers", {})
    out: dict[str, ServerSpec] = {}
    for name, cfg in servers.items():
        # Which ${VAR} placeholders in this server's config are unset/empty? (Before expansion.)
        referenced = set(_ENV_RE.findall(json.dumps(cfg)))
        missing = tuple(sorted(v for v in referenced if not os.environ.get(v)))
        cfg = _expand(cfg)
        out[name] = ServerSpec(
            name=name,
            transport=cfg.get("transport", "stdio"),
            command=cfg.get("command"),
            args=list(cfg.get("args", [])),
            env=dict(cfg.get("env", {})),
            url=cfg.get("url"),
            headers=dict(cfg.get("headers", {})),
            note=cfg.get("note"),
            missing_env=missing,
        )
    return out


# --------------------------------------------------------------------------- #
# The bridge
# --------------------------------------------------------------------------- #
def _result_text(result) -> str:
    """Flatten an MCP CallToolResult into a plain string for the tool loop."""
    parts = [getattr(c, "text", "") for c in getattr(result, "content", [])]
    text = " ".join(p for p in parts if p).strip()
    if not text:
        sc = getattr(result, "structuredContent", None)
        text = json.dumps(sc) if sc is not None else str(result)
    return ("Error: " + text) if getattr(result, "isError", False) else text


AllowFilter = Callable[[str], bool] | Iterable[str] | None


def _as_predicate(allow: AllowFilter) -> Callable[[str], bool]:
    if allow is None:
        return lambda _name: True
    if callable(allow):
        return allow
    allowed = set(allow)
    return lambda name: name in allowed


class MCPClient:
    """Connect to MCP servers and expose their tools as `ToolSpec` + sync handlers.

    Use as a context manager so sessions (and any stdio subprocesses) are cleaned up:

        with MCPClient(specs) as mc:
            provider.run_tools(msgs, tools=mc.tools, handlers=mc.handlers)

    `allow` narrows the exposed tools (least privilege for role agents): a predicate on the
    *un-namespaced* tool name, or an iterable of names to keep.
    """

    def __init__(
        self,
        servers: Iterable[ServerSpec],
        *,
        allow: AllowFilter = None,
        namespace: bool = True,
        call_timeout: float = 30.0,
        connect_timeout: float = 30.0,
    ) -> None:
        self._servers = [s for s in servers if s.startable]
        self._allow = _as_predicate(allow)
        self._namespace = namespace
        self._call_timeout = call_timeout
        self._connect_timeout = connect_timeout

        self.tools: list[ToolSpec] = []
        self.handlers: dict[str, Callable[[dict], str]] = {}
        self._bindings: dict[str, tuple] = {}  # exposed name -> (session, real_tool_name)

        self._loop: asyncio.AbstractEventLoop | None = None
        self._thread: threading.Thread | None = None
        self._ready = threading.Event()
        self._stop: asyncio.Event | None = None
        self._error: BaseException | None = None

    # -- construction helpers ---------------------------------------------- #
    @classmethod
    def from_manifest(
        cls,
        names: Iterable[str] | None = None,
        *,
        path: str | Path | None = None,
        **kwargs,
    ) -> "MCPClient":
        """Build a client from the manifest, optionally limited to `names` (default: all startable)."""
        manifest = load_manifest(path)
        if names is not None:
            absent = [n for n in names if n not in manifest]
            if absent:
                raise KeyError(f"servers not in manifest: {absent} (have: {list(manifest)})")
            specs = [manifest[n] for n in names]
            # Fail loudly if a REQUESTED server can't start (e.g. an env placeholder is unset),
            # rather than silently connecting to nothing.
            broken = [s for s in specs if not s.startable]
            if broken:
                detail = "; ".join(
                    f"{s.name} (set {', '.join(s.missing_env)})" if s.missing_env else f"{s.name} (no command/url)"
                    for s in broken
                )
                raise ValueError(f"MCP server(s) not startable — {detail}")
        else:
            specs = list(manifest.values())
        return cls(specs, **kwargs)

    # -- lifecycle ---------------------------------------------------------- #
    def __enter__(self) -> "MCPClient":
        self._thread = threading.Thread(target=self._run, name="mcp-client-loop", daemon=True)
        self._thread.start()
        if not self._ready.wait(timeout=self._connect_timeout):
            raise TimeoutError("timed out connecting to MCP server(s)")
        if self._error:
            raise self._error
        return self

    def __exit__(self, *exc) -> None:
        if self._loop and self._stop and self._loop.is_running():
            self._loop.call_soon_threadsafe(self._stop.set)
        if self._thread:
            self._thread.join(timeout=10)

    # -- background event loop --------------------------------------------- #
    def _run(self) -> None:
        try:
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)
            self._loop.run_until_complete(self._serve())
        except BaseException as exc:  # surface to __enter__
            self._error = exc
            self._ready.set()
        finally:
            if self._loop is not None:
                self._loop.close()

    async def _serve(self) -> None:
        """Open every session, publish their tools, then idle until __exit__ signals stop."""
        from contextlib import AsyncExitStack

        from mcp import ClientSession

        self._stop = asyncio.Event()
        try:
            async with AsyncExitStack() as stack:
                for spec in self._servers:
                    read, write = await self._open_transport(stack, spec)
                    session = await stack.enter_async_context(ClientSession(read, write))
                    await session.initialize()
                    listed = await session.list_tools()
                    for tool in listed.tools:
                        if not self._allow(tool.name):
                            continue
                        exposed = self._exposed_name(spec.name, tool.name)
                        self.tools.append(
                            ToolSpec(
                                name=exposed,
                                description=tool.description or "",
                                input_schema=tool.inputSchema or {"type": "object", "properties": {}},
                            )
                        )
                        self._bindings[exposed] = (session, tool.name)
                        self.handlers[exposed] = self._make_handler(exposed)
                self._ready.set()  # setup done → __enter__ may proceed
                await self._stop.wait()  # keep sessions alive until __exit__
        except BaseException as exc:
            self._error = exc
            self._ready.set()
            raise

    @staticmethod
    async def _open_transport(stack, spec: ServerSpec):
        """Enter the right transport context and return its (read, write) streams."""
        if spec.transport == "stdio":
            from mcp import StdioServerParameters
            from mcp.client.stdio import stdio_client

            env = {**os.environ, **spec.env} if spec.env else None
            params = StdioServerParameters(command=spec.command, args=spec.args, env=env)
            transport = await stack.enter_async_context(stdio_client(params))
        elif spec.transport == "http":
            from mcp.client.streamable_http import streamablehttp_client

            transport = await stack.enter_async_context(
                streamablehttp_client(spec.url, headers=spec.headers or None)
            )
        else:
            raise ValueError(f"unknown transport {spec.transport!r} for server {spec.name!r}")
        # stdio yields (read, write); http yields (read, write, get_session_id) — take the streams.
        return transport[0], transport[1]

    # -- tool plumbing ------------------------------------------------------ #
    def _exposed_name(self, server: str, tool: str) -> str:
        if not self._namespace:
            return tool
        safe = _TOOL_NAME_RE.sub("_", server)
        return f"{safe}__{tool}"[:64]  # Anthropic tool names: [a-zA-Z0-9_-]{1,64}

    def _make_handler(self, exposed: str) -> Callable[[dict], str]:
        def handler(inp: dict) -> str:
            session, real = self._bindings[exposed]
            if self._loop is None:
                return "Error: MCP client is not connected"
            fut = asyncio.run_coroutine_threadsafe(session.call_tool(real, inp or {}), self._loop)
            try:
                return _result_text(fut.result(timeout=self._call_timeout))
            except Exception as exc:  # tool failures are data for the loop, not crashes
                return f"Error: {exc}"

        return handler
