# Running AI-OS on OpenRouter (no Anthropic key)

AI-OS is model/vendor-agnostic. This guide runs **every topic** through the **OpenRouter**
provider using a **free** model — no Anthropic API key, $0 cost. It reflects a real end-to-end
run of all topics; the sample outputs below are abbreviated from that run.

## One-time setup

```bash
# 1. Install the OpenRouter client (+ the MCP extra for Topics 06/07)
pip install -e ".[openrouter]"
pip install -e ".[mcp]"

# 2. Configure .env  (copy from .env.example, then fill in)
#    AI_OS_PROVIDER=openrouter
#    OPENROUTER_API_KEY=sk-or-...          # from https://openrouter.ai/keys
#    AI_OS_DEFAULT_MODEL=google/gemma-4-31b-it:free
```

**Windows only** — set UTF-8 output once per shell so model text with Unicode (curly quotes, °, …)
doesn't crash the console:

```powershell
$env:PYTHONIOENCODING='utf-8'
```

### Choosing a model
`.env`'s default is `google/gemma-4-31b-it:free` — a free **instruct** model that supports tool
calling *and* structured output *and* returns clean prose (reasoning models leak their
chain-of-thought into demo output). Free slugs change over time; list current free models at
<https://openrouter.ai/models?max_price=0>. Capable free alternates:

| Model | Tools | Structured | Notes |
|---|:---:|:---:|---|
| `google/gemma-4-31b-it:free` | ✅ | ✅ | **default** — cleanest prose |
| `openai/gpt-oss-20b:free` | ✅ | ✅ | good; occasional stray char in JSON |
| `nvidia/nemotron-3-super-120b-a12b:free` | ✅ | ✅ | reasoning model — leaks "thinking" into prose |
| `openrouter/free` | ✅ | ✅ | auto-router across free models |

**Rate limits — two kinds:**

1. **Per-minute throttle** (transient): free models get busy and return HTTP 429. The adapter
   ([providers/openrouter/adapter.py](../providers/openrouter/adapter.py)) **auto-retries with
   backoff** (honoring `Retry-After`), and also retries the two other free-tier hiccups —
   HTTP-200-with-error bodies (`choices=None`) and empty/invalid structured output. Just wait it out.
2. **Daily quota** (hard cap): a free OpenRouter account without credits is limited to
   **~50 free-model requests per day** total. Once exhausted you get
   `Rate limit exceeded: free-models-per-day` and the adapter fails fast with guidance —
   retrying won't help. A single full sweep of all topics makes ~40–50 calls, so you can hit this
   in one sitting.

**The reliable fix:** add **~$10 credit** at <https://openrouter.ai/settings/credits>. This unlocks
**1000 free-model requests/day** (still `$0.00` per call on `:free` models) — or use a cheap **paid**
model (`meta-llama/llama-3.3-70b-instruct`, ~$0.12/$0.30 per 1M, no daily cap). A full paid sweep of
all topics costs well under **$0.05**.

## Run any topic

```bash
python topics/01-foundations/demo.py     # replace with any topic below
python -m compileall -q core providers   # optional: syntax check
```

Every topic prints its section headers, live model output, token `usage`, and estimated `$`.
All demos degrade gracefully with no key (they print their offline sections and stop).

## The topics

Legend — **needs:** key = a live model call · struct = structured output · tools = tool calling ·
mcp = the `[mcp]` extra · offline = runs with no key.

| # | Topic | Needs | What it demonstrates |
|---|---|---|---|
| 01 | Foundations | key | Model catalog & pricing, token counting, a basic call, streaming, thinking/effort. |
| 02 | Prompt Engineering | key, struct | Base→Role→Task→Output hierarchy (offline); weak prose vs a validated JSON object; grounding. |
| 03 | Skills | key | Progressive disclosure: discover → route → load-body → apply. Routing runs offline; only "apply" calls the model. |
| 04 | Projects & Artifacts | key | Load a project manifest (references, not copies); grounded answer; generate + save an artifact to `runtime/artifacts/`. |
| 05 | Tool Use | key, tools | The agentic tool loop: model requests tools → your code runs them → loop repeats. |
| 06 | MCP | mcp | Talk to a local MCP **server** over stdio (tools). **No key.** |
| 07 | Advanced MCP | mcp | MCP resources, prompts, multi-server manifest. **No key.** |
| 08 | Agents | key, tools, struct | Router / pipeline / parallel agent patterns over the shared core. |
| 09 | Subagents & Cowork | key, struct | Decompose → fan-out subagents → synthesize → human-gate. |
| 10 | Context Management | key | Token budgeting + multi-turn. (Prompt caching is Claude-only — see gotcha.) |
| 11 | Claude Code Config | offline | No `demo.py` — the config files *are* the demo; exercised inside Claude Code, not the API. |
| 12 | Production & Platform | key | Cost/observability: token count once, project per-model cost, batch/cache savings. |

## Sample outputs (from the live free-tier run)

**Topic 01 — basic call + streaming**
```
3) Basic Messages API call
The Anthropic Messages API is a REST interface that allows developers to send a sequence of
messages to Claude models to generate text completions in a conversational format.
  [model=google/gemma-4-31b-it:free  stop_reason=stop]
  [tokens: in=196 out=31 total=227]  [est. cost=$0.000000]
```

**Topic 02 — structured output (validated JSON, every time)**
```json
{ "category": "bug", "severity": "high", "needs_human": true,
  "summary": "Customer reports that the app crashes when clicking Export, resulting in lost work." }
```

**Topic 05 — tool loop**
```
-> model calls add({'a': 15, 'b': 27})
-> model calls get_weather({'city': 'Paris'})
final answer: 15 + 27 = 42. The current weather in Paris is 22°C and partly cloudy.
[tool calls=2  loop iterations=3]
```

**Topic 06 — MCP (no key)**
```
Discovered tools: add, reverse_text
add(15, 27) -> 42     reverse_text('AI-OS') -> SO-IA
```

## Gotchas (OpenRouter vs Claude)

- **`count_tokens` is approximate.** OpenRouter has no pre-send count endpoint, so the adapter
  estimates (~chars/4) and prints a one-line note to stderr. Exact counts still come back in
  `usage` after each call.
- **Prompt caching is Claude-only.** Topic 10 will show `cache_read=0` and print its
  "no cache read" branch — that's expected, not a failure. `thinking`/`effort`/`cache` hints are
  silently ignored on OpenRouter.
- **Model capability matters.** Topics 02/05/08/09 need a model that supports structured output
  and/or tool calling — stick to the capable models in the table above.
- **Reasoning models muddy output.** If you switch to a reasoning model, expect visible
  chain-of-thought in prose sections; `google/gemma-4-31b-it:free` avoids this.
- **Free slugs drift.** If a model returns `400 not a valid model ID` or `404 unavailable for
  free`, pick a current one from the free-models list.

## Switching back to Claude

Set `AI_OS_PROVIDER=claude` (or unset it) and provide `ANTHROPIC_API_KEY`. Nothing else changes —
that's the point of the provider-agnostic core.
