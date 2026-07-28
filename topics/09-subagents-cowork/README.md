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

## Orchestration Patterns

If you're preparing for the **Claude Certified Architect (CCA-F/CCA-P)** or designing AI agent systems, **Fan-In** and **Fan-Out** are just two orchestration patterns. Anthropic now groups these into broader **workflow** and **multi-agent coordination** patterns. ([Claude][1])

### Comprehensive Pattern List

| Pattern                                | Description                                                                           | Best Use Case                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Sequential Pipeline**                | One agent's output becomes the next agent's input.                                    | ETL, document processing, multi-step reasoning     |
| **Fan-Out / Fan-In (Parallelization)** | Split work across multiple agents, then aggregate results.                            | Large codebases, research, multi-document analysis |
| **Routing**                            | Decide which specialized agent should handle a task.                                  | Customer support, domain experts                   |
| **Orchestrator-Worker**                | Main agent plans work, delegates to workers, combines answers.                        | Complex software engineering                       |
| **Evaluator-Optimizer**                | One agent generates, another critiques and improves iteratively.                      | High-quality content, code generation              |
| **Generator-Verifier**                 | Generator produces answer; verifier validates correctness.                            | Math, SQL, legal, compliance                       |
| **Reflection / Self-Critique**         | Same agent reviews and improves its own response.                                     | Writing, reasoning                                 |
| **Voting / Consensus**                 | Multiple agents independently solve the same problem; majority or weighted vote wins. | Safety, decision making                            |
| **Debate**                             | Agents argue for different solutions before final decision.                           | Strategic planning, ambiguous problems             |
| **Map-Reduce**                         | Break large input into chunks (Map), summarize/combine (Reduce).                      | Long PDFs, log analysis                            |
| **Hierarchical Agents**                | Multi-level delegation (manager → leads → workers).                                   | Enterprise automation                              |
| **Shared Memory Agents**               | Multiple agents collaborate using shared state or memory.                             | Long-running workflows                             |
| **Message Bus/Event Driven**           | Agents communicate through events rather than directly.                               | Enterprise agent ecosystems                        |
| **Capability-Based Agents**            | Route work based on available tools or skills.                                        | Tool-heavy AI assistants                           |
| **Escalation Pattern**                 | Delegate difficult tasks to a stronger or specialized agent.                          | Cost optimization                                  |
| **Agent Teams**                        | Persistent specialist agents collaborate over multiple tasks.                         | Long-running projects                              |

---

### 1. Fan-Out / Fan-In ⭐⭐⭐⭐⭐

```
            User
              |
      Orchestrator
      /    |    \
   Agent1 Agent2 Agent3
      \    |    /
      Aggregator
          |
      Final Answer
```

Example:

* Search GitHub
* Search Documentation
* Search StackOverflow

Merge results into one response.

**Advantages**

* Fast
* Parallel execution
* Independent context

**Disadvantages**

* Higher token cost
* Requires aggregation logic

Perfect for:

* Research
* Code reviews
* Security scans
* Document analysis

([Claude][1])

---

### 2. Sequential Pipeline

```
Input
  ↓
Research
  ↓
Analysis
  ↓
Implementation
  ↓
Review
  ↓
Output
```

Example:

```
User asks:
Create REST API

↓

Requirements Agent

↓

Design Agent

↓

Coding Agent

↓

Testing Agent
```

Best when every step depends on the previous one.

---

### 3. Routing Pattern

```
                User
                  |
           Router Agent
      /        |        \
 SQL Expert  Legal AI  Coding AI
```

Instead of every agent doing everything:

```
if SQL question
      ↓
SQL Agent

if Legal
      ↓
Legal Agent

if Python
      ↓
Python Agent
```

Very common in enterprise AI.

---

### 4. Orchestrator-Worker ⭐⭐⭐⭐⭐

```
              Manager
          /      |      \
      Worker1 Worker2 Worker3
           \      |      /
          Final Synthesis
```

Manager decides:

> Break task into 10 subtasks.

Workers solve independently.

Manager combines.

Claude Code heavily uses this orchestration style for large engineering tasks. ([Claude][2])

---

### 5. Evaluator-Optimizer

