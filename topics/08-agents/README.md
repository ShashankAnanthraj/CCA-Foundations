# Topic 08 — Agents

**Purpose:** Turn the tool loop into *systems* that reliably do multi-step work. This is the biggest
exam domain (CCA‑F *Agentic Architecture*, 27%).

## Concept
- **An agent = a loop with a goal.** Our `Agent` = provider + system prompt + optional tools; `.run()`
  uses the Topic 05 tool loop when tools are present.
- **When to build an agent** (all four should hold): the task is multi-step & hard to fully specify;
  the outcome justifies cost/latency; Claude is capable at it; errors are catchable/recoverable.
- **Orchestration patterns:**
  - **Router** — classify the input, dispatch to a specialist.
  - **Pipeline** — fixed sequential stages, output feeds the next.
  - **Parallel** — same task to several agents (diverse views / redundancy).
  - **Fan-out** — one agent over many subtasks (Topic 09).
- **SPIDER reliability:** Scope · Plan · Isolate · Detect · Escalate · Recover
  (`prompts/frameworks/spider.md`) — check every agent against it.
- **Managed Agents:** server-hosted alternative (Agent-once → Session-per-run). See `managed_agents.md`.

## When to use which pattern
| Situation | Pattern |
|---|---|
| Inputs vary; need the right specialist | Router |
| Known ordered steps | Pipeline |
| Want multiple perspectives / a vote | Parallel |
| A work-list of independent items | Fan-out (Topic 09) |
| High-risk / irreversible action | Human gate (`approval_gate`) |

## Talking points
1. Don't build a God Agent — compose single-responsibility agents.
2. Router/Pipeline/Parallel cover most production topologies; pick by the shape of the work.
3. Reliability is designed in with SPIDER, not bolted on — especially Detect + Escalate + Recover.
4. Self-hosted (this demo) vs Managed Agents: same concepts, different who-runs-the-loop.

## Run it
```bash
python topics/08-agents/demo.py
```

## Reuses (DRY)
- `core.Agent`, `core.router`, `core.pipeline`, `core.parallel_agents` — orchestration layer
- `providers.claude.ClaudeProvider` (+ `run_tools`, `structured_chat` under the hood)
- `prompts/frameworks/spider.md` — reliability checklist
