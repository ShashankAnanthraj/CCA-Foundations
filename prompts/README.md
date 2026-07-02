# Prompts — hierarchical & inherited (no duplication)

Per the Constitution, prompts compose top-down; shared behavior is written **once** and inherited:

```
Base  →  Role  →  Task  →  Output-Spec  →  User Request
```

| Layer | Folder | Answers | Changes… |
|---|---|---|---|
| **Base** | `base/` | Global behavior & guardrails for all of AI-OS | rarely |
| **Role** | `role/` | Persona/expertise (architect, reviewer, researcher…) | per agent |
| **Task** | `task/` | The specific job & steps | per task |
| **Output-Spec** | `output/` | Exact response shape (JSON schema, format rules) | per contract |

**Assembly:** a caller concatenates `Base + Role + Task + Output-Spec` into the `system` prompt, then
sends the user turn as a message. Because Base/Role are reused across tasks, they stay in the cached
prefix (see Topic 10 — Context Management) and cost ~nothing on repeat.

**Rule:** never paste the same instruction into two prompts. Put it in the lowest layer that owns it.

> `role/`, `task/`, `output/` are populated as topics need them (YAGNI). `base/base_system.md` exists now.
