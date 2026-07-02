"""AI-OS demo MCP server (stdio transport).

Purpose:    A minimal, real Model Context Protocol server exposing the three MCP primitives —
            tools, a resource, and a prompt — so clients (Claude Code, the API connector, or our
            Topic 06/07 demos) can discover and use them.
Run:        python mcp/echo_server/server.py      (speaks MCP over stdio)
Depends on: mcp  (pip install mcp   — or  pip install -e ".[mcp]")
Security:   validate inputs; never trust a client blindly; expose least privilege (Constitution).
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ai-os-echo")


# --- Tools: actions the model can invoke ---------------------------------- #
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b


@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse a string. Input is capped to keep the demo safe."""
    if len(text) > 10_000:  # basic input validation (Security)
        raise ValueError("text too long")
    return text[::-1]


# --- Resource: read-only context the client can fetch --------------------- #
@mcp.resource("info://about")
def about() -> str:
    """Static info resource describing this server."""
    return "AI-OS demo MCP server — tools: add, reverse_text; resource: info://about; prompt: summarize."


# --- Prompt: a reusable, server-provided prompt template ------------------ #
@mcp.prompt()
def summarize(text: str) -> str:
    """Return a summarization prompt for the given text."""
    return f"Summarize the following in one clear sentence:\n\n{text}"


if __name__ == "__main__":
    mcp.run()  # stdio transport by default
