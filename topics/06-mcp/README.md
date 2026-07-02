# Topic 06 — MCP (core)

**Purpose:** Build a capability once and let *any* AI client use it. MCP is the USB-C of AI tooling
(CCA‑F *Tool Design & MCP*, 18%).

## Concept
- **MCP = Model Context Protocol:** a host runs an **MCP client** that connects to independent **MCP
  servers**, each exposing **tools**, **resources**, and **prompts**.
- **Tools vs Topic 05 tools:** in Topic 05 your tools lived *inside* your app. MCP tools live in a
  *separate server* any host can reuse — that's the leap.
- **Transports:** **stdio** (local; host launches the process) vs **SSE/HTTP** (remote; needed for the
  API connector — Topic 07).
- **Our server (`mcp/echo_server/server.py`):** `add`, `reverse_text` (tools), `info://about`
  (resource), `summarize` (prompt) — built with `FastMCP` in ~25 lines.

## When to use MCP (vs a plain in-app tool)
| Situation | Choose |
|---|---|
| Capability reused across apps/teams/hosts | MCP server |
| One-off tool inside a single agent | In-app tool (Topic 05) |
| Third-party integration (GitHub, Slack, DB) | MCP server (often already exists) |

## Talking points
1. Write once, use everywhere: the *same* server answers our Python demo **and** Claude Code (see
   `claude-code-setup.md`).
2. Three primitives — tools (act), resources (read), prompts (reusable templates).
3. stdio = local & simple; SSE/HTTP = remote & networked. Pick per deployment.
4. Servers are independent and lazy-loaded — plug-and-play (Constitution: MCP Design).

## Run it
```bash
pip install -e ".[mcp]"           # installs the MCP SDK (no API key needed)
python topics/06-mcp/demo.py       # client spawns the server and calls its tools
```

## Files
- `mcp/echo_server/server.py` — the server (tools + resource + prompt)
- `topics/06-mcp/demo.py` — a minimal MCP client over stdio
- `topics/06-mcp/claude-code-setup.md` — plug the server into Claude Code