```
Generator
     ↓
Evaluator
     ↓
Feedback
     ↓
Generator
     ↓
Evaluator
```

Loop until:

```
Score > 90%
```

Example:

```
Generate SQL

↓

Check SQL

↓

Improve SQL

↓

Check Again
```

Excellent for:

* Documentation
* Production code
* Emails
* Reports

---

### 6. Generator-Verifier

Very similar, but instead of improving repeatedly:

```
Generator

↓

Verifier

↓

Pass / Fail
```

Example:

```
Generate JSON

↓

Validate JSON Schema

↓

Return
```

Simple.

Fast.

Reliable.

---

### 7. Reflection

Same model.

```
Answer

↓

Review Yourself

↓

Improve
```

Prompt:

```
Answer.

Now critique your answer.

Now improve it.
```

No second model needed.

---

### 8. Voting (Consensus)

```
Problem

↓

5 Agents

↓

Answer A
Answer A
Answer B
Answer A
Answer C

↓

Majority

↓

Answer A
```

Used for:

* Medical
* Finance
* Safety

---

### 9. Debate Pattern

```
Agent A

↓

Agent B challenges

↓

Agent A defends

↓

Judge
```

Example:

```
Should company migrate?

↓

Pro Agent

↓

Con Agent

↓

Judge
```

Great for strategic decisions.

---

### 10. Map-Reduce

```
Large PDF

↓

Split

↓

Summarize Part1

Summarize Part2

Summarize Part3

↓

Merge
```

Perfect for:

* 500-page books
* Large log files
* Multiple reports

---

### 11. Hierarchical Agents

```
CEO Agent

↓

Engineering Manager

↓

Backend Lead

↓

Developer
```

Useful in very large enterprise workflows.

---

### 12. Shared Memory Pattern

```
Agent A

↓

Shared Memory

↑

Agent B

↓

Shared Memory

↑

Agent C
```

All agents read/write to the same knowledge base.

Useful for long-running projects.

---

### 13. Message Bus

```
Agent A

↓

Event Bus

↓

Agent B

↓

Event Bus

↓

Agent C
```

Agents communicate through events rather than calling each other directly.

Used in microservices.

---

### 14. Capability-Based

Instead of asking:

> Which agent?

Ask:

> Which tool?

```
Need SQL
↓

SQL Agent

Need Browser
↓

Browser Agent

Need MCP

↓

MCP Agent
```

---

### 15. Escalation Pattern

```
Small model

↓

Too difficult?

↓

Large model

↓

Answer
```

Saves cost while maintaining quality.

---

### 16. Agent Teams

Instead of spawning temporary workers, keep specialists alive across multiple assignments.

```
Coordinator
   |
+--------+--------+--------+
|Research| Coding | Testing|
| Agent  | Agent  | Agent  |
+--------+--------+--------+
```

These agents retain their own context and specialization over time, making them suitable for long-running projects. ([Claude][2])

---

## Exam Focus

Which patterns are most important for the Claude Certified Architect exam?

Focus on these in order:

1. ⭐⭐⭐⭐⭐ Fan-Out / Fan-In (Parallelization)
2. ⭐⭐⭐⭐⭐ Orchestrator–Worker
3. ⭐⭐⭐⭐⭐ Sequential Pipeline
4. ⭐⭐⭐⭐⭐ Evaluator–Optimizer
5. ⭐⭐⭐⭐ Routing
6. ⭐⭐⭐⭐ Generator–Verifier
7. ⭐⭐⭐ Reflection / Self-Critique
8. ⭐⭐⭐ Voting / Consensus
9. ⭐⭐ Map–Reduce
10. ⭐⭐ Debate
11. ⭐⭐ Escalation
12. ⭐ Agent Teams / Shared Memory / Message Bus (advanced)

These cover the workflow patterns Anthropic emphasizes for production AI systems and the multi-agent coordination approaches you'll encounter when designing scalable Claude-based applications. ([Claude][1])

[1]: https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them?utm_source=chatgpt.com "Common workflow patterns for AI agents | Claude by Anthropic"
[2]: https://claude.com/blog/multi-agent-coordination-patterns?utm_source=chatgpt.com "Multi-agent coordination patterns: Five approaches and when to use them | Claude by Anthropic"
