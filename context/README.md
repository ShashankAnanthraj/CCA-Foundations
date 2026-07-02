# Context — layered, selectively loaded

Context is AI-OS's most valuable resource. It is organized in layers so a request loads **only** what
it needs (Constitution: Context Engineering). The kernel's context engine (`core/context/`, added in
Topic 10) assembles a request from these layers.

| Layer | Folder | Lifetime | Example |
|---|---|---|---|
| **Global** | `global/` | Whole platform | org standards, glossary |
| **Domain** | `domain/` | A problem domain | "customer support" policies |
| **Project** | `project/` | One project | that project's constraints |
| **Runtime** | `runtime/` | One request/session | retrieved docs, tool results |

Conversation / Persistent / Temporary context are runtime concerns handled by the context engine and
memory (Topic 10), not stored as files here.

**Principle:** never load a layer a task doesn't need. Selective loading = lower latency, tokens, cost.

> Layer folders are created as topics require them (YAGNI).
