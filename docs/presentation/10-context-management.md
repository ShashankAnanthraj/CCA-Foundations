# One-pager — Topic 10: Context Management

**Slide headline:** The context window is finite and priced — CALM keeps it fast, sharp, and cheap.

**Demo beats (`topics/10-context-management/demo.py`):**
1. Budget → count the system prompt's tokens before sending. [Limit]
2. Multi-turn → stateless API, history resent, cumulative usage tracked. [Assemble]
3. Caching → large stable prefix: **turn 1 writes the cache, turn 2 reads it** (`cache_read > 0`). [Cache]

**Say this:**
- "CALM = Cache · Assemble selectively · Limit · Manage."
- "Caching is a prefix match — one changed byte invalidates everything after it. Keep volatile data last."
- "Prove hits with `usage.cache_read_input_tokens`; if it's always 0, find the silent invalidator."
- "Lifecycle: editing *clears*, compaction *summarizes*, memory *persists* — pick by need."

**Top pitfall:** a `datetime.now()`/UUID in the cached system prompt → cache never hits, cost never drops.

**CCA‑F:** Context Management (15%).
