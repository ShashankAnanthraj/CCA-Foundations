# Platforms & Migration — reference

## Where Claude runs
| Platform | What it is | Model IDs |
|---|---|---|
| **First-party API** | Anthropic's Claude Developer Platform | bare, e.g. `claude-opus-4-8` |
| **Claude Platform on AWS** | Anthropic-operated via AWS (SigV4, IAM, Marketplace) | bare (same as first-party) |
| **Amazon Bedrock** | AWS-operated | `anthropic.`-prefixed, e.g. `anthropic.claude-opus-4-8` |
| **Google Vertex AI** | GCP-operated | bare (no prefix) |
| **Microsoft Foundry** | Azure-operated | bare |

Use the platform's **dedicated client** (e.g. `AnthropicBedrockMantle`, `AnthropicVertex`), not the
base client with a URL override. Feature availability varies (e.g. Batches/Files not on Bedrock/Vertex;
web search limited on Vertex) — check the availability matrix before relying on a feature off first-party.

## Model selection (cost vs capability)
| Need | Model |
|---|---|
| Hardest reasoning / long agentic | `claude-opus-4-8` (or `claude-fable-5`) |
| High-volume production | `claude-sonnet-5` |
| Simple / latency-sensitive / cheap | `claude-haiku-4-5` |

## Migration notes (current models)
- **Adaptive thinking only** on Fable 5 / Opus 4.8 / 4.7 / Sonnet 5 — `budget_tokens` and sampling
  params (`temperature`/`top_p`/`top_k`) are **removed** (400 error). Use `thinking={"type":"adaptive"}`
  + `output_config={"effort": ...}`.
- **No assistant prefill** on 4.6+/Fable — use structured outputs (`output_config.format`) instead.
- **Effort** replaces fixed thinking budgets; `xhigh` is the sweet spot for coding/agentic on 4.7/4.8/5.
- Use exact model-ID strings; don't append date suffixes to aliases.

## Security checklist (production)
- Secrets in env/vaults, never in code, prompts, or messages.
- Sandbox tool execution; validate every tool input; least privilege.
- Gate irreversible actions behind approval (permissions/hooks or `approval_gate`).
- Log `request_id` + `usage` for observability; handle `stop_reason == "refusal"`.
