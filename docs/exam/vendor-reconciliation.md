# Vendor Reconciliation — Project Conventions vs. Real Anthropic

AI-OS is deliberately **vendor-agnostic** and coins its own names for several things. That's good
architecture, but for the exam you need the **real Anthropic terminology and products**. This table
tells you what to trust as-is, what is project coinage, and what the real equivalent is.

## Frameworks: PRECISE / SPIDER / CALM — **project coinage, NOT vendor terms**
The repo says so itself ("reconcile with vendor"). These are AI-OS teaching checklists, not Anthropic
acronyms. Learn the underlying ideas; **do not cite the acronyms on the exam.**

| Project acronym (`prompts/frameworks/`) | What it's really about | Real Anthropic framing to study |
|---|---|---|
| **PRECISE** (prompting) | Persona/result/examples/context/instructions/spec/eval | Anthropic prompt-engineering guidance: clear role, few-shot, explicit criteria, structured output, self-check. No official "PRECISE." |
| **SPIDER** (agent reliability) | Scope/plan/isolate/detect/escalate/recover | Anthropic **agent design** (bash-vs-dedicated tools, gating, human-in-loop) + reliability practices. No official "SPIDER." |
| **CALM** (context) | Cache/assemble/limit/manage-lifecycle | Real features: **prompt caching**, **context editing**, **compaction**, **memory**. No official "CALM." |

## Model IDs & pricing — **REAL and current ✅ (trust the project here)**
An earlier assessment called these "fictional." **That was wrong.** The IDs and pricing in
`core/config.py` and `providers/claude/adapter.py` match Anthropic's current catalog:

| Project uses | Real? | Context | Input/Output $ per 1M |
|---|---|---|---|
| `claude-opus-4-8` (default) | ✅ real, current | 1M | $5 / $25 |
| `claude-opus-4-7` | ✅ real | 1M | $5 / $25 |
| `claude-sonnet-5` | ✅ real | 1M | $3 / $15 (intro $2/$10 through 2026-08-31) |
| `claude-sonnet-4-6` | ✅ real | 1M | $3 / $15 |
| `claude-haiku-4-5` | ✅ real | 200K | $1 / $5 |
| `claude-fable-5` | ✅ real (most capable) | 1M | $10 / $50 |

Notes for the exam: **use exact IDs, no date suffixes** (except Haiku's optional
`claude-haiku-4-5-20251001`); `claude-opus-4-8` is the default choice unless told otherwise;
`claude-fable-5` has a different API surface (thinking always on; `refusal` stop reason). The
project's model handling is a correct reference — the gap is only a documented **task→model
selection methodology**, not the IDs.

## Abstractions: what the project re-implements vs. the real product
The exam tests Anthropic's actual tooling. Map each `core/` abstraction to the real thing:

| AI-OS abstraction | Real Anthropic equivalent to study |
|---|---|
| `core.providers.LLMProvider` (vendor-neutral interface) | The **Anthropic SDK** directly (`client.messages.create`, `.stream`, `.parse`, `.count_tokens`). The agnostic layer is an *architecture choice*, not an exam topic. |
| `core.agents` loop + `run_tools` | The **tool runner** (`@beta_tool` + `messages.tool_runner`) and the manual agentic loop; **Managed Agents** for server-run loops. |
| `router / pipeline / parallel_agents / fan_out` | Agent orchestration patterns you build on the SDK; **Managed Agents multiagent** (coordinator + threads) for the hosted version. |
| `core.profiles` (role = prompt + toolset) | Agent config (`agents.create` with `system`/`tools`/`skills`) + **permission policies**; Claude Code subagents. |
| `core.mcp_client` (client bridge) | Correct MCP concept ✅. On the API side, the **MCP connector** (`mcp_servers` + `mcp_toolset`); in Managed Agents, MCP servers + **vaults**. |
| `SkillRegistry` + `SKILL.md` | Real **Agent Skills**: Claude Code skills, the Messages-API `container.skills`, and the Skills API — same `SKILL.md` idea, different loading surfaces. |
| `Conversation` + prompt caching demo | Real **prompt caching** semantics (prefix match, TTL, breakpoints, `cache_read_input_tokens`), **context editing**, **compaction**. |
| `approval_gate` | Real **permission policies** (`always_ask` → `tool_confirmation`) in Managed Agents; human-in-the-loop in Claude Code. |

## Thinking / effort — the project is aligned ✅
Demos use `thinking: {type: "adaptive"}` and `output_config.effort` — the **current** API. Just know
the hard rules for the exam: `budget_tokens` is **removed** on Fable 5 / Opus 4.8/4.7 / Sonnet 5
(400); sampling params (`temperature`/`top_p`/`top_k`) are rejected on those models; `thinking.display`
defaults to `"omitted"`.

## One-line takeaway
Trust the project's **model IDs, API-call shapes, thinking/effort usage, and MCP concepts**. Replace
its **coined acronyms** and **re-implemented agent/skill/caching abstractions** with the **real
Claude Agent SDK, Claude Code, Agent Skills, and caching/context features** when you study for the
exam.
