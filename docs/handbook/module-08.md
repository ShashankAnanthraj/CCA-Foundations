## Module 8 — Subagents

So far our agent has been a lone worker doing everything itself. In this module we meet the **subagent**: a helper agent that a main "manager" agent hands a small, focused job to. Think of it as turning one busy employee into a whole team with a boss.

Throughout this module we use one picture: a **software company org chart**. A **lead agent** acts like a team manager who splits a project into tasks and hands each to a **specialist subagent** (a frontend developer, a QA tester, a researcher). The specialists do their part and pass results back up to be combined.

```
                        ┌──────────────────────────┐
                        │   ORCHESTRATOR / LEAD     │
                        │      (the Manager)        │
                        └────────────┬──────────────┘
                 splits the project into tasks
        ┌────────────────┬───────────┴───────────┬────────────────┐
        ▼                ▼                        ▼                ▼
 ┌─────────────┐  ┌─────────────┐         ┌─────────────┐  ┌─────────────┐
 │  Frontend   │  │     QA       │         │  Researcher │  │   Writer    │
 │  Subagent   │  │  Subagent    │         │  Subagent   │  │  Subagent   │
 └──────┬──────┘  └──────┬───────┘         └──────┬──────┘  └──────┬──────┘
        │ result         │ result                 │ result         │ result
        └────────────────┴───────────┬────────────┴────────────────┘
                                      ▼
                        ┌──────────────────────────┐
                        │  Manager MERGES results   │
                        │   into one final answer   │
                        └──────────────────────────┘
```

---

### 8.1 What are Subagents?

#### 1. Definition
A **subagent** is a separate agent instance that a main **orchestrator** (also called the **lead agent**) creates and hands a **scoped sub-task** to. Each subagent usually has its **own focused prompt**, its **own set of tools**, and — most importantly — its **own context window** (its own private notepad and memory). It does one job, returns a result, and the lead combines everything.

> **Trainer Note:** Say this out loud in class: "A subagent is not a new app — it is another copy of the same kind of agent, given a smaller job and a clean desk." The "clean desk" (own context window) is the idea students remember.

#### 2. Why do we need it?
A single agent trying to do a huge job gets **overloaded**: its context window fills up, unrelated details get tangled together, and it slows down. Subagents let the lead **hand off** pieces so each helper stays focused, fast, and hard to confuse. It is the difference between one person building a whole house versus a crew of specialists.

> **Trainer Note:** Tie this back to SPIDER "Scope" from the reliability framework — a narrow scope per agent is what makes each one reliable.

#### 3. Office Analogy
A **project manager** receives a client request: "Ship a new login page." She does not code, test, and write docs alone. She assigns the UI to a **frontend developer**, the testing to a **QA engineer**, and the help article to a **technical writer**. Each employee knows only their slice, works independently, and reports back. The manager assembles the finished feature.

> **Trainer Note:** Ask the room: "Would a good manager give the QA tester the entire company database?" No — leads give each subagent only what its task needs.

#### 4. Real-Life Analogy
A **head chef** during a dinner rush is the orchestrator. She calls out orders to stations: the **grill cook**, the **salad cook**, the **dessert cook**. Each station works on its own dish at the same time, on its own counter, and hands the finished plate back. The head chef **plates** the final meal.

```
Head Chef (lead) ──► Grill station  ──► steak
                └──► Salad station  ──► salad   ──► Chef plates full meal
                └──► Dessert station──► cake
```

> **Trainer Note:** Kitchens make the "same time / own counter" point instantly. That is parallelism plus context isolation in one image.

#### 5. Internal Working (numbered)
1. The user gives the **lead agent** a big goal.
2. The lead **plans** and breaks the goal into smaller sub-tasks.
3. For each sub-task the lead **spawns a subagent**, giving it a focused prompt, the right tools, and a fresh context window.
4. Each subagent **works on its own** and produces a result.
5. The lead **collects** all the results back.
6. The lead **merges** them into one clean final answer for the user.

> **Trainer Note:** Number 3 is the "delegation" moment and number 6 is the "aggregation" moment — flag both; they return as named concepts in 8.3.

