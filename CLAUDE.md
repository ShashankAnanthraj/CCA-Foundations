# CLAUDE.md — AI-OS project memory

AI-OS is a model/vendor-agnostic Claude capability platform that doubles as a team-presentable
reference. Governed by [docs/architecture/00-constitution.md](docs/architecture/00-constitution.md).

## Conventions (follow these)
- **Provider-agnostic:** all model access goes through `core.providers.LLMProvider`. Only
  `providers/<vendor>/` may import a vendor SDK (ADR 0001).
- **DRY demos:** each `topics/NN-*/demo.py` **reuses** `core/` + shared capabilities — never
  re-implements a provider call, prompt, tool, or skill.
- **Many small files**, one responsibility each. Prompts are hierarchical (Base→Role→Task→Output).
- **Secrets** via `.env` only; never in code or prompts.
- **Cost is first-class:** demos print `usage` + estimated `$`.

## Layout (see docs/architecture/02-folder-structure.md)
`core/` kernel · `providers/` adapters · `prompts/ skills/ agents/ mcp/ context/` capabilities ·
`projects/ workflows/` execution · `topics/` presentation spine · `docs/` canon + deck.

## How to extend
| Add a… | Where | Contract |
|---|---|---|
| Provider | `providers/<name>/` | implement `core.providers.LLMProvider` |
| Skill | `skills/<name>/SKILL.md` | frontmatter (name, description) + body |
| Agent | compose via `core.agents` | single responsibility |
| MCP server | `mcp/<name>/` | independent, lazy-loaded |
| Topic | `topics/NN-*/` | README + demo that reuses shared code |

## Commands
```bash
pip install -e .            # or: pip install -e ".[mcp]" for the MCP topics
python topics/01-foundations/demo.py     # any topic
python -m compileall -q core providers topics mcp   # syntax check
```

## Frameworks (exam-relevant, working definitions — reconcile with vendor)
PRECISE (prompting) · SPIDER (agent reliability) · CALM (context) — under `prompts/frameworks/`.
