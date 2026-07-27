## Module 10 — CCA-F Certification Preparation

Welcome to the final module. This is your **revision and exam-prep** cockpit: one section per earlier module, packed with expected questions, confusion-busters, mnemonics, checklists, hands-on drills, mini quizzes, and mock interviews. Work through it slowly, then sit the final mock exam at the end. Treat this module as a map — the single source of truth is always the official exam guide (see 10.1).

---

### 10.1 About the Exam

Let's separate what is **officially confirmed** from what is **reported by third-party prep sites**. On the exam you should trust official Anthropic materials over community rumor — and you should say so if asked.

#### CONFIRMED (official Anthropic)

- The **Claude Certified Architect, Foundations** is a real, Anthropic-administered technical certification. It was announced on **2026-03-12** as Anthropic's **first technical certification**, aimed at **solution architects building production applications with Claude**.
- It is delivered through **Pearson VUE** using **OnVUE online proctoring**. Registration and preparation happen on the **Anthropic Partner Academy** (built on Skilljar).
- Access is currently **gated** to organizations in the **Claude Partner Network** — this is **not yet an open public exam**.
- It validates **four core technology areas**: **Claude Code**, **Claude Agent SDK**, **Claude API**, and **Model Context Protocol (MCP)** — with heavy emphasis on **real-world tradeoff decisions**, not trivia.
- **Retake policy:** 14 days after attempt 1, 30 days after attempt 2, 90 days after attempt 3; up to **4 attempts per rolling 12 months**. All attempts are OnVUE-proctored.

#### UNVERIFIED (reported, not officially confirmed)

> Treat everything below as "reported by third-party prep sites, not officially confirmed." Reconcile against the official guide before quoting any of it.

- **"CCA-F"** is a **community acronym**. One Pearson VUE rendering showed **"CCAR-F"** — so do not rely on the abbreviation as if it were official.
- Reported format: **~60 scenario-based multiple-choice questions**, **120 minutes**, passing score **~720/1000**.
- Reported cost: **~$99 per attempt** (a **$125** figure also appears). **Treat price as unconfirmed.**
- A commonly-reported **five-domain weighting** (percentages **not** confirmed):

| Domain | Reported weight |
|---|---|
| Agentic Architecture & Orchestration | ~27% |
| Claude Code Configuration & Workflows | ~20% |
| Prompt Engineering & Structured Output | ~20% |
| Tool Design & MCP Integration | ~18% |
| Context Management & Reliability | ~15% |

#### The three course frameworks

Across this prep you will keep meeting three checklists. **These are this course's working checklists, aligned to the exam domains — not necessarily Anthropic's official acronyms.** Reconcile the exact letter expansions with the vendor's official materials.

| Framework | Area | Expansion (working) |
|---|---|---|
| **PRECISE** | Prompting | **P**ersona · **R**esult · **E**xamples · **C**ontext · **I**nstructions · **S**pecification · **E**valuation |
| **SPIDER** | Agent reliability | **S**cope · **P**lan · **I**solate · **D**etect · **E**scalate · **R**ecover |
| **CALM** | Context | **C**ache · **A**ssemble selectively · **L**imit · **M**anage lifecycle |

#### The one rule to remember

> The **single authoritative source** is the partner-gated **"Claude Certified Architect – Foundations – Exam Guide" PDF** on the Anthropic Partner Academy. If anything in this handbook disagrees with that PDF, **the PDF wins.**

---

### 10.2 Module 1 — Introduction to Claude

This module covered what Claude is, the model family, how you access it, and the mental model of a **provider-agnostic** platform.

#### Expected Exam Questions

1. **A team wants the cheapest model that still handles simple classification at high volume. Which Claude model tier fits best?** — The **smallest/fastest tier (Haiku-class)**; reserve larger tiers for complex reasoning. *Answer key: match model size to task complexity, not "biggest is best."*
2. **Your architecture must swap vendors later without rewriting business logic. What pattern do you use?** — Route all model calls through a **provider abstraction** (`LLMProvider`); only vendor adapters import the vendor SDK. *Answer key: provider-agnostic core.*
3. **Where should API keys live?** — In **`.env` / environment variables only**, never in code or prompts. *Answer key: secrets via environment.*
4. **What does "context window" describe?** — The **maximum tokens** (input + output) the model can consider in one request. *Answer key: it is per-request, finite.*
5. **A stakeholder asks why you print token usage and a dollar estimate on every demo.** — Because **cost is first-class**; visibility drives good tradeoff decisions. *Answer key: observability of cost.*

#### Frequently Confused Concepts