#### 6. Architecture Diagram (ASCII)
```
 USER
   │  "big goal"
   ▼
┌────────────────┐
│  LEAD AGENT    │  1. plan  →  2. decompose
│ (orchestrator) │
└───┬────────┬───┘
    │ spawn  │ spawn
    ▼        ▼
┌────────┐ ┌────────┐   each has its OWN
│Subagent│ │Subagent│   prompt + tools +
│   A    │ │   B    │   context window
└───┬────┘ └───┬────┘
    │ result   │ result
    └────┬─────┘
         ▼
   ┌────────────┐
   │  LEAD merges│ → final answer → USER
   └────────────┘
```

> **Trainer Note:** Draw this once, then reuse the same shape for every later diagram so students anchor to one mental model.

#### 7. Real Example
A **Multi-Agent Research System**. You ask: "Compare the top three electric cars of 2026." The lead splits this into three sub-questions (one per car), spawns three **researcher subagents** in parallel, each one searches the web and reads sources on its own car, and then the lead writes a single **cited comparison report**. This is one of the CCA-F exam scenarios — know it by name.

> **Trainer Note:** This exact scenario appears on the exam. Have students repeat the flow: "decompose → fan-out → synthesize."

#### 8. Live Demo
Show two versions of the same task. Version A: one agent researches three cars in a single context — watch it get long and mix up facts. Version B: a lead spawns three subagents, each returns a tidy summary, and the lead merges them. Compare the clarity and the usage/`$` printout.

> **Trainer Note:** The AI-OS demo prints `usage` + estimated `$` — point out that Version B may cost more tokens but is clearer and often faster. That trade-off is the teachable moment.

#### 9. Interview Questions (5/5/5)

**Beginner**
1. What is a subagent in one sentence?
2. Who creates subagents — the user or the lead agent?
3. What does "context window" mean for a subagent?
4. Name one specialist a lead might delegate to.
5. What does the lead do after subagents finish?

**Intermediate**
1. Why does giving each subagent its own context window help?
2. How is a subagent different from just a longer prompt?
3. What does "scoped task" mean when delegating?
4. Give an example task worth splitting into subagents.
5. What is the "decompose → fan-out → synthesize" pattern?

**Advanced**
1. When would adding subagents make things worse, not better?
2. How does subagent isolation improve reliability?
3. What is the hardest step in a multi-agent system and why?
4. How do least-privilege tools apply to subagents?
5. How does subagent design relate to SPIDER "Scope"?

> **Trainer Note:** For advanced Q3, guide them to "aggregation/synthesis" — merging messy outputs into one coherent answer is the real engineering challenge.

#### 10. Common Mistakes
- Thinking a subagent is a whole new program (it is another agent instance).
- Believing subagents share one memory — they each have their **own** context window.
- Assuming the user spawns subagents — the **lead** does.
- Using subagents for tiny jobs where one agent was fine.

> **Trainer Note:** The "shared memory" myth is the most common beginner error — correct it early and often.

#### 11. Best Practices
- Give each subagent **one clear job** and a focused prompt.
- Hand over **only** the tools and context that job needs (least privilege).
- Keep sub-task boundaries clean so results are easy to merge.
- Always have the lead **synthesize** — never dump raw subagent output on the user.

> **Trainer Note:** "One job, least tools, clean merge" is a three-word chant worth repeating.

#### 12. One-Page Summary

| Question | Answer |
|---|---|
| What is it? | A separate agent instance the lead delegates a scoped sub-task to |
| Has its own…? | Prompt, tools, and context window |
| Who makes it? | The orchestrator / lead agent |
| Core flow | Plan → decompose → spawn → collect → merge |
| Exam example | Multi-Agent Research System |
| Key benefit | Focus, isolation, speed, contained failures |

> **Trainer Note:** If a student remembers only one row, make it "Has its own prompt, tools, and context window."

---

### 8.2 Why use them?

#### 1. Definition
Using subagents means the lead **deliberately splits work** across focused helpers instead of doing everything in one context. The four headline reasons are **specialization**, **context isolation**, **parallelism**, and **reliability**.

> **Trainer Note:** Write those four words on the board and keep them there for the whole section — every point maps back to one of them.

