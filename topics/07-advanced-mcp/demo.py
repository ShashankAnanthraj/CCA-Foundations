"""Topic 07 — Advanced MCP (runnable demo).

Goes beyond tools to the other MCP primitives, plus multi-server configuration:
  1. Read a server RESOURCE (info://about)
  2. List and render a server PROMPT (summarize)
  3. Show a multi-server manifest (lazy-loaded, plug-and-play)

Run:  python topics/07-advanced-mcp/demo.py
Needs: the MCP SDK  ->  pip install -e ".[mcp]"   (no API key required)
"""

from __future__ import annotations

import asyncio
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SERVER = ROOT / "mcp" / "echo_server" / "server.py"
MANIFEST = ROOT / "mcp" / "servers.example.json"

try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
except ImportError:
    print("MCP SDK not installed. Run:  pip install -e \".[mcp]\"")
    sys.exit(0)


def _texts(obj, attr: str) -> str:
    items = getattr(obj, attr, [])
    return " ".join(getattr(c, "text", "") for c in items).strip()


async def main() -> None:
    params = StdioServerParameters(command=sys.executable, args=[str(SERVER)])
    print("=" * 68 + "\nAdvanced MCP: resources, prompts, multi-server\n" + "=" * 68)

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1) RESOURCE — read-only context fetched by URI
            resources = await session.list_resources()
            print("\nResources:")
            for r in resources.resources:
                print(f"  - {r.uri}  ({r.name})")
            about = await session.read_resource("info://about")
            print(f"  read info://about -> {_texts(about, 'contents')}")

            # 2) PROMPT — reusable server-provided template
            prompts = await session.list_prompts()
            print("\nPrompts:")
            for p in prompts.prompts:
                print(f"  - {p.name}")
            rendered = await session.get_prompt(
                "summarize", {"text": "MCP lets any host reuse a server's tools, resources and prompts."}
            )
            msg = rendered.messages[0]
            print(f"  get_prompt('summarize') -> {getattr(msg.content, 'text', msg.content)}")

    # 3) MULTI-SERVER MANIFEST — lazy-loaded, plug-and-play
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    print("\nConfigured servers (manifest — connect only when needed = lazy loading):")
    for name, cfg in manifest["mcpServers"].items():
        print(f"  - {name}: transport={cfg.get('transport')} "
              f"{cfg.get('url') or cfg.get('command', '')}")

    print("\n" + "=" * 68)
    print("Done — Topic 07. Remote servers + the API connector: see api_connector.md.")
    print("=" * 68)


if __name__ == "__main__":
    asyncio.run(main())