| People confuse X with Y | The difference is… |
|---|---|
| **Model** vs **Provider** | A *model* is the trained brain (e.g., a Sonnet-class model); a *provider* is the access route/SDK that calls it. |
| **Tokens** vs **words** | Tokens are sub-word chunks; ~1 token ≈ 4 characters of English, so tokens ≠ words. |
| **Bigger model** vs **better choice** | Bigger is more capable and pricier; the *better choice* matches capability to the task. |
| **Context window** vs **memory** | Context is what fits in one request; memory is state you persist across requests. |

#### Memory Tricks

- **"Small for simple, big for brainy."** Pick the tier by task difficulty.
- **"Keys in the env, never in the text."**
- **"One door for every model"** — the provider abstraction is the single door.

#### Revision Checklist

- [ ] I can name the Claude model tiers and when to use each.
- [ ] I know why all model access goes through one provider interface.
- [ ] I can explain tokens vs words and the context window.
- [ ] I know secrets live in `.env` only.
- [ ] I can explain why cost visibility is first-class.

#### Hands-on Practice Exercise

1. Run `python topics/01-foundations/demo.py` and read the printed **usage** and **estimated `$`**. Change the prompt length and watch token counts move.
2. Open `core/providers.py` and trace one call from demo → provider interface → vendor adapter. Write one sentence on where you would add a second vendor.

#### Mini Quiz

1. Where do API keys belong? — **In `.env` / environment variables, never in code.**
2. Tokens are closer to (words / sub-word chunks)? — **Sub-word chunks.**
3. What is the context window measured in? — **Tokens (input + output).**
4. Why route all calls through `LLMProvider`? — **To stay vendor-agnostic and swappable.**
5. Pick a model tier by…? — **Task complexity, not "biggest wins."**

#### Mock Interview Questions

1. Explain provider-agnostic design and why it matters for production.
2. How would you decide which Claude model to use for a new feature?
3. What is a token, and how does it affect cost and context limits?
4. How do you keep secrets out of prompts and source control?

---

### 10.3 Module 2 — Prompting

This module covered prompt engineering and the **PRECISE** framework, plus hierarchical prompts (Base → Role → Task → Output).

#### Expected Exam Questions

1. **A prompt gives inconsistent output. Which PRECISE elements most likely fix it?** — Add **Examples** (few-shot) and a tight **Specification** of output format. *Answer key: E + S.*
2. **You want Claude to answer "as a senior security reviewer."** Which element is that? — **Persona.** *Answer key: P.*
3. **How do hierarchical prompts help reuse?** — Shared **Base** and **Role** layers stay constant; only **Task/Output** change per call. *Answer key: DRY prompts.*
4. **A model keeps adding chatty preamble.** Fix? — Constrain **Instructions/Specification** (e.g., "return only JSON, no prose"). *Answer key: I + S.*
5. **How do you know a prompt improved?** — Define **Evaluation** criteria and test against them. *Answer key: E (evaluation).*
6. **Where do you put concrete task background like the user's data?** — **Context.** *Answer key: C.*

#### Frequently Confused Concepts

| People confuse X with Y | The difference is… |
|---|---|
| **Zero-shot** vs **few-shot** | Zero-shot gives no examples; few-shot includes labeled examples to steer format/behavior. |
| **Instructions** vs **Specification** | Instructions say *what to do*; Specification pins the *exact output shape/constraints*. |
| **System prompt** vs **user prompt** | System sets durable role/rules; user carries the specific request. |
| **Persona** vs **Context** | Persona = who Claude acts as; Context = the facts it should use. |

#### Memory Tricks

- **PRECISE** = **P**ersona **R**esult **E**xamples **C**ontext **I**nstructions **S**pecification **E**valuation.
- **"Show, don't just tell"** — examples beat adjectives.
- **"Base → Role → Task → Output"** flows top to bottom, general to specific.

#### Revision Checklist

- [ ] I can expand PRECISE and give an example of each letter.
- [ ] I can layer a prompt Base → Role → Task → Output.
- [ ] I know when few-shot beats zero-shot.
- [ ] I can force strict output with Specification.
- [ ] I can define an Evaluation for a prompt.

#### Hands-on Practice Exercise

1. Take a vague prompt ("summarize this") and rewrite it through all seven PRECISE elements. Compare outputs.
2. Add two few-shot examples and a "JSON only" specification; confirm the preamble disappears.

#### Mini Quiz

1. The "E" that means test-and-measure? — **Evaluation.**
2. Few-shot means…? — **Including examples in the prompt.**
3. Which layer is most reused across tasks? — **Base (and Role).**
4. To stop chatty preamble you tighten…? — **Instructions/Specification.**
5. "Act as a tax auditor" is which element? — **Persona.**

#### Mock Interview Questions

1. Walk me through PRECISE on a real prompt you would deploy.
2. When do examples help and when do they hurt?
3. How do hierarchical prompts keep a codebase DRY?
4. How do you evaluate whether a prompt change is actually better?

