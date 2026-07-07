# Study Guide — Per Domain

For each area: **what AI-OS already teaches**, **what to study beyond it**, and **where**. Doc paths
are under `platform.claude.com/docs/en/…`. Anthropic **Partner Academy** + the gated **Exam Guide
PDF** are the authorities; use them first if you have partner access.

---

## 1. Claude API  *(official core area)*
**AI-OS covers:** Messages API, streaming, tokens & cost, adaptive thinking + effort (Topic 01);
structured output via `output_config.format` (Topic 02); the tool loop (Topic 05).
**Study beyond:**
- **Thinking/effort exactly:** `thinking: {type: "adaptive"}` (Fable 5 / Opus 4.8/4.7 / Sonnet 5 —
  `budget_tokens` is **removed**, 400s); `output_config: {effort: low|medium|high|xhigh|max}`.
- **Structured outputs — the three variants:** `output_config.format` (JSON schema), `strict: true`
  on a tool, and `client.messages.parse()`. Know the JSON-schema limitations (no min/max, no
  recursion, `additionalProperties: false` required).
- **Vision & PDF input:** image content blocks (base64/url), `document` blocks, the Files API
  (`files-api-2025-04-14`), citations. *(AI-OS gap — closing via exam-pack C2.)*
- **Batches** (`messages.batches`, 50% cost, unordered → key by `custom_id`), **token counting**
  (`messages.count_tokens`, never tiktoken).
- Docs: `build-with-claude/{adaptive-thinking,effort,structured-outputs,vision,pdf-support,
  prompt-caching,batch-processing,files}`.

## 2. MCP (Model Context Protocol)  *(official core area — AI-OS's strongest)*
**AI-OS covers:** a real MCP **server** (`mcp/echo_server`), a real **client bridge**
(`core/mcp_client.py`), tools/resources/prompts, stdio + remote HTTP, multi-server manifest, auth
via env, role toolsets (Topics 06–07).
**Study beyond:**
- **API-side MCP connector:** `mcp_servers=[{type:"url", …}]` **plus** a matching
  `tools=[{type:"mcp_toolset", mcp_server_name:…}]` (beta `mcp-client-2025-11-20`) — both halves
  required.
- **Managed-Agents MCP:** servers declared on the agent (no auth) + credentials in **vaults**.
- Docs: `agents-and-tools/tool-use/overview`, `shared` MCP connector notes, `managed-agents/mcp-connector`.

## 3. Claude Agent SDK  *(official core area — AI-OS re-implements, doesn't teach the real SDK)*
**AI-OS covers (as its own abstraction):** `core.agents` loop + router/pipeline/parallel/fan-out;
human-gate. Good for *concepts*.
**Study beyond (the real thing):**
- **Tool runner:** `@beta_tool` + `client.beta.messages.tool_runner(...)` (Python) — the SDK drives
  the agentic loop; contrast with the manual loop.
- **Managed Agents:** the **Agent (once) → Session (every run)** model; `agents.create` (model/
  system/tools/mcp_servers/skills live on the **agent**), `sessions.create` (references agent + env),
  event streaming, **environments**, **vaults**, outcomes, multiagent threads.
- **Agent design tradeoffs:** bash vs. dedicated tools; when to promote a tool (gating, staleness,
  rendering, parallelism); context editing vs. compaction vs. memory.
- Docs: `managed-agents/*` (overview, core, tools, events), `shared/agent-design`.

## 4. Claude Code  *(official core area)*
**AI-OS covers:** CLAUDE.md memory, settings/permissions, slash commands, hooks, MCP wiring
(Topic 11 — reference files, no demo).
**Study beyond:** real **plan mode**, the actual **hook lifecycle** events, **subagents** (Task
tool), custom slash commands & skills in Claude Code, CI/CD integration, MCP server setup in the CLI.
Docs: Claude Code section of the docs + Partner Academy.

## 5. Prompt Engineering & Structured Output  *(reported domain)*
**AI-OS covers:** Base→Role→Task→Output hierarchy, few-shot, personas, CoT, JSON schema (Topic 02;
the `PRECISE` checklist — *project coinage*, see reconciliation doc).
**Study beyond:** validation-retry loops, multi-pass review, tool-based structured extraction,
prescriptive tool descriptions ("call this when…"), and Anthropic's own prompting guidance. Do
**not** cite `PRECISE` as vendor terminology.

## 6. Context Management & Reliability  *(reported domain)*
**AI-OS covers:** token budgeting, a caching demo, multi-turn conversation (Topic 10; the `CALM`
checklist — *project coinage*).
**Study beyond:**
- **Prompt caching depth:** prefix-match invariant, breakpoint placement, `ttl: "5m"|"1h"`, ≤4
  breakpoints, model minimums, verifying via `cache_read_input_tokens`, prewarming. *(C3 closes the demo gap.)*
- **Context editing** (`clear_tool_uses_*`) vs. **compaction** (`compact_20260112`) vs. **memory** —
  and when each applies.
- **Reliability/evals:** LLM-as-judge, rubric grading, regression testing of prompts and agent
  trajectories. *(AI-OS gap — closing via C1.)*
- Docs: `build-with-claude/{prompt-caching,context-editing,compaction}`, `shared/prompt-caching`.

---

## Non-authoritative practice (use for feel, not fact)
Community study guides and Udemy practice exams exist (search "Claude Certified Architect
Foundations"). They're useful for question style; the Exam Guide PDF + Partner Academy remain the
source of record. If `ecanarys.com` is in the Claude Partner Network, request both.
