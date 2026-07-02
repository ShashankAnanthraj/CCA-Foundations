# CALM — context management checklist

The context window is finite and every token costs money and attention. CALM is a four-point
checklist for keeping long/multi-turn interactions affordable and sharp.

| Letter | Principle | What it means | Where it lives in AI-OS |
|---|---|---|---|
| **C** | **Cache** | Reuse stable prefixes so repeat tokens cost ~0.1x. | `provider.chat(cache=True)`, `Conversation(cache_system=True)` |
| **A** | **Assemble selectively** | Load only the context layers the task needs. | `context/` layers, `Project.context_text()` |
| **L** | **Limit (budget)** | Count tokens, cap `max_tokens`, trim/summarize inputs. | `count_tokens`, `max_tokens`, task budgets |
| **M** | **Manage lifecycle** | Clear/summarize/persist context over time. | context editing · compaction · memory |

## The three lifecycle tools (the M)
| Tool | What it does | Use when |
|---|---|---|
| **Context editing** | *Clears* stale tool results / thinking blocks | long tool-heavy runs; old results irrelevant |
| **Compaction** | *Summarizes* earlier history server-side | conversation approaching the context limit |
| **Memory** | *Persists* facts across sessions (files) | state must survive beyond one session |

## Caching rules that bite (exam-relevant)
- Caching is a **prefix match** — any byte change anywhere in the prefix invalidates everything after.
- Keep volatile content (timestamps, UUIDs, per-request IDs) **after** the cached prefix.
- Verify with `usage.cache_read_input_tokens` > 0. If it's always 0, a silent invalidator is at work
  (a `datetime.now()` in the system prompt, unsorted JSON, a varying tool set).
- Minimum cacheable prefix is model-dependent (~1–4K tokens) — short prefixes silently won't cache.

> **Note:** CALM is AI-OS's working checklist for the CCA‑F *Context Management* domain. Reconcile the
> letters with the vendor's wording if it differs — the practices (cache, assemble, limit, manage) hold.
