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

## Consuming external servers (the client bridge)
Hosting a server is half of MCP; the other half is an **agent using one**. `core.mcp_client.MCPClient`
connects (client-side) to any MCP server, discovers its tools, and adapts each into a
`core.tools.ToolSpec` + a synchronous handler — so the shared `run_tools` loop (Topic 05) can call
GitHub / filesystem / docs / deploy tools with **zero kernel changes**. The MCP SDK is async and the
loop is sync, so each session runs on a background event-loop thread; handlers marshal calls onto it.

```python
from core import MCPClient
with MCPClient.from_manifest(["filesystem"], allow=None) as mc:   # least privilege via allow=
    provider.run_tools(msgs, tools=mc.tools, handlers=mc.handlers) # any provider, any role agent
```

The live manifest is `mcp/servers.json` (git-ignored; copy from `servers.example.json`). Secrets are
injected from the environment via `${VAR}` expansion — never inline.

## Role profiles (persona + least-privilege toolset)
A **role** is a persona prompt bound to the MCP servers/tools it may use — composed, never a God
Agent (`core/profiles.py`). `PROFILES["software-engineer"]` and `PROFILES["tech-writer"]` each pair a
`prompts/role/*.md` persona with a server list (e.g. `filesystem` + `github-remote`) and optional
skills. Build one with `build_agent(profile, provider, mc)`.

```python
from core import PROFILES, build_agent, open_toolset, get_provider
with open_toolset(PROFILES["tech-writer"]) as mc:        # opens only that role's servers/tools
    build_agent(PROFILES["tech-writer"], get_provider(), mc).run("Document the bridge, open a PR.")
```

### Document-then-PR (create PRs + generate docs)
`agent_with_mcp.py` proves one agent + one server. `document_and_pr.py` shows the real workflow you'd
run against any project: the **tech-writer** role reads the code via the filesystem MCP and generates
a docs page, then the flow **plans a pull request** via the remote GitHub MCP. It is **dry-run safe**
— docs land in git-ignored `runtime/`, and no branch/commit/PR is created. Go live by setting
`GITHUB_TOKEN` in `.env` (remote GitHub MCP over HTTP) and adding the authorized create-PR step.

## Run it
```bash
pip install -e ".[mcp]"
python topics/07-advanced-mcp/demo.py            # protocol: resources + prompts + multi-server
python topics/07-advanced-mcp/agent_with_mcp.py  # a real agent USES a server (filesystem, else echo)
python topics/07-advanced-mcp/document_and_pr.py # tech-writer generates docs + plans a PR (dry run)
```
`agent_with_mcp.py` degrades gracefully: filesystem MCP if `npx` is present (else the repo echo
server), and a live agent if `ANTHROPIC_API_KEY` is set (else a no-LLM bridge check).

## Files
- `topics/07-advanced-mcp/demo.py` — resources + prompts + multi-server manifest
- `topics/07-advanced-mcp/agent_with_mcp.py` — agent driving a real MCP server via the bridge
- `topics/07-advanced-mcp/document_and_pr.py` — tech-writer role: generate docs + plan a PR (dry run)
- `topics/07-advanced-mcp/api_connector.md` — remote MCP via the Messages API
- `core/mcp_client.py` — the client bridge (manifest → sessions → `ToolSpec` + handlers)
- `core/profiles.py` — role profiles (persona + least-privilege toolset) · `prompts/role/*.md`
- `mcp/servers.json` — live manifest (git-ignored) · `mcp/servers.example.json` — committed template
