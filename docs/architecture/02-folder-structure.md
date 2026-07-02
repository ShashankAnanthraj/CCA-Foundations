# Folder Structure (authoritative map)

Single source of truth for what each folder is for. Folders are created **as topics reach them**
(YAGNI) — this map documents the full intended tree so nothing is ambiguous.

```
CCAF/                              # repo root
├── README.md                      # entry point + quickstart
├── pyproject.toml                 # packaging; installs `core` + `providers`
├── .env.example                   # config template (copy to .env)
├── .gitignore
│
├── docs/
│   ├── architecture/              # canon: constitution, architecture, this map, ADRs
│   │   └── adr/                   # Architecture Decision Records (one per decision)
│   └── presentation/              # team deck outline + per-topic one-pagers
│
├── core/                          # CONTROL PLANE (kernel)
│   ├── config.py                  # env-driven settings (no secrets in code)
│   ├── providers.py               # provider-agnostic LLM interface + normalized types
│   ├── context/                   # context engine (layered, selective loading)   [later]
│   └── registry/                  # skill/agent/prompt/mcp registries              [later]
│
├── providers/                     # CAPABILITY — model adapters (swappable)
│   └── claude/                    # Anthropic implementation of core.providers
│
├── prompts/                       # CAPABILITY — hierarchical: base → role → task → output
├── skills/                        # CAPABILITY — composable expertise (SKILL.md each) [Topic 03]
├── agents/                        # CAPABILITY — single-responsibility agents        [Topic 08]
├── mcp/                           # CAPABILITY — independent MCP servers              [Topic 06/07]
├── knowledge/                     # CAPABILITY — modular KB (RAG/vector/graph-ready)  [later]
├── context/                       # CAPABILITY — context data layers (global/domain/…)
│
├── workflows/                     # EXECUTION — orchestrations (compose only)        [Topic 09]
├── projects/                      # EXECUTION — lightweight, reference shared units   [Topic 04]
│
├── topics/                        # PRESENTATION SPINE — 12 walkable modules
│   ├── README.md                  # index + status tracker
│   └── NN-<topic>/                # README (concept·talking points·run) + demo.py
│
├── platform/                      # OPS — deploy · observability · security          [Topic 12]
├── sdk/                           # DX — CLI + libraries                              [later]
└── tests/                         # pytest
```

`[later]` / `[Topic NN]` = created when we build that increment, to avoid empty-file noise (YAGNI).