#### 2. Why do we need it?
Big tasks push a single agent past its limits: the context window overflows, unrelated facts contaminate each other, everything runs one-at-a-time (slow), and a single failure can sink the whole job. Subagents fix all four problems at once by dividing the work.

> **Trainer Note:** Frame it as "four pains, one cure" — students love a clean one-to-one mapping.

#### 3. Office Analogy
A **team lead** could technically write all the code, test it, and document it alone — but the project would be slow and error-prone. By delegating to specialists who work **in parallel**, the whole feature ships faster and each part is higher quality because an expert owned it.

> **Trainer Note:** Ask: "If one employee quits mid-project, does the whole company stop?" No — that is contained failure / reliability.

#### 4. Real-Life Analogy
Building a house. A **general contractor** hires an electrician, a plumber, and a roofer. They work at the same time on different parts, each an expert. If the roofer is delayed, the plumber keeps going. The contractor coordinates and delivers the finished house.

> **Trainer Note:** The "roofer delayed, plumber keeps going" line is your reliability + parallelism proof in one sentence.

#### 5. Internal Working (numbered)
1. Lead spots that the goal is **large, parallelizable, or needs isolation**.
2. Lead **decomposes** it into independent (or staged) sub-tasks.
3. Lead **delegates** each with least-privilege tools and context.
4. Independent subagents run **at the same time** (fan-out) for speed.
5. If one subagent fails, the lead **retries or routes around it** — the rest are safe.
6. Lead **aggregates** the good results into one answer.

> **Trainer Note:** Step 1 is the decision gate — subagents are a *choice*, not a default. Stress "not for trivial jobs."

#### 6. Architecture Diagram (ASCII)
```
                 ┌─────────────┐
                 │  LEAD AGENT │
                 └──────┬──────┘
     ── FAN-OUT (parallel, independent) ──
        ┌──────────┬──────────┬──────────┐
        ▼          ▼          ▼          ▼
   [Subagent] [Subagent] [Subagent] [Subagent]
    special-   context-    runs at    failure
    ization    isolation   same time  contained
        └──────────┴────┬─────┴──────────┘
                 ── FAN-IN (merge) ──
                        ▼
                 ┌─────────────┐
                 │ ONE ANSWER  │
                 └─────────────┘
```

> **Trainer Note:** Label the two arrows out loud: "fan-out" (spread work) and "fan-in" (gather results). These terms appear on the exam.

#### 7. Real Example
A company wants a market report on 20 competitors. One agent would drown in 20 companies at once. Instead the lead **fans out** 20 researcher subagents (or a few handling several each), each studies one competitor in its own clean context, and the lead **fans in** to write one ranked summary — far faster and cleaner than a single sweep.

> **Trainer Note:** Scale is the argument here: 20 items is obviously a job to split. Contrast with "translate one sentence" — obviously not.

#### 8. Live Demo
Run a 6-source research task twice. First sequentially in one agent (time it). Then with 6 parallel subagents (time it). Show the wall-clock speed-up and the `usage`/`$` figures side by side so students see both the benefit **and** the cost.

> **Trainer Note:** Let them see that faster is not free — parallel subagents can use more total tokens. Honesty about the trade-off builds trust.

#### 9. Interview Questions (5/5/5)

**Beginner**
1. Name the four reasons to use subagents.
2. What does "parallel" mean here?
3. Why is one huge context a problem?
4. Give one task too small for subagents.
5. What does the lead do at the end?

**Intermediate**
1. What is fan-out and what is fan-in?
2. Why does isolation reduce mistakes?
3. When do sub-tasks have to stay sequential?
4. What is a trade-off of using more agents?
5. Why is expert specialization higher quality?

**Advanced**
1. How do you decide the "right number" of subagents?
2. How does contained failure improve system reliability?
3. Why can parallelism raise cost even while saving time?
4. How does context isolation prevent cross-contamination?
5. When is a single agent genuinely the better choice?

> **Trainer Note:** Advanced Q5 keeps them honest — subagents are a tool, not a religion. Reward answers that mention overhead and cost.

#### 10. Common Mistakes
- Reaching for subagents on trivial tasks (added cost, no benefit).
- Running **dependent** tasks in parallel and getting garbage (they must be sequential).
- Forgetting that more agents means more **tokens and coordination overhead**.
- Ignoring aggregation quality — a great sweep with a sloppy merge is a poor answer.

