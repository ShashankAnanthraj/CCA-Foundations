# One-pager — Topic 01: Foundations

**Slide headline:** One endpoint, four model tiers, and cost you can see on every call.

**Demo beats (`topics/01-foundations/demo.py`):**
1. Models & pricing → choose by need (Opus/Fable = hardest; Sonnet = volume; Haiku = cheap/fast).
2. Count tokens before sending (never `tiktoken`).
3. Basic Messages call → text + `stop_reason` + `usage` + `$` cost.
4. Streaming → tokens rendered live.
5. Adaptive thinking + effort → quality vs cost/latency.

**Say this:**
- "Everything is `messages.create` — tools, vision, structured output are options on the same endpoint."
- "`stop_reason` drives control flow: end_turn, max_tokens, tool_use, refusal."
- "Modern models use adaptive thinking + effort — not a fixed `budget_tokens`."
- "We call the provider-agnostic core, so swapping model or vendor is a one-line change."

**Top pitfall:** ignoring `usage`/cost until the bill arrives — surface it on every call from day one.

**CCA‑F:** foundational (underpins all five domains).
