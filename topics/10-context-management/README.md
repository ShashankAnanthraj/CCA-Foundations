# Topic 10 — Context Management

**Purpose:** Keep long and multi-turn interactions fast, sharp, and affordable — the context window is
finite and every token costs (CCA‑F *Context Management*, 15%).

## Concept
- **Stateless API:** the model has no memory between calls — you resend the full history each turn.
  `Conversation` manages that and tracks cumulative usage.
- **Prompt caching:** mark a large **stable prefix** (system prompt) as cacheable; repeat turns pay
  ~0.1x on the cached portion. Caching is a **prefix match** — any byte change invalidates the rest.
- **Token budgeting:** `count_tokens` before sending; cap `max_tokens`; trim/summarize inputs.
- **Lifecycle (choose by need):** context **editing** (clear stale tool results/thinking) vs
  **compaction** (summarize old history) vs **memory** (persist across sessions).
- **CALM framework:** Cache · Assemble selectively · Limit · Manage (`prompts/frameworks/calm.md`).

## When to use which lifecycle tool
| Situation | Tool |
|---|---|
| Long tool-heavy run, old results irrelevant | Context **editing** |
| Conversation nearing the context limit | **Compaction** |
| State must outlive the session | **Memory** |

## Talking points
1. Caching is a **prefix match** — keep timestamps/UUIDs *after* the cached block or you cache nothing.
2. Verify with `usage.cache_read_input_tokens > 0`; if it's always 0, hunt the silent invalidator.
3. Editing *clears*, compaction *summarizes*, memory *persists* — three different tools, three needs.
4. Selective context assembly (only the layers you need) is the cheapest optimization of all.

## Run it
```bash
python topics/10-context-management/demo.py
```
Uses a cheap model + a padded knowledge base so the cache reliably engages: **turn 1 writes the cache,
turn 2 reads it** — watch `cache_write` then `cache_read` in the output.

## Reuses (DRY)
- `core.Conversation` — multi-turn + cached system + usage totals
- `providers.claude.ClaudeProvider.chat(cache=True)` + `count_tokens`
- `prompts/frameworks/calm.md` — the checklist
