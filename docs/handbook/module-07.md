## Module 7 — Agents

So far a model has answered our questions in **one shot**: you ask, it replies, done. In this module we meet the **agent** — a model that works toward a goal by *looping*: it decides an action, uses a tool, looks at the result, and repeats until the job is finished. This is the leap from "smart typewriter" to "worker who gets things done."

---

### 7.1 What is an Agent?

#### 1. Definition

An **agent** is an **LLM (Large Language Model) that pursues a goal by running in a loop**. Instead of producing a single answer, it repeatedly:

1. **decides** what to do next,
2. **uses a tool** to do it,
3. **observes** the result,
4. and **repeats** until the goal is met.

The key phrase: **the model drives its own control flow**. Nobody hand-scripts each step. You give the agent a goal and some tools, and *it* figures out the sequence of actions.

> **Trainer Note:** If students remember one line, make it this: "A chatbot answers; an agent *acts, checks, and repeats*." The loop is the whole idea.

#### 2. Why do we need it?

A plain chatbot is great for questions with a **one-step answer**. But real tasks are messy and multi-step: "Find the cheapest flight, book it, and email me the confirmation." No single reply can do that — it needs *actions*, *fresh information*, and *decisions along the way*.

We need agents because:

- **Real work has many steps**, and the right next step depends on what just happened.
- **The model can't know everything** — it needs tools (search, database, calculator, code) to get current, real facts.
- **Plans change mid-task** — an agent can notice a dead end and try another route, which a fixed script cannot.

| Situation | Plain Chatbot | Agent |
|---|---|---|
| "What's the capital of France?" | Perfect fit (one answer) | Overkill |
| "Check today's weather and pack a list" | Can't — no live data | Fits (uses a tool, then reasons) |
| "Research 3 vendors, compare, recommend" | Can't — too many steps | Fits (loops through steps) |

> **Trainer Note:** Emphasize *goal vs. question*. A question wants information. A goal wants an outcome. Agents are for goals.

#### 3. Office Analogy

Think of a **new intern given a task**, not a script.

You say: *"Book me a meeting room for Tuesday and invite the team."* You don't tell the intern every keystroke. The intern **plans** (check calendar, find a room, send invites), **acts** (opens the booking system), **observes** (room is taken!), **re-plans** (picks another room), and **reports back** when done. If they're unsure, they **ask you** before doing something risky.

That intern is an agent. The booking system, the calendar, the email client — those are its **tools**.

> **Trainer Note:** Contrast with an "order-taker" who only answers questions at a desk. The intern who *goes and does the task* is the mental model for an agent.

#### 4. Real-Life Analogy

Think of **cooking from a goal, not a recipe card**.

