# Topic 12 — Production & Platform

**Purpose:** Ship it: control cost, scale throughput, stay secure, run anywhere, and migrate safely.

## Concept
- **Cost & observability:** treat cost as a prod metric. Count tokens, log `usage` + `request_id`,
  compare models, and use the levers below. The demo projects per-model cost for a real prompt.
- **Throughput levers:** **Batches API** (50% cheaper, async) · **prompt caching** (cached input ~0.1x,
  Topic 10) · **right-sizing the model** (Haiku vs Opus/Fable) · **Files API** (upload once, reuse).
- **Platforms:** first-party API, **Claude Platform on AWS**, Amazon Bedrock, Google Vertex, Microsoft
  Foundry — dedicated clients, differing model-ID formats and feature availability
  (`platform_availability.md`).
- **Migration:** adaptive-thinking-only models, removed `budget_tokens`/sampling params, prefill removal,
  effort tuning (`platform_availability.md`).
- **Security:** secrets in env/vaults, sandboxing, input validation, approval gates, refusal handling.

## When to use which lever
| Situation | Lever |
|---|---|
| Bulk, non-urgent work | Batches (−50%) |
| Repeated large context | Prompt caching (~0.1x input) |
| Simple/high-volume | Cheaper model (Haiku) |
| Same doc across calls | Files API |

## Talking points
1. Cost is measurable and controllable — model choice × batch × cache defines your bill.
2. Batch results are **unordered** — key by `custom_id`.
3. Provider portability is real, but features differ per platform — check availability first.
4. Security is non-negotiable: secrets out of prompts, gate irreversible actions, handle refusals.

## Run it
```bash
python topics/12-production-platform/demo.py
```

## Files
- `topics/12-production-platform/demo.py` — per-model cost projection + savings
- `batches_and_files.md` — Batches + Files API reference
- `platform_availability.md` — platforms, model selection, migration, security checklist
