## Module 9 — The Complete Claude Architecture (End to End)

Modules 1–8 each zoomed in on one part of the machine — prompts, system prompts, context, reasoning, tools, MCP, agents, and subagents. This module snaps all those pieces together into **one picture** and walks the request from the moment a user types it to the moment the answer comes back. By the end you will be able to point at any arrow in the flow and say exactly what happens there.

---

### 9.1 The Big Picture

Here is the whole journey, top to bottom. Notice the **decision diamond** at "Need Tools?" — that is where the request either takes a short path straight to the answer, or a longer path out into the world and back.

```
                        ┌───────────────────┐
                        │       USER        │   types a request
                        └─────────┬─────────┘
                                  │  (1)
                                  ▼
                        ┌───────────────────┐
                        │      PROMPT       │   the user's text request
                        └─────────┬─────────┘
                                  │  (2)
                                  ▼
                        ┌───────────────────┐
                        │  SYSTEM PROMPT    │   persona + rules (set once)
                        └─────────┬─────────┘
                                  │  (3)
                                  ▼
                        ┌───────────────────┐
                        │ CONTEXT MANAGEMENT│   assemble: system + history
                        │   (CALM)          │   + retrieved docs + tool results
                        └─────────┬─────────┘
                                  │  (4)
                                  ▼
                        ┌───────────────────┐
                        │     REASONING     │   the model thinks
                        │     (the model)   │
                        └─────────┬─────────┘
                                  │  (5)
                                  ▼
                          ╱───────────────╲
                         ╱   NEED TOOLS?   ╲
                        ╱   (decision)      ╲
                        ╲                   ╱
                         ╲─────────────────╱
                          │ (6a)      │ (6b)
                     YES  │           │  NO
                          ▼           │
                ┌───────────────────┐ │
                │       MCP /        │ │   standardized reach
                │       TOOLS        │ │   to data + actions
                └─────────┬─────────┘ │
                          │  (7)      │
                          ▼           │
                ┌───────────────────┐ │
                │       AGENT        │ │   plan → act → observe → reflect
                └─────────┬─────────┘ │
                          │  (8)      │
                          ▼           │
                ┌───────────────────┐ │
                │     SUBAGENTS      │ │   specialists, run in parallel
                └─────────┬─────────┘ │
                          │  (9)      │
                          │ results   │
                          ▼           │
                 ┌ ─ ─ ─ ─ ─ ─ ─ ─ ┐ │
                   loop back into      │   observations feed
                 │ CONTEXT/REASONING│───┘   another think-act cycle
                 └ ─ ─ ─ ─ ─ ─ ─ ─ ┘
                          │
                          │  (10)  (when the model decides it is done)
                          ▼
                        ┌───────────────────┐
                        │     RESPONSE      │   final answer to the user
                        └───────────────────┘
```

> **Trainer Note:** The single most important thing on this diagram is the dashed **loop-back** arrow. Beginners imagine the request travels straight down the page once. In reality, reasoning ↔ tools ↔ observation can spin many times — the model acts, sees the result, thinks again, acts again — before it ever reaches "Response." One user prompt can trigger dozens of trips around that loop.

---

### 9.2 Every Arrow Explained

A numbered walk-through. For each arrow: **what enters**, **what happens**, **what leaves**, and **which Module** covered it.

**1. User → Prompt** *(Module 1)*
- **Enters:** a person's intention ("summarize this", "email the team").
- **Happens:** the intention is written down as plain text. This text is the **prompt** — the single request we want answered.
- **Leaves:** a raw text prompt.

**2. Prompt → System Prompt** *(Module 2)*
- **Enters:** the raw prompt.
- **Happens:** the prompt is placed *underneath* the **system prompt** — the global persona and rules ("You are a careful business analyst; be concise; never invent numbers"). The system prompt is set once and applies to every turn.
- **Leaves:** the user's request now wrapped in a standing set of instructions.

**3. System Prompt → Context Management** *(Module 3, framework: CALM)*
- **Enters:** system prompt + user prompt.
- **Happens:** everything the model needs to see is **assembled** into the finite **context window**: the system prompt, the conversation **history**, any **retrieved documents**, and any earlier **tool results**. CALM governs this — **C**ache what repeats, **A**ssemble what is relevant, **L**imit to fit the window, **M**anage what to keep or drop.
- **Leaves:** one tidy, complete package of text — the full working context.

**4. Context Management → Reasoning** *(Module 4)*
- **Enters:** the assembled context package.
- **Happens:** the **model reads it all and thinks** — interpreting the goal, weighing options, planning a first move.
- **Leaves:** an internal plan plus a decision about what to do next.