> **Trainer Note:** "Dependent tasks in parallel" is a classic bug — if Task B needs Task A's output, they cannot run at the same time.

#### 11. Best Practices
- Use subagents when the task is **big, parallelizable, or needs isolation** — otherwise stay single.
- Split **independent** work in parallel; chain **dependent** work in a pipeline.
- Budget for cost; measure `usage`/`$` and compare against a single-agent baseline.
- Invest the most effort in the **synthesis** step — it makes or breaks the result.

> **Trainer Note:** The decision rule "big, parallelizable, or isolation-needed" is exam gold — have them memorize it verbatim.

#### 12. One-Page Summary

| Reason | What it gives you | Analogy |
|---|---|---|
| Specialization | Each agent has one clear job | Frontend dev vs QA |
| Context isolation | Clean window, no cross-contamination | Own desk / own counter |
| Parallelism | Independent tasks run at once = speed | Electrician + plumber together |
| Reliability | One failure stays contained | Roofer delayed, plumber works |

> **Trainer Note:** This table is the whole section. If time runs short, teach this table and move on.

---

### 8.3 How Multi-Agent Systems Work

The four reasons explain *why*. This section explains the *mechanics* — the five moving parts that turn a lead plus helpers into a working team.

#### Delegation
**Delegation** is the moment the lead hands a subagent a **scoped task** plus only the tools and context that task needs — nothing more (**least privilege**). Like a manager giving a contractor a work order and building access for their job only.

```
Lead ──"research car #2, here is web-search only"──► Subagent
```

#### Task Decomposition
**Task decomposition** is the planning step: breaking one big goal into smaller **independent** (or staged) sub-tasks. Good decomposition makes everything after it easy; bad decomposition makes merging impossible. It is the most important thinking the lead does.

```
"Compare 3 cars"  →  [car A] [car B] [car C]   (three clean sub-tasks)
```

