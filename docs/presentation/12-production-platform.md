# One-pager — Topic 12: Production & Platform

**Slide headline:** Shipping = cost control × throughput × security × portability.

**Demo beats (`topics/12-production-platform/demo.py`):**
1. Count a prompt's tokens once.
2. Project cost per model — standard vs **batch (−50%)** vs **cached input (~0.1x)**.
3. List the production levers (batches, caching, model choice, files, platforms).

**Say this:**
- "Cost is a prod metric: model choice × batch × cache defines the bill."
- "Batches: 50% cheaper, async, results **unordered** — key by `custom_id`."
- "Runs on first-party, Claude Platform on AWS, Bedrock, Vertex, Foundry — dedicated clients, differing
  model-ID formats and feature availability."
- "Migration: adaptive thinking only, `budget_tokens`/sampling params removed, no prefill — use effort + structured outputs."

**Top pitfall:** assuming every feature exists everywhere — Batches/Files aren't on Bedrock/Vertex; check availability first.

**CCA‑F:** cross-cutting production knowledge (supports all domains).
