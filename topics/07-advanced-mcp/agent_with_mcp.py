"""Topic 07 — Agent driving a real MCP server (runnable demo).

The other Topic 06/07 demos show the raw protocol (connect, list, call). This one closes the loop:
a real Claude agent USES an external MCP server's tools through the vendor-neutral tool loop —
the exact pattern behind "run this app against any project to create PRs, edit files, deploy…".

    MCP server (filesystem / github / …)  ──►  core.MCPClient  ──►  ToolSpec + handlers
                                                                        │
                                       Agent(provider, system, tools) ──┘ ──► run_tools loop

Graceful degradation (so it always does *something* useful):
  • filesystem MCP (real file actions on a target project)  — if `npx` (Node) is installed
  • else the repo's echo server                              — always available
  • with ANTHROPIC_API_KEY → a live agent decides which tools to call
  • without a key          → a no-LLM bridge check (tools discovered + one direct call)

Run:  python topics/07-advanced-mcp/agent_with_mcp.py
Needs: pip install -e ".[mcp]"   ·   .env with ANTHROPIC_API_KEY (optional)   ·   Node/npx (optional)
"""

from __future__ import annotations

import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

# LLMs emit Unicode (curly quotes, non-breaking hyphens); make stdout safe on cp1252 consoles.
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover — older/redirected streams
    pass

from core import (  # noqa: E402
    ChatMessage,
    MCPClient,
    ServerSpec,
    ToolCall,
    get_provider,
    get_settings,
)


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def pick_server() -> tuple[ServerSpec, str]:
    """Choose the best available MCP server and a task that exercises it."""
    if shutil.which("npx"):
        # Scope filesystem access to THIS repo (least privilege) and ask a read-only question.
        spec = ServerSpec(
            name="filesystem",
            transport="stdio",
            command="npx",
            args=["-y", "@modelcontextprotocol/server-filesystem", str(ROOT)],
        )
        task = (
            "List the entries in the repository root, then read README.md and give me a two-sentence "
            "summary of what this project is. Use the available tools."
        )
        return spec, task
    # Fallback: the repo's own server — proves the same loop with no Node, no auth.
    spec = ServerSpec(
        name="ai-os-echo",
        transport="stdio",
        command=sys.executable,
        args=[str(ROOT / "mcp" / "echo_server" / "server.py")],
    )
    task = "Use the tools to compute 15 + 27 and to reverse the text 'AI-OS'. Report both results."
    return spec, task


def main() -> None:
    settings = get_settings()
    spec, task = pick_server()
    print(f"MCP server: {spec.name}  (transport={spec.transport})")

    with MCPClient([spec]) as mc:
        hr("1) DISCOVER — tools the server exposes (adapted to vendor-neutral ToolSpec)")
        for t in mc.tools:
            print(f"  - {t.name}: {(t.description or '').splitlines()[0][:70]}")

        if not settings.has_api_key:
            hr("2) No ANTHROPIC_API_KEY — running a bridge check instead of a live agent")
            first = mc.tools[0]
            print(f"  Set ANTHROPIC_API_KEY in .env to let an agent choose tools autonomously.")
            print(f"  Direct-call proof — invoking {first.name} through its handler:")
            sample = {"a": 15, "b": 27} if first.name.endswith("__add") else {"path": str(ROOT)}
            print(f"    {first.name}({sample}) -> {mc.handlers[first.name](sample)[:120]}")
            return

        hr("2) AGENT — Claude decides which MCP tools to call, the bridge runs them")
        provider = get_provider()
        system = (
            "You are a capable software engineer. Use the provided tools to inspect the project "
            "and answer precisely. Prefer tool results over guessing; never invent file contents."
        )
        # The composed form is Agent("mcp-worker", provider, system, tools=mc.tools,
        # handlers=mc.handlers).run(task). We call run_tools directly below only to trace each
        # tool call live (Agent.run wraps this exact call without the trace hook).
        print(f"  task: {task}\n")

        def trace(call: ToolCall) -> None:
            print(f"    -> calls {call.name}({call.input})")

        result = provider.run_tools(
            [ChatMessage("user", task)],
            tools=mc.tools,
            handlers=mc.handlers,
            system=system,
            model=settings.default_model,
            max_tokens=settings.max_tokens,
            on_tool_call=trace,
        )
        print(f"\n  final answer:\n  {result.final_text.strip().replace(chr(10), chr(10) + '  ')}")
        cost = provider.estimate_cost(result.usage, settings.default_model)
        print(
            f"\n  [tool calls={len(result.steps)}  iterations={result.iterations}]"
            f"  [tokens in={result.usage.input_tokens} out={result.usage.output_tokens}]"
            f"  [est. cost=${cost:.6f}]"
        )

    hr("Done — a real agent used a real MCP server through the shared tool loop")
    print("  Same pattern with github/docs/deploy servers = PRs, docs, deployments on any project.")


if __name__ == "__main__":
    main()