#### Parallel Execution
**Parallel execution** runs **independent** subagents at the same time — the **fan-out**. This is where the speed comes from, and it shines on research and large sweeps. Warning: **dependent** tasks (where B needs A's output) must stay **sequential** in a pipeline.

```
Parallel (independent):  A │ B │ C   all at once
Pipeline (dependent):    A → B → C   one after another
```

#### Result Aggregation
**Result aggregation** is the **fan-in**: the lead collects every subagent's output, removes duplicates, and **synthesizes** one coherent answer. This is the hard part — the quality of the final result lives or dies here.

```
[result A] [result B] [result C] ──► Lead dedupes + merges ──► one answer
```

#### Multi-Agent Collaboration
These pieces combine into named **collaboration patterns**: a **router** picks the right specialist, a **pipeline** chains stages, **parallel/fan-out** runs many at once, and a **synthesizer** merges everything. Real systems mix them.

| Pattern | What it does | When to use |
|---|---|---|
| Router | Sends the task to the right specialist | Many task types, one entry point |
| Pipeline | Chains stages in order | Each step needs the previous |
| Parallel / Fan-out | Runs many subagents at once | Independent work, need speed |
| Synthesizer | Merges results into one answer | Always, at the end |

> **Trainer Note:** The headline pattern to memorize is **decompose → fan-out → synthesize**. Router and pipeline are the two extra shapes for special cases.

---

### 8.4 Live Demo

Walk the class through the **Multi-Agent Research System** end to end:

1. Ask the lead: "Give me a cited report comparing three electric cars."
2. Watch the lead **decompose** into three sub-questions.
3. Watch it **fan out** three researcher subagents that search in parallel.
4. Watch each subagent return a tidy, sourced summary.
5. Watch the lead **synthesize** one cited report and print `usage` + estimated `$`.

Then rerun the same request as a single agent and compare speed, clarity, and cost so the trade-off is concrete.

```
Ask ─► Lead decomposes ─► fan-out 3 researchers ─► fan-in ─► cited report (+ usage/$)
```

> **Trainer Note:** Keep the DRY rule in mind — the demo should reuse `core/` and shared capabilities, never re-implement a provider call. Point that out; it models good structure.

---

### 8.5 Interview Questions (5/5/5)

**Beginner**
1. What is an orchestrator / lead agent?
2. What is delegation?
3. What does fan-out mean?
4. What does fan-in mean?
5. Name the headline pattern for a research system.

**Intermediate**
1. Why must dependent tasks run sequentially?
2. What makes task decomposition good or bad?
3. What does a router pattern do?
4. Why is aggregation called the hard part?
5. What is least privilege for a subagent?

**Advanced**
1. How would you design a system mixing router, pipeline, and fan-out?
2. How do you keep aggregation quality high across many messy outputs?
3. How do you balance speed gains against token cost?
4. When does decomposition fail and how do you spot it?
5. How do subagent boundaries affect final-answer coherence?

> **Trainer Note:** Great advanced answers name a concrete pattern mix, e.g. "router picks a domain, pipeline stages the analysis, fan-out handles the sources, synthesizer writes the report."

---

### 8.6 Common Mistakes

| Mistake | Why it hurts | Fix |
|---|---|---|
| Subagents for trivial jobs | Extra cost, zero benefit | Use one agent for small tasks |
| Parallelizing dependent tasks | Wrong results (B needed A) | Use a sequential pipeline |
| Sharing one context | Cross-contamination of facts | Give each its own window |
| Weak synthesis | Great research, bad answer | Invest most in aggregation |
| Over-permissioned subagents | Security and confusion risk | Least-privilege tools only |

> **Trainer Note:** Rows 2 and 4 are the most exam-relevant — dependency handling and aggregation quality.

---

### 8.7 Best Practices

- **Decide first:** only reach for subagents when the task is big, parallelizable, or needs isolation.
- **Decompose cleanly:** independent sub-tasks in parallel, dependent ones in a pipeline.
- **Delegate least privilege:** each subagent gets only the tools and context it needs.
- **Synthesize carefully:** the lead merges, dedupes, and produces one coherent, cited answer.
- **Measure cost:** always print `usage` + estimated `$` and compare to a single-agent baseline.
- **Stay DRY:** subagents reuse `core/` and shared capabilities — never re-implement a provider call.

> **Trainer Note:** These six map directly onto the module. If a student can recite them, they understand subagents.

---

### 8.8 One-Page Summary

```
SUBAGENTS = a manager (lead) + specialist employees (subagents)

Each subagent has:  own prompt · own tools · own context window
The lead does:      PLAN → DECOMPOSE → DELEGATE → (fan-out) → AGGREGATE (fan-in)

WHY (4 reasons):    specialization · context isolation · parallelism · reliability
PATTERNS:           router · pipeline · parallel/fan-out · synthesizer
HEADLINE FLOW:      decompose → fan-out → synthesize
EXAM SCENARIO:      Multi-Agent Research System (lead + parallel researchers + cited report)
USE WHEN:           task is big, parallelizable, or needs isolation — NOT for trivial jobs
TRADE-OFF:          more agents = more tokens/cost + coordination; aggregation is the hard part
```

| Concept | One-line meaning |
|---|---|
| Subagent | Separate agent instance with its own prompt, tools, context window |
| Orchestrator / lead | The manager that plans, delegates, and merges |
| Delegation | Handing a scoped task + least-privilege tools to a subagent |
| Decomposition | Breaking a big goal into independent/staged sub-tasks |
| Fan-out | Running independent subagents in parallel |
| Fan-in / aggregation | Collecting and synthesizing results into one answer |

---

### Quick Recap

- A **subagent** is a separate agent instance with its **own prompt, tools, and context window** that the **lead/orchestrator** delegates a scoped sub-task to.
- We use them for four reasons: **specialization, context isolation, parallelism, reliability**.
- The mechanics are **delegation → decomposition → parallel execution (fan-out) → result aggregation (fan-in)**, arranged with **router, pipeline, parallel, and synthesizer** patterns.
- The headline flow to memorize is **decompose → fan-out → synthesize**, and the exam scenario is the **Multi-Agent Research System**.
- Use subagents only when a task is **big, parallelizable, or needs isolation** — never for trivial jobs — and always mind the **cost** and the **quality of the merge**.
