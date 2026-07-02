# AI‑OS — Claude Capability Reference Platform

A production-grade, **model/vendor-agnostic** platform that also serves as a **team-presentable reference** covering every Claude capability — from foundations to advanced MCP, agents, subagents, and cowork.

Built under the [AI‑OS Master Constitution](docs/architecture/00-constitution.md): modular, reusable, token- and context-efficient, single-responsibility, many small files.

## How this repo is organized

| Layer | Folders | Role |
|---|---|---|
| **Control plane** | `core/` | Kernel: config, context engine, registries, provider-agnostic interfaces |
| **Capability plane** | `providers/` `prompts/` `skills/` `agents/` `mcp/` `knowledge/` `context/` | Reusable, single-responsibility building blocks |
| **Execution plane** | `workflows/` `projects/` | Compose capabilities; hold no logic of their own |
| **Presentation** | `topics/` `docs/` | The walkable, demo-able spine you present to the team |
| **Ops / DX** | `platform/` `sdk/` `tests/` | Deploy, observability, security, CLI |

Full map: [docs/architecture/02-folder-structure.md](docs/architecture/02-folder-structure.md).

## The presentation spine — `topics/`
Twelve self-contained modules, each with a one-screen README (concept → talking points → run this) and a working demo that **reuses** the shared components. See [topics/README.md](topics/README.md).

## Quickstart

```bash
# 1. Create a virtual environment
python -m venv .venv
# Windows:  .venv\Scripts\activate     macOS/Linux: source .venv/bin/activate

# 2. Install
pip install -e .          # or: pip install anthropic python-dotenv pydantic

# 3. Configure your key
copy .env.example .env    # macOS/Linux: cp .env.example .env
#   then edit .env and set ANTHROPIC_API_KEY

# 4. Run the first topic
python topics/01-foundations/demo.py
```

## Status
Skeleton + **Topic 01 Foundations** delivered. Remaining topics build one increment at a time — see the tracker in [topics/README.md](topics/README.md).
