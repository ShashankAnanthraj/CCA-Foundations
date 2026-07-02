# Wiring the MCP server into Claude Code

The same `mcp/echo_server` you ran in the demo plugs straight into Claude Code — no code changes.

## Option A — project config file (`.mcp.json` at the repo root)
Create `.mcp.json` so anyone who opens this project gets the server:

```json
{
  "mcpServers": {
    "ai-os-echo": {
      "command": "python",
      "args": ["mcp/echo_server/server.py"]
    }
  }
}
```

Restart Claude Code in this directory; it launches the server over stdio and its tools
(`add`, `reverse_text`), resource (`info://about`), and prompt (`summarize`) become available.

## Option B — CLI
```bash
claude mcp add ai-os-echo -- python mcp/echo_server/server.py
```

## Scopes
- **project** (`.mcp.json`, committed) — shared with the team.
- **user** (`~/.claude` / `claude mcp add --scope user`) — just you, across all projects.
- **local** — this machine/project only.

## Verify inside Claude Code
Ask it to "use the ai-os-echo tools to add 2 and 3" — it should call the MCP `add` tool.
List configured servers with `claude mcp list`.

> Remote (SSE/HTTP) servers are added the same way but with a URL instead of a command — and can be
> used from the **API MCP connector** too (Topic 07).
