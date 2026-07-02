# One-pager — Topic 07: Advanced MCP

**Slide headline:** MCP as production infrastructure — resources, prompts, many servers, remote + auth.

**Demo beats (`topics/07-advanced-mcp/demo.py`):**
1. Read a **resource** (`info://about`) — read-only context by URI.
2. List + render a **prompt** (`summarize`) — a reusable template shipped by the server.
3. Print a **multi-server manifest** — plug-and-play, connect only when needed (lazy loading).

**Say this:**
- "A server is more than tools: resources (read) and prompts (templates) ship with it."
- "Hosts run many independent servers and lazy-load them — add/remove without touching the rest."
- "Remote servers use the API connector: `mcp_servers` + a matching `mcp_toolset` (both required)."
- "Secrets live in vaults (Managed Agents), injected at egress — never in prompts or messages."

**Top pitfall:** trusting the server/tooling blindly — validate inputs, least privilege, gate destructive
actions behind approval, pin versions.

**CCA‑F:** Tool Design & MCP (18%) — the depth end of the domain.
