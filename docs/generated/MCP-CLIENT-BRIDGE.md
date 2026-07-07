# MCP Client Bridge

**What it is**  
The MCP client bridge (`core/mcp_client.py`) lets agents use tools provided by external MCP servers (e.g., filesystem, GitHub, docs, deploy) without any changes to the core kernel. It discovers the tools a server offers, registers them as `ToolSpec` objects, and supplies synchronous handlers that forward calls to the server’s async MCP API.

**Key points**

| Aspect | Detail |
|--------|--------|
| **Location** | `core/mcp_client.py` (next to `ToolSpec` and the `run_tools` contract) |
| **Dependencies** | `mcp` SDK (`pip install -e "[mcp]"`), Python stdlib (`asyncio`, `threading`, `json`, …) |
| **Security** | Tools are filtered via an `allow` predicate; secrets are injected only through `${ENV}` placeholders in the manifest. |
| **Transport** | Supports `stdio` (local subprocess) and `http` (remote streamable HTTP). |
| **Naming** | By default tools are namespaced as `<server>__<tool>` (max 64 chars); can be disabled with `namespace=False`. |

## Quick usage

```python
from core.mcp_client import MCPClient

# Load the manifest and expose only the "filesystem" server
with MCPClient.from_manifest(["filesystem"]) as mc:
    # Pass the discovered tools and handlers to any provider's run_tools loop
    agent = Agent(
        name="dev",
        provider=provider,
        system=system_prompt,
        tools=mc.tools,          # list of ToolSpec objects
        handlers=mc.handlers,    # dict: tool name → synchronous callable
    )
    agent.run("List the files in the repo and give a short summary of README.md.")
```

*The `with` block starts a background asyncio event loop, connects to the requested MCP server(s), and tears everything down automatically when the block exits.*