---

### 10.4 Module 3 — Structured Output & Tool Use

This module covered getting reliable JSON, the **tool-use loop**, and designing tools Claude can call.

#### Expected Exam Questions

1. **You need machine-parseable results every time. Best approach?** — Define a strict **schema/specification** and validate; use tool/structured-output patterns. *Answer key: schema + validation.*
2. **Order the tool-use loop.** — **Claude requests a tool → your code executes it → you return a `tool_result` → Claude continues.** *Answer key: request → execute → result.*
3. **A tool call throws an exception. How do you report it back?** — Return a `tool_result` with **`is_error: true`** so Claude can recover. *Answer key: `is_error`.*
4. **What makes a good tool description?** — Clear name, purpose, and **typed input schema** so Claude picks and fills it correctly. *Answer key: precise schema.*
5. **Claude "hallucinates" a field your parser rejects. First fix?** — Tighten the **output schema** and add an example; validate and re-ask on failure. *Answer key: constrain + validate.*

#### Frequently Confused Concepts

| People confuse X with Y | The difference is… |
|---|---|
| **Tool use** vs **structured output** | Tool use lets Claude *call your code*; structured output shapes the *text it returns*. |
| **Claude runs the tool** vs **your code runs it** | Claude only *requests*; **your code executes** and returns the result. |
| **`is_error`** vs **crashing** | `is_error: true` tells Claude the tool failed so it can adapt; crashing kills the loop. |
| **Function name** vs **description** | The name identifies; the description + schema teach Claude *when and how* to use it. |

#### Memory Tricks

- **"Claude asks, you act, you answer."** (request → execute → result)
- **"Errors go home flagged"** — return failures with `is_error: true`.
- **"Schema is the contract."**

#### Revision Checklist

- [ ] I can list the four steps of the tool-use loop.
- [ ] I know Claude requests but never executes tools itself.
- [ ] I return failures as `tool_result` with `is_error: true`.
- [ ] I can write a tool input schema.
- [ ] I can force strict JSON output and validate it.

#### Hands-on Practice Exercise

1. Define a `get_weather(city)` tool with a typed schema; simulate the loop: request → execute → `tool_result` → final answer.
2. Make the tool raise an error; return `is_error: true` and watch Claude recover gracefully.

#### Mini Quiz

1. Who executes the tool? — **Your code, not Claude.**
2. How do you signal a failed tool? — **`tool_result` with `is_error: true`.**
3. What teaches Claude how to call a tool? — **Its name, description, and input schema.**
4. What comes right after "Claude requests a tool"? — **Your code executes it.**
5. Best fix for unparseable output? — **Tighten the schema and validate.**

#### Mock Interview Questions

1. Describe the full tool-use loop end to end.
2. How do you handle a tool that errors mid-loop?
3. How do you guarantee valid JSON from a model?
4. What separates a well-designed tool from a confusing one?

---

### 10.5 Module 4 — Claude Code

This module covered **Claude Code** as an agentic coding tool: configuration, workflows, permissions, and project memory (`CLAUDE.md`).

#### Expected Exam Questions

1. **Where do project-wide conventions and memory live for Claude Code?** — In **`CLAUDE.md`** at the project root. *Answer key: CLAUDE.md.*
2. **You want to stop repeated permission prompts for safe read commands.** What do you configure? — An **allowlist in settings** (permissions). *Answer key: settings permissions.*
3. **A teammate wants an action to run automatically after every edit.** Memory or hooks? — **Hooks** in settings.json — the harness runs them, not the model. *Answer key: hooks.*
4. **Which file scopes are there for settings?** — **User** vs **project** settings (project overrides user for that repo). *Answer key: user/project scope.*
5. **How does Claude Code stay safe with the filesystem/shell?** — Through the **permission system** and sandboxing, prompting before risky actions. *Answer key: permissions/sandbox.*

#### Frequently Confused Concepts

| People confuse X with Y | The difference is… |
|---|---|
| **CLAUDE.md** vs **a prompt** | CLAUDE.md is persistent project memory/instructions; a prompt is one request. |
| **Memory/preferences** vs **hooks** | Preferences guide Claude; hooks are code the *harness* runs automatically on events. |
| **User settings** vs **project settings** | User = your global defaults; project = repo-specific, overrides user there. |
| **Permission allow** vs **auto-run everything** | Allowlisting known-safe commands still keeps risky actions gated. |

#### Memory Tricks

- **"CLAUDE.md is the project's long-term memory."**
- **"Automatic = hooks, guidance = memory."**
- **"Project beats user"** (settings precedence).

#### Revision Checklist

- [ ] I know CLAUDE.md holds project conventions and memory.
- [ ] I can add a permission allowlist entry.
- [ ] I know hooks (not memory) create automatic behaviors.
- [ ] I understand user vs project settings scope.
- [ ] I can explain the permission/sandbox safety model.

