# One-pager — Topic 06: MCP (core)

**Slide headline:** Write a capability once; every AI host can use it. MCP is USB-C for AI tools.

**Demo beats (`topics/06-mcp/demo.py`):**
1. Client spawns `mcp/echo_server` over stdio and initializes the session.
2. Lists the server's tools (`add`, `reverse_text`).
3. Calls both and prints results — pure protocol, no Claude in the loop.
4. Then: the *same* server drops into Claude Code via `.mcp.json` (see `claude-code-setup.md`).

**Say this:**
- "Topic 05 tools lived inside our app. MCP moves them to an independent server any host reuses."
- "Three primitives: tools (act), resources (read-only context), prompts (reusable templates)."
- "Transports: stdio for local, SSE/HTTP for remote (and the API connector)."
- "~25 lines with FastMCP gives a real, reusable server."

**Top pitfall:** hard-coding secrets or over-broad access in the server — servers are independent trust
boundaries; validate inputs, least privilege, secrets via env only.

**CCA‑F:** Tool Design & MCP (18%).
