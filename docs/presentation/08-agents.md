# One-pager — Topic 08: Agents

**Slide headline:** An agent is a loop with a goal. Reliability comes from composition + SPIDER.

**Demo beats (`topics/08-agents/demo.py`):**
1. **Router** → classifies a coding question, dispatches to the `code` specialist. [Scope]
2. **Pipeline** → extractor → headline, output feeds the next stage. [Plan]
3. **Parallel** → optimist + skeptic answer the same proposal at once. [Isolate]

**Say this:**
- "Don't build a God Agent. Compose single-responsibility agents with router / pipeline / parallel / fan-out."
- "Build an agent only when the task is multi-step, valuable, viable, and errors are recoverable."
- "SPIDER = Scope · Plan · Isolate · Detect · Escalate · Recover — the reliability checklist."
- "Managed Agents = same ideas, Anthropic runs the loop: Agent once → Session per run."

**Top pitfall:** putting `model`/`system`/`tools` on a Managed-Agents *session* — they belong to the *agent*; the session is just a pointer.

**CCA‑F:** Agentic Architecture (27%) — the highest-weight domain.
