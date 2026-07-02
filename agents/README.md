# Agents — single-responsibility, composed by orchestration

An **agent** here is small: a provider + a system prompt + (optionally) tools. It has **one
responsibility**. Complex behavior comes from *composing* agents, not from one God Agent
(Constitution: Agent Design).

## The building block
`core.agents.Agent(name, provider, system, tools=?, handlers=?)` → `.run(task) -> AgentResult`.
If the agent has tools, `.run` uses the tool loop (Topic 05); otherwise a single call.

## Orchestration patterns (in `core/agents.py`)
| Pattern | Function | Shape | Use when |
|---|---|---|---|
| **Router** | `router(...)` | classify → dispatch to one agent | inputs vary; pick the right specialist |
| **Pipeline** | `pipeline(...)` | A → B → C (output feeds next) | fixed sequential stages |
| **Parallel** | `parallel_agents(...)` | same task → many agents at once | diverse perspectives / redundancy |
| **Fan-out** | `fan_out(...)` | one agent → many subtasks at once | subagents over a work-list (Topic 09) |
| **Human gate** | `approval_gate(...)` | pause for approval | high-risk / irreversible actions |

## Reliability
Every orchestration should be checked against **SPIDER** (`prompts/frameworks/spider.md`):
Scope · Plan · Isolate · Detect · Escalate · Recover.

## Managed Agents (server-hosted) vs self-hosted (here)
- **Self-hosted (this repo):** you run the loop; full control, host your own compute. Topics 08–09.
- **Managed Agents:** Anthropic runs the loop + a per-session container. Create an Agent once, start
  Sessions per run, stream events. See `topics/08-agents/managed_agents.md`.
