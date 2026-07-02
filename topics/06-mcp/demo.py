"""Topic 06 — MCP core (runnable demo).

Spawns the local MCP server over stdio, then acts as an MCP client:
  1. initialize the session
  2. list the server's tools
  3. call two tools and print results

Run:  python topics/06-mcp/demo.py
Needs: the MCP SDK  ->  pip install -e ".[mcp]"   (no API key required)

Note: this demo talks to an MCP *server*, not to Claude — it shows the protocol itself.
"""

from __future__ import annotations

import asyncio
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SERVER = ROOT / "mcp" / "echo_server" / "server.py"

try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
except ImportError:
    print("MCP SDK not installed. Run:  pip install -e \".[mcp]\"   (or: pip install mcp)")
    sys.exit(0)


def _text(result) -> str:
    """Extract text from an MCP tool result's content blocks."""
    parts = [getattr(c, "text", "") for c in getattr(result, "content", [])]
    return " ".join(p for p in parts if p).strip()


async def main() -> None:
    params = StdioServerParameters(command=sys.executable, args=[str(SERVER)])
    print("=" * 68)
    print("Connecting to mcp/echo_server over stdio ...")
    print("=" * 68)

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("\nDiscovered tools:")
            for t in tools.tools:
                print(f"  - {t.name}: {t.description}")

            print("\nCalling tools:")
            r1 = await session.call_tool("add", {"a": 15, "b": 27})
            print(f"  add(15, 27)            -> {_text(r1)}")
            r2 = await session.call_tool("reverse_text", {"text": "AI-OS"})
            print(f"  reverse_text('AI-OS')  -> {_text(r2)}")

    print("\n" + "=" * 68)
    print("Done — Topic 06 complete. Same server plugs into Claude Code (see claude-code-setup.md).")
    print("=" * 68)


if __name__ == "__main__":
    asyncio.run(main())
