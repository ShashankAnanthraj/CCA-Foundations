# One-pager — Topic 09: Subagents & Cowork

**Slide headline:** Decompose → fan-out subagents → synthesize → human gate = a reliable research system.

**Demo beats (`topics/09-subagents-cowork/demo.py`):**
1. Decompose a question into 3 sub-questions (structured output). [Plan]
2. Fan-out: a researcher subagent answers all three in parallel. [Isolate]
3. Synthesize the answers into one grounded brief. [Detect]
4. Human gate: approve before "publishing" — the agent never acts alone. [Escalate]

**Say this:**
- "Break-down → fan-out → synthesize is the backbone of every research/analysis agent."
- "Subagents have isolated context — one bad thread can't poison the run."
- "Cowork = a gate between *propose* and *act*; irreversible steps need a human/policy."
- "Same shape maps to Claude Code subagents (Task tool) and Managed Agents multiagent."

**Top pitfall:** letting a subagent take the irreversible action itself — put the gate before publish/spend/delete.

**CCA‑F:** Agentic Architecture (27%) — the multi-agent half.