#### Hands-on Practice Exercise

1. Add a short convention to this repo's `CLAUDE.md` and observe Claude Code honoring it.
2. Add an allowlist entry for a safe read-only command in project settings and confirm the prompt disappears.

#### Mini Quiz

1. Where does project memory live? — **CLAUDE.md.**
2. Automatic "after every X" behavior needs…? — **A hook in settings.json.**
3. Which settings win in a repo? — **Project settings.**
4. What gates risky filesystem/shell actions? — **The permission system.**
5. Preferences change Claude's…? — **Guidance/behavior, not automatic execution.**

#### Mock Interview Questions

1. How do you give Claude Code durable project context?
2. When would you use a hook instead of a written instruction?
3. Explain the settings precedence between user and project.
4. How does Claude Code stay safe when running commands?

---

### 10.6 Module 5 — Agents & the Agent SDK

This module covered building agents: the **agent loop**, **max-iteration caps**, **subagents** (decompose → fan-out → synthesize), and the **SPIDER** reliability checklist.

#### Expected Exam Questions

1. **An agent loops forever calling tools. What safeguard is missing?** — A **max-iteration cap** on the loop. *Answer key: iteration limit.*
2. **A big research task has independent parts. Best pattern?** — **Subagents**: decompose, fan-out in parallel, then **synthesize**. *Answer key: decompose→fan-out→synthesize.*
3. **Which SPIDER step means "keep a failing subtask from corrupting the whole run"?** — **Isolate.** *Answer key: I.*
4. **The agent hits something it cannot safely handle.** Which SPIDER step? — **Escalate** (hand to human/higher authority). *Answer key: E.*
5. **After a tool failure the agent should retry/back off/repair.** Which step? — **Recover.** *Answer key: R.*
6. **Before starting, the agent should define boundaries and a plan.** Which steps? — **Scope** then **Plan.** *Answer key: S + P.*

#### Frequently Confused Concepts

| People confuse X with Y | The difference is… |
|---|---|
| **Agent** vs **single prompt** | An agent loops with tools toward a goal; a single prompt is one shot. |
| **Detect** vs **Recover** | Detect *notices* a problem; Recover *fixes/retries* it. |
| **Isolate** vs **Escalate** | Isolate contains a failure locally; Escalate hands it upward. |
| **Subagent fan-out** vs **one giant agent** | Fan-out parallelizes independent work and keeps contexts clean. |
| **Max iterations** vs **timeout** | Iteration cap limits *loop turns*; timeout limits *wall-clock time*. |

#### Memory Tricks

- **SPIDER** = **S**cope **P**lan **I**solate **D**etect **E**scalate **R**ecover.
- **"Decompose, fan-out, synthesize."**
- **"Always cap the loop."**

#### Revision Checklist

- [ ] I can describe the agent loop and why it needs a max-iteration cap.
- [ ] I can expand SPIDER and give a scenario per letter.
- [ ] I know the subagent pattern: decompose → fan-out → synthesize.
- [ ] I can distinguish Detect vs Recover and Isolate vs Escalate.
- [ ] I know when a single prompt beats a full agent.

#### Hands-on Practice Exercise

1. Sketch (or code) an agent loop with a hard cap of, say, 8 iterations; log each turn.
2. Take a multi-part question, split it into 3 subagent tasks, run them, and write a synthesis step that merges results.

#### Mini Quiz

1. What stops an infinite agent loop? — **A max-iteration cap.**
2. SPIDER's "I" is…? — **Isolate.**
3. Merging subagent outputs is called…? — **Synthesize.**
4. Handing a hard failure to a human is…? — **Escalate.**
5. Noticing vs fixing a failure = ? — **Detect vs Recover.**

#### Mock Interview Questions

1. Walk through your agent loop and its safety limits.
2. Explain SPIDER with a real reliability incident.
3. When do you reach for subagents instead of one agent?
4. How do you contain a failing subtask?

---

### 10.7 Module 6 — Model Context Protocol (MCP)

This module covered **MCP**: the client/server model, the **"USB-C for AI"** analogy, and lazy-loaded servers that expose tools/resources.

#### Expected Exam Questions

1. **What problem does MCP solve?** — A **standard way to connect Claude to external tools/data**, so integrations are reusable across apps ("USB-C for AI"). *Answer key: standard connector.*
2. **In MCP, which side exposes tools and which side consumes them?** — The **server exposes**; the **client (the app/host)** consumes. *Answer key: server exposes, client consumes.*
3. **Why lazy-load MCP servers?** — Start them only when needed to save resources and keep the core independent. *Answer key: lazy, independent.*
4. **You want the same weather integration usable by many Claude apps.** Build it as…? — An **MCP server**. *Answer key: reusable server.*
5. **What is the USB-C analogy teaching?** — **One standard port** replaces many custom cables/integrations. *Answer key: universal interface.*