Goal: "Make dinner with what's in the fridge." You **look** (observe what's there), **plan** (pasta tonight), **act** (start boiling water), **check** (out of salt — adjust), and **keep going** until dinner is served. You loop between doing and checking. You stop when dinner is ready (goal met) — or if you realize you truly can't cook it, you order takeout instead (escalate/fallback).

> **Trainer Note:** The "keep tasting and adjusting" habit is exactly **Reflection**. Everyone has done it; use it to make the loop feel natural.

#### 5. Internal Working

Here is what actually happens under the hood, step by step:

1. **Goal in** — you give the agent a goal and a list of **tools** it may use.
2. **Plan** — the model breaks the goal into smaller steps.
3. **Reason & Decide** — it thinks about the current state and picks the next action (and which tool).
4. **Act** — it emits a **`tool_use`** request (a function call), e.g. `search("flights to Rome")`.
5. **Tool runs** — your code actually runs that tool and gets a real result.
6. **Observe** — the result comes back as a **`tool_result`** and is fed to the model.
7. **Reflect** — the model evaluates: are we closer? Any mistake to fix? Adjust the plan.
8. **Loop or stop** — if the goal is **not** met, go back to step 3. If it **is** met (or a guardrail trips), produce the final answer.

> **Trainer Note:** Steps 4–6 are a *handshake*: the model asks (`tool_use`), your program answers (`tool_result`). The model never runs tools itself — it *requests*, your code *executes*.

#### 6. Architecture Diagram

```
                 ┌─────────────────────────────────────────┐
                 │                  AGENT                    │
                 │                                           │
   GOAL ───────▶ │   ┌──────────┐      ┌──────────────┐      │
                 │   │   LLM     │      │  Tool Set     │     │
                 │   │ (brain):  │      │ - search      │     │
                 │   │  plan     │◀────▶│ - calculator  │     │
                 │   │  reason   │      │ - database    │     │
                 │   │  decide   │      │ - code runner │     │
                 │   │  reflect  │      └──────────────┘      │
                 │   └────┬─────┘                             │
                 │        │  tool_use ▲ tool_result           │
                 └────────┼───────────┼─────────────────────┘
                          ▼           │
                    ( action runs, result returns )
                          │
                          ▼
                   goal met? ──No──▶ loop back to LLM
                          │
                         Yes
                          ▼
                    FINAL ANSWER
```

> **Trainer Note:** Point out the two-way arrow between brain and tools — that's the loop's engine. The "goal met?" diamond is the stop condition; without it, agents run forever.

#### 7. Real Example

**Goal:** "What's the total cost in USD of 3 nights at the Rome hotel that costs €180/night?"

1. **Plan:** find nightly price → multiply by 3 → convert EUR to USD.
2. **Act:** `calculator(180 * 3)` → **Observe:** `540`.
3. **Reason:** now I need today's EUR→USD rate.
4. **Act:** `get_exchange_rate("EUR","USD")` → **Observe:** `1.08`.
5. **Act:** `calculator(540 * 1.08)` → **Observe:** `583.2`.
6. **Reflect:** goal met — I have the USD total.
7. **Respond:** "Total: about **$583.20** (€540 at 1.08)."

A plain chatbot would *guess* the rate. The agent *fetched* it — that's the difference.

> **Trainer Note:** Highlight that the agent chose **two different tools** in sequence, and each next step depended on the previous result. That dependency is why a loop (not a script) is needed.

#### 8. Live Demo

Run the foundations demo and watch the loop print each action and observation:

```bash
python topics/07-agents/demo.py
# or, if not yet present:
python topics/01-foundations/demo.py
```

Watch the console for `tool_use` (the agent's requested action) and `tool_result` (what came back), plus the final `usage` and estimated `$`. Trace how many loop iterations it took.

> **Trainer Note:** Ask the class to *predict* the tool calls before running. Comparing prediction vs. reality makes the loop click.

#### 9. Interview Questions

**Basic (5):**
1. In one sentence, what is an agent?
2. How is an agent different from a normal chatbot?
3. What does "the model drives its own control flow" mean?
4. Name three tools an agent might use.
5. What are `tool_use` and `tool_result`?

**Intermediate (5):**
1. Walk me through one full turn of the agent loop.
2. Why can't a single one-shot answer replace an agent for multi-step tasks?
3. Who actually *runs* the tool — the model or your code? Explain the handshake.
4. What stop conditions end an agent loop?
5. Why must every step's decision depend on the previous observation?

**Scenario (5):**
1. Your agent keeps calling the same tool forever. What's happening and how do you fix it?
2. An agent booked the wrong flight from bad search data. Which safeguards were missing?
3. You must add "delete customer records" as a tool. What precaution do you take?
4. A task sometimes needs a human's approval. How would you design that pause?
5. Your agent's cost per task is too high. Where in the loop do you look first?

> **Trainer Note:** For scenario Q1, guide students toward **max iterations** as the answer — it's the single most common beginner fix.

#### 10. Common Mistakes

- **Confusing an agent with a chatbot** — thinking "it's just a smarter reply." No: it's a *loop that acts*.
- **Assuming the model runs the tools** — it only *requests*; your code executes and returns results.
- **No iteration cap** — leading to infinite loops and runaway cost.
- **Giving it every tool "just in case"** — more tools = more ways to go wrong.
- **Trusting tool output blindly** — bad or hallucinated data can send the whole loop off a cliff.

> **Trainer Note:** These five map almost one-to-one to the SPIDER letters coming in 7.2. Foreshadow that.

#### 11. Best Practices

- **One clear goal, one clear responsibility** per agent (no "do-everything" agent).
- **Always cap iterations** and set a budget.
- **Give the fewest tools needed** (least privilege).
- **Validate tool results** before acting on them.
- **Require human approval** for risky or irreversible actions.

> **Trainer Note:** Tell students these aren't optional polish — they are what separates a demo toy from something safe to run for real.

#### 12. One-Page Summary

| Item | Takeaway |
|---|---|
| **What** | An LLM that pursues a goal in a loop |
| **How** | Decide → Act (tool) → Observe → Repeat |
| **Vs chatbot** | Chatbot = 1 request→1 answer; Agent = many self-directed steps |
| **Handshake** | Model requests `tool_use`; your code returns `tool_result` |
| **Stops when** | Goal met OR guardrail (max iterations / budget / needs human) |
| **Golden rule** | Always cap the loop |

> **Trainer Note:** This table is your whiteboard recap for 7.1. If time is short, teach only this and the diagram in §6.

---

### 7.2 Agent Loop

#### 1. Definition

The **agent loop** is the **repeating cycle** an agent runs to get from a goal to a finished result. One trip around the loop is: **reason → decide → act → observe → reflect**, and then either **loop again** or **stop**. It's the engine inside every agent.

> **Trainer Note:** 7.1 answered "what is an agent." 7.2 zooms into the *machinery* — the loop is that machinery.

#### 2. Why do we need it?

Because **you can't know the right steps in advance**. The next action depends on what the last action revealed. A search might return five results or zero; a calculation might succeed or error. The loop lets the agent **adapt after each observation** instead of blindly following a fixed script.

- Handles **uncertainty** — react to whatever the tool actually returns.
- Enables **self-correction** — catch and fix mistakes mid-task (Reflection).
- Provides a **natural stopping point** — loop until the goal is genuinely met.

> **Trainer Note:** Stress "adapt after each observation." That adaptivity is *why* it's a loop and not a straight line.

#### 3. Office Analogy

A **project manager running a status cycle**. Each day: check progress (observe), decide what's next (reason/decide), assign the task (act), review results tomorrow (observe again), adjust the plan (reflect). The project ends when the deliverable ships (goal met) — or gets escalated to a director if it's stuck (guardrail).

> **Trainer Note:** The daily "stand-up" rhythm is a perfect real-world loop. Reuse it — students already know it.

#### 4. Real-Life Analogy

**Using GPS while driving.** The GPS sets a route (plan), you drive a bit (act), it sees where you actually are (observe), and if you miss a turn it **recalculates** (reflect + re-plan). It loops every few seconds until you arrive (goal met). Miss too many turns and it just finds a new road — it never gives up mid-drive without a plan.

> **Trainer Note:** "Recalculating…" is Reflection in one word. Great hook for the loop's self-correcting nature.

#### 5. Internal Working

1. **Start** with a goal and available tools.
2. **Reason** about the current state (what do I know, what's missing?).
3. **Decide** the single next action and which tool to use.
4. **Act** — emit the `tool_use` request.
5. **Observe** — receive the `tool_result` / new information.
6. **Reflect** — did that help? Any error? Update the plan.
7. **Check the stop condition:** goal met? out of iterations/budget? needs a human?
8. If **stop** → produce final answer. If **continue** → go back to step 2.

> **Trainer Note:** Number 7 is the safety valve. Walk through it slowly — beginners forget the loop *must* be able to end.

#### 6. Architecture Diagram — The Complete Agent Loop

```
        ┌──────────────────────────────────────────────────────────┐
        │                                                          │
        │   GOAL                                                   │
        │     │                                                   │
        │     ▼                                                   │
        │   ┌──────┐                                              │
        │   │ PLAN │  break goal into steps                       │
        │   └──┬───┘                                              │
        │      ▼                                                  │
        │   ┌──────────────────┐                                 │
        │   │ REASON / DECIDE   │  what to do next? which tool?   │
        │   └──────┬───────────┘                                 │
        │          ▼                                             │
        │   ┌──────────────┐                                     │
        │   │ ACT           │  call the tool   (tool_use)         │
        │   └──────┬───────┘                                     │
        │          ▼                                             │
        │   ┌──────────────┐                                     │
        │   │ OBSERVE       │  read the result (tool_result)      │
        │   └──────┬───────┘                                     │
        │          ▼                                             │
        │   ┌──────────────┐                                     │
        │   │ REFLECT       │  progress? mistake? adjust plan     │
        │   └──────┬───────┘                                     │
        │          ▼                                             │
        │    ╱────────────╲                                      │
        │   ╱ GOAL  MET ?   ╲── No, and iterations left ──┐      │
        │   ╲  OR  STOP ?   ╱                             │      │
        │    ╲────┬───────╱                               │      │
        │         │ Yes (goal met)                        │      │
        │         │  OR max iterations / budget / human   │      │
        │         ▼                        loop back ◀────┘      │
        │   ┌──────────────┐                                     │
        │   │ DONE / RESPOND│  final answer                      │
        │   └──────────────┘                                     │
        │                                                        │
        └──────────────────────────────────────────────────────────┘

   STOP CONDITION = goal achieved  OR  max iterations reached
                    OR  budget exceeded  OR  needs human approval
```

> **Trainer Note:** This is the **must-know diagram** of the module. Have students redraw it from memory. The loop-back arrow and the stop diamond are the two things they must never omit.

#### 7. Real Example

**Goal:** "Is our office open on the next public holiday?"

| Iteration | Reason/Decide | Act (tool_use) | Observe (tool_result) | Reflect |
|---|---|---|---|---|
| 1 | Need the next holiday date | `get_next_holiday()` | "Aug 15" | Have date, need policy |
| 2 | Need the office policy | `lookup_policy("Aug 15")` | "Closed on public holidays" | Enough to answer |
| — | Goal met → stop | — | — | Respond |

**Answer:** "No — the office is closed on Aug 15 (public holiday)." Two loop iterations, then a clean stop.

> **Trainer Note:** The table form makes each iteration visible. Copy this table style onto the board and fill it in live with the class.

#### 8. Live Demo

```bash
python topics/07-agents/demo.py
python -m compileall -q core providers topics   # optional: syntax check
```

Count the iterations printed. Then **lower the max-iteration cap** in the code and re-run: watch the agent get cut off early. That single experiment teaches the stop condition better than any slide.

> **Trainer Note:** Deliberately triggering the cap is the highlight demo. It turns "max iterations" from an abstract rule into something they *saw* happen.

#### 9. Interview Questions

**Basic (5):**
1. What is the agent loop, in one sentence?
2. Name the stages of one loop iteration in order.
3. What does the loop do after it observes a tool result?
4. What makes the loop stop?
5. Why is it a loop and not a straight list of steps?

**Intermediate (5):**
1. What is Reflection and why does it matter?
2. Difference between Reasoning, Deciding, and Acting?
3. Where does the `tool_use` / `tool_result` handshake sit in the loop?
4. Why must you cap iterations? Give a failure it prevents.
5. Name three different stop conditions.

**Scenario (5):**
1. An agent loops 50 times without finishing. Diagnose and fix.
2. A tool returns garbage; the agent acts on it anyway. Which stage failed?
3. You want the agent to pause before spending money. Where in the loop do you add the gate?
4. The agent finishes but the goal isn't actually met. What's wrong with its stop check?
5. How would you log each iteration to debug an agent in production?

> **Trainer Note:** Intermediate Q2 (reason vs decide vs act) trips people up — rehearse it. Reason = *think*, Decide = *choose*, Act = *do*.

#### 10. Common Mistakes

- **No stop condition** → infinite loop, runaway cost.
- **Skipping Reflection** → the agent never catches its own errors.
- **Acting before observing** → decisions made on stale or missing data.
- **One giant step instead of many small ones** → no chance to adapt.
- **Forgetting the loop can end early** (budget/human) — treating "goal met" as the only exit.

> **Trainer Note:** Tie each mistake to a stage of the diagram in §6. Visual anchoring makes them stick.

#### 11. Best Practices — use **SPIDER**

Design reliable loops with the **SPIDER** framework:

| Letter | Principle | In the loop |
|---|---|---|
| **S** | **Scope** — one clear responsibility, no "God agent" | Keep the goal narrow |
| **P** | **Plan** — decompose the goal first | The Plan stage |
| **I** | **Isolate** — least-privilege tools | Give only tools this goal needs |
| **D** | **Detect** — validate results, add guardrails | Check every Observation |
| **E** | **Escalate** — route risky/low-confidence to a human | Approval gate before Act |
| **R** | **Recover** — retries, fallbacks, loop caps | The stop condition |

> **Trainer Note:** Chant it: **S**cope, **P**lan, **I**solate, **D**etect, **E**scalate, **R**ecover. SPIDER is the single most exam-relevant mnemonic in this module.

#### 12. One-Page Summary

| Item | Takeaway |
|---|---|
| **What** | The repeating cycle an agent runs |
| **One iteration** | Reason → Decide → Act → Observe → Reflect |
| **Then** | Check stop condition → loop back OR respond |
| **Stops when** | Goal met / max iterations / budget / needs human |
| **Reliability** | **SPIDER**: Scope, Plan, Isolate, Detect, Escalate, Recover |
| **Golden rule** | Every loop MUST be able to end |

> **Trainer Note:** Pair this table with the §6 diagram for a complete 7.2 recap.

---

### 7.3 The Agent Loop, Stage by Stage

Now let's walk each stage of the loop on its own. Keep the §6 diagram in mind — every stage below is one box in that picture.

#### Planning

**Planning** is breaking the big goal into smaller, doable steps before diving in. Instead of "book my trip," the agent lays out: find flights → pick one → book → confirm. A good plan makes every later decision easier and gives the agent something to adjust when things change.

*Where in the loop:* right after the **Goal** arrives — the very first stage, and revisited whenever Reflection says the plan needs updating.

#### Reasoning

**Reasoning** is the agent thinking about **what to do next given the current state**: what do I already know, what's still missing, what would help most right now? It's the internal "thinking out loud" that happens before any action is chosen. Good reasoning uses the latest observation, not stale assumptions.

*Where in the loop:* at the top of every iteration, feeding into Decision Making.

#### Acting

**Acting** is the agent **taking the step** — calling a tool. Concretely, the model emits a **`tool_use`** request like `search("hotels in Rome")`. This is the only way the agent affects the outside world; everything before it was just thinking. Your code then actually runs that tool.

*Where in the loop:* the **Act** box, right after a decision is made.

#### Observation

**Observation** is the agent **reading the result** of its action — the **`tool_result`** or new information that comes back. This fresh data is what makes the next iteration smart instead of blind. If the agent ignores observations, the whole loop is pointless.

*Where in the loop:* immediately after Acting; it feeds Reflection.

#### Reflection

**Reflection** is the agent **evaluating progress and adjusting**: Did that action help? Was there an error? Should I change the plan? This is where an agent catches its own mistakes and self-corrects — the "recalculating" moment. Without it, agents repeat errors instead of fixing them.

*Where in the loop:* right after Observation, just before the stop-condition check.

#### Decision Making

**Decision Making** is **choosing the next concrete action** — including *which tool* to use — based on the reasoning. Reasoning is the thinking; Decision Making is the commitment. A clear decision turns vague thoughts into a specific `tool_use`.

*Where in the loop:* between Reasoning and Acting.

#### Tool Usage

**Tool Usage** is the **concrete mechanism** the agent uses to act — commonly called **function calling**. Tools are the agent's hands: search, calculator, database, code runner. The model requests a tool via `tool_use`; your code executes it and returns a `tool_result`. Give the fewest tools needed (least privilege).

*Where in the loop:* the machinery *inside* the Act and Observe stages — it's how Acting actually happens.

Here's how the stages line up:

```
 Planning ─▶ Reasoning ─▶ Decision Making ─▶ Acting ─▶ Observation ─▶ Reflection ─┐
     ▲            ▲            (choose tool)   (tool_use)  (tool_result)           │
     │            └───────────────────────────────────────────────── loop back ◀──┘
     └── (Tool Usage = the function-calling mechanism powering Act + Observe)
```

> **Trainer Note:** The classic confusion is Reasoning vs. Decision Making. Nail it with: **Reasoning = think, Decision = choose, Acting = do.** Say it three times.

---

### 7.4 Live Demo

**Goal:** see a real agent loop run end to end, and see the stop condition fire.

```bash
# 1. Install (once)
pip install -e .

# 2. Run the agents topic
python topics/07-agents/demo.py
#    (fall back to topics/01-foundations/demo.py if 07 isn't present yet)

# 3. Syntax check anything you edit
python -m compileall -q core providers topics
```

**What to watch for:**

1. Each **`tool_use`** line = the agent *deciding and acting*.
2. Each **`tool_result`** line = the agent *observing*.
3. The iteration **count** — how many loops to reach the goal.
4. The final **`usage`** and estimated **`$`** (cost is first-class here).

**Two experiments that teach the most:**

- **Lower the max-iteration cap** and re-run — watch the agent get cut off (the stop condition in action).
- **Remove a tool** the agent needs — watch it get stuck or escalate (why least-privilege *and* the right tools both matter).

> **Trainer Note:** Have students predict the tool calls *before* running, then compare. The gap between guess and reality is where the real learning lands.

---

### 7.5 Interview Questions

**Basic (5):**
1. What is an agent, and how is it different from a chatbot?
2. List the stages of one agent-loop iteration.
3. What are `tool_use` and `tool_result`?
4. What always stops an agent loop? Name at least one condition.
5. Who runs the tool — the model or your code?

**Intermediate (5):**
1. Explain Reasoning vs. Decision Making vs. Acting.
2. What is Reflection and what problem does it solve?
3. Why must you always cap iterations?
4. What does "least-privilege tools" mean and why does it help?
5. Where does the `tool_use`/`tool_result` handshake sit in the loop?

**Scenario (5):**
1. An agent runs forever calling the same tool. Diagnose and fix.
2. An agent took an irreversible action (deleted data) it shouldn't have. Which SPIDER letters were missing?
3. A task needs a manager's sign-off before spending money. How do you build that in?
4. Your agent acts on hallucinated search results. Which stage and which safeguard failed?
5. One agent is trying to do five unrelated jobs and keeps failing. What's the fix?

> **Trainer Note:** Scenario Q2 and Q5 are pure SPIDER checks (Escalate/Recover, and Scope). Use them to confirm the mnemonic stuck.

---

### 7.6 Common Mistakes

| Mistake | Why it's bad | Fix |
|---|---|---|
| **No iteration cap** | Infinite loop, runaway cost | Always set max iterations |
| **Trusting tool output blindly** | Acts on bad/hallucinated data | Validate results (Detect) |
| **Irreversible action, no approval** | Damage you can't undo | Escalate risky actions to a human |
| **"God agent" doing everything** | Confused, unreliable, hard to debug | One agent, one responsibility (Scope) |
| **Too many tools "just in case"** | More ways to go wrong | Least privilege (Isolate) |
| **Thinking the model runs tools** | Wrong mental model | Model *requests*; your code *executes* |
| **Skipping Reflection** | Repeats its own errors | Evaluate progress each iteration |

> **Trainer Note:** Every row maps to a SPIDER letter or the golden rule. Have students name the letter for each — great 5-minute quiz.

---

### 7.7 Best Practices — SPIDER

Build reliable agents with **SPIDER**:

```
 S  Scope     → one clear responsibility, no "God agent"
 P  Plan      → decompose the goal into steps first
 I  Isolate   → give least-privilege tools only
 D  Detect    → validate tool results, add guardrails
 E  Escalate  → route risky / low-confidence actions to a human
 R  Recover   → retries, fallbacks, and ALWAYS a loop cap
```

Plus the non-negotiables:

- **Always cap iterations and set a budget.** Every loop must be able to end.
- **Print `usage` + estimated `$`.** Cost is first-class.
- **Require human approval** before anything irreversible.
- **Log each iteration** (reason → act → observe) so you can debug.

> **Trainer Note:** SPIDER is *the* exam takeaway of this module. If you teach nothing else in Best Practices, teach the six letters and the "always cap the loop" rule.

---

### 7.8 One-Page Summary

| Concept | One-liner |
|---|---|
| **Agent** | An LLM that pursues a goal in a **loop** |
| **Agent loop** | Reason → Decide → Act → Observe → Reflect → (repeat or stop) |
| **Planning** | Break the goal into steps |
| **Reasoning** | Think about what to do next |
| **Decision Making** | Choose the next action / tool |
| **Acting** | Call the tool (`tool_use`) |
| **Observation** | Read the result (`tool_result`) |
| **Reflection** | Evaluate progress, fix mistakes |
| **Tool Usage** | The function-calling mechanism to act |
| **Stops when** | Goal met OR max iterations / budget / needs human |
| **Agent vs chatbot** | Chatbot = 1 request→1 answer; Agent = many self-directed steps |
| **Reliability** | **SPIDER**: Scope, Plan, Isolate, Detect, Escalate, Recover |
| **Golden rule** | **Always cap the loop** |

> **Trainer Note:** This single table is a complete revision sheet for Module 7. Photocopy-worthy.

---

### Quick Recap

- An **agent** is an LLM that works toward a **goal** by running in a **loop** — deciding, acting with tools, observing, and repeating — instead of answering in one shot. **The model drives its own control flow.**
- One loop iteration = **Reason → Decide → Act (`tool_use`) → Observe (`tool_result`) → Reflect**, then loop back or stop.
- The loop **must always be able to end**: goal met, max iterations, budget exceeded, or needs a human.
- The model **requests** actions; **your code executes** them and returns results.
- Build reliable agents with **SPIDER** — **S**cope, **P**lan, **I**solate, **D**etect, **E**scalate, **R**ecover — and **always cap the loop.**
