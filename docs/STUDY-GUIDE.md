# CCA‑F Study Guide — topics → domains → frameworks

Use AI-OS as your hands-on study path for the **Claude Certified Architect – Foundations (CCA‑F)** exam
(60 scenario MCQs · 120 min · pass 720/1000). Each topic below is a runnable demo + a one-page talking
sheet in `docs/presentation/`.

> The prep vendor (claudecertifiedarchitects.com) is independent of Anthropic. SPIDER / PRECISE / CALM
> are its proprietary frameworks; the versions here are AI-OS **working definitions** — reconcile the
> exact letter expansions against the vendor's own materials.

## Domain coverage map
| CCA‑F domain | Weight | Topics that cover it | Framework |
|---|---|---|---|
| Agentic Architecture | 27% | 05 Tool Use · 08 Agents · 09 Subagents & Cowork | **SPIDER** |
| Claude Code Configuration | 20% | 03 Skills · 11 Claude Code Config | — |
| Prompt Engineering | 20% | 02 Prompt Engineering | **PRECISE** |
| Tool Design & MCP | 18% | 05 Tool Use · 06 MCP · 07 Advanced MCP | — |
| Context Management | 15% | 04 Projects & Artifacts · 10 Context Management | **CALM** |
| (Foundational / cross-cutting) | — | 01 Foundations · 12 Production & Platform | — |

## Frameworks (memorize these)
- **PRECISE** (prompting): Persona · Result · Examples · Context · Instructions · Specification · Evaluation
- **SPIDER** (agent reliability): Scope · Plan · Isolate · Detect · Escalate · Recover
- **CALM** (context): Cache · Assemble selectively · Limit · Manage
Details: `prompts/frameworks/{precise,spider,calm}.md`.

## The 6 exam scenarios → which topics prepare you
| Scenario | Lean on |
|---|---|
| Customer Support Resolution Agent | 08 (router) · 05 (tools) · 09 (human gate) |
| Code Generation with Claude Code | 11 · 02 |
| Multi-Agent Research System | 09 (decompose→fan-out→synthesize) · 10 |
| Developer Productivity with Claude | 11 · 03 |
| Claude Code for CI | 11 (hooks/permissions) |
| Structured Data Extraction | 02 (structured output) · 10 (caching) |

## Suggested sprint (2–3 weeks)
1. **Frameworks first** — read the three `prompts/frameworks/*.md`, build recall.
2. **Run every demo** in order (01→12); explain each design choice out loud.
3. **Scenario drills** — for each of the 6 scenarios, state the right pattern + top pitfall.
4. **Practice bank + timed sims** (vendor) — target ≥750 before booking.

## Readiness checklist
- [ ] Can reproduce PRECISE, SPIDER, CALM from memory and apply each to a scenario.
- [ ] Can explain Agent-vs-Session (Managed Agents) and router/pipeline/parallel/fan-out.
- [ ] Can explain prompt caching prefix rule + how to verify a hit.
- [ ] Can wire an MCP server into Claude Code and via the API connector.
- [ ] Can configure CLAUDE.md + permissions + a hook + a slash command.
- [ ] Timed-sim score ≥ 750.
