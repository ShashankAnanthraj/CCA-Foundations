# MCP — Model Context Protocol

MCP is a standard way to expose **tools, resources, and prompts** to any AI client. Write a server
once; every MCP-aware host (Claude Code, Claude Desktop, the API connector, custom clients) can use it.
Independent, plug-and-play, lazy-loaded (Constitution: MCP Design).

## The three primitives
| Primitive | What it is | Example here |
|---|---|---|
| **Tools** | Actions the model can invoke | `add`, `reverse_text` |
| **Resources** | Read-only context the client can fetch (by URI) | `info://about` |
| **Prompts** | Reusable server-provided prompt templates | `summarize` |

## Architecture
```
Host (Claude Code / API / your app)
  └─ MCP Client ──(transport)── MCP Server ──> tools · resources · prompts
```

## Transports
| Transport | Use when | Notes |
|---|---|---|
| **stdio** | Local server, same machine | Host launches the process; simplest. Our `echo_server` uses this. |
| **SSE / streamable HTTP** | Remote server, over the network | Needed for the API MCP connector (Topic 07) and hosted servers. |

## Run the demo server
```bash
pip install -e ".[mcp]"          # installs the `mcp` SDK
python mcp/echo_server/server.py  # now speaking MCP over stdio
```

## Servers (this repo)
- `echo_server/` — tools + resource + prompt (Topics 06 & 07).

## Consuming servers (client side)
This folder holds servers we **author**. To let our agents **use** external MCP servers (GitHub,
filesystem, docs, deploy…), see `core/mcp_client.py` — it reads `servers.json`, connects, and adapts
each server's tools into the vendor-neutral `run_tools` loop. (The bridge lives in `core/`, not here,
so this folder never needs an `__init__.py` that would shadow the installed `mcp` SDK on `sys.path`.)
- `servers.json` — live manifest (git-ignored; may hold `${ENV}` secrets)
- `servers.example.json` — committed template (copy it to `servers.json`)

## Security (always)
Validate every tool input; expose the minimum surface; don't trust client-supplied paths/URLs; keep
secrets out of the server code (env vars only). See Topic 07 for auth, vaults, and remote servers.