#### Frequently Confused Concepts

| People confuse X with Y | The difference is… |
|---|---|
| **MCP client** vs **MCP server** | Client = the host app using tools; server = the process exposing tools/resources. |
| **MCP** vs **the tool-use loop** | MCP is *how tools are connected/standardized*; the tool-use loop is *how a call is executed within a turn*. |
| **MCP server** vs **API endpoint** | An MCP server speaks the MCP protocol so any MCP client can plug in, not a bespoke API. |
| **Tools** vs **resources** | Tools are actions Claude can invoke; resources are data/context the server exposes. |

#### Memory Tricks

- **"MCP = USB-C for AI"** — one port, many devices.
- **"Server serves, client consumes."**
- **"Lazy servers stay light."**

#### Revision Checklist

- [ ] I can state the problem MCP solves in one sentence.
- [ ] I know which side is client vs server.
- [ ] I can explain the USB-C analogy.
- [ ] I know why servers are independent and lazy-loaded.
- [ ] I can tell tools apart from resources.

#### Hands-on Practice Exercise

1. Install the MCP extra (`pip install -e ".[mcp]"`) and run an MCP topic demo; identify the client and the server in the flow.
2. Sketch a small MCP server exposing one tool and one resource; note how any client could reuse it.

#### Mini Quiz

1. MCP is often called…? — **USB-C for AI.**
2. Which side exposes tools? — **The server.**
3. Why lazy-load servers? — **Save resources / stay independent.**
4. Reusable integration across apps = build a…? — **MCP server.**
5. Actions vs data on a server = ? — **Tools vs resources.**

#### Mock Interview Questions

1. Explain MCP to a non-technical stakeholder using the USB-C analogy.
2. What are the roles of client and server in MCP?
3. When would you build an MCP server instead of a one-off tool?
4. How does MCP improve reuse across multiple Claude apps?

---

### 10.8 Module 7 — Context Management

This module covered the **CALM** checklist, **prompt caching** (the prefix rule), and **context vs memory**.

#### Expected Exam Questions

1. **Your cached prompt stopped getting cache hits after you added a timestamp near the top. Why?** — Any change to the **cached prefix invalidates** it; volatile data must go **after** the prefix. *Answer key: prefix rule.*
2. **How do you verify a cache hit actually happened?** — Check that **`cache_read_input_tokens > 0`** in the usage. *Answer key: read the usage field.*
3. **Where should you place static system instructions vs the user's changing question?** — Static, reusable content **first (cacheable prefix)**; volatile content **after**. *Answer key: stable prefix, volatile tail.*
4. **CALM's "L" tells you to…?** — **Limit** what you load into context (don't dump everything). *Answer key: Limit.*
5. **Difference between context and memory?** — **Context** is per-request working data; **memory** is state **persisted** across requests. *Answer key: per-request vs persisted.*
6. **You keep hitting the context window. Which CALM steps help most?** — **Assemble selectively** and **Limit**. *Answer key: A + L.*

#### Frequently Confused Concepts

| People confuse X with Y | The difference is… |
|---|---|
| **Context** vs **memory** | Context = what's in this request; memory = what you save and reload later. |
| **Prompt caching** vs **memory** | Caching reuses a *token prefix* for speed/cost; memory persists *facts/state*. |
| **Cache prefix** vs **whole prompt** | Only the *unchanged prefix* is cached; edit it and you lose the hit. |
| **Assemble selectively** vs **stuff everything** | Selective assembly picks only relevant context; stuffing wastes tokens and money. |

#### Memory Tricks

- **CALM** = **C**ache · **A**ssemble selectively · **L**imit · **M**anage lifecycle.
- **"Stable stuff first, volatile stuff last."** (the prefix rule)
- **"No `cache_read_input_tokens`, no cache hit."**
- **"Context is now; memory is later."**

#### Revision Checklist

- [ ] I can expand CALM.
- [ ] I can state the prompt-caching prefix rule.
- [ ] I know volatile data goes after the cached prefix.
- [ ] I verify hits with `cache_read_input_tokens > 0`.
- [ ] I can clearly separate context from memory.

#### Hands-on Practice Exercise

1. Build a prompt with a large stable system prefix + a small changing question. Send it twice and confirm `cache_read_input_tokens > 0` on the second call.
2. Now move a timestamp into the prefix; observe the cache miss and explain why.

#### Mini Quiz

1. Editing the cached prefix does what? — **Invalidates the cache.**
2. Volatile data belongs…? — **After the prefix.**
3. Prove a cache hit with…? — **`cache_read_input_tokens > 0`.**
4. CALM's "A" means…? — **Assemble selectively.**
5. Persisted-across-requests state is…? — **Memory (not context).**

