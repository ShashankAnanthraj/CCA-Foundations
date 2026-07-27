# Real Claude Agent SDK & Claude Code — Reference

> **Anthropic-specific by design.** This page documents Anthropic's *actual* products (which the exam
> tests), not AI-OS abstractions. It is **reference only** — no code lives here, so the vendor-agnostic
> `core/` and ADR-0001 (only `providers/claude/` imports the SDK) stay intact. AI-OS re-implements
> these ideas in `core.agents`; the exam expects the real thing. Verify against Anthropic docs before
> relying on any API shape — these move fast.

---

## Two ways to "run an agent" on the Claude API

### A. Tool runner (SDK helper) — you host the loop
The SDK drives the agentic loop for you: call model → execute your tools → feed results → repeat.
- **Python:** decorate tools with `@beta_tool`, then `client.beta.messages.tool_runner(model=…,
  tools=[…], messages=[…])`; iterate the runner (each yield is a message) or `until_done()`.
- **TypeScript:** `betaZodTool({...})` + `client.beta.messages.toolRunner(...)`.
- Use the **manual loop** when you need fine control (approval gates, custom logging): loop until
  `stop_reason == "end_turn"`, append the full `response.content` each turn, return `tool_result`
  blocks (with matching `tool_use_id`) in **one** user message.
- **Map to AI-OS:** `core.agents.Agent.run` + `provider.run_tools` ≈ the manual loop; the SDK tool
  runner is the managed convenience the project doesn't use.

### B. Managed Agents — Anthropic hosts the loop *and* a per-session container
Anthropic runs the agent loop and provisions a sandbox where tools (bash, file ops, code) execute.

**The mandatory flow — Agent (once) → Session (every run):**
```
agents.create(...)      # model, system, tools, mcp_servers, skills live HERE — created once, versioned
   → store agent.id
sessions.create(agent=agent.id, environment_id=env.id)   # every run; references the agent by ID
   → stream events, send user messages / tool results
```
- **Anti-pattern the exam will test:** putting `model`/`system`/`tools` on `sessions.create`, or
  calling `agents.create()` on every request. Those fields live on the **agent**; create it once,
  reuse the ID.
- **Environments** = reusable container templates (`config.type: "cloud" | "self_hosted"`, networking).
- **Vaults** = credential store; **MCP auth and API keys never enter the sandbox** — injected at
  egress by Anthropic-side proxies. MCP servers are declared on the agent (`mcp_servers`, no auth);
  credentials live in a vault attached via `vault_ids`.
- **Events** stream over SSE (`agent.message`, `agent.tool_use`, `session.status_idle`, …); **open the
  stream before sending** the kickoff, and break on `status_idle` with a terminal `stop_reason` (not
  idle alone) or `status_terminated`.
- **Outcomes** (`user.define_outcome` + rubric) run an iterate→grade→revise loop — the hosted analog
  of AI-OS's evals + approval gate.
- **Multiagent:** `multiagent: {type: "coordinator", agents: [...]}` on the agent; subagents run in
  their own **threads** — the real version of Topic 09's fan-out.
- **Map to AI-OS:** `core.profiles` (role = prompt + toolset) ≈ an agent config; `approval_gate` ≈
  permission policies (`always_ask` → `user.tool_confirmation`); `fan_out` ≈ multiagent threads.

**Tradeoff to know:** tool runner / manual loop = you host compute and control the loop; Managed
Agents = Anthropic hosts the loop + sandbox (persisted versioned configs, file mounts, MCP + skills).

---

## MCP on the API (beyond AI-OS's client bridge)
AI-OS's `core.mcp_client` is a correct *client* concept. The API also offers:
- **MCP connector:** `mcp_servers=[{type:"url", url, name}]` **and** a matching
  `tools=[{type:"mcp_toolset", mcp_server_name: name}]` (beta `mcp-client-2025-11-20`). Both halves
  are required — omitting the toolset is a validation error. Anthropic makes the MCP connection
  server-side.
- **Managed-Agents MCP:** servers on the agent + credentials in a vault (above).

---

## Agent Skills (real) vs. AI-OS `SkillRegistry`
Same `SKILL.md` + progressive-disclosure idea, three real loading surfaces:
- **Claude Code skills** (files the CLI discovers).
- **Messages API:** `container={"skills":[{"type":"anthropic","skill_id":"pptx",…}]}` + the
  `code_execution` tool + betas `code-execution-2025-08-25` and `skills-2025-10-02`.
- **Skills API** (`/v1/skills`) for managing custom skill definitions; Managed Agents reference them
  by `skill_id`.
- **Map to AI-OS:** `core.skills.SkillRegistry` mimics discovery + on-demand body load; the exam
  expects the real surfaces above.

---

## Claude Code — what to study for real
AI-OS Topic 11 covers the *concepts* (CLAUDE.md, settings, permissions, hooks, slash commands, MCP
wiring) as reference files. For the exam, know the actual product behaviors:
- **CLAUDE.md** memory hierarchy (project/user), and how it loads into context.
- **Permissions:** allow / ask / deny; how tool calls are gated.
- **Hooks:** the real lifecycle events (pre/post tool use, stop, etc.) — hooks are executed by the
  harness, not the model.
- **Slash commands & skills** in Claude Code; **subagents** via the Task tool.
- **Plan mode**, and CI/CD / headless usage.
- **MCP servers** configured in the CLI (stdio + remote), and auth.

---

## Agent design tradeoffs the exam rewards
- **Bash vs. dedicated tool:** start with bash for breadth; **promote** an action to a typed tool
  when you must gate it (irreversible/external), enforce staleness, render custom UI, or parallelize.
- **Context over long runs:** **context editing** (prune stale tool results/thinking) vs.
  **compaction** (summarize near the limit) vs. **memory** (persist across sessions) — often all three.
- **Caching for agents:** don't change tools/model mid-session (invalidates the cache); append a
  `role:"system"` message instead of editing the system prompt (Opus 4.8); use **tool search** to add
  tools without breaking the prefix.

**Bottom line:** AI-OS teaches the *shapes* (loop, orchestration, roles, skills, MCP). The exam grades
you on Anthropic's *real* implementations of them — study this page's products directly from the docs.
