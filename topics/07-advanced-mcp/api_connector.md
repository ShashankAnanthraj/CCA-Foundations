# Remote MCP via the API connector — reference

Beyond local stdio servers, Claude can connect to **remote** MCP servers directly from the Messages
API. Two parameters are required **together**: `mcp_servers` (the connections) and a matching
`mcp_toolset` tool that references each server by name.

```python
import anthropic
client = anthropic.Anthropic()

resp = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    betas=["mcp-client-2025-11-20"],
    mcp_servers=[
        {"type": "url", "name": "my-tools", "url": "https://example.com/mcp",
         "authorization_token": "..."}      # optional bearer for the remote server
    ],
    tools=[{"type": "mcp_toolset", "mcp_server_name": "my-tools"}],
    messages=[{"role": "user", "content": "Use the available tools to ..."}],
)
```

Rules:
- Every server in `mcp_servers` must be referenced by exactly one `mcp_toolset` — omitting it is a 400.
- `mcp_server_name` must match a `name` in `mcp_servers`.
- Allowlist tools with `mcp_toolset.default_config = {"enabled": false}` + per-tool `configs`.

## Authentication & secrets
- Simple case: a bearer `authorization_token` on the server entry.
- **Managed Agents** (server-hosted agents): credentials live in **vaults** and attach to a session via
  `vault_ids`; Anthropic injects/refreshes OAuth tokens at egress so the sandbox never sees the secret.
  Never put secrets in the system prompt or messages.

## Local (stdio) vs remote (this connector)
| | Local stdio | Remote (API connector) |
|---|---|---|
| Transport | stdio (host launches process) | HTTP/SSE (URL) |
| Auth | usually none (local trust) | bearer / OAuth / vault |
| Where | Claude Code, desktop, our demos | Messages API, hosted agents |

See `mcp/servers.example.json` for the multi-server manifest shape.