#### Mock Interview Questions

1. Explain prompt caching and the prefix rule with a failure example.
2. How do you verify caching is actually saving cost?
3. Contrast context and memory in a production app.
4. How do you keep a long-running task under the context limit?

---

### 10.9 Module 8 — Reliability, Cost & Production

This module covered making Claude apps production-ready: **cost estimation**, **evaluation**, error handling, and applying SPIDER/CALM together.

#### Expected Exam Questions

1. **Two designs both work; one uses a bigger model on every call. How do you choose?** — Weigh **cost vs quality tradeoff**; use the smaller model where quality holds, escalate only when needed. *Answer key: tradeoff decision.*
2. **How do you know a prompt/agent change didn't regress quality?** — Run it against an **evaluation set** with defined criteria. *Answer key: evals.*
3. **A production agent occasionally fails a tool call. What must exist?** — **Detect + Recover** (retry/backoff) and **Escalate** paths. *Answer key: SPIDER reliability.*
4. **Costs spiked. First things to inspect?** — **Token usage**, model tier, and whether **caching** is being hit. *Answer key: usage + caching.*
5. **Why print usage and `$` on every demo?** — To make **cost a first-class, visible** design input. *Answer key: cost observability.*

#### Frequently Confused Concepts

| People confuse X with Y | The difference is… |
|---|---|
| **Works once** vs **reliable** | A demo can work once; reliability means it handles failures every time. |
| **Cheaper model** vs **cheaper system** | A cheaper model can cost more if it needs retries; measure the *whole* flow. |
| **Evaluation** vs **eyeballing** | Evals are repeatable, criteria-based; eyeballing doesn't catch regressions. |
| **Latency** vs **cost** | Faster ≠ cheaper; both are separate tradeoff levers. |

#### Memory Tricks

- **"Measure the flow, not the model."**
- **"If you can't eval it, you can't trust it."**
- **"Cost is a feature."**

#### Revision Checklist

- [ ] I can reason about cost/quality/latency tradeoffs.
- [ ] I can build a small evaluation to catch regressions.
- [ ] I apply Detect/Recover/Escalate for reliability.
- [ ] I can diagnose a cost spike (tokens, tier, caching).
- [ ] I treat cost visibility as first-class.

#### Hands-on Practice Exercise

1. Take one demo and compute its per-call cost from printed usage; try a smaller model and compare quality vs price.
2. Write a 5-case evaluation set with pass/fail criteria and run it before and after a prompt change.

#### Mini Quiz

1. Prove a change didn't regress quality? — **Run an evaluation set.**
2. First suspects in a cost spike? — **Token usage, model tier, caching.**
3. Reliability needs which SPIDER trio most? — **Detect, Recover, Escalate.**
4. Cheaper model that retries a lot may be…? — **More expensive overall.**
5. Why is cost first-class? — **It's a real design tradeoff, made visible.**

#### Mock Interview Questions

1. How do you make a Claude feature production-reliable?
2. Describe your evaluation strategy for prompt/agent changes.
3. How do you keep costs under control at scale?
4. Give an example of a cost vs quality tradeoff you'd make.

---

### 10.10 Module 9 — Complete Architecture

This capstone tied everything together: a **provider-agnostic kernel**, shared capabilities (prompts, skills, agents, MCP, context), and how the pieces compose into a production system.

#### Expected Exam Questions

1. **Only which folder may import a vendor SDK?** — Only **`providers/<vendor>/`**; the core stays vendor-agnostic (ADR 0001). *Answer key: provider adapters only.*
2. **A demo re-implements its own provider call. What convention does it break?** — **DRY demos** must reuse `core/` + shared capabilities, never re-implement. *Answer key: DRY / reuse.*
3. **Design principle for files?** — **Many small files, one responsibility each.** *Answer key: single responsibility.*
4. **You must add a new skill. Where and how?** — `skills/<name>/SKILL.md` with **frontmatter (name, description) + body**. *Answer key: SKILL.md contract.*
5. **How does the architecture combine PRECISE, SPIDER, and CALM?** — Prompting (**PRECISE**) feeds agents (**SPIDER** reliability) that manage context (**CALM**), all behind the provider kernel. *Answer key: layered composition.*
6. **Where does a new provider plug in and what must it implement?** — In `providers/<name>/`, implementing **`core.providers.LLMProvider`**. *Answer key: implement the interface.*

#### Frequently Confused Concepts

| People confuse X with Y | The difference is… |
|---|---|
| **Kernel/core** vs **capabilities** | Core is the vendor-agnostic engine; capabilities (prompts/skills/agents/MCP) plug into it. |
| **Reusing core** vs **re-implementing** | DRY demos call shared code; re-implementing a provider call violates conventions. |
| **Skill** vs **agent** | A skill is a packaged instruction set; an agent composes capabilities toward a goal. |
| **Topic** vs **project/workflow** | Topics are the presentation spine (README + demo); projects/workflows are execution. |

