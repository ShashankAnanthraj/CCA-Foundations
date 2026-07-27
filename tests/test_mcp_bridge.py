"""core.mcp_client.MCPClient — the async→sync bridge, exercised against the repo's echo server.

Integration test: spawns `mcp/echo_server/server.py` over stdio (pure Python, no API key). Skips if
the `mcp` SDK is not installed so the base suite still passes.
"""

from __future__ import annotations

import pathlib
import sys

import pytest

pytest.importorskip("mcp")  # needs: pip install -e ".[mcp]"

from core.mcp_client import MCPClient, ServerSpec  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
ECHO = ROOT / "mcp" / "echo_server" / "server.py"


@pytest.fixture
def echo_spec() -> ServerSpec:
    return ServerSpec(name="ai-os-echo", transport="stdio", command=sys.executable, args=[str(ECHO)])


def test_discovers_and_calls_tools(echo_spec):
    with MCPClient([echo_spec]) as mc:
        names = {t.name for t in mc.tools}
        assert names == {"ai-os-echo__add", "ai-os-echo__reverse_text"}
        # Sync handler marshals onto the background loop and returns a string.
        assert mc.handlers["ai-os-echo__add"]({"a": 15, "b": 27}) == "42"
        assert mc.handlers["ai-os-echo__reverse_text"]({"text": "AI-OS"}) == "SO-IA"


def test_tool_error_is_returned_not_raised(echo_spec):
    with MCPClient([echo_spec]) as mc:
        out = mc.handlers["ai-os-echo__reverse_text"]({"text": "x" * 20001})
        assert out.startswith("Error:")  # server-side validation surfaced as data


def test_allow_filter_narrows_tools(echo_spec):
    with MCPClient([echo_spec], allow={"add"}) as mc:
        assert {t.name for t in mc.tools} == {"ai-os-echo__add"}


def test_bridge_to_run_tools_loop(echo_spec, fake_provider):
    """The whole point: MCP tools drop straight into a provider's run_tools loop with no adaptation."""
    with MCPClient([echo_spec]) as mc:
        result = fake_provider.run_tools([], tools=mc.tools, handlers=mc.handlers, system=None)
        # Both discovered MCP tools were invoked through the bridge during the loop.
        assert {s.name for s in result.steps} == {"ai-os-echo__add", "ai-os-echo__reverse_text"}
        assert result.final_text  # handler outputs (strings) came back, not exceptions