**5. Reasoning → Need Tools? (decision)** *(Module 4/5)*
- **Enters:** the model's plan.
- **Happens:** the model asks itself one question: *"Can I answer from what I already know, or must I act in the world — look something up, run something, send something?"*
- **Leaves:** a Yes or a No.

**6. Need Tools? → MCP (Yes) / → Response (No)** *(Module 5)*
- **No branch (6b):** nothing external is needed. The model writes the answer directly and jumps to step 10.
- **Yes branch (6a):** the model needs external data or an action. It hands off toward **tools / MCP**.
- **Leaves:** either a finished answer, or a tool request.

**7. MCP → Agent** *(Module 6)*
- **Enters:** the tool request.
- **Happens:** **MCP (Model Context Protocol)** is the *standard plug* that lets Claude reach outside systems — databases, search, files, APIs — the same way every time. This capability is driven by the **agent**, the loop that will actually run the plan.
- **Leaves:** a live tool call executed through a standard interface.

**8. Agent → Subagents** *(Module 7 & 8, framework: SPIDER)*
- **Enters:** a big or many-part task.
- **Happens:** the **agent** runs its loop — **plan → act → observe → reflect** — and when the job is large, it **delegates** slices to **subagents**: specialist agents given one narrow job each (e.g. "research Competitor A"). SPIDER keeps this reliable — **S**cope, **P**lan, **I**solate, **D**etect, **E**scalate, **R**ecover.
- **Leaves:** several focused sub-tasks running, often **in parallel**.

**9. Subagents → results back to Agent / Context** *(Module 8)*
- **Enters:** each subagent's finding.
- **Happens:** the parent agent **aggregates** all the pieces back together and feeds them into the context as fresh **observations**.
- **Leaves:** combined results that re-enter the loop — back up to Context/Reasoning (the dashed arrow) for another think-act cycle if needed.

**10. → Response** *(Module 1–8, together)*
- **Enters:** everything the model has gathered and reasoned through.
- **Happens:** once the model judges the goal is met, it stops looping and composes the final answer.
- **Leaves:** the **response** delivered to the user.

---

### 9.3 A Full Worked Example

**Request:** *"Research our top 3 competitors' new features and draft a one-page summary email."*

Follow it through every stage:

| Stage | What happens to this request |
|---|---|
| **User → Prompt** | The manager's intent becomes text: *"Research top 3 competitors' new features and draft a one-page summary email."* |
| **System Prompt** | Standing rules apply: *"You are our market-analysis assistant. Cite sources. Never invent facts. Keep emails under one page."* |
| **Context Management (CALM)** | The system assembles: the system prompt, who the 3 competitors are (from company memory/history), the email format template, and an empty slot for research results. It trims anything irrelevant to fit the window. |
| **Reasoning** | The model plans: *"I need current, external information I don't have. This needs tools. And it splits cleanly into 3 independent research jobs."* |
| **Need Tools? → YES** | It cannot answer from memory — competitor features are live, external facts. Yes branch. |
| **MCP / Tools** | Through **MCP**, the agent opens a web-search / data tool with a standard, repeatable interface. |
| **Agent** | The agent runs its loop and decides to **fan out** the work rather than research all three itself. |
| **Subagents (parallel)** | Three subagents launch at once: `Subagent A → Competitor 1`, `Subagent B → Competitor 2`, `Subagent C → Competitor 3`. Each searches, reads, and extracts that one rival's new features. |
| **Results back → Context** | Each subagent returns a short, sourced list. The parent agent **aggregates** all three into the context as new observations. |
| **Loop / Reasoning again** | The model reviews the combined findings, notices one competitor's data is thin, sends that subagent back for one more pass, then confirms it now has enough. |
| **Response** | It writes the one-page email: three tight sections, sources cited, under a page — and delivers it. |

> **Trainer Note:** Watch the **fan-out**. One prompt did not become one long search — it became three small searches running side by side, then merged. That is why agent systems feel fast on big tasks: the parallelism happens at the subagent layer, invisible to the user who just sees a clean email arrive.

---

### 9.4 Layered Reference Diagram

Same system, viewed as **stacked layers** instead of a flow. Each layer has one job.

```
┌──────────────────────────────────────────────────────────────┐
│  INTERFACE LAYER          user  ·  prompt                     │  what the user gives
├──────────────────────────────────────────────────────────────┤
│  INSTRUCTION LAYER        system prompt (persona + rules)     │  the standing law
├──────────────────────────────────────────────────────────────┤
│  CONTEXT LAYER            context window · history · memory   │  what the model can see
│                           · retrieved docs · tool results     │
├──────────────────────────────────────────────────────────────┤
│  REASONING LAYER          the model — thinks, plans, decides  │  the brain
├──────────────────────────────────────────────────────────────┤
│  CAPABILITY LAYER         tools  ·  MCP (standard plug)       │  hands into the world
├──────────────────────────────────────────────────────────────┤
│  ORCHESTRATION LAYER      agent (loop)  ·  subagents (fan-out)│  who runs the plan
├──────────────────────────────────────────────────────────────┤
│  OUTPUT LAYER             response                            │  what the user gets
└──────────────────────────────────────────────────────────────┘
        ▲                                                  │
        └───────── control loop repeats between layers ────┘
        (reasoning ↔ capability ↔ context can cycle many times)
```

