# Topic 01 — Foundations

**Purpose:** The bedrock every other topic builds on — how you actually talk to Claude and reason
about cost.

## Concept (what your team must know)
- **Models & when to use them:** `claude-opus-4-8` (default, most capable Opus), `claude-sonnet-5`
  (balanced, high-volume), `claude-haiku-4-5` (fast/cheap), `claude-fable-5` (most capable, priciest).
- **Messages API:** stateless request → response. You send `messages` (+ optional `system`); you get
  `content` blocks, a `stop_reason`, and `usage`.
- **Streaming:** render tokens as they arrive (better UX; required for large outputs).
- **Thinking & effort:** adaptive thinking (`{"type":"adaptive"}`) + `effort` (low→max) trade quality
  for cost/latency. Note: modern models use adaptive thinking — **not** a fixed `budget_tokens`.
- **Tokens & cost:** always read `usage`; estimate `$` from a pricing table. Count tokens with the
  API's `count_tokens`, never `tiktoken`.

## When to use what
| Need | Reach for |
|---|---|
| Hardest reasoning / long agentic runs | Opus 4.8 (or Fable 5) + higher effort |
| High-volume production | Sonnet 5 |
| Simple, latency-sensitive | Haiku 4.5, low effort, thinking off |
| Live UX / big outputs | Streaming |

## Talking points (for the presentation)
1. Everything is one endpoint (`messages.create`) — tools, vision, structured output are options on it.
2. `stop_reason` drives control flow (`end_turn`, `max_tokens`, `tool_use`, `refusal`).
3. Cost is a first-class metric — we surface `usage` + `$` on every call (Constitution: cost economy).
4. The demo calls the **provider-agnostic core**, not the vendor SDK — swap models/vendors freely.

## Run it
```bash
python topics/01-foundations/demo.py
```
Requires `.env` with `ANTHROPIC_API_KEY`. Keep `AI_OS_MAX_TOKENS` small to control spend.

## Reuses (DRY)
- `core.get_settings` — config
- `providers.claude.ClaudeProvider` — the `core.providers.LLMProvider` implementation
- `prompts/base/base_system.md` — shared Base system prompt
