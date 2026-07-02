# Topic 09 — Subagents & Cowork

**Purpose:** Coordinate many agents (and humans) on one goal — the "Multi-Agent Research System" exam
scenario made concrete (CCA‑F *Agentic Architecture*, 27%).

## Concept
- **Subagents:** an orchestrator delegates independent subtasks to worker agents. Here: decompose a
  question → `fan_out` a researcher over the sub-questions in **parallel** → **synthesize**.
- **Coordinator / handoffs / threads:** one agent routes work to others and merges results. Each
  subagent has isolated context (no cross-contamination) — that isolation is a feature (SPIDER: Isolate).
- **Cowork (human-in-the-loop):** agents and humans collaborate. High-risk/irreversible steps pass
  through an `approval_gate` — the agent proposes, a human/policy disposes (SPIDER: Escalate).
- **Where this runs in the ecosystem:**
  - **Claude Code subagents** — the `Task` tool spawns subagents for parallel/independent work.
  - **Managed Agents multiagent** — an agent declares a coordinator roster (`multiagent`) and delegates
    across session threads. (See `topics/08-agents/managed_agents.md`.)

## Pattern shape
```
question --decompose--> [q1, q2, q3] --fan-out(parallel)--> [a1, a2, a3]
                                                   \--synthesize--> brief --human gate--> publish?
```

## When to use
| Situation | Reach for |
|---|---|
| Independent subtasks over a work-list | Subagent **fan-out** |
| Need to merge many results | **Synthesize** step |
| Irreversible/expensive final action | **Human gate** |
| Fixed order instead of fan-out | **Pipeline** (Topic 08) |

## Talking points
1. Break-down → fan-out → synthesize is the backbone of research/analysis agents.
2. Subagent **isolation** prevents one bad thread from poisoning the whole run.
3. Cowork = the agent never takes the irreversible step alone — a gate stands between propose and act.
4. Same pattern maps to Claude Code subagents and Managed Agents multiagent.

## Run it
```bash
python topics/09-subagents-cowork/demo.py
```

## Reuses (DRY)
- `core.fan_out`, `core.Agent`, `core.approval_gate` — orchestration + human gate
- `core.assemble_system` + `prompts/role/researcher.md`, `prompts/role/synthesizer.md`
- `providers.claude.ClaudeProvider.structured_chat` — decomposition
- `prompts/frameworks/spider.md` — reliability mapping