#### Memory Tricks

- **"One door for models, one job per file."**
- **"Vendors only in `providers/`."**
- **"Demos reuse, never re-do."**

#### Revision Checklist

- [ ] I know only `providers/<vendor>/` may import a vendor SDK.
- [ ] I can explain the DRY-demo rule.
- [ ] I can add a provider, skill, agent, MCP server, or topic by its contract.
- [ ] I can describe how PRECISE, SPIDER, and CALM compose.
- [ ] I understand core vs capabilities vs execution layers.

#### Hands-on Practice Exercise

1. Trace one topic demo from `topics/NN-*/demo.py` through `core/` to a provider adapter; mark every reuse point.
2. Draft a `skills/<name>/SKILL.md` with valid frontmatter and a short body describing when to use it.

#### Mini Quiz

1. Who may import a vendor SDK? — **Only `providers/<vendor>/`.**
2. Demos must…? — **Reuse core, never re-implement.**
3. A new provider implements…? — **`core.providers.LLMProvider`.**
4. A skill is defined in…? — **`skills/<name>/SKILL.md` (frontmatter + body).**
5. Files should have…? — **One responsibility each.**

#### Mock Interview Questions

1. Whiteboard the full architecture from demo to provider.
2. Why isolate vendor SDKs to the providers layer?
3. How do PRECISE, SPIDER, and CALM fit into one system?
4. Show how you'd extend the platform with a new capability.

---

### 10.11 Final Mock Exam

Fifteen mixed, scenario-style questions. Pick one option. **Answer key is at the very end — resist peeking.**

**Q1.** A team wants to swap model vendors later without touching business logic. Best design?
- A) Call the vendor SDK directly from each demo
- B) Route all model calls through a single provider interface
- C) Hard-code the vendor in the core
- D) Duplicate provider code per topic

**Q2.** You added a timestamp to the top of a cached prompt and cache hits vanished. Why?
- A) Timestamps can't be cached
- B) The cache expired
- C) Any change to the cached prefix invalidates it
- D) Caching only works for output tokens

**Q3.** Which SPIDER step means containing a failing subtask so it doesn't corrupt the whole run?
- A) Detect
- B) Escalate
- C) Recover
- D) Isolate

**Q4.** In MCP, which side exposes tools/resources?
- A) The client
- B) The server
- C) The model
- D) The proxy

**Q5.** A tool call throws an exception mid-loop. How do you report it to Claude?
- A) Silently drop it
- B) Crash the loop
- C) Return a `tool_result` with `is_error: true`
- D) Retry forever with no signal

**Q6.** Where do project-wide conventions and memory live for Claude Code?
- A) In each prompt
- B) In `CLAUDE.md`
- C) In the vendor SDK
- D) In environment variables

**Q7.** Which PRECISE element pins the exact output format?
- A) Persona
- B) Context
- C) Specification
- D) Result

**Q8.** How do you verify a prompt-cache hit actually occurred?
- A) The response is faster
- B) `cache_read_input_tokens > 0` in usage
- C) The prompt is shorter
- D) You can't verify it

**Q9.** A big research task has independent parts. Best pattern?
- A) One giant single prompt
- B) Subagents: decompose → fan-out → synthesize
- C) Increase the temperature
- D) Remove the iteration cap

**Q10.** Which folder is the ONLY place allowed to import a vendor SDK?
- A) `topics/`
- B) `core/`
- C) `providers/<vendor>/`
- D) `skills/`

**Q11.** You need a "run automatically after every edit" behavior. What do you use?
- A) A written preference in memory
- B) A hook in settings.json
- C) A longer prompt
- D) A bigger model

**Q12.** What is the correct order of the tool-use loop?
- A) Your code executes → Claude requests → return result
- B) Claude requests → your code executes → return `tool_result`
- C) Return result → Claude requests → your code executes
- D) Claude executes → you request → Claude returns

**Q13.** Which best describes context vs memory?
- A) They are the same thing
- B) Context persists forever; memory is per-request
- C) Context is per-request; memory is persisted across requests
- D) Both are only about caching

**Q14.** According to the confirmed facts, the CCA-F exam is currently…
- A) An open public exam anyone can book
- B) Gated to Claude Partner Network organizations
- C) Free and unproctored
- D) Retired

**Q15.** A cheaper model needs many retries to succeed. What's the right conclusion?
- A) It's always cheaper — pick it
- B) Measure the whole flow; it may cost more overall
- C) Retries are free
- D) Model tier never affects cost

#### Answer Key

