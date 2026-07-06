"""Shared pytest fixtures — a key-free FakeProvider so the whole suite runs offline.

Every test in this suite is deterministic and needs no API key: LLM behaviour is exercised through
`FakeProvider`, a tiny `core.providers.LLMProvider` subclass with canned responses. The only test
that touches the network-shaped path (the MCP bridge) spawns the repo's own echo server over stdio,
which is pure Python — still no key.
"""

from __future__ import annotations

import json
import pathlib
import sys

import pytest

# Make `import core` work when running `pytest` from the repo root without an editable install.
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.providers import ChatMessage, LLMProvider, LLMResponse, Usage  # noqa: E402
from core.tools import ToolCall, ToolLoopResult  # noqa: E402


class FakeProvider(LLMProvider):
    """Deterministic provider for offline tests — no SDK, no network, no key.

    - `chat` echoes the last user message with a fixed usage, so callers can assert token accounting.
    - `structured_chat` picks the first schema enum value whose label appears in the prompt (drives
      `router`), else the first enum / a minimal object — always valid against the schema shape used
      in this repo.
    - `run_tools` invokes every provided handler once and concatenates results (drives Agent-with-tools).
    """

    pricing = {"fake-1": (1.0, 2.0)}  # $/1M (input, output) — for estimate_cost assertions
    DEFAULT_MODEL = "fake-1"

    def __init__(self, reply: str | None = None) -> None:
        self._reply = reply

    def chat(
        self,
        messages,
        *,
        system=None,
        model=None,
        max_tokens=None,
        thinking=False,
        effort=None,
        cache=False,
    ) -> LLMResponse:
        norm = self._normalize(messages)
        last_user = next((m["content"] for m in reversed(norm) if m["role"] == "user"), "")
        text = self._reply if self._reply is not None else f"echo: {last_user}"
        return LLMResponse(
            text=text,
            model=model or self.DEFAULT_MODEL,
            stop_reason="end_turn",
            usage=Usage(input_tokens=10, output_tokens=5),
        )

    def stream_chat(self, messages, *, system=None, model=None, max_tokens=None):
        yield from (self.chat(messages, system=system, model=model, max_tokens=max_tokens).text,)

    def count_tokens(self, messages, *, system=None, model=None) -> int:
        return sum(len(m["content"].split()) for m in self._normalize(messages))

    def structured_chat(self, messages, *, schema, system=None, model=None, max_tokens=None):
        norm = self._normalize(messages)
        prompt = " ".join(m["content"] for m in norm).lower()
        obj: dict = {}
        for key, spec in schema.get("properties", {}).items():
            enum = spec.get("enum")
            if enum:
                obj[key] = next((v for v in enum if str(v).lower() in prompt), enum[0])
            elif spec.get("type") == "array":
                obj[key] = []
            else:
                obj[key] = ""
        resp = LLMResponse(json.dumps(obj), model or self.DEFAULT_MODEL, "end_turn", Usage(8, 4))
        return obj, resp

    def run_tools(
        self,
        messages,
        *,
        tools,
        handlers,
        system=None,
        model=None,
        max_tokens=None,
        max_iters=5,
        on_tool_call=None,
    ) -> ToolLoopResult:
        steps: list[ToolCall] = []
        outputs: list[str] = []
        for i, tool in enumerate(tools):
            call = ToolCall(id=f"t{i}", name=tool.name, input={})
            steps.append(call)
            if on_tool_call:
                on_tool_call(call)
            handler = handlers.get(tool.name)
            outputs.append(handler({}) if handler else f"(no handler {tool.name})")
        return ToolLoopResult(" | ".join(outputs), Usage(12, 6), steps, 1)


@pytest.fixture(autouse=True)
def _clear_settings_cache():
    """`core.config.get_settings` is `lru_cache`d; reset it around every test so env patches apply."""
    from core.config import get_settings

    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


@pytest.fixture
def fake_provider() -> FakeProvider:
    return FakeProvider()


@pytest.fixture
def make_message():
    return ChatMessage
