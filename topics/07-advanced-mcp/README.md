# Topic 07 — Advanced MCP

**Purpose:** Everything past "a server with tools" — resources, prompts, multiple servers, remote
connections, auth, and security. This is where MCP becomes production infrastructure
(CCA‑F *Tool Design & MCP*, 18%).

## Concept
- **Resources & prompts (not just tools):** servers also expose read-only **resources** (fetched by
  URI, e.g. `info://about`) and reusable **prompts** (e.g. `summarize`). The demo exercises both.
- **Multi-server & lazy loading:** a host configures many independent servers (`mcp/servers.example.json`)
  and connects to each **only when needed** — plug-and-play, no coupling (Constitution: MCP Design).
- **Remote servers & the API connector:** connect over HTTP/SSE via `mcp_servers` + `mcp_toolset`
  (`api_connector.md`).
- **Auth & secrets:** bearer tokens for simple cases; **vaults** (Managed Agents) for OAuth with
  auto-refresh, injected at egress so the sandbox never sees the secret.
- **Security:** validate inputs, least privilege, don't trust server output, pin server versions,
  control network egress, and gate destructive tools behind approval (permission policies).

## When to reach for what
| Need | Reach for |
|---|---|
| Share read-only context | MCP **resource** |
| Ship a reusable prompt with a server | MCP **prompt** |
| Many integrations, loosely coupled | **Multi-server** manifest + lazy load |
| Hosted/remote tools from the API | **API connector** (`mcp_servers` + `mcp_toolset`) |
| Third-party auth without leaking secrets | **Vaults** (Managed Agents) |

## Talking points
1. MCP isn't just tools — resources and prompts ship with the server too.
2. Servers are independent and lazy-loaded; add/remove without touching the others.
3. Remote = HTTP/SSE + auth; the API connector needs `mcp_servers` **and** a matching `mcp_toolset`.
4. Secrets belong in vaults/env, never in prompts — and every tool input is untrusted.

## Run it
```bash
pip install -e ".[mcp]"
python topics/07-advanced-mcp/demo.py
```

## Files
- `topics/07-advanced-mcp/demo.py` — resources + prompts + multi-server manifest
- `topics/07-advanced-mcp/api_connector.md` — remote MCP via the Messages API
- `mcp/servers.example.json` — multi-server config shape