| Q | Answer | Q | Answer | Q | Answer |
|---|---|---|---|---|---|
| 1 | **B** | 6 | **B** | 11 | **B** |
| 2 | **C** | 7 | **C** | 12 | **B** |
| 3 | **D** | 8 | **B** | 13 | **C** |
| 4 | **B** | 9 | **B** | 14 | **B** |
| 5 | **C** | 10 | **C** | 15 | **B** |

**Scoring guide (informal):** 13–15 = exam-ready; 10–12 = solid, revise weak spots; below 10 = redo the module checklists.

---

### 10.12 Two-Week Study Plan

A steady ~1–1.5 hour/day plan. Adjust to your schedule, but keep the **review days** and the **two full mocks**.

| Day | Focus | Do this |
|---|---|---|
| **Day 1** | 10.1 Exam facts | Memorize CONFIRMED vs UNVERIFIED; note the four core areas. |
| **Day 2** | Module 1 (10.2) | Provider-agnostic design, tokens, model tiers. Run the foundations demo. |
| **Day 3** | Module 2 (10.3) | Drill PRECISE; rewrite a vague prompt through all 7 elements. |
| **Day 4** | Module 3 (10.4) | Tool-use loop + `is_error`; structured output. Do the weather-tool drill. |
| **Day 5** | Module 4 (10.5) | Claude Code: CLAUDE.md, hooks vs memory, settings scope. |
| **Day 6** | Module 5 (10.6) | Agent loop, iteration caps, SPIDER, subagents. |
| **Day 7** | **Review + mini-mock** | Redo mini quizzes for Modules 1–5; note weak spots. |
| **Day 8** | Module 6 (10.7) | MCP client/server, USB-C analogy, tools vs resources. |
| **Day 9** | Module 7 (10.8) | CALM, prompt-caching prefix rule, context vs memory. Do the cache drill. |
| **Day 10** | Module 8 (10.9) | Cost/quality tradeoffs, evaluations, reliability. |
| **Day 11** | Module 9 (10.10) | Full architecture; trace a demo to a provider. |
| **Day 12** | **Full mock #1** | Sit 10.11 timed; grade; list every miss. |
| **Day 13** | **Targeted repair** | Re-study only your missed topics; redo their checklists. |
| **Day 14** | **Full mock #2 + light review** | Retake 10.11, skim all mnemonics, rest before exam. |

> Golden rule: end each day able to **expand PRECISE, SPIDER, and CALM from memory**. If you can recite those three and the prompt-caching prefix rule, you've covered the spine of the exam.

---

### 10.13 Exam-Day Tips

**Before the exam**
- Confirm your **OnVUE / Pearson VUE** system check and quiet, well-lit room the day before.
- Have ID ready; clear your desk (online proctoring is strict).
- Re-skim only your **mnemonics and checklists** — no cramming new material.

**During the exam**
- Questions are **scenario-based**: read for the *actual constraint* (cost? reliability? reuse?) before choosing.
- Watch for **tradeoff wording** ("cheapest that still…", "without rewriting…") — the answer usually balances, not maximizes.
- Eliminate obviously wrong options first; two choices are often near-duplicates — the *precise* one wins.
- **Flag and move on** if stuck; time is finite (reported ~120 min for ~60 questions ≈ 2 min each).
- When unsure between "model runs the tool" vs "your code runs the tool," remember **your code executes**.
- If a question references official policy, favor the **official/confirmed** answer over community rumor.

**Mindset**
- Trust your checklists. Most traps are *plausible-but-imprecise* distractors, not trick math.
- Answer every question — there's no benefit to leaving blanks.

---

### Quick Recap

- The **CCA-F (Claude Certified Architect, Foundations)** is Anthropic's real, partner-gated technical cert delivered via **Pearson VUE / OnVUE**, validating **Claude Code · Agent SDK · Claude API · MCP** with a focus on **tradeoffs**. Details like question count, price, and domain weights are **reported but unconfirmed** — reconcile against the **official Exam Guide PDF**.
- Master the three working checklists: **PRECISE** (prompting), **SPIDER** (agent reliability), **CALM** (context).
- Nail the mechanics: **prompt-caching prefix rule** (stable first, volatile last; verify with `cache_read_input_tokens > 0`), the **tool-use loop** (Claude requests → your code executes → return `tool_result`, flag failures with `is_error`), **MCP** (server exposes, client consumes — "USB-C for AI"), **agent loops** with **max-iteration caps**, **subagents** (decompose → fan-out → synthesize), and **context vs memory** (per-request vs persisted).
- Study with the **two-week plan**, sit both **full mocks**, and on exam day read for the **constraint** and pick the **precise** answer.
- When in doubt, the **official Anthropic Partner Academy Exam Guide is the single source of truth.** Good luck — you've got this.
