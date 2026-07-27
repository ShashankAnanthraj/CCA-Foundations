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

Full instructions — every demo, provider switching, the MCP bridge, and validation — are in
**[docs/RUNNING.md](docs/RUNNING.md)**.

## Validate

Key-free and free of cost:

```bash
python -m compileall -q core providers topics mcp   # syntax check
pip install -e ".[mcp,dev]" && pytest -q            # offline test suite (FakeProvider, no API key)
```
CI runs both on every push (`.github/workflows/ci.yml`).

## Exam readiness (Claude Certified Architect: Foundations)
Studying this repo for the CCA-F exam? Read **[docs/exam/](docs/exam/)** first — it maps each topic to
the real exam domains, flags the gaps (evals, vision/PDF, real Agent SDK, caching depth), and
reconciles the project's coined frameworks with actual Anthropic terminology. Honest take: a strong
conceptual foundation, **not sufficient alone** — pair it with the official Exam Guide + Partner Academy.

## Status
All 12 topics are delivered — see the tracker in [topics/README.md](topics/README.md). The platform
also ships an MCP **client bridge** (`core/mcp_client.py`) so agents can use external MCP servers
(filesystem, GitHub, docs, deploy, …); see [topics/07-advanced-mcp/](topics/07-advanced-mcp/).
