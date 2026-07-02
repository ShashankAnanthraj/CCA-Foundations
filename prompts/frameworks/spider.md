# SPIDER — agent reliability checklist

Agents fail in ways single calls don't: they loop, act on bad data, or take irreversible actions.
SPIDER is a six-point checklist for making an agentic system reliable in production.

| Letter | Principle | What it means | Where it shows up in AI-OS |
|---|---|---|---|
| **S** | **Scope** | Give the agent one clear responsibility and hard boundaries. | `Agent` = single responsibility; no God Agents |
| **P** | **Plan** | Decompose before acting; know the steps. | Decompose → subtasks (Topic 09) |
| **I** | **Isolate** | Least-privilege tools; isolate subagents so one failure can't cascade. | Separate agents/tools; MCP servers as trust boundaries |
| **D** | **Detect** | Validate every tool result and output; add guardrails. | Structured outputs, `is_error` tool results, checks |
| **E** | **Escalate** | Route low-confidence / high-risk actions to a human. | `approval_gate` (human-in-the-loop) |
| **R** | **Recover** | Retries, fallbacks, graceful degradation, loop caps. | `max_iters` in the tool loop; SDK auto-retries |

## How to apply it
- **Before building:** write down S and P — scope + plan. Most agent failures are really scope failures.
- **While building:** wire D and R — validation + recovery — into the loop, not bolted on after.
- **Before shipping:** decide E — which actions require a human. Irreversible/expensive ⇒ gate them.

## Cost/latency note
Reliability isn't free — detection and escalation add calls and steps. Match rigor to blast radius:
a read-only summarizer needs little; an agent that spends money or deletes data needs all six.

> **Note:** SPIDER is AI-OS's working checklist for the CCA‑F *Agentic Architecture* domain's
> "reliability patterns." If the exam vendor publishes a different letter expansion, reconcile here —
> the practices (scope, plan, isolate, detect, escalate, recover) are what the exam tests.
