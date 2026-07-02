# Topic 05 — Tool Use

**Purpose:** Give the model hands. Tools turn a text generator into something that can *act* — the
foundation of every agent (CCA‑F *Tool Design & MCP*, 18%; feeds *Agentic Architecture*, 27%).

## Concept
- **User-defined tool** = `name` + `description` + `input_schema` (JSON Schema). The model *requests*
  a call; **your code executes it** and returns a `tool_result`.
- **The loop:** model → `stop_reason == "tool_use"` → run handlers → append results → call again →
  repeat until `end_turn`. Packaged as the reusable `provider.run_tools` (core primitive).
- **Parallel tool use:** one assistant turn can contain several `tool_use` blocks — return **all**
  results in **one** user message (our loop does this).
- **`tool_choice`:** `auto` (default), `any` (must use a tool), `tool` (force one), `none`.
- **Manual loop vs runner:** the manual loop is transparent (you see every step); a "runner" (our
  `run_tools`, or the SDK's `client.beta.messages.tool_runner`) automates it. Same mechanics.
- **Server-side tools** (run on Anthropic infra: `web_search`, `code_execution`) vs **client-side
  tools** (you execute: `bash`, `text_editor`, `memory`) vs **your custom tools** (this demo).

## When to use what
| Need | Reach for |
|---|---|
| Full control / approval gates / logging | Manual loop (transparent) |
| Just get it done | Runner (`run_tools`) |
| Live web info | Server tool `web_search` |
| Run code / files | `code_execution` (server) or `bash`/`text_editor` (client) |

## Talking points
1. The model never executes anything — it emits a request; **your handler is the trust boundary** (validate inputs).
2. Good `description`s drive correct tool selection — write them like tiny specs.
3. Return tool errors as `tool_result` with `is_error: true` (data, not exceptions) so the model can recover.
4. This loop is reused verbatim by the Agents topics — an agent *is* this loop plus a goal.

## Run it
```bash
python topics/05-tool-use/demo.py
```

## Reuses (DRY)
- `core.ToolSpec` / `core.ToolCall` — normalized tool types
- `providers.claude.ClaudeProvider.run_tools` — the transparent, reusable tool loop
