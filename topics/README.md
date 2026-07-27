# Topics — the presentation spine

Twelve self-contained modules covering every Claude capability. Each folder has a one-screen
`README.md` (concept → when to use → talking points → run this) and a `demo.py` that **reuses**
the shared `core/`, `providers/`, `prompts/`, `skills/`, `agents/`, `mcp/` — never duplicating them.

Build order is foundational → advanced; each topic ships something you can demo live.

| # | Topic | Covers | CCA‑F domain | Status |
|---|---|---|---|---|
| 01 | Foundations | Models, Messages API, streaming, thinking/effort, tokens & cost | — | ✅ Done |
| 02 | Prompt Engineering | Hierarchy, few-shot, personas, CoT, structured output, PRECISE | Prompt (20%) | ✅ Done |
| 03 | Skills | `SKILL.md`, progressive disclosure, custom + prebuilt | Claude Code (20%) | ✅ Done |
| 04 | Projects & Artifacts | Project context/knowledge, artifact generation | Context (15%) | ✅ Done |
| 05 | Tool Use | User-defined tools, tool_choice, runner vs manual loop, server/client tools | Tool & MCP (18%) | ✅ Done |
| 06 | MCP (core) | Client/server, tools·resources·prompts, stdio/SSE, build a server | Tool & MCP (18%) | ✅ Done |
| 07 | Advanced MCP | Multi-server, auth/vaults, security, remote MCP + agents | Tool & MCP (18%) | ✅ Done |
| 08 | Agents | Loop, orchestration (router/pipeline/parallel), Managed Agents, SPIDER | Agentic (27%) | ✅ Done |
| 09 | Subagents & Cowork | Coordinator/threads, handoffs, parallel fan-out, human-in-loop | Agentic (27%) | ✅ Done |
| 10 | Context Management | Token budgets, prompt caching, editing/compaction/memory, CALM | Context (15%) | ✅ Done |
| 11 | Claude Code Config | CLAUDE.md, settings, permissions, slash commands, hooks, MCP wiring | Claude Code (20%) | ✅ Done |
| 12 | Production & Platform | Batches, files, cost/observability, security, migration | — | ✅ Done |

**Run any topic:** `python topics/NN-<topic>/demo.py` (needs `.env` with `ANTHROPIC_API_KEY`).

> The **CCA‑F domain** weights above are third-party/**unverified** — the project is built to them, but
> the official blueprint is partner-gated. **Studying for the exam?** See [../docs/exam/](../docs/exam/):
> coverage map, gap analysis, and a reconciliation of the coined frameworks (PRECISE/SPIDER/CALM) and
> abstractions with real Anthropic terminology.
