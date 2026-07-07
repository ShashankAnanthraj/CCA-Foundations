# Coverage Map — AI-OS vs. the Exam

How far each AI-OS topic gets you toward the four official areas (Claude Code · Claude Agent SDK ·
Claude API · MCP) and the reported five domains. Ratings: **✅ Covered** (solid, hands-on) ·
**◑ Partial** (concept present, but shallow or via a re-implementation) · **✗ Gap** (absent or only
mentioned).

| # | Topic | Maps to | Rating | Note |
|---|---|---|---|---|
| 01 | Foundations | Claude API | ✅ | Real Messages API, tokens, cost, streaming, adaptive thinking + effort. |
| 02 | Prompt Engineering | Prompt & Structured Output | ✅ | Hierarchy, few-shot, JSON-schema structured output — solid. |
| 03 | Skills | Claude Code / Agent SDK | ◑ | `SKILL.md` + progressive disclosure done well; but exam skills live in Claude Code / Agent SDK / API `container`, not this custom registry. |
| 04 | Projects & Artifacts | Context | ◑ | "Project = reference bundle" is a project abstraction, not the real Claude.ai Projects/Artifacts feature set. |
| 05 | Tool Use | Tool Design & MCP | ✅ | Real tool loop, `tool_choice`, parallel tool use, server/client taxonomy. |
| 06 | MCP core | Tool Design & MCP | ✅ | Real MCP server + client over stdio — a genuine exam pillar. |
| 07 | Advanced MCP | Tool Design & MCP | ✅ | Multi-server, remote/HTTP, the MCP client bridge, role profiles, auth notes. Strongest area. |
| 08 | Agents | Agentic Architecture | ◑ | Orchestration patterns are sound, but re-implemented in `core.agents` — **not** the real Claude Agent SDK (tool runner, Managed Agents). |
| 09 | Subagents & Cowork | Agentic Architecture | ◑ | Fan-out/synthesize/gate concept is right; SDK/Managed-Agents subagents (threads, sessions) not shown. |
| 10 | Context Management | Context & Reliability | ◑ | Token budgets + one caching demo; missing caching TTL tiers, multiple breakpoints, context editing, compaction. |
| 11 | Claude Code Config | Claude Code | ◑ | CLAUDE.md, settings, hooks, slash commands as reference; no deep plan-mode / real hook lifecycle / CI. |
| 12 | Production & Platform | (platform) | ◑ | Cost/observability executed; batches/Files/platforms documented, not exercised. |

## Cross-cutting gaps (not owned by any topic)
- **✗ Real Claude Agent SDK** — tool runner (`@beta_tool` / `messages.tool_runner`), Managed Agents
  (agents → sessions → environments, event streams, vaults).
- **✗ Evaluations / testing of prompts & agent trajectories** — no eval harness, LLM-as-judge, or
  regression testing (this repo's `tests/` covers code, not model quality). *(Closing via exam-pack C1.)*
- **◑ Prompt caching depth** — TTL (`ttl: "1h"`), multiple breakpoints, invalidation audit, prewarm.
- **✗ Vision / PDF input** — multimodal content blocks not demonstrated. *(Closing via C2.)*
- **✗ Structured-output nuances** — `output_config.format` vs. strict tool use vs. `messages.parse()`.
- **◑ Model selection** — the project's model IDs are **correct and current** (see
  [vendor-reconciliation.md](vendor-reconciliation.md)); what's missing is a task→model methodology.

## Blunt readiness estimate
- **Strong (exam-ready with light review):** MCP (Topics 05–07), core prompt engineering (02),
  API foundations (01).
- **Partial (know the concept, learn the real product):** agents/subagents (08–09), Claude Code
  config (11), context/caching (10).
- **Not covered (study elsewhere):** the real Claude Agent SDK, evaluations, vision/PDF, caching
  depth, structured-output variants.

**Bottom line:** studying + building this project plausibly gets you **~60–70% of the conceptual
way**. Close the gaps above with the official Exam Guide, Anthropic Partner Academy, and the
Anthropic docs linked in [study-guide.md](study-guide.md).
