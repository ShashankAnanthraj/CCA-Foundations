# AI‑OS — Team Presentation Outline

A 45–60 min walkthrough. Each topic = one slide/section backed by a live, runnable demo in
`topics/NN-*/`. Narrative goes foundational → advanced; every section reuses the shared core.

## Arc
1. **Why AI‑OS** — one platform, model/vendor-agnostic, reference for every Claude capability. Show the 3-plane architecture (`docs/architecture/01-architecture.md`).
2. **Foundations** (Topic 01) — models, Messages API, streaming, thinking/effort, tokens & cost. *Live demo.*
3. **Prompt Engineering** (Topic 02) — hierarchy, few-shot, personas, PRECISE, structured output.
4. **Skills** (Topic 03) — `SKILL.md`, progressive disclosure, custom + prebuilt.
5. **Tool Use** (Topic 05) — user-defined tools, tool-runner vs manual loop, server/client tools.
6. **MCP** (Topic 06) — client/server, tools·resources·prompts, stdio/SSE; build a server.
7. **Advanced MCP** (Topic 07) — multi-server, auth/vaults, security, remote MCP + agents.
8. **Agents** (Topic 08) — loop, orchestration (router/pipeline/parallel), Managed Agents, SPIDER.
9. **Subagents & Cowork** (Topic 09) — coordinator/threads, handoffs, parallel fan-out, human-in-loop.
10. **Projects & Artifacts** (Topic 04) — project context/knowledge, artifact generation.
11. **Context Management** (Topic 10) — token budgets, prompt caching, editing/compaction/memory, CALM.
12. **Claude Code Config** (Topic 11) — CLAUDE.md, settings, slash commands, hooks, MCP wiring.
13. **Production & Platform** (Topic 12) — batches, files, cost/observability, security, migration.
14. **Close** — extension points: add a provider/skill/agent/MCP without redesign (scale target).

## Delivery tips
- Keep each demo cheap (`AI_OS_MAX_TOKENS` small); pre-run once so cache is warm.
- For every capability, state **when to use it** and the **top pitfall** — that's what the CCA‑F exam rewards.

> Per-topic one-pagers live beside this file (`docs/presentation/NN-*.md`) and mirror each topic's README talking points.
