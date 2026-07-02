# One-pager — Topic 05: Tool Use

**Slide headline:** Tools turn a text generator into an actor — and the loop is the heart of every agent.

**Demo beats (`topics/05-tool-use/demo.py`):**
1. Define two tools (`add`, `get_weather`) with JSON-Schema inputs + Python handlers.
2. Ask a question needing both → model requests both in one turn (parallel).
3. `run_tools` executes handlers, feeds results back, loops → final answer + tool-call trace + cost.

**Say this:**
- "The model doesn't run code — it *requests* a call; your handler runs it. That handler is the trust boundary."
- "Loop = model → tool_use → run → feed results → repeat until end_turn. Manual loop and 'runner' are the same mechanics."
- "Three tool families: your custom tools, server-side (web_search, code_execution), client-side (bash, editor, memory)."

**Top pitfall:** splitting parallel `tool_result`s across multiple user messages — return them together, or the model stops parallelizing.

**CCA‑F:** Tool Design & MCP (18%); the loop underpins Agentic Architecture (27%).
