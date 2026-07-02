# AI‑OS Architecture

## Purpose
Define the high-level structure so every component has one home and one responsibility.

## Three planes (Separation of Concerns)

```
┌──────────────────────────────────────────────────────────────┐
│  PRESENTATION      topics/ · docs/      (walkable, demo-able)  │
├──────────────────────────────────────────────────────────────┤
│  EXECUTION         workflows/ · projects/   (compose only)    │
├──────────────────────────────────────────────────────────────┤
│  CAPABILITY        providers/ prompts/ skills/ agents/ mcp/   │
│                    knowledge/ context/   (reusable units)     │
├──────────────────────────────────────────────────────────────┤
│  CONTROL           core/  (config · context-engine · registry │
│                           · provider-agnostic interfaces)     │
└──────────────────────────────────────────────────────────────┘
```

**Rule of dependency:** upper planes depend on lower planes, never the reverse.
`topics/` and `projects/` **compose** capabilities; they hold no business logic.

## Key decisions
- **Provider-agnostic core.** All model access goes through `core.providers.LLMProvider`.
  Concrete adapters (`providers/claude/…`) are swappable; nothing above the capability plane
  imports a vendor SDK directly. See [ADR 0001](adr/0001-provider-agnostic-core.md).
- **Layered context.** `core.context` assembles per-request context from Global → Domain →
  Project → Task → Runtime layers, loading only what's needed (Context Engineering).
- **Hierarchical prompts.** `prompts/` = Base → Role → Task → Output-Spec; inherited, never repeated.
- **DRY demos.** Each `topics/NN-*/demo.py` **reuses** shared capabilities — it never re-implements
  a provider call, a prompt, or a tool.

## Extension points (how to grow to the scale target without redesign)
| Add a… | Drop it in | It must implement / follow |
|---|---|---|
| Model provider | `providers/<name>/` | `core.providers.LLMProvider` |
| Skill | `skills/<name>/` | Skill spec (Purpose…Best Practices) |
| Agent | `agents/<name>/` | Single responsibility + typed I/O |
| MCP server | `mcp/<name>/` | Independent, lazy-loaded, one transport |
| Workflow | `workflows/<name>/` | Composition of agents/skills only |
| Project | `projects/<name>/` | References shared components only |

## Risks & mitigations
- **Scope sprawl** → every artifact needs a purpose; topics index tracks status.
- **Vendor lock-in** → provider-agnostic interface enforced by the dependency rule.
- **Context bloat / cost** → selective loading + prompt caching (see Topic 10).

## Future improvements
Registry auto-discovery, RAG over `knowledge/`, observability hooks in `platform/`, CLI in `sdk/`.
