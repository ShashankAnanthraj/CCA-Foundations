## MCP Client Bridge  

**What it is**  
The MCP client bridge (`core/mcp_client.py`) connects the AI‑OS kernel to external **MCP servers** (e.g., filesystem, GitHub, docs, deployment tools). It discovers each server’s tools, converts them into `core.tools.ToolSpec` objects, and provides synchronous handler functions so any provider’s `run_tools` loop can call those tools without knowing about async MCP internals.

**Why use it**  
- Enables agents to invoke **vendor‑neutral MCP tools** hosted anywhere (local subprocesses or HTTP services).  
- Keeps the kernel’s tool‑execution path synchronous while the MCP SDK remains asynchronous.  
- Supports least‑privilege exposure via an `allow` filter and optional namespacing of tool names.  

**Key concepts**  

| Concept | Meaning |
|--------|---------|
| **ServerSpec** | Normalized description of an MCP server from `servers.json` (transport, command, URL, env, etc.). |
| **Manifest** | JSON file (`mcp/servers.json` or fallback `servers.example.json`) listing available MCP servers. |
| **ToolSpec** | Core‑OS representation of a tool (name, description, input schema). |
| **Handler** | Synchronous callable that forwards a tool call to the MCP server and returns a plain‑text result. |
| **Namespace** | When enabled (`namespace=True`), tool names are prefixed with a sanitized server identifier (`server__tool`). |

**Typical usage**

```python
from core.mcp_client import MCPClient

# Load the manifest and expose only the "filesystem" server’s tools
with MCPClient.from_manifest(["filesystem"]) as mc:
    # mc.tools  -> list of ToolSpec objects for the server
    # mc.handlers -> dict {tool_name: sync_handler}
    # Pass these into any provider that runs tools, e.g.:
    agent = Agent(
        name="dev",
        provider=my_provider,
        system="You are a helpful assistant.",
        tools=mc.tools,
        handlers=mc.handlers,
    )
    agent.run("List the files in the current directory and summarize README.md.")
```

*Steps*  

1. **Prepare a manifest** (`mcp/servers.json`) describing the MCP servers you want to use.  
2. **Create the client** via `MCPClient.from_manifest([...])`, optionally filtering tools with `allow` or disabling namespacing (`namespace=False`).  
3. **Enter the context manager** – it starts a background asyncio loop, connects to each server, and registers their tools.  
4. **Supply `mc.tools` and `mc.handlers`** to the agent (or any `run_tools` implementation).  
5. **When the `with` block ends**, the client cleanly shuts down subprocesses or HTTP connections.  

**Security note**  
Only tools matching the `allow` filter are exposed, and environment variables in the manifest are expanded from the process env (`${VAR}`), never hard‑coded. This follows the platform’s “least‑privilege” principle.