Read it top-down for "who does what," but remember the **control loop** on the side: the middle layers talk back and forth repeatedly before the Output layer ever fires.

---

### 9.5 How the Frameworks Map On

Each framework from earlier modules governs a specific stretch of the pipeline.

| Framework | Stands for | Governs which stage(s) |
|---|---|---|
| **PRECISE** | good prompting discipline | **Prompt** (Arrow 1) and **System Prompt** (Arrow 2) — writing clear requests and rules |
| **CALM** | **C**ache · **A**ssemble · **L**imit · **M**anage | **Context Management** (Arrow 3) — packing the finite context window well |
| **SPIDER** | **S**cope · **P**lan · **I**solate · **D**etect · **E**scalate · **R**ecover | **Agent, Tools, Subagents** (Arrows 5–9) — keeping the acting loop reliable |

Quick way to remember: **PRECISE goes in, CALM holds the middle, SPIDER runs the loop.**

---

### 9.6 Interview Questions

**Basic**
1. In one sentence each, what is a prompt vs. a system prompt?
2. What does "context management" assemble into the context window?
3. What question does the model ask at the "Need Tools?" decision?
4. What is MCP, in plain words?
5. What is the difference between an agent and a subagent?

**Intermediate**
6. Why is the reasoning ↔ tools ↔ observation *loop* more accurate than picturing a single pass?
7. Which framework governs context management, and what do its letters stand for?
8. When the model takes the "No" branch at "Need Tools?", what path does the request follow?
9. How do subagent results re-enter the system, and where do they go?
10. Name the seven layers in the layered diagram, top to bottom.

**Scenario-based**
11. A request says "email finance last quarter's totals." Walk it to the correct branch at "Need Tools?" and justify it.
12. A task must research 5 products fast. Which layer makes it fast, and how?
13. The context window is overflowing with old history. Which framework and which of its letters address this?
14. A subagent returns thin, low-quality data. Which stage catches this, and what happens next (name the SPIDER letters involved)?
15. A user complains the assistant "made up" a competitor feature. Which layer's rules should have prevented it, and how would you fix it?

---

### 9.7 Common Mistakes (architecture level)

- **Thinking it's one straight pass.** Forgetting the loop-back; assuming every request goes top-to-bottom exactly once.
- **Skipping the "Need Tools?" decision.** Sending everything to tools (slow, costly) or nothing to tools (stale, made-up answers).
- **Overstuffing the context window.** Dumping all history and every document in — CALM's *Limit* and *Manage* exist to prevent this.
- **Confusing agent with subagent.** The agent is the orchestrator; subagents are its delegated specialists. They are not the same box.
- **Treating MCP as "just an API."** MCP is the *standard* interface — its value is that every tool connects the same way.
- **Putting rules in the user prompt.** Persona and policy belong in the **system prompt**, not repeated in every request.

---

### 9.8 Best Practices (production level)

- **Make the loop observable.** Log each plan → act → observe cycle so you can see where a run went wrong.
- **Keep the system prompt as the single source of rules.** Change behavior there, once, not scattered across prompts.
- **Right-size the context.** Cache stable parts, assemble only what's relevant, and prune aggressively (CALM).
- **Delegate deliberately.** Use subagents for independent, parallelizable slices — not for everything.
- **Isolate and recover (SPIDER).** Give each subagent a narrow scope, detect bad results early, and recover or escalate instead of shipping them.
- **Gate the tool decision.** Answer from knowledge when you safely can; reach for tools when facts must be live or actions must happen.
- **Cite and cost.** Carry sources through to the response, and track token usage — every loop around the cycle costs money.

---

### Quick Recap

- The full flow is **User → Prompt → System Prompt → Context → Reasoning → Need Tools? → (MCP → Agent → Subagents → back) → Response.**
- The **decision diamond** splits a quick answer from a longer trip into the world.
- The **control loop** (reasoning ↔ tools ↔ observation) can repeat many times before a response — not one pass.
- **Subagents fan out** independent work in parallel, then results **aggregate** back into context.
- Frameworks map cleanly: **PRECISE** goes in (prompts), **CALM** holds the middle (context), **SPIDER** runs the loop (agent/tools/subagents).
