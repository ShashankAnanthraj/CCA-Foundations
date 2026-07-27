# The CCA‑F Training Handbook

### A Beginner‑Friendly Guide to Claude, Prompting, Context, Tools, MCP, and Agents — Built for the Anthropic *Claude Certified Architect – Foundations* Exam

*A classroom‑ready training handbook. Assumes basic programming, assumes zero Claude experience, and builds every concept from first principles.*

---

## Who this handbook is for

This book is written for people who can **write a little code** but have **never worked with Claude**:

- Software Engineers · Data Engineers · Cloud Engineers
- AI beginners and freshers
- Experienced professionals moving into AI for the first time

If you have never touched an AI model in your life, you are in the right place. Every term is explained in plain English before it is used.

---

## How to use this handbook

**If you are a learner** — read the modules in order (1 → 10). Each concept is taught the same way every time, so you always know what is coming next. Do the *Live Demos* as you go; they make abstract ideas click. Finish with **Module 10**, which is pure exam preparation.

**If you are a trainer** — every topic has a `> Trainer Note` with a tip for presenting it live, a *Live Demo* you can run on screen, and *Interview Questions* you can use as classroom checks. Each module ends with a **Quick Recap** slide you can read aloud.

**If you are revising for the exam** — jump straight to **Module 10 (Certification Preparation)**, then use the per‑module *One‑Page Summaries* and the **Glossary** at the back as flashcards.

---

## The teaching method (every topic follows this)

To make learning predictable, **every topic** in this handbook is taught in the same 12 steps:

| # | Step | What it gives you |
|---|---|---|
| 1 | **Definition** | What it is, in 5–8 plain lines |
| 2 | **Why do we need it?** | The problem it solves |
| 3 | **Office Analogy** | The idea, mapped to a software company |
| 4 | **Real‑Life Analogy** | One everyday comparison |
| 5 | **Internal Working** | Step‑by‑step, what happens inside |
| 6 | **Architecture Diagram** | A clean ASCII picture |
| 7 | **Real Example** | A realistic business case |
| 8 | **Live Demo** | Something to run in class |
| 9 | **Interview Questions** | 5 basic · 5 intermediate · 5 scenario |
| 10 | **Common Mistakes** | What beginners get wrong, and why |
| 11 | **Best Practices** | How the pros use it |
| 12 | **One‑Page Summary** | Key points, terms, revision notes, mnemonic |

When you see the same shape again and again, the *content* is all you have to focus on.

---

## Three frameworks you will memorize

Three simple checklists run through the whole book. Learn them now; you will meet them in every module and on the exam.

```
 PRECISE  → how to write a good PROMPT
 CALM     → how to manage CONTEXT (the model's working memory)
 SPIDER   → how to make an AGENT reliable
```

| Framework | Domain | The letters |
|---|---|---|
| **PRECISE** | Prompt Engineering | **P**ersona · **R**esult · **E**xamples · **C**ontext · **I**nstructions · **S**pecification · **E**valuation |
| **CALM** | Context Management | **C**ache · **A**ssemble selectively · **L**imit (budget) · **M**anage lifecycle |
| **SPIDER** | Agent Reliability | **S**cope · **P**lan · **I**solate · **D**etect · **E**scalate · **R**ecover |

> **A note on names:** PRECISE, SPIDER, and CALM are this course's **working checklists**, aligned to the exam's domains. The *practices* they describe are stable and correct. If the official exam materials spell the acronyms differently, trust the official wording for the letters — but the underlying habits are what actually get tested.

---

## What's in the box — module map

| Module | Title | You will learn |
|---|---|---|
| **1** | Introduction to Claude | What Claude is, the model family, the API, capabilities & limits |
| **2** | Prompting | Prompts, system/user/assistant roles, prompt engineering, XML, few‑shot, roles, chaining |
| **3** | Context Management | Context, context window, tokens, history, long context, compression, editing, overflow, limits |
| **4** | Memory | Context vs memory, stateless vs stateful, persistent & external memory |
| **5** | Tool Use | Tools, function calling, tool schema, tool results, parallel tool calls |
| **6** | Model Context Protocol (MCP) | The "USB‑C for AI" — clients, servers, resources, tools, prompts, sampling, transport, auth, security |
| **7** | Agents | What an agent is and the full agent loop |
| **8** | Subagents | Delegation, decomposition, parallel execution, aggregation, multi‑agent teams |
| **9** | Complete Claude Architecture | Every piece connected, end to end, every arrow explained |
| **10** | CCA‑F Certification Preparation | Exam facts, per‑module drills, mock exam, study plan |

At the very back you will find a **Glossary** of every Claude and Anthropic term used in this book.

---

## A quick, honest word about the exam

The **Claude Certified Architect – Foundations** exam is a **real, Anthropic‑administered** certification (announced 2026‑03‑12, delivered through Pearson VUE). It is currently **gated to Claude Partner Network organizations**. It tests four core areas — **Claude Code, the Claude Agent SDK, the Claude API, and MCP** — with a strong emphasis on making **real‑world trade‑off decisions**.

Some widely‑circulated details (the "CCA‑F" abbreviation, ~60 questions, 120 minutes, ~720/1000 to pass, the domain percentages) come from **third‑party prep sites and are not officially confirmed**. This handbook flags what is official and what is not. The single source of truth is the official **Exam Guide PDF** on the Anthropic Partner Academy — always reconcile against it.

Now — let's begin.

---


---

## Module 1 — Introduction to Claude

Welcome to your first module. Here you will meet **Claude**, understand the different Claude models, learn how programs talk to Claude through the **API**, and see honestly what Claude can and cannot do. No prior AI knowledge is assumed — we build every idea from the ground up.

---

### 1.1 What is Claude?

#### 1. Definition
**Claude** is a family of **large language model (LLM)** AI assistants built by **Anthropic**, an AI safety company. In plain words, Claude is a computer program that reads text you give it and writes helpful text back. It can answer questions, write and explain code, summarize documents, and much more. You reach Claude through the **Claude apps** (chat), the **Claude API** (for developers), and tools like **Claude Code**. Claude is designed to be **helpful, honest, and harmless**.

#### 2. Why do we need it?
Before assistants like Claude, software could only do exactly what a programmer coded, step by step. Anything involving **human language** — reading an email, summarizing a report, answering a customer — needed a human or a very rigid, brittle rule-set. That does not scale: humans are slow and expensive, and rules break the moment wording changes. Claude solves this by **understanding and generating natural language**, so one system can handle open-ended language tasks that used to require a person.

#### 3. Office Analogy
Imagine a software company hires a brilliant **new employee** who has read an enormous library of books, manuals, and code. You can hand this employee almost any text task — "summarize this ticket," "draft this email," "explain this function" — and they respond quickly. They do not replace the CEO or your database; they are a smart, tireless **generalist assistant** sitting at a desk, ready whenever you ask.

#### 4. Real-Life Analogy
Claude is like a **knowledgeable librarian** you can talk to. You walk up, ask a question in normal language, and the librarian gives a clear, helpful answer drawn from everything they have read. But like any librarian working from memory, they can occasionally misremember — so for critical facts you still verify.

#### 5. Internal Working
1. You send Claude some **text** (your question or instruction).
2. Claude breaks the text into small pieces called **tokens** (roughly word-parts).
3. Claude's neural network predicts the most suitable **next token**, over and over.
4. Those predicted tokens are joined back into readable text.
5. Claude returns that text to you as its **reply**.
6. Each request is (by default) **independent** — Claude does not remember past chats unless you resend them.

#### 6. Architecture Diagram
```
   YOU / YOUR APP                 CLAUDE (the model)
 ┌───────────────┐   text in    ┌─────────────────────┐
 │  Question or  │ ───────────► │  1. Split into      │
 │  instruction  │              │     tokens          │
 └───────────────┘              │  2. Predict next    │
         ▲                      │     token, repeat   │
         │      text out        │  3. Build reply     │
         └───────────────────── └─────────────────────┘
```

#### 7. Real Example
A support team gets a long, angry customer email. They send it to Claude with the instruction: *"Summarize this email in 3 bullet points and suggest a polite reply."* Claude reads the whole email, identifies the core complaint, and returns a short summary plus a draft response. What took an agent 10 minutes now takes seconds, and the agent just reviews and sends.

#### 8. Live Demo
In the Claude app (or via the API), type:
> *"In one sentence, explain what you are and what you can help me with."*

Claude will describe itself as an AI assistant. Then ask a follow-up like *"Now summarize that in 5 words."* Learners immediately see that Claude **understands** the request and **reshapes** its own answer — no coding required.

#### 9. Interview Questions
**Basic**
1. What is Claude in one sentence?
2. Who builds Claude?
3. Name three ways you can access Claude.
4. What does "LLM" stand for?
5. What are the three design goals (helpful, honest, harmless) called?

**Intermediate**
1. Why is Claude better than rigid rule-based systems for language tasks?
2. What is a token, and why does it matter?
3. Does Claude remember previous conversations by default? Explain.
4. What kind of input does Claude take, and what does it return?
5. How does Claude differ from a search engine?

**Scenario-based**
1. A team wants to auto-summarize support tickets. How would Claude help?
2. A junior dev asks Claude to explain unfamiliar code. Is that a good use? Why?
3. Your manager asks if Claude can replace the company database. How do you answer?
4. A user complains Claude "forgot" what they said earlier. What is the likely cause?
5. When would you NOT trust Claude's answer without checking?

#### 10. Common Mistakes
- **Thinking Claude "knows" everything perfectly** — it predicts likely text and can be wrong.
- **Assuming Claude remembers past chats** — by default each call is independent.
- **Treating Claude as a database or calculator** — it is a language model, not exact storage or math.
- **Giving vague instructions** — unclear prompts give unclear answers.

#### 11. Best Practices
- Give **clear, specific** instructions.
- State the **format** you want (bullets, table, one sentence).
- **Verify** important facts from a trusted source.
- Use Claude for **language-heavy** work; use real databases/tools for exact data.

#### 12. One-Page Summary
- **Key points:** Claude is an Anthropic LLM assistant; reads text, writes text; accessed via apps, API, and Claude Code; built to be helpful, honest, harmless.
- **Important terms:** LLM, token, Anthropic, prompt, assistant.
- **Quick revision:** Text in → tokens → predict → text out. Stateless by default.
- **Mnemonic:** **CLAUDE** = **C**omputer **L**anguage **A**ssistant, **U**nderstands & writes, **D**esigned safe, **E**asy to access.

> **Trainer Note:** Open with a live chat on the projector before any theory — seeing Claude answer a real question hooks beginners faster than any slide.

---

### 1.2 Claude Model Family

#### 1. Definition
Claude is not a single program — it is a **family of models**. Each model offers a different balance of **capability, speed, and cost**. Current families include the **Claude 5 family** (for example **Sonnet 5** and **Fable 5**), plus **Opus 4.8** (deepest reasoning, most capable) and **Haiku 4.5** (fastest, most economical). The simple rule of thumb: **Opus** = hardest reasoning, **Sonnet** = balanced everyday default, **Haiku** = fast, cheap, high-volume. Model IDs look like `claude-opus-4-8`, `claude-sonnet-5`, `claude-haiku-4-5`.

#### 2. Why do we need it?
One-size-fits-all is wasteful. Using a huge, powerful model for a tiny task wastes **money and time**; using a tiny model for a hard task gives **poor results**. A family lets you match the **right tool to the right job** — pay for deep reasoning only when you need it, and use a fast cheap model for simple, high-volume work.

#### 3. Office Analogy
Think of three staff levels. **Opus** is the senior architect — brilliant, thorough, but expensive and takes their time on hard problems. **Sonnet** is the reliable mid-level engineer — great at most daily work, good speed, sensible cost. **Haiku** is the quick intern — lightning fast and cheap, perfect for lots of small, routine tasks. A smart manager assigns each task to the right person.

#### 4. Real-Life Analogy
It is like choosing transport. **Opus** is a chauffeured car for a critical, complex journey. **Sonnet** is your everyday reliable sedan. **Haiku** is a bicycle — fast, cheap, and ideal for short, frequent trips. You pick based on distance, urgency, and budget.

#### 5. Internal Working
1. You decide what the task needs: deep reasoning, balance, or raw speed.
2. You pick a **model ID** (e.g., `claude-sonnet-5`).
3. Your request is routed to that specific model.
4. The model processes your text at its own capability/speed level.
5. You get a reply plus **usage** info (tokens used → basis for cost).
6. You can switch models later by changing just the model ID.

#### 6. Architecture Diagram
```
                 ┌──────────────────────────────┐
   Your task ──► │      Pick a model ID         │
                 └──────────────┬───────────────┘
        ┌───────────────┬───────┴───────┬───────────────┐
        ▼               ▼               ▼
   ┌─────────┐    ┌───────────┐    ┌──────────┐
   │  OPUS   │    │  SONNET   │    │  HAIKU   │
   │ deepest │    │ balanced  │    │ fastest  │
   │ reasoning│   │  default  │    │ cheapest │
   └─────────┘    └───────────┘    └──────────┘
   more capable  ◄───────────────►  more speed/cheaper
```

#### 7. Real Example
A fintech app has two needs. (1) Classify thousands of incoming transactions as "safe" or "review" — simple and high-volume → use **Haiku**. (2) Analyze a complex fraud case with many documents and subtle reasoning → use **Opus**. For most general chat features, they default to **Sonnet**. One family, three smart choices.

#### 8. Live Demo
Ask the **same** hard reasoning question to a Haiku-tier and an Opus-tier model (or discuss expected differences). Then run a **simple** task ("capitalize this sentence") on both. Learners see Opus shine on the hard task while Haiku answers the simple one just as well but faster/cheaper — proving why matching model to task matters.

#### 9. Interview Questions
**Basic**
1. Name the three rule-of-thumb tiers and their strengths.
2. Which model is best for the hardest reasoning?
3. Which model is fastest and cheapest?
4. What does a model ID look like?
5. What is the "balanced default" model?

**Intermediate**
1. What three factors trade off across the family?
2. Why not always use the most powerful model?
3. How do you switch models in a request?
4. Give a task suited to Haiku and one suited to Opus.
5. Where should you check the current list of models and prices?

**Scenario-based**
1. You must process 1 million short classification calls cheaply. Which tier?
2. A legal team needs deep multi-document analysis. Which tier?
3. Costs are too high on a chat feature using Opus. What do you try?
4. Quality is too low on a hard task using Haiku. What do you change?
5. A client asks you to hard-code today's prices in the handbook. Why refuse?

#### 10. Common Mistakes
- **Always using the biggest model** — burns money on easy tasks.
- **Always using the smallest model** — fails on hard reasoning.
- **Memorizing exact prices** — they change; always check live docs.
- **Assuming model names never change** — the family evolves over time.

#### 11. Best Practices
- **Start with Sonnet** as your default, then adjust.
- **Downshift to Haiku** for simple, high-volume tasks to save cost.
- **Upshift to Opus** only for genuinely hard reasoning.
- Always **check Anthropic's current docs** for the live model list and pricing.

#### 12. One-Page Summary
- **Key points:** A family trades capability vs speed vs cost. Opus = deepest reasoning, Sonnet = balanced default, Haiku = fast/cheap.
- **Important terms:** model ID, tier, Opus, Sonnet, Haiku, capability/speed/cost.
- **Quick revision:** Match model to task. Default Sonnet; scale up or down as needed.
- **Mnemonic:** **O-S-H** = **O**pus (hardest), **S**onnet (standard), **H**aiku (hurry/cheap).

> **Trainer Note:** Draw the capability↔cost slider on the whiteboard and let learners place sample tasks on it — this makes model selection intuitive, not memorized.

---

### 1.3 Claude API

#### 1. Definition
The **Claude API** (also called the **Anthropic API**) is the doorway that lets **your own programs** talk to Claude over the internet. It uses the **Messages API**: you send a **list of messages** — each with a **role** (`system`, `user`, or `assistant`) — and Claude returns an **assistant** message in reply. The response also includes a **`usage`** object with **input and output token counts**, which is the basis for calculating cost. An **API** simply means a defined way for software to request a service and get a structured result back.

#### 2. Why do we need it?
The chat app is great for humans, but real products need Claude **inside their software** — a website, a backend, a mobile app. The API makes that possible: your code sends text and receives Claude's reply **programmatically**, so you can automate tasks at scale, build features, and integrate Claude into existing systems. Without an API, Claude would be limited to manual chatting.

#### 3. Office Analogy
The API is like the company's **Outlook/email system for machines**. Instead of walking to the smart employee's desk, your software sends a structured "message" and gets a structured "reply" back — reliably, at scale, and logged. The `system` message is like the **job description** you pin above the desk ("you are a support agent"), the `user` message is the actual **request**, and the `assistant` message is the **reply**.

#### 4. Real-Life Analogy
Think of a **restaurant drive-through**. You (the app) speak your **order** (user message) into the intercom, following the menu's rules (system message). The kitchen (Claude) prepares it and hands back your food (assistant message). The **receipt** listing items and price is like the **usage** object — it tells you exactly what you consumed.

#### 5. Internal Working
1. Your program builds a **messages list** (system + user roles).
2. It sends an HTTP request with your **API key** to the Claude API.
3. The API routes it to the chosen **model**.
4. The model generates an **assistant** reply.
5. The API returns the reply **plus a `usage`** object (input/output tokens).
6. Your code reads the reply and can estimate **cost** from the token counts.

#### 6. Architecture Diagram
```
 ┌──────────────┐    request: messages + model + API key
 │  YOUR APP    │ ───────────────────────────────────────►┐
 │ (code)       │                                         │
 └──────────────┘                                    ┌────▼──────────┐
        ▲                                            │  CLAUDE API   │
        │                                            │  (Messages)   │
        │   response: assistant message + usage      └────┬──────────┘
        └─────────────────────────────────────────────── │
                                                     ┌────▼──────┐
                                                     │  MODEL    │
                                                     └───────────┘
 roles:  system = rules  ·  user = request  ·  assistant = reply
```

#### 7. Real Example
An e-commerce site wants an auto-reply bot. In code they send:
- **system:** "You are a polite support agent for ShopFast."
- **user:** "Where is my order #123?"

Claude returns an **assistant** message with a helpful reply, plus `usage` showing, say, 40 input + 60 output tokens. The site displays the reply and logs the tokens to track spend.

#### 8. Live Demo
Show a minimal script (pseudocode is fine in class):
```
messages = [
  {role: "system",  content: "You are a helpful tutor."},
  {role: "user",    content: "Explain an API in one line."}
]
response = claude.create(model="claude-sonnet-5", messages=messages)
print(response.text)
print(response.usage)   # input/output tokens
```
Run it live and point out the **reply** and the **usage** numbers.

#### 9. Interview Questions
**Basic**
1. What is the Claude API used for?
2. What is the Messages API?
3. Name the three message roles.
4. What is inside the `usage` object?
5. What is an API key for?

**Intermediate**
1. What does the `system` role do vs the `user` role?
2. Why is `usage` important for a business?
3. How do you choose which model the API call uses?
4. Is one API call aware of a previous call? How do you add memory?
5. What comes back in the API response besides the text?

**Scenario-based**
1. You want a support bot to always stay polite. Which role encodes that?
2. Your monthly bill is unexpectedly high. Where do you look first?
3. You need Claude to reply in JSON. How might the messages help?
4. Two users' requests get mixed up. What likely went wrong with messages/state?
5. A teammate hard-codes the API key in public GitHub. Why is that dangerous?

#### 10. Common Mistakes
- **Putting the API key in code or prompts** — leaks secrets; use `.env` only.
- **Forgetting the API is stateless** — you must resend context for "memory."
- **Ignoring `usage`** — you lose track of cost.
- **Mixing up roles** — putting instructions in the wrong role weakens control.

#### 11. Best Practices
- Store keys in **`.env`**, never in code (project rule).
- Use the **system** message for durable rules/persona.
- **Log `usage`** to monitor and estimate cost.
- Resend needed **history** to simulate memory across calls.

#### 12. One-Page Summary
- **Key points:** API = programmatic access; Messages API uses system/user/assistant roles; response includes `usage` tokens for cost.
- **Important terms:** Messages API, role, system/user/assistant, API key, usage, token.
- **Quick revision:** Send messages list → get assistant reply + usage. Stateless; keys in `.env`.
- **Mnemonic:** **SUA** = **S**ystem (rules), **U**ser (ask), **A**ssistant (answer).

> **Trainer Note:** Physically point at each role in the code on screen as you narrate "rules, request, reply" — the role model is the single most important idea beginners must internalize here.

---

### 1.4 Claude Capabilities

#### 1. Definition
**Capabilities** are the useful things Claude can do with language and other inputs. These include **natural-language understanding and generation**, **summarization**, **extraction** (pulling out specific facts), **classification** (sorting into categories), **coding**, **reasoning**, **long-context reading** (handling big documents), **tool use / function calling** (letting Claude call your functions), **vision** (reading images), and **structured output** (replying in formats like JSON). All of this is shaped by Anthropic's safety focus: **helpful, honest, harmless**.

#### 2. Why do we need it?
Businesses drown in unstructured text and images: emails, tickets, PDFs, code, receipts. Traditional software struggles with this messy, human data. Claude's capabilities turn that mess into **useful action** — a summary, a category, a JSON record, a code fix — without building a custom system for each task. One assistant, many jobs.

#### 3. Office Analogy
Claude is the **multi-skilled employee** who can, in one afternoon: summarize a meeting, sort the inbox into folders (classification), pull the invoice numbers out of attachments (extraction), fix a bug (coding), and read a screenshot you paste (vision). And if they need data from another department, they can **file a request** through the right system (tool use) instead of guessing.

#### 4. Real-Life Analogy
Think of a **hospital's front-desk nurse**: they listen to your problem (understanding), summarize it for the doctor (summarization), note your details on the form (extraction), decide which department you need (classification), and if a test is required, they **order it from the lab** (tool use). One helpful person coordinating many kinds of work.

#### 5. Internal Working
1. Claude reads your input — **text, and/or an image** (vision).
2. It interprets the **instruction** (summarize? classify? extract?).
3. It applies its trained abilities to produce the result.
4. If **tools/functions** are provided, it can ask to call one and use the result.
5. If a **format** (like JSON) is requested, it shapes the output accordingly.
6. It returns the finished result, guided by safety training.

#### 6. Architecture Diagram
```
        INPUTS                    CLAUDE CAPABILITIES               OUTPUTS
 ┌──────────────────┐      ┌───────────────────────────┐    ┌────────────────┐
 │ text / documents │─────►│ understand · summarize     │───►│ summary        │
 │ images (vision)  │      │ extract · classify · code  │    │ category / JSON│
 │ tool definitions │◄────►│ reason · long-context read │    │ code · answer  │
 └──────────────────┘ call │ tool use / structured out  │    └────────────────┘
                      back  └───────────────────────────┘
                     (helpful · honest · harmless)
```

#### 7. Real Example
An insurance firm uploads a **photo of a damaged car** plus a claim description. Claude uses **vision** to read the photo, **extracts** the policy number from the text, **classifies** the claim type, **summarizes** the incident, and returns a **structured JSON** record ready to save. Several capabilities combine in one request.

#### 8. Live Demo
Run three quick prompts in class:
1. *"Summarize this paragraph in 2 bullets."* (summarization)
2. *"Extract every email address from this text as a list."* (extraction)
3. *"Classify this review as positive, neutral, or negative."* (classification)

Optionally paste an **image** and ask *"What does this screenshot show?"* to demo **vision**. Learners see multiple capabilities in minutes.

#### 9. Interview Questions
**Basic**
1. Name five Claude capabilities.
2. What is summarization?
3. What is extraction?
4. What is classification?
5. What does "vision" mean here?

**Intermediate**
1. What is the difference between extraction and classification?
2. What is "structured output" and why is it useful?
3. What does "tool use / function calling" let Claude do?
4. What does "long-context reading" enable?
5. How does the "helpful, honest, harmless" goal shape outputs?

**Scenario-based**
1. You need invoice numbers pulled from 1,000 PDFs. Which capability?
2. You must sort support tickets by urgency. Which capability?
3. You need Claude's answer as JSON for your database. What do you request?
4. Claude needs live stock prices it doesn't know. Which capability helps?
5. A user uploads a receipt photo for logging. Which capability reads it?

#### 10. Common Mistakes
- **Expecting perfect accuracy** — always review extracted/critical data.
- **Not asking for a format** — you get prose when you needed JSON.
- **Forgetting tools for live data** — Claude alone can't fetch fresh info.
- **Overloading one prompt** — cramming ten tasks lowers quality; split them.

#### 11. Best Practices
- **Name the capability** you want ("extract", "classify", "summarize").
- **Specify output format** explicitly for machine use.
- Use **tools/function calling** for live or external data.
- **Validate** structured output before trusting it downstream.

#### 12. One-Page Summary
- **Key points:** Claude understands/generates language; summarizes, extracts, classifies, codes, reasons, reads long context and images, uses tools, returns structured output — safely.
- **Important terms:** extraction, classification, tool use/function calling, vision, structured output, long context.
- **Quick revision:** Many capabilities, one assistant. Ask clearly; specify format; use tools for fresh data.
- **Mnemonic:** **SECRET-V** = **S**ummarize, **E**xtract, **C**lassify, **R**eason, **E**ngineer code, **T**ools, **V**ision.

> **Trainer Note:** Let each learner suggest one capability that maps to their own job — this personal connection makes the capability list memorable instead of abstract.

---

### 1.5 Claude Limitations

#### 1. Definition
**Limitations** are the honest boundaries of what Claude can do. Claude can **hallucinate** (state wrong facts confidently), has a **knowledge cutoff** (it does not know events after its training and needs tools/search for fresh info), has **no true memory** between calls unless you provide it, works within a **finite context window**, produces **non-deterministic** outputs (the same prompt can vary), has **costs that scale with tokens**, is **not a database or calculator** (it can make arithmetic slips), and **needs guardrails** for production use.

#### 2. Why do we need it?
Knowing the limits keeps you **safe and professional**. If you assume Claude is always right, you can ship wrong facts, leak costs, or build fragile systems. Understanding limitations tells you **where to add checks**: verify facts, connect tools for live data, resend context for memory, use real calculators/databases for exact work, and put guardrails around production.

#### 3. Office Analogy
Even a brilliant employee has limits: they **misremember** occasionally (hallucinate), only know things up to the day they were last trained (knowledge cutoff), **forget** a conversation once they leave the room (no memory), can only hold **so many pages** on their desk at once (context window), and shouldn't be trusted to do payroll math by hand (not a calculator). A good manager adds **review steps**, not blind trust.

#### 4. Real-Life Analogy
Claude is like a **taxi driver** with excellent general knowledge but an **out-of-date map** (knowledge cutoff) and no live traffic feed unless you give them one (tools). They are confident and helpful, but for a brand-new road or exact toll amount, you check a current source. Trust, but verify.

#### 5. Internal Working
1. Claude predicts likely text — plausible-sounding output can still be **wrong** (hallucination).
2. Its knowledge is **frozen** at training time (cutoff); it has no live feed.
3. Each call is **fresh** — no stored memory unless you resend history.
4. Input must fit the **context window**; overflow gets dropped or errors.
5. Sampling makes outputs **vary** between runs (non-deterministic).
6. More tokens = **more cost** and, past limits, truncation.

#### 6. Architecture Diagram
```
   ┌───────────────────────── LIMITATIONS ──────────────────────────┐
   │  Hallucination ──► verify facts                                 │
   │  Knowledge cutoff ──► add tools / search for fresh info         │
   │  No memory ──► resend conversation history                      │
   │  Finite context window ──► trim / chunk large inputs            │
   │  Non-deterministic ──► test; don't expect identical outputs     │
   │  Cost scales w/ tokens ──► track usage, pick right model        │
   │  Not a DB/calculator ──► use real tools for exact data/math     │
   │  Needs guardrails ──► validate + add safety checks in prod      │
   └────────────────────────────────────────────────────────────────┘
```

#### 7. Real Example
A team asks Claude for "the exact current exchange rate." Claude gives a confident number — but it is from **training data**, possibly stale (**cutoff + hallucination risk**). The fix: connect a **live rate tool** so Claude uses real-time data, and **verify** before showing it to customers. The limitation isn't a failure — it tells you exactly what guardrail to add.

#### 8. Live Demo
Run the same creative prompt (*"Give me a startup name"*) **three times** — learners see **different** answers (non-deterministic). Then ask about a **very recent** event and watch Claude note its **knowledge cutoff** or hedge. Finally, ask a tricky **long-multiplication** problem and check the arithmetic — a great, safe way to show why Claude is not a calculator.

#### 9. Interview Questions
**Basic**
1. What is a hallucination?
2. What is a knowledge cutoff?
3. Does Claude remember past calls by default?
4. What is the context window?
5. What does "non-deterministic" mean?

**Intermediate**
1. Why can costs grow unexpectedly?
2. Why shouldn't Claude be your calculator or database?
3. How do you give Claude fresh, post-cutoff information?
4. How do you add "memory" across API calls?
5. Why does production use need guardrails?

**Scenario-based**
1. Claude states a wrong fact confidently to a customer. What safeguard was missing?
2. You need today's news in an answer. What do you add?
3. A very long document won't fit in one call. What do you do?
4. Your token bill spiked. Name two likely causes and fixes.
5. Two identical prompts gave different outputs and a tester filed a "bug." Is it a bug?

#### 10. Common Mistakes
- **Blindly trusting confident answers** — confidence is not correctness.
- **Expecting fresh knowledge** — it can't know post-cutoff events unaided.
- **Assuming memory** — you must resend context.
- **Using Claude for exact math/data** — use real calculators/databases.
- **Shipping to production without guardrails** — invites errors and abuse.

#### 11. Best Practices
- **Verify** important facts from trusted sources.
- **Connect tools/search** for live data.
- **Resend history** when continuity matters.
- **Chunk** large inputs to fit the context window.
- **Track usage** and add **validation + guardrails** in production.

#### 12. One-Page Summary
- **Key points:** Claude can hallucinate, has a cutoff, no default memory, finite context, varies outputs, costs scale with tokens, isn't a DB/calculator, and needs guardrails.
- **Important terms:** hallucination, knowledge cutoff, context window, non-deterministic, guardrails, tokens.
- **Quick revision:** Trust but verify. Add tools, context, guardrails where limits bite.
- **Mnemonic:** **HALT-CNG** — **H**allucinate, **A**mnesia (no memory), **L**imited context, **T**ime cutoff, **C**ost scales, **N**on-deterministic, **G**uardrails needed.

> **Trainer Note:** Frame limitations as an engineering checklist, not bad news — each limit maps to a concrete guardrail, which is exactly what an architect gets paid to design.

---

### Quick Recap
- **Claude** is Anthropic's family of LLM assistants — reads text, writes text — accessed via apps, the API, and Claude Code; built to be **helpful, honest, harmless**.
- The **model family** trades **capability vs speed vs cost**: **Opus** (deepest reasoning), **Sonnet** (balanced default), **Haiku** (fast/cheap). Always check live docs for the current list and pricing.
- The **Claude API** uses the **Messages API** with **system/user/assistant** roles and returns a reply plus a **`usage`** object (tokens → cost). It is **stateless**; keep keys in `.env`.
- **Capabilities:** understanding/generation, summarization, extraction, classification, coding, reasoning, long-context, tool use, vision, and structured output.
- **Limitations:** hallucination, knowledge cutoff, no default memory, finite context, non-determinism, token-based cost, not a DB/calculator, and the need for guardrails — each pointing to a specific safeguard.


---

## Module 2 — Prompting

Prompting is how you *talk* to Claude. This module starts from the very first idea — "what is a prompt?" — and builds up to professional techniques like XML tags, few-shot examples, roles, and chaining. No prior Claude experience needed; if you can write a sentence and read basic code, you're ready.

---

### 2.1 Prompt

#### 1. Definition
A **prompt** is simply the text instruction you give Claude. It's the message you type when you want Claude to *do* something — answer a question, write code, summarize a document, or translate a sentence. Think of it as the "input" to the model. Claude reads your prompt, thinks, and returns an output (called the **response**). A prompt can be one short line ("Translate 'hello' to French") or many paragraphs with rules, examples, and data. Everything you send Claude — instructions, context, questions — is part of the prompt.

#### 2. Why do we need it?
Claude cannot read your mind. It only knows what you *tell* it. The prompt is the single channel through which you communicate intent. A vague prompt gives vague answers; a clear prompt gives sharp answers. Because the prompt is the *only* thing that steers the model, learning to write good prompts is the single highest-leverage skill in this entire course.

#### 3. Office Analogy (software company)
Imagine you're a manager and Claude is a brilliant new hire on their first day. They're smart and fast, but they know **nothing** about your company. The prompt is the **task ticket** you hand them: "Build a login page using our React style guide." A one-line ticket gets a guessed result; a detailed ticket gets exactly what you wanted.

#### 4. Real-Life Analogy (everyday)
A prompt is like the **order you give a waiter**. "Food, please" gets you *something*, but maybe not what you wanted. "A medium-rare cheeseburger, no onions, with fries" gets you exactly your meal. The more specific the order, the better the plate.

#### 5. Internal Working (numbered steps)
1. You type text (the prompt) and send it to Claude.
2. Claude breaks the text into **tokens** (small chunks of words).
3. The model reads all tokens and predicts the most likely helpful continuation.
4. It generates the response token by token.
5. The finished text is sent back to you as the **assistant response**.

#### 6. Architecture Diagram (ASCII)
```
   YOU                    CLAUDE                   YOU
 +--------+   prompt    +-----------+  response  +--------+
 |  text  | ----------> |  model    | ---------> | output |
 | "..."  |             | (tokens → |            | "..."  |
 +--------+             |  predict) |            +--------+
                        +-----------+
```

#### 7. Real Example
A support team wants to reply to an angry customer email. **Business input:** the customer's email text. **Prompt:** "Write a polite, apologetic reply to this customer email offering a refund: <email>...</email>". **How Claude processes it:** it reads the email, detects the frustrated tone, understands the goal (apologize + offer refund), and drafts a calm, professional reply.

#### 8. Live Demo (classroom)
Open the demo and send two prompts side by side:
- Prompt A: `"Explain recursion."`
- Prompt B: `"Explain recursion to a 10-year-old using a mirror analogy, in 3 sentences."`
Read both answers aloud. The class instantly sees how specificity changes the output — same model, different prompt, very different result.

#### 9. Interview Questions
**Basic**
1. What is a prompt?
2. Is the data you paste in also part of the prompt?
3. What does Claude return after reading a prompt?
4. Can a prompt be a single word?
5. What is a token, in one line?

**Intermediate**
1. Why does a more specific prompt usually give better results?
2. What's the difference between a prompt and a response?
3. How does Claude decide what to output?
4. Why can't the model "just know" your company's rules?
5. Name two things a prompt can contain besides a question.

**Scenario-based**
1. Your prompt returns answers that are too long. What do you change?
2. A teammate says "Claude is dumb, it ignored my request." How do you diagnose it?
3. You need the same output format every time. What prompt detail helps?
4. A prompt works in English but fails in French. What might be missing?
5. You must summarize a 50-page PDF. What goes in the prompt?

#### 10. Common Mistakes
- **Being vague** ("make it better") — Claude doesn't know your definition of "better."
- **Assuming shared context** — the model doesn't know your project unless you tell it.
- **Burying the ask** — the real request is hidden in paragraph 5; state it clearly.
- **No output format** — you get prose when you wanted JSON.

#### 11. Best Practices
- Say exactly **what** you want and **how** it should look.
- Put the most important instruction where it's easy to find (start or end).
- Include only the context that's needed — extra text costs tokens and can distract.
- Test with a few different inputs before trusting a prompt.

#### 12. One-Page Summary
- **Key points:** A prompt is the text input to Claude; it's the only way to steer the model; specificity drives quality.
- **Important terms:** prompt, response, token, context.
- **Quick revision:** vague in → vague out; clear in → clear out.
- **Mnemonic:** **"Clear Prompt, Clear Product."**

> **Trainer Note:** Have each student rewrite one vague prompt into a specific one. This single exercise teaches more than an hour of theory.

---

### 2.2 System Prompt

#### 1. Definition
A **system prompt** is a special, top-level instruction that sets Claude's **persona, global rules, and behavior** for the whole conversation. In the Claude Messages API it's the `system` field, set **once**. It's not the user's question — it's the standing orders that apply to *every* reply. Use it to say "who Claude is" (a tax expert), "how it should behave" (concise, formal), and "hard rules" (never give medical advice). Because it applies globally, the system prompt shapes tone and boundaries without being repeated in each message.

#### 2. Why do we need it?
Without a system prompt, you'd have to repeat "be concise, be formal, you're a lawyer" in *every single message*. The system prompt lets you set these rules **once** and have them stick for the whole chat. It cleanly separates the "who you are and how you behave" (system) from the "what I need right now" (user), which keeps prompts organized and reliable.

#### 3. Office Analogy (software company)
The system prompt is the **employee handbook + job description** given on day one. "You are a backend engineer. Follow our security policy. Always write tests." The employee doesn't re-read the handbook for each task — it's simply *how they operate* for everything they do.

#### 4. Real-Life Analogy (everyday)
It's the **house rules** posted on the fridge: "No shoes inside. Quiet after 10pm." Every guest follows them automatically without being told again for each activity.

#### 5. Internal Working (numbered steps)
1. You set the `system` field once when starting the conversation.
2. Claude reads it **before** any user message.
3. It treats these instructions as high-priority, always-on context.
4. Each user message is interpreted *through the lens* of the system prompt.
5. The persona and rules persist across every turn until you change them.

#### 6. Architecture Diagram (ASCII)
```
 +----------------------- CONVERSATION -----------------------+
 |  SYSTEM: "You are a formal tax advisor. Be concise."       |
 |  ......(applies to everything below)......                 |
 |                                                            |
 |  USER:      "Can I deduct my home office?"                 |
 |  ASSISTANT: (answers as a concise, formal tax advisor)     |
 |  USER:      "What about my car?"                           |
 |  ASSISTANT: (still concise, still a tax advisor)           |
 +------------------------------------------------------------+
```

#### 7. Real Example
A bank builds a chatbot. **System prompt:** "You are the bank's virtual assistant. Be polite and professional. Never reveal account passwords. If asked for legal advice, tell the user to consult a lawyer." **How Claude processes it:** for every customer question, it stays polite, refuses to leak secrets, and redirects legal questions — automatically, on every turn.

#### 8. Live Demo (classroom)
Run the same user question twice with different system prompts:
- System: `"You are a pirate."` → User: `"Explain HTTP."`
- System: `"You are a strict university professor."` → User: `"Explain HTTP."`
The class sees identical questions produce wildly different tones — proof the system prompt controls behavior.

#### 9. Interview Questions
**Basic**
1. What is a system prompt?
2. How often is the system prompt set?
3. Which API field holds it?
4. Does the user see the system prompt in a chat UI?
5. Name one thing a system prompt commonly defines.

**Intermediate**
1. Why put rules in the system prompt instead of every user message?
2. How does a system prompt differ from a user prompt?
3. What happens to the system prompt across multiple turns?
4. Where would you put "never give medical advice"?
5. Can you change the system prompt mid-conversation? What's the effect?

**Scenario-based**
1. Your bot keeps forgetting to stay formal. Where do you fix it?
2. You need the bot to always answer in JSON. System or user prompt?
3. A rule must never be broken by any user. Where does it go?
4. Two products share one model but need different tones. What do you change per product?
5. A user tries to "jailbreak" the bot. Which prompt is your defense line?

#### 10. Common Mistakes
- **Putting the actual task in the system prompt** — the specific request belongs in the user message.
- **Overstuffing it** — a giant system prompt wastes tokens and buries the important rules.
- **SHOUTING rules** ("YOU MUST NEVER...") — plain, clear rules work better; over-forcing backfires.
- **Contradicting yourself** — conflicting rules confuse the model.

#### 11. Best Practices
- Keep it to **who Claude is + how it behaves + hard rules**.
- State each rule **once**, plainly.
- Use the system prompt for the **persona/role** (the "P" in PRECISE).
- Keep task-specific details in the user message, not here.

#### 12. One-Page Summary
- **Key points:** Global, set-once instructions defining persona and rules; applies to every turn.
- **Important terms:** system prompt, persona, global rules, `system` field.
- **Quick revision:** system = "who you are + how you behave"; user = "what I need now."
- **Mnemonic:** **"System = Standing orders."**

> **Trainer Note:** Emphasize the split: system = identity & rules, user = the request. Beginners often cram everything into one place.

---

### 2.3 User Prompt

#### 1. Definition
A **user prompt** is the message from the **human** — the actual request or question you want Claude to handle right now. In the Messages API it has the role `user`. While the system prompt sets standing rules, the user prompt carries the specific, changing ask: "Summarize this article," "Fix this bug," "What's 15% of 240?". In a multi-turn chat, every human turn is a new user message, and they alternate with Claude's assistant replies.

#### 2. Why do we need it?
This is where the real work is requested. The system prompt is the setup; the user prompt is the *actual job*. Every task Claude performs starts with a user prompt. Without it, there's nothing to do. It's also where you attach the data for the task (the document to summarize, the code to review).

#### 3. Office Analogy (software company)
If the system prompt is the job description, the user prompt is the **individual ticket in Jira**: "Fix the checkout button on the mobile app." It's the concrete, day-to-day work item handed to the employee.

#### 4. Real-Life Analogy (everyday)
The user prompt is **what you actually say to the waiter** after they've explained the house rules: "I'll have the pasta, extra cheese." It's your specific order for this moment.

#### 5. Internal Working (numbered steps)
1. The human types a request with role `user`.
2. Claude combines it with the system prompt and any earlier turns.
3. It figures out the specific intent of *this* message.
4. It generates an assistant response.
5. The next human message becomes the next user prompt, continuing the alternation.

#### 6. Architecture Diagram (ASCII)
```
 SYSTEM  (rules, set once)
    |
    v
 USER  ->  "Summarize this report: <report>...</report>"
    |
    v
 ASSISTANT  ->  "Here is the summary: ..."
    |
    v
 USER  ->  "Now make it shorter."   (next turn)
```

#### 7. Real Example
An HR team wants job descriptions written. **User prompt:** "Write a job description for a junior Python developer, 5 bullet points, friendly tone." **How Claude processes it:** it reads the request, applies any system rules (tone, format), and produces a 5-bullet description in a friendly voice.

#### 8. Live Demo (classroom)
Keep one system prompt fixed ("You are a helpful assistant. Be brief."). Then send three different user prompts in a row:
1. "What is Python?"
2. "Give me a Python one-liner to reverse a string."
3. "Now explain that one-liner."
Students watch the conversation build turn by turn, each user prompt driving a new response.

#### 9. Interview Questions
**Basic**
1. What is a user prompt?
2. What role name does it use in the API?
3. Who writes the user prompt?
4. Where do you attach the document to summarize?
5. In a chat, what comes after a user prompt?

**Intermediate**
1. How does a user prompt differ from a system prompt?
2. Why does the task go in the user prompt, not the system prompt?
3. What is a "turn" in a conversation?
4. How do user and assistant messages relate in multi-turn chat?
5. Can a user prompt include both instructions and data? Give an example.

**Scenario-based**
1. Claude ignored part of a long user prompt. What might have gone wrong?
2. You want to refine a previous answer. What do you send?
3. A user prompt mixes three unrelated tasks. What's a better approach?
4. You need to pass a 10,000-word document. Where and how?
5. The tone is wrong on every reply — is that a user-prompt or system-prompt fix?

#### 10. Common Mistakes
- **Cramming many tasks into one user prompt** — split them or chain them.
- **Forgetting to include the data** — asking to "summarize the article" without pasting the article.
- **Putting persona rules here** — those belong in the system prompt.
- **Ambiguous references** ("fix it") without saying what "it" is.

#### 11. Best Practices
- One clear ask per prompt when possible.
- Clearly separate **instructions** from **data** (use XML tags — see 2.6).
- Include the **Result, Examples, Context, Instructions** (the middle of PRECISE) here.
- Reference earlier turns explicitly when refining.

#### 12. One-Page Summary
- **Key points:** The human's actual request; role `user`; carries the task and its data; alternates with assistant turns.
- **Important terms:** user prompt, turn, multi-turn, `user` role.
- **Quick revision:** system sets the stage, user asks the question.
- **Mnemonic:** **"User = the ask."**

> **Trainer Note:** Show a real multi-turn transcript so students *see* user/assistant alternation, not just hear about it.

---

### 2.4 Assistant Response

#### 1. Definition
The **assistant response** is Claude's reply — the output text it generates after reading the system and user prompts. In the Messages API it has the role `assistant`. It's what the model produces: an answer, some code, a summary, a translation. In multi-turn chats, past assistant responses stay in the conversation history so Claude remembers what it already said. You can also *pre-fill* an assistant message to guide how Claude starts its next reply (an advanced trick).

#### 2. Why do we need it?
The response is the whole point — it's the value Claude delivers. Understanding it as a distinct **role** matters because the conversation is a back-and-forth of `user` and `assistant` messages. Past assistant responses become **memory**: they let Claude stay consistent and build on earlier answers instead of starting fresh each turn.

#### 3. Office Analogy (software company)
The assistant response is the **completed pull request** the engineer submits back to you. It's the deliverable. And just like past PRs live in the repo history, past responses live in the conversation history for reference.

#### 4. Real-Life Analogy (everyday)
It's the **meal the waiter brings to your table** after your order. It's the result you actually consume — and the waiter remembers what you ordered if you ask for a refill.

#### 5. Internal Working (numbered steps)
1. Claude reads system + all prior turns + the latest user prompt.
2. It predicts the best response one token at a time.
3. The tokens form the reply text.
4. This reply is tagged with the `assistant` role.
5. It's added to the conversation history so the next turn has full context.

#### 6. Architecture Diagram (ASCII)
```
 HISTORY: [system][user][assistant][user] ---> latest
                                        |
                                        v
                              +------------------+
                              |  Claude predicts |
                              |  next tokens     |
                              +------------------+
                                        |
                                        v
                        ASSISTANT: "Here is your answer..."
                                        |
                             (appended back to HISTORY)
```

#### 7. Real Example
A developer asks Claude to write a function. **Assistant response:** a Python function plus a short explanation. **How Claude processes it:** it generates the code, keeps it in history, so when the developer next says "add error handling," Claude edits *that* function rather than guessing.

#### 8. Live Demo (classroom)
Ask Claude a question, then follow up with "make it shorter" *without* repeating the topic. The class sees Claude use its own previous response as memory. Then demo **prefill**: start an assistant message with `{` and watch Claude continue in JSON.

#### 9. Interview Questions
**Basic**
1. What is the assistant response?
2. What role name does it carry?
3. Who or what produces it?
4. Where does a past response go after it's generated?
5. Does Claude remember its earlier responses in the same chat?

**Intermediate**
1. How does conversation history use assistant responses?
2. What is assistant prefill and why is it useful?
3. Why does the response come token by token?
4. How do assistant and user messages alternate?
5. What happens if you delete past assistant turns from history?

**Scenario-based**
1. Claude contradicts an earlier answer. What context might be missing?
2. You want replies to always start with "Summary:". How can prefill help?
3. A long chat gets expensive. What role of messages is piling up?
4. You need Claude to output only JSON. What prefill trick helps?
5. Claude "forgot" what it said 10 turns ago. Why might that happen?

#### 10. Common Mistakes
- **Assuming infinite memory** — very long histories can exceed the context window and get truncated.
- **Ignoring history cost** — every past turn is re-sent and costs tokens.
- **Not using prefill** when you need a strict output start.
- **Editing history carelessly** — removing turns can break Claude's continuity.

#### 11. Best Practices
- Keep conversation history tidy; trim old, irrelevant turns to save tokens.
- Use **prefill** to lock output format (e.g., start with `{`).
- Remember responses are **memory** — reference them instead of repeating yourself.
- Watch cost: history grows every turn (cost is first-class in this project).

#### 12. One-Page Summary
- **Key points:** Claude's reply, role `assistant`; becomes memory in history; can be prefilled.
- **Important terms:** assistant response, prefill, conversation history, context window.
- **Quick revision:** the response is both the deliverable *and* future memory.
- **Mnemonic:** **"Assistant = the answer that remembers."**

> **Trainer Note:** The prefill demo always earns an "aha." Budget five minutes for it.

---

### 2.5 Prompt Engineering

#### 1. Definition
**Prompt engineering** is the craft of *designing* prompts so the model reliably produces the output you want. It's not random typing — it's a deliberate skill: choosing the right role, giving clear instructions, adding examples, supplying context, and specifying the output format. In this course we use a checklist called **PRECISE**: **P**ersona · **R**esult · **E**xamples · **C**ontext · **I**nstructions · **S**pecification · **E**valuation. Good prompt engineering turns a flaky "sometimes it works" prompt into a dependable one.

#### 2. Why do we need it?
The same model can give brilliant or useless answers depending on the prompt. Prompt engineering is how you get **consistent, correct, production-ready** results without changing the model or writing code. It's the cheapest, fastest lever you have. For a certification and for real work, it's the core skill.

#### 3. Office Analogy (software company)
Prompt engineering is **writing a great spec/ticket**. A vague ticket ("improve the app") gets random work. A precise ticket with acceptance criteria, examples, and constraints gets exactly the feature you wanted — every time. The engineer (Claude) is the same; the spec quality decides the outcome.

#### 4. Real-Life Analogy (everyday)
It's like **giving directions to a driver**. "Go downtown" is risky. "Take Main St, turn left at the 2nd light, it's the blue building on the right" gets you there reliably. Same driver, better instructions, better arrival.

#### 5. Internal Working (numbered steps)
1. Decide the **Persona** (role) → often the system prompt.
2. State the desired **Result** and show **Examples**.
3. Add the needed **Context** (only what's necessary).
4. Give clear **Instructions** (steps, constraints).
5. Add a **Specification** of the output format.
6. Include **Evaluation** criteria (how to check it's correct).
7. Test, observe failures, and refine.

#### 6. Architecture Diagram (ASCII)
```
        PRECISE  CHECKLIST
   +-----------------------------+
   | P  Persona   -> Role        |  --> System prompt
   | R  Result    -\             |
   | E  Examples    \            |
   | C  Context      >-> Task    |  --> User prompt
   | I  Instructions/            |
   +-----------------------------+
   | S  Specification -\         |
   | E  Evaluation     >-> Output|  --> Output spec
   +-----------------------------+
```

#### 7. Real Example
A fintech wants to classify transactions as "fraud" or "safe." **Weak prompt:** "Is this fraud?" **Engineered prompt (PRECISE):** Persona = fraud analyst; Result = a label; Examples = 3 labeled transactions; Context = account history; Instructions = check amount, location, time; Specification = output only `fraud` or `safe`; Evaluation = flag if unsure. **How Claude processes it:** with structure and examples, it returns consistent one-word labels instead of rambling.

#### 8. Live Demo (classroom)
Take a weak prompt and improve it live, one PRECISE letter at a time, re-running after each addition. The class watches the output get sharper with each step — Persona, then Examples, then Specification. This makes the checklist tangible.

#### 9. Interview Questions
**Basic**
1. What is prompt engineering?
2. What does PRECISE stand for?
3. Does prompt engineering change the model?
4. Why is it a cheap lever?
5. Which PRECISE letter maps to the role?

**Intermediate**
1. How does PRECISE map to system/user/output?
2. Why do examples improve reliability?
3. What does "Specification" add to a prompt?
4. Why include "Evaluation" criteria?
5. How do you know a prompt is "good enough"?

**Scenario-based**
1. A prompt works 60% of the time. How do you use PRECISE to improve it?
2. Output format keeps drifting. Which PRECISE letters help?
3. The model refuses a valid task. What might you adjust?
4. You have limited tokens. How does that affect "Context"?
5. Two engineers get different results from the same task. How do you standardize?

#### 10. Common Mistakes
- **SHOUTING everywhere** ("CRITICAL: YOU MUST!!!") — modern Claude follows plain instructions; over-forcing backfires. State each rule once, plainly.
- **Dumping the whole knowledge base** into context — include only what's needed (token economy).
- **No output specification** — you can't parse inconsistent output.
- **Skipping examples** for tricky formats.
- **Never testing** on varied inputs.

#### 11. Best Practices
- Follow **PRECISE**: Persona · Result · Examples · Context · Instructions · Specification · Evaluation.
- Map it to structure: Persona→system, Result/Examples/Context/Instructions→user task, Specification/Evaluation→output spec.
- Keep prompts **hierarchical**: Base → Role → Task → Output-spec (small, composable pieces).
- Include only necessary context (token economy).
- Iterate: test, observe, refine.

#### 12. One-Page Summary
- **Key points:** Deliberate prompt design for reliable output; use the PRECISE checklist; iterate.
- **Important terms:** prompt engineering, PRECISE, output specification, token economy.
- **Quick revision:** structure + examples + clear output spec = reliable results.
- **Mnemonic:** **PRECISE** — **P**ersona **R**esult **E**xamples **C**ontext **I**nstructions **S**pecification **E**valuation.

> **Trainer Note:** PRECISE is the backbone of the whole module. Have students memorize it here — every later topic plugs into a letter.

---

### 2.6 XML Prompting

#### 1. Definition
**XML prompting** means wrapping parts of your prompt in tags — like `<document>...</document>`, `<instructions>...</instructions>`, or `<example>...</example>` — so Claude can clearly tell one section from another. It's not real XML with strict rules; it's just simple tag markers that act like labeled folders. Claude was trained to respond very well to this kind of structure. It removes ambiguity: Claude knows exactly which text is data, which is instructions, and which is an example.

#### 2. Why do we need it?
When you paste a document *and* instructions in one blob, Claude can confuse the two — sometimes it summarizes your instructions or treats data as commands. Tags draw clear boundaries. They make prompts **easier to parse, safer, and more reliable**, especially with long inputs. They also make your prompt readable for humans on your team.

#### 3. Office Analogy (software company)
XML tags are like **labeled sections in a project brief**: a "Requirements" heading, a "Reference Material" heading, a "Deliverables" heading. The engineer never mixes up the reference docs with the actual tasks because each is clearly labeled.

#### 4. Real-Life Analogy (everyday)
It's like using **labeled boxes when moving house**: "Kitchen," "Books," "Fragile." Everyone knows what's inside without opening them. Tags label the parts of your prompt the same way.

#### 5. Internal Working (numbered steps)
1. You wrap each part of the prompt in named tags.
2. Claude reads the tags and treats each block by its label.
3. `<instructions>` is followed as commands; `<document>` is treated as data.
4. Claude can "point" to a tag when answering ("Based on the `<document>`...").
5. Clear boundaries reduce mistakes and make output more predictable.

#### 6. Architecture Diagram (ASCII)
```
 PROMPT
 +--------------------------------------------+
 | <instructions>                             |
 |   Summarize the document in 3 bullets.     |
 | </instructions>                            |
 |                                            |
 | <document>                                 |
 |   ...long text to summarize...             |
 | </document>                                |
 +--------------------------------------------+
        |  Claude separates: DO vs DATA
        v
   3-bullet summary of the document
```

#### 7. Real Example
A legal team reviews contracts. **Prompt:**
```
<instructions>List every payment deadline mentioned.</instructions>
<contract>
...20 pages of contract text...
</contract>
```
**How Claude processes it:** it treats the contract purely as data to scan and the instruction as the task — so it lists deadlines instead of accidentally "responding to" contract clauses.

#### 8. Live Demo (classroom)
Give Claude a document that itself contains the word "ignore previous instructions." First without tags (Claude may get confused), then wrapped in `<document>` tags (Claude treats it as plain data). The class sees tags act as a safety boundary.

#### 9. Interview Questions
**Basic**
1. What is XML prompting?
2. Give two example tag names.
3. Is it strict, real XML?
4. Why does Claude respond well to tags?
5. What does `<document>` typically wrap?

**Intermediate**
1. How do tags reduce confusion between data and instructions?
2. Why are tags helpful for long inputs?
3. How can tags improve safety?
4. Can you reference a tag in your instructions? How?
5. How do tags help human teammates read a prompt?

**Scenario-based**
1. Claude keeps "answering" text inside your pasted document. What fixes it?
2. You pass three documents. How do you keep them separate?
3. You want output in a tag too. How would you request that?
4. A prompt mixes examples and data. How do tags help?
5. A user input contains fake instructions. How do tags defend you?

#### 10. Common Mistakes
- **Mismatched tags** (`<doc>...</document>`) — keep open/close names identical.
- **No tags on long inputs** — data and instructions blur together.
- **Over-tagging tiny prompts** — one-line prompts don't need heavy structure.
- **Vague tag names** (`<stuff>`) — use meaningful names like `<email>`.

#### 11. Best Practices
- Use clear, consistent tag names: `<instructions>`, `<document>`, `<example>`.
- Separate **instructions from data** with tags — pairs perfectly with the user prompt (2.3).
- Ask Claude to put its answer in a tag when you need easy parsing.
- Keep it simple; tags are labels, not code.

#### 12. One-Page Summary
- **Key points:** Wrap prompt parts in named tags so Claude separates sections cleanly and safely.
- **Important terms:** XML prompting, tags, `<document>`, `<instructions>`, `<example>`.
- **Quick revision:** tags = labeled boxes; data vs instructions never blur.
- **Mnemonic:** **"Tag it to bag it"** (bag = keep each part cleanly separated).

> **Trainer Note:** The "ignore previous instructions" demo drives home *why* tags matter, not just how. Don't skip it.

---

### 2.7 Few-shot Prompting

#### 1. Definition
**Few-shot prompting** means including a few worked **input → output examples** in your prompt to teach Claude the exact format and edge cases you want. Instead of *describing* the format in words, you *show* it. Terms: **zero-shot** = no examples, **one-shot** = one example, **few-shot** = several examples. Examples teach format faster and more precisely than long prose descriptions, because Claude simply mimics the pattern you demonstrated.

#### 2. Why do we need it?
Some formats and rules are hard to describe but easy to *show*. Two or three good examples can replace a paragraph of confusing instructions and get far more consistent results. Few-shot is the go-to fix when the output format keeps drifting or when there are tricky edge cases the model keeps getting wrong.

#### 3. Office Analogy (software company)
It's like showing a new developer **three sample pull requests** that follow the team's style, instead of writing a 10-page style guide. They copy the pattern from real examples and get it right immediately.

#### 4. Real-Life Analogy (everyday)
It's like a **worked example in a math textbook**. Before the exercises, the book solves 2–3 problems step by step. You copy the method and solve the rest correctly.

#### 5. Internal Working (numbered steps)
1. You provide several example pairs: input then desired output.
2. Claude detects the pattern across the examples.
3. It infers the format, tone, and edge-case handling.
4. When it sees your real input, it applies the same pattern.
5. Output matches the examples' style closely.

#### 6. Architecture Diagram (ASCII)
```
 EXAMPLES (teach the pattern)
 +-------------------------------------+
 | Input:  "I love it!"   -> Positive  |
 | Input:  "It broke."    -> Negative  |
 | Input:  "It's okay."   -> Neutral   |
 +-------------------------------------+
                |
                v  (Claude learns the mapping)
 REAL INPUT: "Best purchase ever!"  ->  Positive
```

#### 7. Real Example
A company classifies support tickets by urgency. **Few-shot prompt:** three examples like `"Server down!" -> High`, `"Typo on page -> Low"`, `"Login slow -> Medium"`. Then the real ticket. **How Claude processes it:** it copies the labeling pattern and returns `High/Medium/Low` consistently, without inventing new categories.

#### 8. Live Demo (classroom)
Run the same classification task twice: once **zero-shot** (no examples) and once **few-shot** (three examples). Compare consistency across 5 test inputs. The class sees the few-shot version stick to the exact labels and format.

#### 9. Interview Questions
**Basic**
1. What is few-shot prompting?
2. What's the difference between zero-shot, one-shot, and few-shot?
3. What does each example contain?
4. Why show instead of describe?
5. How many examples make it "few-shot"?

**Intermediate**
1. When is few-shot better than a prose description?
2. How do examples handle edge cases?
3. Can bad examples hurt? How?
4. Does adding examples cost tokens? Trade-off?
5. How do you pick which examples to include?

**Scenario-based**
1. Output format keeps drifting. How does few-shot help?
2. The model mislabels sarcastic reviews. What example do you add?
3. You have limited tokens but need format control. How many examples?
4. Your examples are all "Positive." What might go wrong?
5. You need consistent JSON keys. How do examples enforce them?

#### 10. Common Mistakes
- **Inconsistent examples** — if your examples vary in format, output will too.
- **Biased examples** (all one label) — the model may over-predict that label.
- **Too many examples** — wastes tokens; a few good ones usually suffice.
- **Examples that don't cover edge cases** you actually care about.

#### 11. Best Practices
- Use **2–5 clean, consistent** examples that all follow the exact target format.
- Cover important **edge cases** (sarcasm, empty input, unusual formats).
- Balance labels so you don't bias the model.
- Wrap examples in `<example>` tags (combine with XML prompting, 2.6).
- This is the **"E" (Examples)** in PRECISE.

#### 12. One-Page Summary
- **Key points:** Show a few input→output examples to teach format and edge cases; more reliable than prose.
- **Important terms:** few-shot, zero-shot, one-shot, examples, edge cases.
- **Quick revision:** show, don't tell; examples teach format fastest.
- **Mnemonic:** **"Show a few, they'll follow through."**

> **Trainer Note:** Stress *consistency* of examples. One sloppy example poisons the pattern.

---

### 2.8 Role Prompting

#### 1. Definition
**Role prompting** means assigning Claude a **persona or role** — "You are a senior tax accountant," "You are a friendly kindergarten teacher" — usually in the system prompt. The role steers Claude's **tone, vocabulary, depth, and rigor**. A tax-accountant role produces precise, careful, jargon-aware answers; a kindergarten-teacher role produces simple, warm ones. It's a quick, powerful way to shape *how* Claude answers, not just *what* it answers.

#### 2. Why do we need it?
The same facts can be explained many ways. A role tells Claude which "voice" and level of expertise to use, so the answer fits your audience. It also raises quality on specialized tasks: telling Claude it's an expert in a field nudges it toward more careful, domain-appropriate reasoning and vocabulary.

#### 3. Office Analogy (software company)
It's like **assigning the right specialist** to a task. You wouldn't ask the graphic designer to review database security. Giving Claude the role "senior security engineer" is like routing the ticket to the right expert who speaks the right language.

#### 4. Real-Life Analogy (everyday)
It's like asking **"explain it like a doctor" vs "explain it like a friend."** Same topic (a health question), but the role changes the vocabulary, depth, and tone of the explanation.

#### 5. Internal Working (numbered steps)
1. You state the role, usually in the system prompt ("You are a...").
2. Claude adopts that persona as its behavioral frame.
3. It selects vocabulary, tone, and rigor matching the role.
4. Every answer is filtered through that persona.
5. Change the role, and the whole voice changes.

#### 6. Architecture Diagram (ASCII)
```
 SYSTEM: "You are a senior tax accountant."
                 |
                 v
        +------------------+
        |  Persona filter  |
        |  tone/vocab/rigor|
        +------------------+
                 |
 USER: "Can I deduct my laptop?"
                 v
 ASSISTANT: precise, jargon-aware, cautious tax answer
```

#### 7. Real Example
An ed-tech app explains science to kids. **Role:** "You are a fun, patient science teacher for 8-year-olds. Use simple words and everyday examples." **How Claude processes it:** even for a question like "why is the sky blue?", it avoids jargon and uses a kid-friendly analogy, because the role sets the voice.

#### 8. Live Demo (classroom)
Ask the same question — "Explain compound interest" — under three roles: (1) a Wall Street analyst, (2) a friendly uncle, (3) a strict math professor. The class hears three distinct voices for identical content, proving the role controls style and depth.

#### 9. Interview Questions
**Basic**
1. What is role prompting?
2. Where is the role usually set?
3. What does a role steer?
4. Give an example role.
5. Which PRECISE letter is this?

**Intermediate**
1. Why can a role improve answer quality on expert tasks?
2. How does role prompting differ from just adding instructions?
3. Can the role change vocabulary? Give an example.
4. What happens if you change the role mid-project?
5. How do role prompting and system prompts relate?

**Scenario-based**
1. Answers are too technical for customers. What role fix helps?
2. You need legal-grade caution. What role would you assign?
3. Two audiences (kids and experts) need the same facts. What do you change?
4. The tone feels cold and robotic. How can a role warm it up?
5. A role alone isn't enough for accuracy. What else do you add? (Hint: context/examples.)

#### 10. Common Mistakes
- **Vague roles** ("be helpful") — not specific enough to steer voice.
- **Role but no task clarity** — a persona doesn't replace clear instructions.
- **Conflicting role + instructions** ("be a strict lawyer" + "be super casual").
- **Assuming the role guarantees facts** — it shapes *style*, not truth; still add context.

#### 11. Best Practices
- Put the role in the **system prompt** (ties to 2.2).
- Be specific: field, seniority, audience, tone.
- Combine role (**Persona**, the "P" in PRECISE) with clear task instructions.
- Match the role to your **audience**, not just the topic.

#### 12. One-Page Summary
- **Key points:** Assign Claude a persona (usually in system prompt) to steer tone, vocabulary, and rigor.
- **Important terms:** role prompting, persona, tone, rigor.
- **Quick revision:** the role sets the *voice*; instructions set the *task*.
- **Mnemonic:** **"Give a role, hit the goal."**

> **Trainer Note:** Reinforce that a role shapes *style*, not *facts*. Students often expect a role to fix accuracy — it won't; context and examples do.

---

### 2.9 Prompt Chaining

#### 1. Definition
**Prompt chaining** means breaking a big task into a **sequence of smaller prompts**, where each step's output feeds the next. For example: **extract** key data → **summarize** it → **format** as a report. Instead of one giant, do-everything prompt, you run a pipeline of focused steps. Each step is simpler, more reliable, and independently testable. Chaining trades one risky mega-prompt for several dependable small ones.

#### 2. Why do we need it?
One huge prompt asking Claude to "extract, analyze, summarize, translate, and format" often does some parts poorly. Splitting the work lets each step focus on one job, which raises accuracy. You can also **test and debug each step** on its own, swap a step out, or add validation between steps. It's the classic "divide and conquer" applied to prompts.

#### 3. Office Analogy (software company)
It's an **assembly line / CI pipeline**. Instead of one engineer building an entire product alone, the work flows through stages: design → build → test → deploy. Each stage does one thing well, and the output of one feeds the next. Bugs are caught at the stage where they happen.

#### 4. Real-Life Analogy (everyday)
It's like **cooking a recipe in steps**: chop the vegetables → cook them → plate the dish. You don't do everything at once; each step's result feeds the next, and you can fix a step without redoing the whole meal.

#### 5. Internal Working (numbered steps)
1. Split the big task into logical steps (extract → summarize → format).
2. Run prompt 1; capture its output.
3. Feed that output as input to prompt 2.
4. Repeat down the chain, optionally validating between steps.
5. The final step's output is your result.

#### 6. Architecture Diagram (ASCII)
```
 INPUT
   |
   v
 +-----------+     +------------+     +-----------+
 | Prompt 1  | --> | Prompt 2   | --> | Prompt 3  | --> OUTPUT
 | EXTRACT   |     | SUMMARIZE  |     | FORMAT    |
 +-----------+     +------------+     +-----------+
   (data)            (summary)         (report)
   each step is small, focused, testable
```

#### 7. Real Example
A firm turns messy meeting transcripts into clean reports. **Chain:** Step 1 extracts action items from the transcript → Step 2 groups them by owner → Step 3 formats a Markdown report. **How Claude processes it:** each prompt handles one job, so the extraction is accurate, the grouping is clean, and the formatting is consistent — far better than one prompt doing all three.

#### 8. Live Demo (classroom)
Take a paragraph of raw customer feedback. Run three prompts live: (1) "Extract complaints as a list," (2) "Group these into themes," (3) "Write a 3-sentence summary for the manager." Show the output flowing from one step to the next. Then contrast with a single "do it all" prompt and compare quality.

#### 9. Interview Questions
**Basic**
1. What is prompt chaining?
2. What connects one step to the next?
3. Give a simple 3-step chain example.
4. Why not just use one big prompt?
5. What is the output of the final step?

**Intermediate**
1. Why does chaining improve reliability?
2. How does chaining help debugging?
3. What can you add *between* steps? (validation)
4. What's a downside of chaining? (more calls, more latency/cost)
5. How do you decide where to split a task?

**Scenario-based**
1. A single prompt does extraction poorly. How does chaining help?
2. One step in your chain fails often. How do you isolate and fix it?
3. You need to validate data before formatting. Where does that go?
4. Latency matters — how do you balance chaining vs one prompt?
5. A step's output format breaks the next step. What technique locks it? (XML/few-shot)

#### 10. Common Mistakes
- **Chaining everything** — simple tasks don't need a pipeline; it adds cost and latency.
- **Loose hand-offs** — if step 1's output format is inconsistent, step 2 breaks.
- **No validation between steps** — errors silently flow downstream.
- **Ignoring cost** — each step is a separate call (cost is first-class here).

#### 11. Best Practices
- Split into **focused, single-responsibility** steps (mirrors the project's "many small files" ethos).
- Lock each step's output format with **XML tags** and **few-shot examples** so hand-offs are clean.
- Add **validation** between steps when correctness matters.
- Balance reliability against added **latency and cost**.
- Test each step independently.

#### 12. One-Page Summary
- **Key points:** Break a big task into a sequence of small prompts; each output feeds the next; more reliable and testable.
- **Important terms:** prompt chaining, pipeline, hand-off, validation step.
- **Quick revision:** divide and conquer — small steps beat one mega-prompt.
- **Mnemonic:** **"Chain the steps, keep the reps"** (each step repeats one reliable job).

> **Trainer Note:** Have students draw the pipeline before coding it. Seeing the boxes and arrows makes chaining click.

---

### Quick Recap
- **Prompt (2.1):** the text you give Claude — the only way to steer it. Clear in, clear out.
- **System prompt (2.2):** set-once global rules and persona; "who you are + how you behave."
- **User prompt (2.3):** the human's actual request and data; "what I need now."
- **Assistant response (2.4):** Claude's reply and future memory; role `assistant`; can be prefilled.
- **Prompt engineering (2.5):** deliberate design using the **PRECISE** checklist for reliable output.
- **XML prompting (2.6):** wrap parts in tags so Claude separates data from instructions cleanly and safely.
- **Few-shot (2.7):** show a few input→output examples to teach format and edge cases.
- **Role prompting (2.8):** assign a persona to steer tone, vocabulary, and rigor (usually in the system prompt).
- **Prompt chaining (2.9):** split a big task into a sequence of small, testable steps.

**Golden thread:** everything maps to **PRECISE** — Persona (role/system), Result/Examples/Context/Instructions (user task, with XML + few-shot), Specification/Evaluation (output spec) — and prompts stay **hierarchical**: Base → Role → Task → Output-spec. State each rule once, plainly, and include only the context you need.


---

## Module 3 — Context Management

Claude has no memory of its own. Everything it "knows" for a single request lives in the **context** you send it. This module teaches you what context is, how it is measured, how it fills up, and how to keep it lean, cheap, and accurate using the **CALM** checklist.

---

### 3.1 Context

#### 1. Definition
**Context** is *everything* you send to the model for one single request. It includes the **system prompt**, the **conversation history**, any **retrieved documents**, any **tool results**, and the **current user message**. The model has **no memory of its own** — the context is its entire working knowledge for that one call. When the call ends, the model forgets everything. Nothing carries over unless *you* send it again. Think of context as the model's short-term desk, wiped clean after every task.

#### 2. Why do we need it?
Because the model is **stateless**. It cannot "remember" your name, your last question, or a document you showed it a minute ago. If you want it to know something, you must place that something *inside the context* of the current request. Context is the only channel through which knowledge, instructions, and history reach the model. Get context right and answers are sharp; get it wrong and the model guesses.

#### 3. Office Analogy
Imagine a brilliant consultant with **total amnesia**. Every morning they arrive knowing nothing about yesterday. To get useful work, you hand them a **folder** containing: the company rulebook (system prompt), the meeting notes so far (history), the reference reports (documents), the calculator printouts (tool results), and today's actual question. The consultant reads only what is in that folder. Leave a page out, and they simply don't know it.

#### 4. Real-Life Analogy
Context is like a **whiteboard in a meeting room** that gets erased after every meeting. Whatever you want discussed must be written on the board *now*. The people in the room can only reason about what is currently on the board — not what was written last week.

#### 5. Internal Working
1. You **assemble** all the pieces: system prompt, history, documents, tools, user message.
2. These pieces are **concatenated** into one big text payload.
3. The payload is **converted into tokens** (see 3.3).
4. The model **reads all tokens at once** and produces an output.
5. The output is returned; the context is **discarded** by the model.
6. For the next request, you **re-send** everything you still want the model to know.

#### 6. Architecture Diagram
```
        WHAT YOU SEND (one request)
   ┌───────────────────────────────────┐
   │  System Prompt   (rules/role)     │
   │  Conversation History (past turns)│
   │  Retrieved Documents (RAG)        │
   │  Tool Results    (API/DB output)  │
   │  Current User Message             │
   └───────────────┬───────────────────┘
                   │  all combined = CONTEXT
                   ▼
            ┌─────────────┐
            │    MODEL    │  (no memory of its own)
            └──────┬──────┘
                   ▼
              Response  → context discarded
```

#### 7. Real Example
You are building a support bot. For a customer asking "Is my order shipped?", the context you send is: a system prompt ("You are a polite support agent"), the last 3 chat turns, the customer's order record pulled from a database (tool result), and the current question. The model reads all of it and replies with the shipping status — because you *put the order record in the context*.

#### 8. Live Demo
```python
# Reuses core.providers.LLMProvider (see CLAUDE.md conventions)
from core.providers import get_provider

provider = get_provider()  # vendor-agnostic

messages = [
    {"role": "system",    "content": "You are a concise support agent."},
    {"role": "user",      "content": "My name is Sam."},
    {"role": "assistant", "content": "Hi Sam, how can I help?"},
    {"role": "user",      "content": "What is my name?"},  # only works if history is re-sent
]

resp = provider.chat(messages, max_tokens=100)
print(resp.text)          # -> "Your name is Sam."
print(resp.usage)         # input/output token counts
```
Try deleting the middle two lines: the model will no longer know the name — proof that context, not memory, is doing the work.

#### 9. Interview Questions

**Basic**
1. What is context in the context of an LLM?
2. Does the model remember previous requests on its own?
3. Name the five things that typically make up context.
4. What happens to context after the model responds?
5. Where does the current user message fit in?

**Intermediate**
1. Why is "the model is stateless" an important idea for developers?
2. How does retrieved-document context differ from conversation history?
3. If a fact is not in context, how can the model still answer correctly? (It can't reliably — it guesses.)
4. Why can two identical questions give different answers if the surrounding context differs?
5. What is the risk of putting too much into context?

**Scenario**
1. A chatbot "forgot" the user's name after 10 messages. What likely happened?
2. Your bot leaks another user's data. How could context assembly cause this?
3. You must summarize a 300-page PDF. How does context shape your approach?
4. A demo works locally but fails in production with missing details — how do you debug the context?
5. Cost suddenly doubled with no code change. How could context be the cause?

#### 10. Common Mistakes
- **Assuming the model remembers** — it does not; you must re-send. *Why: it is stateless.*
- **Dumping everything into context** — bloats cost and confuses the model. *Why: more tokens ≠ better answers.*
- **Forgetting tool results** — the model can't see an API call you didn't include. *Why: only in-context data is visible.*
- **Mixing secrets into context** — leaks credentials. *Why: violates the .env-only rule.*

#### 11. Best Practices
- Follow **CALM**: **C**ache stable prefixes, **A**ssemble only needed layers, **L**imit token count, **M**anage lifecycle.
- Treat context as a **deliberate build**, not a dumping ground.
- Keep the **system prompt stable** (helps caching) and volatile data last.
- Always inspect `usage` to know how big your context really is.

#### 12. One-Page Summary
- **Key points:** Context = all input for one request. Model has no memory. Re-send what you want remembered.
- **Important terms:** context, stateless, system prompt, tool result, retrieved document.
- **Quick revision:** No context in → no knowledge available. Context is the model's only window.
- **Mnemonic:** **"Model forgets; the folder remembers."**

> **Trainer Note:** Spend real time here — every other topic in this module is just "what fills the context" or "what happens when it gets too full." If learners internalize *stateless + folder*, the rest clicks.

---

### 3.2 Context Window

#### 1. Definition
The **context window** is the **maximum number of tokens** the model can consider at once — counting **both input and output together**. It is a hard, finite ceiling. Modern Claude models support **very large windows** (generally up to **~200K tokens**, with a **1M-token** window available on some Claude models/tiers). If your input plus your requested output exceeds this window, the request fails or content is dropped. The window is the size of the model's "desk" — big, but not infinite.

#### 2. Why do we need it?
Because it defines the **budget** you are working within. Every design decision — how much history to keep, how many documents to load, how long the answer can be — is bounded by the window. Knowing the window stops you from sending more than the model can hold and helps you plan trimming, chunking, and summarizing before you hit the wall.

#### 3. Office Analogy
The consultant's **desk** can only hold so many pages. Once the desk is full, adding a new page means one falls off the edge. A bigger desk (larger window) fits more reports, but there is still an edge. You plan which pages get desk space.

#### 4. Real-Life Analogy
A **suitcase** with a fixed size. You can pack a lot, but not everything. Bring the essentials; if you overpack, the zipper won't close (the request errors).

#### 5. Internal Working
1. The model has a fixed **token capacity** (e.g., 200K).
2. Your **input tokens** are counted (system + history + docs + message).
3. Your **max_tokens** (requested output) is reserved from the same budget.
4. **Input + output must fit** within the window.
5. If the total would exceed it, the request is **rejected** (overflow) or older content must be trimmed.

#### 6. Architecture Diagram
```
   CONTEXT WINDOW  (e.g., 200,000 tokens total)
   ┌──────────────────────────────────────────────┐
   │  INPUT TOKENS                | OUTPUT TOKENS   │
   │  system+history+docs+msg     | (max_tokens)    │
   │  ◄────────── must all fit ──────────────────►  │
   └──────────────────────────────────────────────┘
       exceed the edge  ──►  ERROR / dropped content
```

#### 7. Real Example
You load a 150K-token legal contract and ask for a 5K-token summary. Input (150K) + output (5K) = 155K, comfortably inside a 200K window — fine. But load *two* such contracts (300K) and you exceed 200K → you must chunk, summarize, or move to a 1M-token tier.

#### 8. Live Demo
```python
from core.providers import get_provider
provider = get_provider()

print(provider.context_window)   # e.g., 200000

# Estimate before sending
input_tokens = provider.count_tokens(big_document + question)
print("input:", input_tokens, "budget left:", provider.context_window - input_tokens)

resp = provider.chat(messages, max_tokens=2000)  # reserve 2000 for the answer
```

#### 9. Interview Questions

**Basic**
1. What is a context window?
2. Does it count input only, or input and output?
3. Roughly how large are modern Claude windows?
4. What happens when you exceed it?
5. Is the window infinite?

**Intermediate**
1. Why must `max_tokens` be considered part of the window budget?
2. How does a 1M-token window change your design choices?
3. Why doesn't a bigger window automatically mean better answers?
4. How would you measure how full your window is?
5. What is the trade-off of always using the largest window?

**Scenario**
1. A request fails with a "too many tokens" error. Walk through your fix.
2. You need both huge input and a long answer but hit the ceiling. Options?
3. Your history grows every turn and eventually overflows. Strategy?
4. Cost is high with a 1M window on short tasks — what's wrong?
5. You must process a 2M-token codebase. What's your approach?

#### 10. Common Mistakes
- **Forgetting output counts too** — reserving no room for the answer. *Why: input+output share one budget.*
- **Assuming bigger is always better** — larger windows cost more and can dilute attention. *Why: "lost in the middle" and cost.*
- **Not measuring before sending** — surprise overflow errors. *Why: no token count = flying blind.*

#### 11. Best Practices
- Know your model's exact window; don't guess.
- Always **reserve headroom** for `max_tokens`.
- Prefer the **smallest window that fits** the task (the **L** in CALM).
- Count tokens *before* you send.

#### 12. One-Page Summary
- **Key points:** Fixed token ceiling; input + output share it; ~200K common, 1M on some tiers.
- **Important terms:** context window, token budget, max_tokens, overflow.
- **Quick revision:** Window = desk size. Fill = input + requested output.
- **Mnemonic:** **"One desk, shared by question and answer."**

> **Trainer Note:** The most common beginner bug is forgetting that the *response* eats from the same budget. Hammer "input + output = one window."

---

### 3.3 Tokens

#### 1. Definition
**Tokens** are the small pieces text is broken into before the model reads it. A token is roughly **a few characters**, or about **¾ of a word** in English. Both your **input** and the model's **output** are measured in tokens. **Cost and limits are both counted in tokens**, not words or characters. The model never sees letters — it sees tokens. The API's `usage` field reports the exact **input and output token counts** for every request, which is how you track size and cost.

#### 2. Why do we need it?
Because tokens are the **unit of everything**: the context window is measured in tokens, pricing is per token, and rate limits are per token. To predict cost, avoid overflow, and budget your context, you must think in tokens — not the words you happen to type.

#### 3. Office Analogy
The print shop charges **per line printed**, not per idea. A short memo and a long memo cost differently because they use different numbers of lines. Tokens are those billable "lines" — the shop counts them whether you like it or not.

#### 4. Real-Life Analogy
Like **SMS message segments**: your one long text quietly gets split into several 160-character segments, and you're billed per segment. You typed "one message"; the carrier counted several.

#### 5. Internal Working
1. Text enters a **tokenizer**.
2. The tokenizer splits it into tokens (common words = 1 token; rare/long words = several).
3. Each token maps to a **number (ID)**.
4. The model processes these numbers and emits **output tokens**.
5. Output tokens are converted **back into text**.
6. `usage` reports **input_tokens** and **output_tokens** for billing and limits.

#### 6. Architecture Diagram
```
 "Claude is helpful"
        │  tokenizer
        ▼
 ["Claude"]["is"]["help"]["ful"]   ~4 tokens
        │  IDs
        ▼
   [ 8912, 402, 771, 233 ]
        │  model
        ▼
   output tokens ──► text  + usage{input, output}
```

#### 7. Real Example
"unbelievable" may split into `["un","believ","able"]` = 3 tokens, while "cat" is 1 token. A 1,000-word English email is roughly **1,300 tokens**. If a model costs, say, a few dollars per million tokens, you can now estimate that email's price precisely.

#### 8. Live Demo
```python
from core.providers import get_provider
provider = get_provider()

text = "Claude is helpful and provider-agnostic."
n = provider.count_tokens(text)
print("tokens:", n)

resp = provider.chat(
    [{"role": "user", "content": text}], max_tokens=50)
print(resp.usage.input_tokens, resp.usage.output_tokens)

# Cost is first-class (CLAUDE.md): print estimated $
price_in, price_out = 3.0/1e6, 15.0/1e6   # example $/token
cost = resp.usage.input_tokens*price_in + resp.usage.output_tokens*price_out
print(f"est. ${cost:.6f}")
```

#### 9. Interview Questions

**Basic**
1. What is a token?
2. Roughly how many characters or words is one token?
3. Are outputs counted in tokens too?
4. What does the `usage` field report?
5. Are cost and limits measured in words or tokens?

**Intermediate**
1. Why does the same sentence tokenize to different counts in different languages?
2. Why do rare words cost more tokens than common ones?
3. How do you estimate the cost of a request before sending it?
4. Why can't you rely on character count for budgeting?
5. How do input and output tokens differ in typical pricing?

**Scenario**
1. Your bill is high but your prompts look short — where do you look?
2. A non-English app uses far more tokens than expected. Why?
3. You must cap cost per request — which knobs do you turn?
4. You want to compare two prompts' cost — how?
5. A JSON payload balloons the token count — how do you trim it?

#### 10. Common Mistakes
- **Counting words, not tokens** — undershoots real size. *Why: 1 word ≈ 1.3 tokens.*
- **Ignoring output tokens in cost** — outputs are often priced higher. *Why: generation is expensive.*
- **Assuming all languages tokenize equally** — many use more tokens. *Why: tokenizer favors English.*

#### 11. Best Practices
- Always read `usage` and **print estimated $** (CLAUDE.md rule).
- **Count tokens** during development, not after the bill.
- Trim verbose formatting (extra whitespace, redundant JSON keys).
- Cap `max_tokens` to control the priciest side of the bill.

#### 12. One-Page Summary
- **Key points:** Tokens = text pieces (~¾ word). Input+output both counted. `usage` reports them.
- **Important terms:** token, tokenizer, input_tokens, output_tokens, usage.
- **Quick revision:** Everything is priced and limited in tokens, not words.
- **Mnemonic:** **"The meter runs in tokens."**

> **Trainer Note:** Have learners paste text into a token counter live. Seeing "12 words = 17 tokens" makes the concept stick better than any slide.

---

### 3.4 Conversation History

#### 1. Definition
**Conversation history** is the running list of prior **user and assistant turns** that you **re-send on every call** so the model appears to "remember" the chat. Underneath, the model is **stateless** — it has no memory — so the illusion of memory comes entirely from you resending the past turns each time. Every new request carries the whole relevant history plus the new message. The longer the chat, the bigger this history grows, and the more of your context window it consumes.

#### 2. Why do we need it?
Because without it, every message would be a **cold start** with no idea what was said before. History gives conversations continuity: follow-up questions, pronouns ("it", "that"), and running context all depend on the past turns being present. It is what turns isolated calls into a coherent dialogue.

#### 3. Office Analogy
The consultant with amnesia keeps a **running meeting-minutes document**. Before each new question, you hand them the minutes so far. They read it, answer, and you append their answer to the minutes for next time. The minutes are the "memory" — kept by *you*, not them.

#### 4. Real-Life Analogy
A **group chat where everyone has amnesia**: before speaking, someone reads the entire thread aloud. Only then can the next person reply sensibly. Skip the readout, and replies make no sense.

#### 5. Internal Working
1. Start with an empty `messages` list.
2. Append the user's message; send the list.
3. Append the model's reply to the list.
4. On the next turn, **append the new user message** and send the **whole list again**.
5. Repeat — the list keeps growing.
6. Eventually it risks **overflow**, so you trim or summarize old turns.

#### 6. Architecture Diagram
```
 Turn 1 sends:  [U1]
 Turn 2 sends:  [U1, A1, U2]
 Turn 3 sends:  [U1, A1, U2, A2, U3]
 Turn N sends:  [U1, A1, ... , U(N)]   ← grows every turn
                 └─────────────────┘
                  re-sent EACH time (stateless underneath)
```

#### 7. Real Example
A tutoring bot: turn 1 the student says "Explain photosynthesis." Turn 2 they say "Give me an example of *it*." The word "it" only resolves because turns 1 and 2 are both in the resent history. Drop turn 1 and the model has no idea what "it" refers to.

#### 8. Live Demo
```python
from core.providers import get_provider
provider = get_provider()

history = [{"role": "system", "content": "You are a friendly tutor."}]

def ask(user_msg):
    history.append({"role": "user", "content": user_msg})
    resp = provider.chat(history, max_tokens=200)
    history.append({"role": "assistant", "content": resp.text})
    return resp.text

print(ask("Explain photosynthesis in one line."))
print(ask("Give me an example of it."))   # 'it' works — history is resent
print("history turns:", len(history))
```

#### 9. Interview Questions

**Basic**
1. What is conversation history?
2. Why does the model seem to remember if it is stateless?
3. What do you do with the model's reply after each turn?
4. Does history grow or shrink over a long chat?
5. What is re-sent on every call?

**Intermediate**
1. Why do follow-up questions with "it/that" need full history?
2. What is the cost implication of growing history?
3. How does history relate to the context window filling up?
4. When would you *not* include the full history?
5. How do you keep a system prompt stable while history grows (hint: caching)?

**Scenario**
1. A long chat starts erroring — what happened and what's the fix?
2. You want to reduce cost on a 200-turn chat. Options?
3. The bot "forgets" early facts after many turns — why, and how to fix?
4. Two users' histories got mixed. What went wrong in assembly?
5. You need to keep key facts but drop chit-chat. How?

#### 10. Common Mistakes
- **Not appending the assistant reply** — the model loses its own prior answers. *Why: continuity breaks.*
- **Sending unbounded history** — eventual overflow and rising cost. *Why: history grows forever.*
- **Mixing users' histories** — data leaks. *Why: shared or mislabeled lists.*

#### 11. Best Practices
- Keep the **system prompt first and stable** (caches well).
- **Cap or summarize** old turns before overflow (see 3.6).
- Store history **per user/session**, never shared.
- Watch `usage` to see history's growing token cost (**L** in CALM).

#### 12. One-Page Summary
- **Key points:** History = resent past turns = the "memory" illusion. Grows each turn.
- **Important terms:** turn, messages list, stateless, session.
- **Quick revision:** Memory is a resend, not a recall.
- **Mnemonic:** **"Remembering = resending."**

> **Trainer Note:** Show the growing `messages` list on screen turn by turn. The "aha" is watching it balloon — it motivates 3.6 (compression) naturally.

---

### 3.5 Long Context

#### 1. Definition
**Long context** means tasks that load **large inputs** into the window — whole documents, books, or entire codebases — often tens or hundreds of thousands of tokens. It becomes possible with big windows, but brings three watch-outs: **cost** (more tokens = more money), **latency** (more tokens = slower), and the **"lost in the middle"** effect, where the model pays *less attention to material buried in the center* of a very long input. Good structure and placement fight these effects.

#### 2. Why do we need it?
Because real work involves big material: analyzing a contract, answering over a manual, or reviewing a codebase. Long context lets the model reason over all of it **at once** instead of in disconnected fragments. But used carelessly it is slow, expensive, and can miss the exact detail you needed — so you manage it deliberately.

#### 3. Office Analogy
You give the consultant a **1,000-page binder** and one question. They *can* read it all, but it takes longer (latency), costs more of their time (cost), and they may skim the middle chapters (lost in the middle). So you put a **sticky note with the question right next to the relevant chapter** and add clear section tabs.

#### 4. Real-Life Analogy
Reading a **thick textbook the night before an exam**. You remember the first pages and the last pages well, but the middle blurs. Smart students put their key question beside the exact paragraph and use headings to navigate.

#### 5. Internal Working
1. A large document is loaded into the input.
2. The model reads **all tokens**, but attention is **uneven** — edges get more focus than the middle.
3. You **structure** the input with headings/XML tags so sections are findable.
4. You **place the question near the relevant material** (top or bottom, next to the evidence).
5. The model answers; you **verify** it used the right section.

#### 6. Architecture Diagram
```
   LONG INPUT (attention strength)
   HIGH │████                    ████│ HIGH
        │    ██              ██      │
   LOW  │        ████████████        │  ← "lost in the middle"
        └────────────────────────────┘
   Fix: put QUESTION + key evidence near an EDGE,
        add ## headings / <tags> to structure.
```

#### 7. Real Example
You paste a 120K-token API manual and ask, "What's the rate limit for the /orders endpoint?" If that detail sits in the exact middle, the model may miss it. So you either place the question right after the /orders section, or you retrieve just that section — and accuracy jumps.

#### 8. Live Demo
```python
from core.providers import get_provider
provider = get_provider()

doc = load_manual()  # ~120k tokens
prompt = f"""<manual>
{doc}
</manual>

Question (answer using ONLY the manual above):
What is the rate limit for the /orders endpoint?"""

resp = provider.chat([{"role":"user","content":prompt}], max_tokens=300)
print(resp.text, resp.usage)   # watch input_tokens + latency
```
Note the **question is placed AFTER the document** (near an edge) and the doc is wrapped in **XML tags** for structure.

#### 9. Interview Questions

**Basic**
1. What is long context?
2. Name three watch-outs of long context.
3. What is the "lost in the middle" effect?
4. Where should you place your question in a long input?
5. Why use headings or XML tags?

**Intermediate**
1. Why does latency rise with input size?
2. How does long context affect cost, and how do you mitigate it?
3. When is retrieval (RAG) better than stuffing everything in?
4. Why do edges of long inputs get more attention?
5. How does structure improve accuracy on long inputs?

**Scenario**
1. The model misses a fact known to be in the middle. Fixes?
2. Responses got slow after you enlarged the input. Why and what next?
3. You must answer over 5 large docs but only one is relevant. Approach?
4. Accuracy drops as documents grow — how do you diagnose?
5. Cost is fine but answers cite the wrong section — remedy?

#### 10. Common Mistakes
- **Dumping raw text with no structure** — model can't navigate. *Why: no anchors = poor retrieval of detail.*
- **Burying the question in the middle** — worst attention zone. *Why: lost in the middle.*
- **Stuffing everything when retrieval would do** — slow and costly. *Why: you loaded irrelevant tokens.*

#### 11. Best Practices
- Put the **question near the relevant material** (an edge).
- Structure with **headings / XML tags**.
- Prefer **retrieval of the needed slice** over loading everything (**A** in CALM: assemble selectively).
- Watch **cost and latency** in `usage`.

#### 12. One-Page Summary
- **Key points:** Big inputs = powerful but costly, slow, and prone to "lost in the middle."
- **Important terms:** long context, latency, lost in the middle, structure, retrieval.
- **Quick revision:** Big binder works only with tabs and a well-placed sticky note.
- **Mnemonic:** **"Edges win; structure the middle."**

> **Trainer Note:** "Lost in the middle" surprises beginners who assume the model reads everything equally. Demo it: hide a fact mid-document and watch it get missed.

---

### 3.6 Context Compression

#### 1. Definition
**Context compression** (also called **compaction**) means **summarizing earlier history** so it still fits inside the window. Instead of resending 200 raw turns, you replace the old ones with a short summary that captures the key facts. This keeps recent turns detailed while shrinking the old ones. The main **risk** is **losing detail** — a summary may drop a fact you later need. Compression is the standard cure for a conversation that would otherwise **overflow** the window.

#### 2. Why do we need it?
Because history grows forever, but the window is finite. Without compression, long chats eventually overflow or become too expensive. Compression lets a conversation continue **indefinitely** by trading old verbatim detail for a compact summary — keeping cost and token count under control.

#### 3. Office Analogy
The meeting minutes are getting too thick to carry. So an assistant writes a **one-page executive summary** of the first hour and staples it in front, discarding the long transcript. Everyone keeps working from the summary plus the recent notes — lighter to carry, but some fine detail is gone.

#### 4. Real-Life Analogy
**"Previously on..."** at the start of a TV episode. Instead of replaying whole past episodes, a 30-second recap covers what matters so the story continues. You lose scene details but keep the plot.

#### 5. Internal Working
1. Detect that history is **approaching the token limit**.
2. Take the **oldest turns** (least likely to need verbatim).
3. Ask the model (or a rule) to **summarize** them into a compact note.
4. **Replace** those old turns with the summary in the messages list.
5. Keep **recent turns full**; continue the conversation.
6. Repeat as the chat grows again.

#### 6. Architecture Diagram
```
 BEFORE (overflowing):
 [U1 A1 U2 A2 ... U40 A40 U41]   ← too many tokens

           │ summarize oldest
           ▼
 AFTER (compressed):
 [ SUMMARY(U1..A38) , U39 A39 U40 A40 U41 ]
   └── small ──┘      └──── recent, full ────┘
```

#### 7. Real Example
A coding-assistant chat hits 190K tokens. You summarize the first 150 turns into a 2K-token "Project so far: goals, decisions, file names" note, drop the raw turns, and keep the last 10 turns verbatim. The chat drops to ~15K tokens and continues smoothly — though a tiny detail from turn 12 might now be gone.

#### 8. Live Demo
```python
from core.providers import get_provider
provider = get_provider()

def compress(history, keep_last=6):
    old, recent = history[:-keep_last], history[-keep_last:]
    summary = provider.chat(
        [{"role":"user","content":
          "Summarize these turns, keep decisions & names:\n"+str(old)}],
        max_tokens=400).text
    return [{"role":"system","content":"Summary so far:\n"+summary}] + recent

if provider.count_tokens(str(history)) > 150_000:
    history = compress(history)
print(provider.count_tokens(str(history)))  # much smaller
```

#### 9. Interview Questions

**Basic**
1. What is context compression / compaction?
2. What problem does it solve?
3. What is its main risk?
4. Which turns do you usually compress first?
5. What replaces the old turns?

**Intermediate**
1. How do you decide *when* to compress?
2. Why keep recent turns full while summarizing old ones?
3. What information should a good summary always preserve?
4. How does compression interact with prompt caching?
5. What's the trade-off between summary size and detail retained?

**Scenario**
1. After compressing, the bot forgot a key requirement. How do you prevent this?
2. A chat must run for thousands of turns cheaply. Design the compression.
3. Summaries keep dropping file names the user needs. Fix?
4. Compression made responses vaguer. What went wrong?
5. You need auditability of what was summarized away. Approach?

#### 10. Common Mistakes
- **Summarizing too aggressively** — loses needed detail. *Why: over-compression drops facts.*
- **Compressing recent turns** — hurts immediate coherence. *Why: recent context matters most.*
- **No rule for what to preserve** — random detail loss. *Why: summaries need explicit "keep" instructions.*

#### 11. Best Practices
- Compress **oldest** turns; keep **recent** turns verbatim.
- Tell the summarizer **exactly what to preserve** (names, decisions, IDs).
- Trigger on a **token threshold**, not turn count alone.
- Keep an **archive** of raw turns if auditability matters (**M** in CALM: manage lifecycle).

#### 12. One-Page Summary
- **Key points:** Summarize old history to fit the window; risk = lost detail.
- **Important terms:** compaction, summary, threshold, preserve list.
- **Quick revision:** Trade old verbatim for a compact recap so the chat can continue.
- **Mnemonic:** **"Previously on... keeps the story going."**

> **Trainer Note:** Contrast with 3.7 next: compression *summarizes conversation*, editing *removes stale tool/thinking junk*. Beginners blur the two — draw the line clearly.

---

### 3.7 Context Editing

#### 1. Definition
**Context editing** means **clearing stale, no-longer-needed material** out of the window during long, **tool-heavy** runs — most often old **tool results** and prior **thinking blocks**. When an agent calls many tools, each result piles up in context; once a result has been used, keeping it just wastes tokens. Editing surgically **removes** those dead items while keeping the live conversation intact. Unlike compression (which *summarizes* dialogue), editing *deletes* obsolete scaffolding.

#### 2. Why do we need it?
Because agentic runs with many tool calls fill the window fast with data that mattered only for one step. Old API dumps, intermediate reasoning, and superseded results become **dead weight** — raising cost and crowding out useful context. Editing keeps long tool-loops running without overflowing, by throwing out what is no longer relevant.

#### 3. Office Analogy
During a long project, the consultant's desk fills with **printouts they already used** — yesterday's spreadsheet, a draft they've since finalized. An assistant **clears the used printouts** off the desk so there's room for the current step, while leaving the active documents in place.

#### 4. Real-Life Analogy
**Closing browser tabs** you're done with. You opened 40 tabs researching, but once you've extracted what each one gave you, you close them so the browser (and your brain) stays responsive.

#### 5. Internal Working
1. During an agent loop, each **tool call** adds a result to the context.
2. Track which results have been **consumed** and are now stale.
3. When nearing a limit, **remove** old tool results and old thinking blocks.
4. **Keep** the user goal, key findings, and recent steps.
5. Continue the loop with a **leaner** window.

#### 6. Architecture Diagram
```
 BEFORE editing (tool-heavy run):
 [goal][toolA-result][think][toolB-result][think][toolC-result][step]

        │ drop consumed tool results + old thinking
        ▼
 AFTER editing:
 [goal][key finding][toolC-result][step]
   └── only what the next step actually needs ──┘
```

#### 7. Real Example
A research agent runs 30 web-fetch tools. Each fetch dumps a full page into context. After the agent extracts the one fact it needed from fetch #7, that giant page is dead weight. Context editing removes fetches #1–#25's raw bodies (keeping their extracted notes), so the run continues without overflow.

#### 8. Live Demo
```python
# Conceptual: prune consumed tool results from the messages list
def edit_context(messages, keep_recent_tools=3):
    kept, tool_seen = [], 0
    for m in reversed(messages):
        if m.get("role") == "tool":
            tool_seen += 1
            if tool_seen > keep_recent_tools:
                continue  # drop stale tool result
        kept.append(m)
    return list(reversed(kept))

messages = edit_context(messages)   # leaner window, same goal
```

#### 9. Interview Questions

**Basic**
1. What is context editing?
2. What kinds of content does it usually remove?
3. When is it most useful?
4. How does it differ from compression?
5. Does it delete or summarize?

**Intermediate**
1. Why do tool-heavy agents fill context so fast?
2. How do you decide a tool result is "stale"?
3. What must you never edit out during a run?
4. How does editing reduce cost and overflow risk?
5. How do editing and caching interact?

**Scenario**
1. An agent overflows after 40 tool calls. How does editing help?
2. You edited out a result the agent still needed. Prevention?
3. Latency climbs as an agent loop runs. What might you prune?
4. You must keep an audit trail but a lean live window. Approach?
5. Thinking blocks are eating tokens — safe to drop? When?

#### 10. Common Mistakes
- **Editing out still-needed results** — breaks the task. *Why: not all old results are stale.*
- **Never editing** — long agent runs overflow. *Why: tool dumps accumulate.*
- **Dropping the user goal by accident** — agent loses direction. *Why: goal must always stay.*

#### 11. Best Practices
- Keep a **small window of recent** tool results; drop older consumed ones.
- **Extract-then-drop**: save the needed note, discard the raw dump.
- **Never remove** the user goal or key decisions.
- Combine with compression for very long runs (**M** in CALM).

#### 12. One-Page Summary
- **Key points:** Delete stale tool results / thinking during long tool-heavy runs.
- **Important terms:** context editing, tool result, thinking block, stale, prune.
- **Quick revision:** Close the tabs you're done with; keep the goal open.
- **Mnemonic:** **"Editing deletes junk; compression summarizes talk."**

> **Trainer Note:** Emphasize the editing-vs-compression distinction in one line: *editing = remove dead tool scaffolding; compression = summarize the conversation.* This is a classic exam trap.

---

### 3.8 Context Overflow

#### 1. Definition
**Context overflow** happens when the **total tokens exceed the context window** — input plus requested output no longer fit. The result is an **error** (the request is rejected) or **dropped content** (older material silently falls out of the window). It is the failure mode all the other tools in this module aim to prevent. The fix is straightforward in principle: **trim** old turns, **summarize** (compress), or **chunk** the input into pieces that each fit.

#### 2. Why do we need it (to understand)?
Because it is the #1 practical failure in real chat and agent apps. Long conversations, huge documents, and endless tool loops all trend toward overflow. Knowing how it happens — and the three standard fixes — is what keeps production systems from crashing or silently losing information.

#### 3. Office Analogy
The consultant's desk is **full**, and you keep handing over more pages. Either they say **"I can't take more"** (error) or a page **slides off the back edge unnoticed** (dropped content). To keep working, you must **remove, summarize, or split** the paperwork before adding more.

#### 4. Real-Life Analogy
An **overflowing suitcase**: the zipper won't close (error), or you force it and socks fall out on the way (dropped content). You fix it by removing items, rolling clothes tighter (compress), or using a second bag (chunk).

#### 5. Internal Working
1. You assemble context that totals more tokens than the window.
2. The system checks: **input + max_tokens > window?**
3. If yes → **reject with an error**, *or* **truncate** older tokens.
4. Truncation may **silently drop** early history or document tails.
5. You detect it (error or missing info) and apply a fix: **trim / summarize / chunk**.
6. Re-send within budget.

#### 6. Architecture Diagram
```
   WINDOW ┌───────────────── 200K ─────────────────┐
   need   │███████████████████████████████████ 230K│▓▓▓
          └─────────────────────────────────────┘  ▲
                                        overflow ───┘
   FIXES:  Trim old turns │ Summarize (compress) │ Chunk input
```

#### 7. Real Example
A support chat reaches 210K tokens on a 200K model. The API returns an error. You (a) summarize the first 180 turns to 3K tokens, (b) drop resolved sub-issues, and (c) re-send at 30K tokens — the request now succeeds. Had the system silently truncated instead, the bot might have "forgotten" the customer's original problem.

#### 8. Live Demo
```python
from core.providers import get_provider
provider = get_provider()

def safe_send(messages, max_tokens=1000):
    budget = provider.context_window - max_tokens
    while provider.count_tokens(str(messages)) > budget and len(messages) > 2:
        messages.pop(1)          # trim oldest non-system turn
    return provider.chat(messages, max_tokens=max_tokens)

resp = safe_send(long_history)   # never overflows
print(resp.usage)
```

#### 9. Interview Questions

**Basic**
1. What is context overflow?
2. What two outcomes can it cause?
3. What three fixes address it?
4. Does output count toward overflow?
5. Why is silent truncation dangerous?

**Intermediate**
1. How do you detect overflow before it happens?
2. When is chunking better than summarizing?
3. Why can dropped content be worse than an outright error?
4. How does `max_tokens` contribute to overflow?
5. How do compression and editing prevent overflow?

**Scenario**
1. Production throws token-limit errors under load. Plan?
2. Answers quietly lose early context — diagnose and fix.
3. A single document alone exceeds the window. Approach?
4. You must never lose the user's original request — how?
5. Overflow only happens on long answers. What knob helps?

#### 10. Common Mistakes
- **Ignoring `max_tokens` in the math** — overflow from the output side. *Why: output shares the budget.*
- **Letting silent truncation happen** — invisible data loss. *Why: dropped content isn't announced.*
- **Trimming the system prompt or goal** — breaks behavior. *Why: those must always stay.*

#### 11. Best Practices
- **Count tokens and reserve headroom** before every send (**L** in CALM).
- Prefer **summarize/chunk** over blind truncation.
- Protect the **system prompt and user goal** from trimming.
- Fail **loudly**, not silently — log when you trim.

#### 12. One-Page Summary
- **Key points:** Overflow = tokens exceed window → error or dropped content. Fix: trim / summarize / chunk.
- **Important terms:** overflow, truncation, dropped content, chunking.
- **Quick revision:** Too much in the window = crash or silent loss. Budget first.
- **Mnemonic:** **"Trim, Summarize, Chunk — or it sinks."**

> **Trainer Note:** Stress that *silent* truncation is scarier than a clean error — the app "works" but forgets. Make learners prefer explicit budgeting.

---

### 3.9 Token Limits

#### 1. Definition
**Token limits** are the **hard caps** you work within. There are two key ones: the **context window size** (the total tokens for input + output combined) and **`max_tokens`** (the cap *you* set on the length of the model's response). The window is fixed by the model; `max_tokens` is your dial. Together they bound every request. Setting `max_tokens` too low cuts answers off; too high wastes budget and risks overflow. Rate limits (tokens-per-minute) are a related account-level cap.

#### 2. Why do we need it?
Because limits are the **guardrails** that keep requests valid and costs predictable. `max_tokens` protects you from runaway, expensive responses and reserves room in the window. The window cap forces disciplined context assembly. Knowing both lets you size requests correctly instead of discovering limits through errors.

#### 3. Office Analogy
Two office rules: the **desk size** (window — set by the building) and a **page cap on each report** the consultant writes (`max_tokens` — set by you). You can't change the desk, but you *can* say "give me at most a two-page answer" to keep things fast, cheap, and fitting on the desk.

#### 4. Real-Life Analogy
A **phone plan**: a total monthly data cap (window) and a per-app limit you set to stop one app eating it all (`max_tokens`). One is fixed by the carrier; the other is your own control.

#### 5. Internal Working
1. The model defines a fixed **context window** (e.g., 200K).
2. You set **`max_tokens`** = the most output tokens allowed.
3. The system reserves `max_tokens` from the window for the reply.
4. **Input must fit in** window − `max_tokens`.
5. The model **stops generating** at `max_tokens` even mid-sentence (a "cutoff").
6. **Rate limits** (tokens/minute) may also throttle rapid requests.

#### 6. Architecture Diagram
```
   ┌──────────── CONTEXT WINDOW (fixed) ────────────┐
   │  INPUT must fit here      │  max_tokens (yours) │
   │◄──── window − max_tokens ─►│◄──── reserved ────►│
   └────────────────────────────────────────────────┘
   Too-low max_tokens → answer cut off mid-sentence
   Too-high max_tokens → wasted budget + overflow risk
   Plus: account rate limit = tokens per minute
```

#### 7. Real Example
You ask for a detailed report and set `max_tokens=100`. The answer stops abruptly after two sentences — a cutoff. You raise it to `max_tokens=1500` and the full report comes through. But if you'd loaded a 199K-token input on a 200K window, even `max_tokens=1500` overflows — you must trim the input first.

#### 8. Live Demo
```python
from core.providers import get_provider
provider = get_provider()

# 1) Too low -> cutoff
short = provider.chat([{"role":"user","content":"Explain RAG in detail."}],
                      max_tokens=30)
print(short.text)                 # stops mid-thought

# 2) Right-sized, and check we fit the window
inp = provider.count_tokens(prompt)
assert inp + 800 < provider.context_window, "trim input!"
full = provider.chat([{"role":"user","content":prompt}], max_tokens=800)
print(full.text, full.usage)
```

#### 9. Interview Questions

**Basic**
1. Name the two main token limits.
2. Which one do you set yourself?
3. What does `max_tokens` control?
4. What happens if `max_tokens` is too low?
5. Is the context window changeable by you?

**Intermediate**
1. How does `max_tokens` reserve space in the window?
2. Why can a valid `max_tokens` still overflow if input is huge?
3. What is a rate limit, and how does it differ from the window?
4. How do you choose a good `max_tokens` value?
5. What are the symptoms of a `max_tokens` cutoff?

**Scenario**
1. Answers keep cutting off mid-sentence. Fix?
2. Costs spike from overly long responses. Which limit helps?
3. You get rate-limit errors during a burst. Strategy?
4. Big input + long answer won't fit. How do you balance the two?
5. You must guarantee short answers for a widget. Setting?

#### 10. Common Mistakes
- **Setting `max_tokens` too low** — truncated answers. *Why: model stops at the cap.*
- **Setting it needlessly high** — wasted budget and overflow risk. *Why: it reserves window space.*
- **Ignoring rate limits** — burst traffic gets throttled. *Why: tokens-per-minute cap.*

#### 11. Best Practices
- **Size `max_tokens` to the task** — enough to finish, no more (**L** in CALM).
- Always check **input + max_tokens < window** before sending.
- Handle **rate-limit errors** with backoff/retry.
- Watch for **cutoffs** (unfinished output) and raise the cap when needed.

#### 12. One-Page Summary
- **Key points:** Two caps — fixed **window** and your **`max_tokens`**; plus account **rate limits**.
- **Important terms:** token limit, max_tokens, context window, rate limit, cutoff.
- **Quick revision:** Window is fixed; `max_tokens` is your dial; input + output must fit.
- **Mnemonic:** **"Window is theirs, max_tokens is yours."**

> **Trainer Note:** The cutoff demo (set `max_tokens=20`) is the fastest way to make `max_tokens` real. Then show input + max_tokens < window as the pre-flight check every request needs.

---

### Quick Recap

| # | Topic | One-line takeaway |
|---|-------|-------------------|
| 3.1 | Context | Everything you send for one request; the model has no memory of its own. |
| 3.2 | Context Window | The fixed token ceiling; **input + output share it** (~200K, up to 1M on some tiers). |
| 3.3 | Tokens | The unit of size, cost, and limits (~¾ word); `usage` reports input/output counts. |
| 3.4 | Conversation History | Past turns **re-sent every call** — memory is a resend, not a recall. |
| 3.5 | Long Context | Big inputs are powerful but costly, slow, and prone to "lost in the middle." |
| 3.6 | Context Compression | Summarize old history to fit; risk = losing detail. |
| 3.7 | Context Editing | Delete stale tool results / thinking during long tool-heavy runs. |
| 3.8 | Context Overflow | Tokens exceed the window → error or dropped content; fix: trim / summarize / chunk. |
| 3.9 | Token Limits | Fixed **window** + your **`max_tokens`** (+ rate limits) bound every request. |

**The CALM checklist for context** — carry this into every design:
```
 C  Cache      reuse stable PREFIXES (~0.1x cost on repeats;
               keep timestamps/UUIDs AFTER the cached prefix;
               verify usage.cache_read_input_tokens > 0)
 A  Assemble   load only the layers you need (selective context)
 L  Limit      count tokens, cap max_tokens, trim/summarize
 M  Manage     manage the lifecycle — compress old, edit out stale
```
Stay **CALM** and your context stays lean, cheap, and correct.


---

## Module 4 — Memory

Welcome to Module 4. Here we tackle one of the most misunderstood ideas in working with Claude: how an AI can *seem* to remember you when the model itself remembers nothing. We will slowly separate two words that look similar but mean very different things — **Context** and **Memory** — and then build up from stateless calls all the way to external memory systems like RAG.

---

### 4.1 Memory vs Context

#### 1. Definition

**Context** is everything you send to Claude in **one single API call** — the system prompt, the chat history, any documents, and the tool definitions. It is temporary: the moment the model finishes answering, that context is gone. The model does **not** keep it.

**Memory** is information you deliberately **store outside the model** (in a file or database) and **reload later** so knowledge survives across many calls and sessions. The model is stateless; "memory" is something *your application* builds around it.

The golden rule: **every memory eventually becomes context** when you load it back into a prompt.

#### 2. Why do we need it?

Beginners constantly confuse these two words and then get confused about why Claude "forgot" something. If you understand that **context = one request only** and **memory = storage you re-inject**, almost every mystery about AI forgetfulness disappears. This distinction is the foundation for everything else in this module.

#### 3. Office Analogy

Think of an employee at a desk. **Context** is the pile of papers currently on the desk for the task they are doing *right now*. When the task is done, the desk is cleared. **Memory** is the filing cabinet behind them — they walk over, pull the right folder, and place those papers back on the desk when needed. The desk is always emptied; the cabinet keeps things forever.

#### 4. Real-Life Analogy

Context is like your **short-term working memory (RAM)** — what you are actively holding in your head this second. Memory is like a **notebook or hard drive** — you write things down, close the book, and open it again tomorrow. Your brain clears; the notebook stays.

#### 5. Internal Working (numbered)

1. You collect the pieces you want Claude to see (instructions, history, documents).
2. You assemble them into **one prompt** — this is the context.
3. You send that context in a single API call.
4. Claude reads the whole context and produces an answer.
5. Claude **discards** the context; it retains nothing.
6. If you want Claude to "remember," **you** save the important bits to memory (file/DB).
7. Next time, you **retrieve** those saved bits and put them back into the new context.

#### 6. Architecture Diagram (ASCII fenced)

```
        MEMORY (durable, stored by YOU)
     +----------------------------------+
     |  files / database / vector store |
     +----------------------------------+
                |  load relevant           ^ save important
                v  pieces                  | facts
     +----------------------------------+
     |   CONTEXT (one API call only)    |
     |  system + history + docs + tools |
     +----------------------------------+
                |
                v
          +-----------+
          |  CLAUDE    |  <- stateless, keeps nothing
          +-----------+
                |
                v
             answer (context then vanishes)
```

#### 7. Real Example

You tell Claude "My name is Priya." Later in the *same* chat, it says "Sure, Priya!" — that feels like memory, but it is really just **context**: your app resent the earlier message. Close the app, start fresh tomorrow, and Claude has no idea who Priya is — unless you *saved* the name to a file and loaded it back.

#### 8. Live Demo

```python
# Context vs Memory, shown in one script
# Uses the project's provider abstraction (core.providers), never a vendor SDK directly.
from core.providers import get_provider

llm = get_provider()

# --- CONTEXT: everything for ONE call lives here ---
context = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "My name is Priya."},
]
r1 = llm.chat(context)
print(r1.text)              # "Nice to meet you, Priya!"
print(r1.usage, "$", r1.cost_usd)   # cost is first-class

# --- MEMORY: we persist the fact ourselves ---
import json, pathlib
mem = pathlib.Path("memory.json")
mem.write_text(json.dumps({"user_name": "Priya"}))   # stored OUTSIDE the model

# ...next session, brand new context...
saved = json.loads(mem.read_text())
new_context = [
    {"role": "system", "content": f"The user's name is {saved['user_name']}."},
    {"role": "user", "content": "What's my name?"},
]
r2 = llm.chat(new_context)
print(r2.text)             # "Your name is Priya." -> memory re-injected as context
```

#### 9. Interview Questions

**Basic**
1. What is context in one API call?
2. What is memory in an AI application?
3. Does the model keep context after answering?
4. Which one is temporary — context or memory?
5. Give one everyday analogy for each.

**Intermediate**
1. Why does "every memory becomes context"?
2. How is context like RAM and memory like a hard disk?
3. Where does memory physically live?
4. Who is responsible for memory — the model or the app?
5. Why can context grow expensive per call?

**Scenario**
1. A user says Claude "forgot" their name after restarting the app. Explain what happened.
2. You need Claude to recall a decision from last week. What must you build?
3. Chat history is getting huge and costly. How do you manage context lifecycle?
4. You saved 10,000 facts but a prompt only fits a few. What do you do?
5. Design a note-taking assistant that remembers preferences across sessions.

#### 10. Common Mistakes (+ why)

| Mistake | Why it's wrong |
|---|---|
| Thinking the model "remembers" chats | It is stateless; your app resends history each time |
| Confusing context with memory | Context is one-call-only; memory is durable storage |
| Dumping ALL memory into every prompt | Wastes tokens and money; only load relevant pieces |
| Assuming saved data is auto-available | You must explicitly retrieve and re-inject it |

#### 11. Best Practices

- Keep a clear line: **context = per request, memory = persisted store**.
- Store only what matters, and **retrieve selectively**.
- Summarize long history before it bloats the context.
- Always remember memory must be **re-injected** to have any effect.
- Track token usage and cost per call.

#### 12. One-Page Summary

**Context vs Memory (the table to memorize):**

| Aspect | **Context** | **Memory** |
|---|---|---|
| Scope | One API call | Across calls & sessions |
| Lifespan | Vanishes after the call | Durable / persistent |
| Analogy | RAM / desk | Hard disk / filing cabinet |
| Who holds it | Sent in the prompt | Stored by your app |
| Model retains it? | No | No (app reloads it) |
| Becomes context? | It *is* context | Yes, when reloaded |

- **Key points:** Model is stateless; context is temporary; memory is your storage; memory becomes context on reload.
- **Important terms:** context, memory, stateless, re-inject.
- **Quick revision:** Desk clears every time; cabinet keeps everything.
- **Mnemonic:** **"RAM forgets, the Notebook keeps."**

> **Trainer Note:** Spend real time here. If students leave with only one idea from Module 4, it must be: *the model remembers nothing — memory is something we build around it.*

---

### 4.2 Stateless Systems

#### 1. Definition

A **stateless system** treats every request as **completely independent**. The server keeps **no memory** of anything that happened before. Give it the same input twice and it behaves the same both times — like a pure math function. Plain **HTTP** works this way, and so does the **Claude API**: it is fundamentally stateless. It only "remembers" a conversation because you **resend the entire history** with each new request.

#### 2. Why do we need it?

Statelessness makes systems **simple, scalable, and reliable**. Any server can handle any request because none of them hold hidden state. Understanding this explains *why* you must resend chat history — and why Claude never magically recalls past chats on its own.

#### 3. Office Analogy

Imagine a help desk with a strict rule: **every clerk forgets you the instant you walk away.** To be helped, you must hand over a folder describing your whole situation every single time. Any clerk can serve you because everything they need is in the folder you carry — nothing is stored at the desk.

#### 4. Real-Life Analogy

A **vending machine**: insert coins, press a button, get a snack. It doesn't remember your last purchase or who you are. Each transaction stands entirely on its own.

#### 5. Internal Working (numbered)

1. A request arrives carrying **all** the information it needs.
2. The server processes it using only that information.
3. The server returns a response.
4. The server **forgets everything** immediately.
5. The next request must again carry everything it needs.
6. To simulate a conversation, the **client** resends prior messages each time.

#### 6. Architecture Diagram (ASCII fenced)

```
Request 1 (full history) --> [ SERVER ] --> Response 1
                              (forgets)
Request 2 (full history) --> [ SERVER ] --> Response 2
                              (forgets)
Request 3 (full history) --> [ SERVER ] --> Response 3
                              (forgets)

   No arrow connects the boxes -> no shared state.
```

#### 7. Real Example

A weather API: `GET /weather?city=Delhi` returns Delhi's weather. It doesn't matter what you asked a minute ago — same call, same behavior. Claude's API is the same: each call is judged only by the messages you send in that call.

#### 8. Live Demo

```python
from core.providers import get_provider
llm = get_provider()

# Two SEPARATE calls. The 2nd has NO knowledge of the 1st.
a = llm.chat([{"role": "user", "content": "My favorite color is green."}])
print(a.text)

b = llm.chat([{"role": "user", "content": "What is my favorite color?"}])
print(b.text)   # "I don't know" -> the server kept no state

# To make it work, the CLIENT resends history:
c = llm.chat([
    {"role": "user", "content": "My favorite color is green."},
    {"role": "assistant", "content": a.text},
    {"role": "user", "content": "What is my favorite color?"},
])
print(c.text)   # "Green." -> only because history was resent
```

#### 9. Interview Questions

**Basic**
1. What is a stateless system?
2. Is the Claude API stateful or stateless?
3. Why is HTTP called stateless?
4. What is a pure function?
5. Does a stateless server remember past requests?

**Intermediate**
1. How does a stateless API "seem" to hold a conversation?
2. Why does statelessness help scaling?
3. What must the client include in every call?
4. What are downsides of resending full history?
5. How is a vending machine stateless?

**Scenario**
1. Your chatbot forgets everything each message. What are you missing?
2. Costs rise as chats get longer. Why, and how do you fix it?
3. You load-balance across 5 servers; will conversations break? Why not?
4. A user expects Claude to recall yesterday's chat. Explain the gap.
5. Design the minimum needed to fake a stateful chat over a stateless API.

#### 10. Common Mistakes (+ why)

| Mistake | Why it's wrong |
|---|---|
| Sending only the latest message | Server has no earlier context; it "forgets" |
| Expecting the API to store chats | It is stateless by design |
| Ignoring growing history cost | Every resend adds tokens and money |
| Relying on server "sessions" | Claude keeps none; state lives with the client |

#### 11. Best Practices

- Treat each call as **self-contained** — include what it needs.
- **Resend** relevant history to maintain a conversation.
- Trim or summarize history to control cost.
- Never assume hidden server-side memory.
- Log inputs so you can reproduce any call.

#### 12. One-Page Summary

- **Key points:** Each request is independent; server keeps no state; Claude API is stateless; client resends history.
- **Important terms:** stateless, pure function, HTTP, resend history.
- **Quick revision:** No memory at the server — you carry the folder every time.
- **Mnemonic:** **"Vending machine: coin in, snack out, no memory."**

> **Trainer Note:** Emphasize that statelessness is a *feature*, not a flaw — it is what makes Claude scalable. Statefulness is something we add on top.

---

### 4.3 Stateful Systems

#### 1. Definition

A **stateful system tracks information across interactions**. It remembers what happened before, so later requests build on earlier ones — like a **logged-in session** or a **database-backed app**. Since Claude itself is stateless, **you** make it *feel* stateful by **storing and reloading state yourself** between calls. The state lives in your application, not inside the model.

#### 2. Why do we need it?

Real assistants need continuity: to remember your name, your task, your last decision. Statefulness gives users a smooth, connected experience instead of starting from zero every message. It is how a raw stateless API turns into a helpful, ongoing assistant.

#### 3. Office Analogy

A **personal assistant who keeps your file open**. Every time you speak, they glance at your file, add new notes, and respond with full awareness of your history. The file (state) is maintained by the assistant's system — not by your memory.

#### 4. Real-Life Analogy

**Logging into your email.** The site remembers you are signed in, your inbox, your drafts. It maintains a **session** so each click continues where you left off, rather than asking you to log in again every time.

#### 5. Internal Working (numbered)

1. A request comes in tied to a **session or user ID**.
2. The app **loads saved state** for that session.
3. The app **merges** new input with the loaded state.
4. It builds the context (state + new message) and calls Claude.
5. Claude replies using the full picture.
6. The app **updates and saves** the state for next time.

#### 6. Architecture Diagram (ASCII fenced)

```
  User msg --> [ APP ]
                 |  1. load state (by session id)
                 v
            +---------+      +-----------------+
            |  STATE  |<---->|  build context  |--> [CLAUDE] --> reply
            |  store  |      +-----------------+
            +---------+  2. save updated state
                 ^_______________|
             (state carries across turns)
```

#### 7. Real Example

A support chatbot on a website. It knows your order number, your previous questions, and where the conversation stands — because the app stores that session state and reloads it on every message. Claude only sees it because the app rebuilds the context each turn.

#### 8. Live Demo

```python
from core.providers import get_provider
llm = get_provider()

# A tiny stateful wrapper: WE hold the state (history) in memory.
class Session:
    def __init__(self):
        self.history = []          # this is the "state"
    def ask(self, text):
        self.history.append({"role": "user", "content": text})
        r = llm.chat(self.history)  # full state -> context
        self.history.append({"role": "assistant", "content": r.text})
        return r.text

s = Session()
print(s.ask("My name is Priya."))
print(s.ask("What's my name?"))   # "Priya" -> app kept the state
```

#### 9. Interview Questions

**Basic**
1. What is a stateful system?
2. Give one example of stateful software.
3. Is Claude naturally stateful?
4. What is a session?
5. Where does the state live in a Claude app?

**Intermediate**
1. How do you make a stateless API feel stateful?
2. What's the difference between state and context here?
3. Why tie state to a session or user ID?
4. What must happen after each reply to stay stateful?
5. Compare stateful vs stateless in one line.

**Scenario**
1. Two users share one global history and see each other's data. What's the bug?
2. State grows too large per turn. How do you keep it manageable?
3. Your app restarts and all sessions vanish. What kind of memory do you need next?
4. A user switches devices and loses their chat. How would you fix continuity?
5. Design session state for a multi-user helpdesk bot.

#### 10. Common Mistakes (+ why)

| Mistake | Why it's wrong |
|---|---|
| One shared history for all users | Sessions must be isolated per user ID |
| Forgetting to save state after a reply | Next turn loses continuity |
| Keeping state only in RAM | It disappears on restart (need persistence) |
| Loading state but never trimming it | Context bloats and costs rise |

#### 11. Best Practices

- Key all state by a **unique session/user ID**.
- **Save after every turn**, load before every turn.
- Isolate users — never mix sessions.
- Trim or summarize state to stay affordable.
- For durability across restarts, back state with persistent storage (next topic).

#### 12. One-Page Summary

- **Key points:** Stateful tracks across turns; Claude is stateless so the app holds state; load-merge-save each turn; key by session.
- **Important terms:** stateful, session, state store, user ID.
- **Quick revision:** App loads state, calls Claude, saves state — repeat.
- **Mnemonic:** **"Login remembers you — the APP holds the session."**

> **Trainer Note:** Draw the "load → build → call → save" loop on the board. Students should see statefulness as a *loop the app runs*, not a model feature.

---

### 4.4 Persistent Memory

#### 1. Definition

**Persistent memory** means facts saved **durably** — to **files or a database** — so they **survive process restarts and future sessions**. Think user preferences, past decisions, and project facts written to disk and reloaded when relevant. Unlike RAM-only state (which dies when the app stops), persistent memory lives on. **Claude Code**, for example, uses a **CLAUDE.md** project memory file plus a file-based memory directory.

#### 2. Why do we need it?

In-memory state vanishes the moment your program stops. Persistent memory keeps knowledge alive for **tomorrow, next week, and across restarts**. It lets an assistant genuinely "know" you over time, remember project rules, and avoid re-asking the same questions.

#### 3. Office Analogy

The **filing cabinet that stays overnight**. Even when everyone goes home and the lights turn off, the folders remain. Tomorrow anyone can open the cabinet and continue exactly where things left off. Sticky notes on a desk (RAM) get cleared; the cabinet (disk) endures.

#### 4. Real-Life Analogy

**Saving a document.** If you only type in an unsaved editor and the power cuts, it's gone. Once you hit **Save** to disk, the file survives shutdowns and reopens later exactly as stored.

#### 5. Internal Working (numbered)

1. The app identifies a fact worth keeping (a preference, a decision).
2. It **writes** that fact to durable storage (file or database).
3. The process can stop, crash, or restart — the fact remains.
4. Later, the app **reads** the relevant facts back.
5. It **injects** them into the new context.
6. Claude answers with knowledge that outlived the original session.

#### 6. Architecture Diagram (ASCII fenced)

```
   Session A                     Session B (days later)
   +--------+                    +--------+
   |  APP    | --write--> DISK   |  APP    |
   +--------+           +------+ +--------+
        |               | file | ^   |
        |               |  DB  |-+   | read relevant
     save fact -------> +------+     v
                         (survives   build context --> [CLAUDE]
                          restart)
```

#### 7. Real Example

**Claude Code** reads a **CLAUDE.md** file in your project each session. It contains conventions, layout, and commands — so the assistant "remembers" your project's rules every time, even after your machine reboots. That file *is* persistent memory on disk.

#### 8. Live Demo

```python
import json, pathlib
from core.providers import get_provider
llm = get_provider()

STORE = pathlib.Path("user_memory.json")

def remember(key, value):
    data = json.loads(STORE.read_text()) if STORE.exists() else {}
    data[key] = value
    STORE.write_text(json.dumps(data))     # durable on disk

def recall():
    return json.loads(STORE.read_text()) if STORE.exists() else {}

remember("prefers", "short answers")       # saved once...

# ...even after a full restart, this still works:
prefs = recall()
ctx = [
    {"role": "system", "content": f"User preferences: {prefs}"},
    {"role": "user", "content": "Explain gravity."},
]
print(llm.chat(ctx).text)   # respects saved preference
```

#### 9. Interview Questions

**Basic**
1. What is persistent memory?
2. Name two places to store it.
3. What survives a restart — RAM state or disk state?
4. What file does Claude Code use for project memory?
5. Why isn't in-memory state persistent?

**Intermediate**
1. How do save and load work together?
2. Difference between session state and persistent memory?
3. Why store user preferences durably?
4. What happens if you save but never reload?
5. When is a file enough vs when do you need a database?

**Scenario**
1. Your app forgets preferences after every restart. What's missing?
2. Two users' preferences overwrite each other in one file. Fix it.
3. Stored facts grow endlessly. How do you keep only the useful ones?
4. You must remember a decision made three months ago. How?
5. Design persistent memory for a coding assistant's project rules.

#### 10. Common Mistakes (+ why)

| Mistake | Why it's wrong |
|---|---|
| Keeping "memory" only in RAM | Lost on restart — not persistent |
| Saving but never reloading | Stored data has zero effect on answers |
| One file for all users | Data collides and overwrites |
| Storing everything forever | Grows unmanageable; store what's relevant |

#### 11. Best Practices

- Write important facts to **disk or a database** promptly.
- Separate storage **per user/project** (avoid collisions).
- Reload only the **relevant** facts into context.
- Prune or summarize old memory to keep it useful.
- Treat memory files (like CLAUDE.md) as living, versioned documents.

#### 12. One-Page Summary

- **Key points:** Persistent memory survives restarts; stored in files/DB; save-then-reload; Claude Code uses CLAUDE.md.
- **Important terms:** persistent memory, disk, database, CLAUDE.md.
- **Quick revision:** Save to disk today, reload it tomorrow.
- **Mnemonic:** **"Hit Save, and it survives."**

> **Trainer Note:** Point students to this very project's CLAUDE.md as a real, living example of persistent memory they can open and read.

---

### 4.5 External Memory

#### 1. Definition

**External memory** means storing knowledge **outside the context window** and retrieving **only the relevant pieces on demand**. Tools include **vector databases / RAG (Retrieval-Augmented Generation)**, key-value stores, and files. It solves two hard limits — the **finite context window** and **stale knowledge**: store everything externally, then fetch just what each question needs. This keeps prompts small, cheap, and fresh.

#### 2. Why do we need it?

A context window can only hold so much, and the model's built-in knowledge has a cutoff date. External memory lets you keep **unlimited, up-to-date knowledge** outside the model and pull in **only the slice** relevant to the current query — instead of stuffing everything (impossible) into one prompt.

#### 3. Office Analogy

A **giant library with a smart librarian**. You don't carry every book to your desk. You ask a question; the librarian fetches the **few exact pages** you need and hands them over. The library (external store) is huge; your desk (context) stays light.

#### 4. Real-Life Analogy

**Searching the web.** You don't memorize the internet. You type a query, get the most relevant results, and read just those. The knowledge lives outside your head; you retrieve on demand.

#### 5. Internal Working (numbered)

1. Break your knowledge into small chunks and store them externally.
2. For vector search, convert each chunk into an **embedding** (a number vector) in a **vector DB**.
3. A user asks a question.
4. Convert the question into an embedding too.
5. **Retrieve** the chunks most similar to the question.
6. Inject only those chunks into the context and call Claude (this is **RAG**).
7. Claude answers grounded in the freshly retrieved, relevant knowledge.

#### 6. Architecture Diagram (ASCII fenced)

```
   Big knowledge base            Question
   +------------------+             |
   | vector DB / files|             v
   | (all chunks)      |     +--------------+
   +------------------+     | 1. embed query|
            ^  2. similarity +--------------+
            |     search           |
            +----- retrieve top-k --+
                       |
                       v
            +---------------------+
            | context = query +    |--> [CLAUDE] --> grounded answer
            | ONLY relevant chunks |
            +---------------------+
```

#### 7. Real Example

A company help bot backed by 5,000 pages of docs. You can't fit 5,000 pages in one prompt. Instead, the docs live in a **vector database**; when a user asks "How do I reset my password?", the system retrieves the 3 most relevant paragraphs and gives Claude just those. Fast, cheap, and accurate.

#### 8. Live Demo

```python
from core.providers import get_provider
llm = get_provider()

# Toy "external memory": a tiny store + naive keyword retrieval.
KB = {
    "password": "To reset your password, go to Settings > Security > Reset.",
    "refund":   "Refunds are processed within 5 business days.",
    "hours":    "Support is available 9am-6pm, Monday to Friday.",
}

def retrieve(question):                 # pick only relevant chunk(s)
    return [v for k, v in KB.items() if k in question.lower()]

q = "How do I reset my password?"
chunks = retrieve(q)                    # -> just the password entry
ctx = [
    {"role": "system", "content": "Answer using ONLY these notes: " + " ".join(chunks)},
    {"role": "user", "content": q},
]
print(llm.chat(ctx).text)   # grounded, and we sent almost no tokens
```

#### 9. Interview Questions

**Basic**
1. What is external memory?
2. What does RAG stand for?
3. What is a vector database?
4. Why not put all knowledge in one prompt?
5. What is the context window limit problem?

**Intermediate**
1. What is an embedding?
2. How does similarity search find relevant chunks?
3. How does RAG keep answers fresh?
4. Why chunk documents before storing them?
5. Compare external memory vs persistent memory.

**Scenario**
1. Your docs are 10,000 pages. How do you let Claude use them?
2. Answers are outdated after a policy change. How does external memory help?
3. Retrieval returns irrelevant chunks. What might be wrong?
4. Costs spike from huge prompts. How does RAG reduce them?
5. Design a support bot over a large, frequently-updated knowledge base.

#### 10. Common Mistakes (+ why)

| Mistake | Why it's wrong |
|---|---|
| Stuffing all data into one prompt | Exceeds context window; expensive and slow |
| Retrieving too many chunks | Adds noise and cost; keep top-k small |
| Never updating the store | Answers go stale; refresh the knowledge base |
| Poor chunking (too big/small) | Retrieval misses the right piece |

#### 11. Best Practices

- Store knowledge **externally**, retrieve **only what's relevant**.
- Chunk documents thoughtfully (coherent, right-sized pieces).
- Keep the store **fresh**; update it as facts change.
- Limit to the **top-k** most relevant chunks per query.
- Cite or ground answers in the retrieved chunks to reduce errors.

#### 12. One-Page Summary

- **Key points:** External memory keeps knowledge outside the window; RAG retrieves relevant chunks on demand; solves finite-context and freshness limits.
- **Important terms:** external memory, RAG, vector database, embedding, retrieval, top-k.
- **Quick revision:** Store everything outside; fetch only what each query needs.
- **Mnemonic:** **"Librarian fetches only the page you need."**

> **Trainer Note:** Tie this back to the CALM framework's *Manage lifecycle* idea — clear, summarize, and persist context over time so it never overflows.

---

### Quick Recap

Module 4 is really one big idea seen from five angles: **the model remembers nothing; memory is what we build around it.**

**The distinction to lock in — Context vs Memory:**

| | **Context** | **Memory** |
|---|---|---|
| What | Everything in ONE API call | Info stored outside the model |
| Lifespan | Vanishes after the call | Durable across sessions |
| Analogy | RAM / desk | Hard disk / filing cabinet |
| Held by | The prompt you send | Your application (file/DB) |
| Rule | It *is* context | Becomes context when reloaded |

**Topic-by-topic:**

- **4.1 Memory vs Context** — Context = temporary per-request working memory; Memory = deliberately stored, re-injected knowledge. Every memory becomes context on reload.
- **4.2 Stateless Systems** — Each request is independent; the Claude API keeps no state; you resend history to fake continuity.
- **4.3 Stateful Systems** — The *app* holds state per session: load → build → call → save, every turn.
- **4.4 Persistent Memory** — Save facts to disk/DB so they survive restarts (e.g., CLAUDE.md).
- **4.5 External Memory** — Keep knowledge outside the window; use RAG/vector DBs to retrieve only the relevant pieces on demand.

**One mnemonic for the whole module:** **"RAM forgets, the Notebook keeps — so we save, reload, and retrieve."**


---

## Module 5 — Tool Use

Claude is brilliant with words, but on its own it only produces text — it can't check today's weather, run code, or look inside your database. **Tools** are the bridge that connect Claude to the real world. This module explains, step by step, how Claude asks for a tool, how *your* code runs it, and how the answer flows back.

---

### 5.1 What are Tools?

#### 1. Definition

A **tool** is a capability you hand to Claude so it can do something it cannot do with words alone. Examples: fetch live data, call an API, run code, query a database, do exact math, or send an email. The important idea: **the model itself only produces text.** Tools connect that text-only brain to real actions in the outside world. You describe the tools; Claude decides *when* to use one and *what* to ask for; **your application actually runs it.**

#### 2. Why do we need it?

Claude is trained on data up to a point in time, and it lives inside a conversation — it has no hands. Ask it "What's the weather in Paris *right now*?" and it simply cannot know; there is no live internet inside the model. Ask it to multiply two 15-digit numbers and it may guess wrong, because it predicts text rather than calculating. Tools fix both problems. They let Claude reach out for **fresh, exact, real-world information and actions** instead of inventing an answer.

#### 3. Office Analogy

Imagine a **very smart manager** sitting in an office with no phone and no computer. The manager can reason, plan, and write beautiful memos — but cannot personally check the warehouse stock or send a courier. So the manager writes a note: *"Please look up how many blue chairs are in stock."* An **assistant** takes the note, walks to the warehouse, counts, and brings back the number. The manager then finishes the memo. Claude is the manager; the **tool** is the assistant; **your code** is what carries the notes back and forth.

#### 4. Real-Life Analogy

Think of a **TV quiz-show contestant** who is allowed a "phone a friend" lifeline. The contestant is smart but doesn't know everything. When stuck, they don't guess — they *ask to call someone*. The show's host dials the number, the friend answers, and the answer comes back so the contestant can respond. The contestant never dials the phone themselves. Claude is the contestant; the tool is the friend on the phone; the host (your app) makes the actual call.

#### 5. Internal Working (numbered)

1. **You** send Claude the user's message **plus** a list of available tools (their names and what they do).
2. **Claude reads** the request and decides: can I answer with words alone, or do I need a tool?
3. If a tool is needed, **Claude asks for it** by returning a special "use this tool" request with the arguments filled in. It does **not** run the tool.
4. **Your code** receives that request, runs the real tool (calls the API, queries the DB, etc.).
5. **You send the result back** to Claude.
6. **Claude reads the result** and writes the final answer for the user — or asks for another tool. This repeats as a **loop**.

#### 6. Architecture Diagram (ASCII fenced)

```
        +-----------+        "I need the weather tool"        +-------------+
User -->|   YOUR    |--- message + tool list -------------->  |             |
        |   APP     |                                         |   CLAUDE    |
        |  (code)   |<-- "please run get_weather(Paris)" ----|  (text only)|
        +-----------+                                         +-------------+
             |                                                       ^
             | runs the real tool                                   |
             v                                                       |
        +-----------+                                                |
        |  WEATHER  |  result: "18C, sunny"                          |
        |    API    |------------------------------------------------+
        +-----------+           app sends result back to Claude

  KEY IDEA: Claude only ASKS. Your app RUNS the tool and returns the answer.
```

#### 7. Real Example

A travel chatbot is asked: *"Should I bring an umbrella to London tomorrow?"* Claude cannot know tomorrow's forecast. So it asks for a `get_forecast` tool with `{ "city": "London", "day": "tomorrow" }`. The app calls a real weather service, gets back `"70% chance of rain"`, and sends that to Claude. Claude then replies: *"Yes — there's a 70% chance of rain in London tomorrow, so pack an umbrella."* Without the tool, Claude could only guess.

#### 8. Live Demo

```python
# demo_tools_intro.py — conceptual walk-through (pseudo-code)
from core.providers import LLMProvider   # provider-agnostic (see CLAUDE.md)

# 1) Describe ONE tool to Claude
tools = [{
    "name": "get_weather",
    "description": "Get the current weather for a city.",
    "input_schema": {
        "type": "object",
        "properties": {"city": {"type": "string"}},
        "required": ["city"],
    },
}]

# 2) Ask a question that needs live data
reply = LLMProvider.chat(
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=tools,
)

# 3) Claude does NOT answer directly — it asks for the tool:
#    reply -> tool_use: get_weather(city="Paris")
print(reply)   # shows a 'tool_use' request, not a final answer

# Your code would then run the real weather API and send the result back.
```

Run it (any topic follows the same pattern):

```bash
python topics/05-tool-use/demo.py
```

#### 9. Interview Questions

**Basic**
1. In one sentence, what is a tool in the context of Claude?
2. Does Claude run tools by itself? Who runs them?
3. Give two things Claude *cannot* do without tools.
4. Why does the model only produce text?
5. Name three example tools.

**Intermediate**
1. Walk through the six steps from user message to final answer.
2. Why is sending a "tool list" important — what happens if you forget it?
3. How do tools help with the model's knowledge cutoff?
4. Why is doing exact math a good use case for a tool?
5. What is the difference between Claude *deciding* to use a tool and *executing* it?

**Scenario**
1. A user asks for today's stock price and Claude answers with an old number. What went wrong?
2. Your chatbot must send emails. Should Claude send them directly? How would you design it?
3. A tool exists but Claude never uses it. Where would you look first?
4. You want Claude to look up an order in your database. Sketch the flow.
5. A teammate says "let's let Claude run any command it wants." Why is that risky?

#### 10. Common Mistakes (+ why)

- **Expecting Claude to run the tool itself.** It only *asks*; your code must execute it. *Why: the model has no hands — forgetting this breaks the whole loop.*
- **Not sending the tool list.** No list means Claude can't ask for a tool. *Why: it can only choose from what you offer.*
- **Trusting a guessed answer for live data.** Without a tool, "today's price" is a guess. *Why: the model has no live feed.*
- **Giving Claude one giant do-everything tool.** *Why: vague, hard to use, and hard to secure.*

#### 11. Best Practices

- **One tool = one clear job** (many small tools beat one big one).
- Apply **least-privilege** (SPIDER: *Isolate*): give only the tools that task truly needs.
- **Always validate** what a tool returns before trusting it (SPIDER: *Detect*).
- Keep the human in control for risky actions (sending money, deleting data).
- Write tools so a beginner could understand what each one does at a glance.

#### 12. One-Page Summary

- **Key points:** Tools connect text-only Claude to the real world. Claude *asks*; your app *runs*. Used for live data, APIs, code, DBs, exact math, email.
- **Important terms:** tool, model, text-only, capability, least-privilege.
- **Quick revision:** Model = brain with no hands. Tool = the hands. Your code = the messenger.
- **Mnemonic:** **"Claude ASKS, your App ACTS."**

> **Trainer Note:** Spend real time on the single idea "Claude never runs the tool." Almost every later confusion traces back to students thinking the model executes code. Draw the diagram twice.

---

### 5.2 Function Calling

#### 1. Definition

**Function calling** (also called **tool use**) is the back-and-forth *process* that lets Claude use a tool. You send a message plus tool definitions; Claude replies with a **`tool_use`** block (tool name + JSON arguments) when it wants one; **your code runs the function** and returns the answer as a **`tool_result`**; Claude reads it and continues. It is a **loop** — Claude may call several tools in a row before giving a final answer.

#### 2. Why do we need it?

A tool is useless without a reliable *procedure* for using it. Function calling is that procedure. It gives everyone — Claude and your code — a shared, predictable dance: *ask → run → return → continue.* Without a defined loop, you'd never know when Claude wants a tool, what arguments to use, or where to put the answer. Function calling turns "Claude is smart" into "Claude can actually get real work done, safely and step by step."

#### 3. Office Analogy

The manager (Claude) and the assistant (your app) follow an **office procedure**. Manager writes a request form (`tool_use`) with a **reference number**. The assistant does the task and staples the reply to a **matching form** (`tool_result`) carrying the same reference number, so nobody mixes up which answer belongs to which request. The manager reads the reply and either finishes the report or fills out **another form**. Same paperwork, every time — that's the loop.

#### 4. Real-Life Analogy

Ordering at a **restaurant**. You (Claude) tell the **waiter** (your app) what you want. The waiter carries the order to the **kitchen** (the tool), waits, and brings the food back to your table. You taste it and maybe order dessert — another round. You never walk into the kitchen yourself; you just keep sending orders through the waiter until the meal is done.

#### 5. Internal Working (numbered)

1. You send the user message **+ tool definitions**.
2. Claude returns either a normal answer **or** a **`tool_use`** block: `{ name, input(JSON args), id }`.
3. If it's `tool_use`, **your code runs** that function with those arguments.
4. You send Claude a **`tool_result`** message referencing the same **`tool_use_id`**.
5. Claude reads the result and **either** produces the final answer **or** emits another `tool_use`.
6. Repeat 2–5 until Claude gives a final text answer. Add a **loop cap** (`max_iters`) so it can't loop forever.

#### 6. Architecture Diagram (ASCII fenced)

```
   +--------+   1. user msg + tools    +---------+
   |  USER  |------------------------->|         |
   +--------+                          | CLAUDE  |
                                       |         |
   +----------------+  2. tool_use     |         |
   |    YOUR APP    |<-----------------|  (loop) |
   |                |  (name+args+id)  |         |
   |  3. run func   |                  |         |
   |  4. tool_result|----------------->|         |
   +----------------+  (same id)       +---------+
          ^                                 |
          |     5. final answer OR          |
          +------- another tool_use <-------+
                   (repeat = the loop)
```

#### 7. Real Example

A support bot is asked *"Where is my order #A17?"* Turn 1: Claude emits `tool_use: lookup_order(order_id="A17")`. Your code queries the database and returns `tool_result: {status:"shipped", eta:"Friday"}`. Turn 2: Claude reads it and may emit a *second* `tool_use: get_tracking(carrier="UPS")`. Your code returns the tracking link. Turn 3: Claude writes the final reply combining both. Two tool calls, one smooth loop.

#### 8. Live Demo

```python
# demo_function_calling.py — the tool loop
from core.providers import LLMProvider

messages = [{"role": "user", "content": "What's the weather in Paris?"}]

for step in range(5):                       # max_iters = 5 (loop cap!)
    reply = LLMProvider.chat(messages=messages, tools=tools)

    if reply.stop_reason != "tool_use":     # Claude gave a final answer
        print("FINAL:", reply.text)
        break

    # Claude asked for a tool -> WE run it
    call = reply.tool_use                    # {id, name, input}
    result = run_local_tool(call.name, call.input)   # your real function

    messages.append(reply.as_message())      # record Claude's request
    messages.append({                        # send the answer back
        "role": "user",
        "content": [{
            "type": "tool_result",
            "tool_use_id": call.id,           # MUST match!
            "content": str(result),
        }],
    })
```

#### 9. Interview Questions

**Basic**
1. What is function calling in one sentence?
2. What does a `tool_use` block contain?
3. Who runs the function — Claude or your code?
4. What message type do you send the answer back in?
5. Why is it called a "loop"?

**Intermediate**
1. What is `stop_reason` and how do you use it to end the loop?
2. Why must the `tool_result` reference the `tool_use_id`?
3. What is `max_iters` and why does it matter?
4. Can Claude call more than one tool before answering? Explain.
5. What happens if you never send the `tool_result` back?

**Scenario**
1. Your loop never stops. What are two likely causes?
2. Claude calls a second tool you didn't expect. Is that a bug? Why or why not?
3. You forgot to append Claude's `tool_use` to the message history. What breaks?
4. A tool takes 30 seconds. How does the loop handle the wait?
5. You want to log every tool Claude calls. Where in the loop do you add it?

#### 10. Common Mistakes (+ why)

- **No loop cap.** Claude can bounce forever. *Why: some tasks chain many calls; `max_iters` is your safety net.*
- **Mismatched or missing `tool_use_id`.** *Why: Claude can't tell which answer belongs to which request.*
- **Forgetting to append Claude's request to history.** *Why: the conversation loses context and the loop desyncs.*
- **Treating every reply as a final answer.** *Why: you must check `stop_reason` first.*

#### 11. Best Practices

- Always **check `stop_reason`** before reading the text.
- Set a sensible **`max_iters`** cap (SPIDER: *Recover*).
- **Echo the exact `tool_use_id`** in every result.
- **Log each tool call** for debugging and cost tracking.
- Keep tool functions **fast and independent** where possible.

#### 12. One-Page Summary

- **Key points:** Function calling = the ask→run→return→continue loop. `tool_use` out, `tool_result` in, matched by id. Cap the loop.
- **Important terms:** function calling, `tool_use`, `tool_result`, `tool_use_id`, `stop_reason`, `max_iters`.
- **Quick revision:** Ask, run, return, repeat — until a final answer.
- **Mnemonic:** **"ARRR"** — **A**sk, **R**un, **R**eturn, **R**epeat.

> **Trainer Note:** Have students trace one full loop on the whiteboard with sticky notes for each message. Physically matching a `tool_use_id` sticky to its `tool_result` sticky makes the "id must match" rule unforgettable.

---

### 5.3 Tool Schema

#### 1. Definition

A **tool schema** is the *definition card* you give Claude for each tool. It has three parts: a **`name`** (what the tool is called), a **`description`** (what it does and *when* to use it — Claude reads this to decide), and an **`input_schema`** (a **JSON Schema** listing the parameters, their types, and which are required). Good names and descriptions are the single biggest factor in whether Claude picks the *right* tool at the *right* time.

#### 2. Why do we need it?

Claude can only use what it understands. The schema is how Claude *learns* a tool exists, what it's for, and how to fill in the arguments correctly. A vague description like *"does stuff with data"* leaves Claude guessing; a clear one like *"Look up a customer's order status by order ID"* makes the choice obvious. The `input_schema` also acts as a **contract**: it tells Claude the exact shape of arguments to send, so your code receives clean, predictable input.

#### 3. Office Analogy

Think of the **tool catalog** in an office supply room. Each item has a **label** (name), a **note explaining what it's for** (description), and a **form specifying what info to fill in** to request it (input_schema). If the label is clear and the note is helpful, the manager grabs the right item instantly. If the label just says "Box #4," nobody knows when to use it. Your schema is that catalog entry.

#### 4. Real-Life Analogy

A **recipe card**. The title (name) tells you the dish. The short blurb (description) tells you *when* you'd make it ("a quick weeknight dinner"). The ingredients list (input_schema) says exactly what you need and how much — 2 eggs (required), a pinch of salt (optional). A well-written card means anyone can follow it; a sloppy one leads to a ruined meal.

#### 5. Internal Working (numbered)

1. You write a schema for each tool: `name`, `description`, `input_schema`.
2. You send all schemas alongside the user message.
3. Claude reads each **description** to judge which tool (if any) fits the request.
4. Claude reads the **input_schema** to know what arguments to build and their types.
5. Claude fills the arguments as **JSON** matching that schema, marking required fields.
6. Your code receives arguments already shaped to the contract — easy to validate and run.

#### 6. Architecture Diagram (ASCII fenced)

```
   TOOL SCHEMA (the "definition card")
   +-----------------------------------------------+
   | name:        "get_weather"                    |  <- what it's called
   | description: "Get current weather for a city. |  <- WHEN to use it
   |               Use when the user asks about     |     (Claude reads this)
   |               live weather conditions."        |
   | input_schema:                                  |
   |   { type: object,                              |  <- shape of arguments
   |     properties: { city: {type: string} },      |
   |     required: [ "city" ] }                      |  <- must be provided
   +-----------------------------------------------+
                     |
                     v
        Claude reads it and asks:  get_weather(city="Paris")
```

#### 7. Real Example

Compare two descriptions for the same tool:

| Field | Weak version | Strong version |
|---|---|---|
| name | `data1` | `search_products` |
| description | "handles data" | "Search the product catalog by keyword; use when the user is shopping or asks if we sell something." |
| input_schema | none (Claude guesses) | `{keyword: string (required), max_results: integer}` |
| Result | Claude picks it randomly or not at all | Claude picks it correctly and sends clean arguments |

The strong version costs a few extra minutes to write and saves hours of debugging.

#### 8. Live Demo

```python
# demo_tool_schema.py — a well-written schema
search_products = {
    "name": "search_products",
    "description": (
        "Search the product catalog by keyword. "
        "Use when the user is shopping or asks whether we sell an item."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "keyword":     {"type": "string",  "description": "What to search for"},
            "max_results": {"type": "integer", "description": "How many to return"},
        },
        "required": ["keyword"],          # keyword MUST be provided
    },
}

# Send it and watch Claude fill the arguments correctly:
reply = LLMProvider.chat(
    messages=[{"role": "user", "content": "Do you sell running shoes?"}],
    tools=[search_products],
)
# -> tool_use: search_products(keyword="running shoes")
```

#### 9. Interview Questions

**Basic**
1. What three parts make up a tool schema?
2. Which part does Claude use to decide *when* to call a tool?
3. What is `input_schema` written in?
4. What does `required` mean in a schema?
5. Why does a good `name` matter?

**Intermediate**
1. Why is the description "the most important field"?
2. How does `input_schema` act as a contract?
3. What happens if two tools have very similar descriptions?
4. Should optional parameters be in `required`? Why not?
5. How do parameter `type`s help your code?

**Scenario**
1. Claude keeps calling the wrong tool. What do you fix first?
2. Claude sends a number as text ("5" not 5). What schema fix helps?
3. You add a new tool but Claude ignores it. Likely cause?
4. A tool needs an email address argument. How do you make sure Claude sends one?
5. Two tools do similar things. How do you help Claude choose?

#### 10. Common Mistakes (+ why)

- **Vague descriptions.** *Why: Claude decides from the description — vague in, wrong tool out.*
- **Missing `required` fields.** *Why: Claude may omit arguments your code depends on.*
- **Wrong or missing types.** *Why: you get messy input that's hard to validate.*
- **Cryptic names like `func1`.** *Why: names guide selection; unclear names confuse the model.*

#### 11. Best Practices

- Write the **description as if teaching a new intern** — say *what* and *when*.
- Name tools with clear **verb_noun** style (`send_email`, `get_order`).
- Mark truly **required** fields and describe each parameter.
- Keep each tool's job **distinct** so descriptions don't overlap.
- Test with real questions and check Claude picks the right tool.

#### 12. One-Page Summary

- **Key points:** Schema = name + description + input_schema. Description drives selection; input_schema is the argument contract (JSON Schema).
- **Important terms:** tool schema, name, description, input_schema, JSON Schema, required.
- **Quick revision:** Good name + good description = right tool, right arguments.
- **Mnemonic:** **"NDI"** — **N**ame, **D**escription, **I**nput_schema.

> **Trainer Note:** Run a live experiment: give Claude the "weak" schema, then the "strong" one, for the same question. Watching it fail then succeed teaches the value of a good description faster than any lecture.

---

### 5.4 Tool Results

#### 1. Definition

A **tool result** is how you hand a tool's output back to Claude. After your code runs a tool, you send a **`tool_result`** block tied to the original **`tool_use_id`**, so Claude knows which request it answers. A result can also carry **`is_error: true`** to signal that the tool *failed* — letting Claude react, retry, or explain the problem instead of pretending it worked. Always **validate** a result before you trust it.

#### 2. Why do we need it?

The loop is only complete when Claude *sees* the answer. The `tool_result` is that answer, delivered in a form Claude understands and correctly matched to the request. Without the matching **id**, Claude can't tell which answer goes with which question. And without an **error signal**, a failed tool (network down, no record found) would look like success — and Claude would build a confident, wrong answer on top of it. Tool results close the loop *safely*.

#### 3. Office Analogy

The assistant returns to the manager's desk and staples the reply to the **exact request form** (same reference number) so it's clear which task it answers. If the warehouse was locked and the count couldn't be done, the assistant attaches a big red **"FAILED — try again later"** note instead of a fake number. The manager reads the note and adjusts — maybe asks the assistant to retry, maybe tells the customer to wait.

#### 4. Real-Life Analogy

You text a friend *"What time does the pharmacy close?"* They reply *"9 PM"* — that's a good result, and you trust it. But if they reply *"Not sure, the website is down,"* that's an **error result**. You don't invent a closing time; you plan around the uncertainty. Same for Claude: a clear error beats a confident guess.

#### 5. Internal Working (numbered)

1. Your code runs the tool Claude asked for.
2. You capture the output (a value, JSON, text, etc.).
3. You **validate** it — is it the right shape? Did it actually work?
4. You build a **`tool_result`** block with the matching **`tool_use_id`**.
5. If the tool failed, set **`is_error: true`** and include a short message.
6. You send it to Claude; Claude reads it and continues — using a success normally, or reacting to an error (retry / explain).

#### 6. Architecture Diagram (ASCII fenced)

```
   Claude asked:  tool_use  id=abc123  get_weather(city="Paris")
                                |
                                v
   +-----------------------------------------------+
   |  YOUR APP runs the tool, then validates        |
   +-----------------------------------------------+
        |                                   |
   SUCCESS                              FAILURE
        v                                   v
   tool_result                        tool_result
   id=abc123                          id=abc123
   content="18C, sunny"               is_error: true
   is_error: false                    content="API timed out"
        \                                 /
         \                               /
          v                             v
   +-----------------------------------------------+
   |  CLAUDE reads result (matched by id):          |
   |   - success -> use it in the final answer      |
   |   - error   -> retry OR explain the problem    |
   +-----------------------------------------------+
```

#### 7. Real Example

A banking bot calls `get_balance(account="123")`. The database is briefly down, so the call fails. Your code returns `tool_result { tool_use_id: "...", is_error: true, content: "Balance service unavailable" }`. Claude reads the error and replies: *"I'm sorry, I can't reach your balance right now — please try again in a moment."* — instead of inventing a fake balance. That honesty is only possible because you flagged the error.

#### 8. Live Demo

```python
# demo_tool_results.py — returning success and error results
def make_tool_result(call, run_fn):
    try:
        output = run_fn(call.name, call.input)   # run the real tool
        if not is_valid(output):                 # VALIDATE before trusting
            raise ValueError("bad output shape")
        return {
            "type": "tool_result",
            "tool_use_id": call.id,               # match the request
            "content": str(output),
        }
    except Exception as e:
        return {
            "type": "tool_result",
            "tool_use_id": call.id,
            "is_error": True,                     # tell Claude it failed
            "content": f"Tool failed: {e}",
        }

# Send the block back inside a user message; Claude reacts accordingly.
```

#### 9. Interview Questions

**Basic**
1. What is a `tool_result`?
2. What links a result to its request?
3. What does `is_error: true` tell Claude?
4. Why validate a result before using it?
5. In which message role do you send the result back?

**Intermediate**
1. Why is signaling errors better than returning a fake value?
2. What can Claude do after it sees an error result?
3. What happens if the `tool_use_id` doesn't match?
4. What kinds of content can a tool_result carry?
5. How does validation relate to SPIDER's "Detect"?

**Scenario**
1. A DB call times out. What exactly do you send Claude?
2. A tool returns an empty list. Is that an error? How do you decide?
3. Claude keeps building on bad data. What safeguard was missing?
4. You want Claude to retry a flaky API once. How do results enable that?
5. A tool returns sensitive data you shouldn't show. Where do you filter it?

#### 10. Common Mistakes (+ why)

- **Returning a fake value on failure.** *Why: Claude will confidently use wrong data.*
- **Skipping validation.** *Why: garbage results lead to garbage answers (SPIDER: Detect).*
- **Wrong `tool_use_id`.** *Why: Claude matches the answer to the wrong question.*
- **Dumping huge raw output.** *Why: it wastes tokens and buries the useful part.*

#### 11. Best Practices

- **Always validate** results before returning them (SPIDER: *Detect*).
- Use **`is_error: true`** for real failures — don't hide them.
- **Match the `tool_use_id`** exactly, every time.
- Return **clean, concise** content — just what Claude needs.
- **Filter sensitive fields** before sending results back.

#### 12. One-Page Summary

- **Key points:** `tool_result` closes the loop, matched by `tool_use_id`. Flag failures with `is_error`. Validate first.
- **Important terms:** tool_result, tool_use_id, is_error, validation.
- **Quick revision:** Match the id, validate the output, flag the errors.
- **Mnemonic:** **"MVE"** — **M**atch, **V**alidate, **E**rror-flag.

> **Trainer Note:** Deliberately break a tool live (unplug the demo API) and show Claude reacting gracefully to `is_error`. The contrast with a fake-value answer drives home why honest error results matter.

---

### 5.5 Parallel Tool Calls

#### 1. Definition

**Parallel tool calls** happen when Claude, in a **single turn**, asks for **multiple independent tools at once** — for example, checking the weather in three cities. Because the calls don't depend on each other, **your code can run them concurrently** (at the same time) for speed, then return all the results together. Use this only when the calls are truly **independent**; anything where one call needs another's answer must stay **sequential** (ordered).

#### 2. Why do we need it?

Speed. If Claude needs weather for New York, London, and Tokyo, running them one-by-one means waiting three times. Running them **in parallel** means waiting roughly once. For users, that's the difference between a snappy reply and a slow one. Parallel calls let Claude gather several independent facts efficiently, then combine them into one answer — without wasting time on tasks that could have happened simultaneously.

#### 3. Office Analogy

The manager needs three reports and hands **three request forms to three different assistants at the same time**. All three go off, do their tasks in parallel, and return. The manager waits only as long as the *slowest* one, not the sum of all three. But if report B needs a number *from* report A, the manager must send A first and wait — that's a sequential job, not a parallel one.

#### 4. Real-Life Analogy

Cooking a big meal. You put the **rice on to boil, the oven preheating, and the salad chopping all at once** — independent tasks running in parallel, so dinner is ready fast. But you can't *ice* a cake before you've *baked* it — that step depends on the previous one, so it must wait its turn. Parallel where possible, sequential where required.

#### 5. Internal Working (numbered)

1. Claude sees a request needing several independent pieces of info.
2. In one turn, Claude emits **multiple `tool_use` blocks**, each with its own **id**.
3. Your code detects there are several calls and **runs them concurrently**.
4. Each call finishes; you build a **`tool_result` for each**, matched by its own **id**.
5. You send **all results back together** in one message.
6. Claude reads them all and writes a single combined answer.

#### 6. Architecture Diagram (ASCII fenced)

```
                     ONE TURN, THREE REQUESTS
   CLAUDE emits:  tool_use id=1 weather(NYC)
                  tool_use id=2 weather(London)
                  tool_use id=3 weather(Tokyo)
                          |
                          v
              +-----------------------+
              |   YOUR APP (concurrent)|
              +-----------------------+
               |          |          |
               v          v          v
            [NYC API] [London API] [Tokyo API]   <- run at the SAME time
               |          |          |
               v          v          v
           result id=1  id=2       id=3
               \          |          /
                \         |         /
                 v        v        v
              +-----------------------+
              |  all 3 tool_results    |---> back to CLAUDE (one message)
              +-----------------------+          -> one combined answer

   NOTE: parallel ONLY when calls are independent. Dependent = sequential.
```

#### 7. Real Example

A user asks: *"Compare the weather in Paris, Rome, and Madrid for my trip."* Claude issues three `weather` tool calls in one turn (ids 1, 2, 3). Your app fires all three requests at once; they return in about the time of the slowest single call. You send back all three results, and Claude replies with a tidy comparison: *"Paris 15C rainy, Rome 24C sunny, Madrid 27C sunny — Madrid looks best."* One fast turn instead of three slow ones.

#### 8. Live Demo

```python
# demo_parallel_tools.py — run independent calls concurrently
import concurrent.futures as cf

reply = LLMProvider.chat(messages=messages, tools=tools)

if reply.tool_calls and len(reply.tool_calls) > 1:      # multiple at once
    with cf.ThreadPoolExecutor() as pool:               # run in parallel
        futures = {
            pool.submit(run_local_tool, c.name, c.input): c
            for c in reply.tool_calls
        }
        results = []
        for fut in cf.as_completed(futures):
            call = futures[fut]
            results.append({
                "type": "tool_result",
                "tool_use_id": call.id,                  # each keeps its id
                "content": str(fut.result()),
            })
    # send ALL results back together
    messages.append({"role": "user", "content": results})
```

#### 9. Interview Questions

**Basic**
1. What is a parallel tool call?
2. In how many turns does Claude issue them?
3. Why run independent calls concurrently?
4. Give an example where parallel calls make sense.
5. When must calls stay sequential instead?

**Intermediate**
1. How does your code know to run calls in parallel?
2. How do results stay matched to the right request?
3. What's the time saving versus running sequentially?
4. How do you send several results back to Claude?
5. What defines "independent" calls?

**Scenario**
1. Claude issues two calls where the second needs the first's output. What do you do?
2. One of three parallel calls fails. How do you report back?
3. Your parallel results come back out of order. Is that a problem? Why not?
4. Users complain the multi-city lookup is slow. What would you check?
5. When would forcing parallelism actually cause a bug?

#### 10. Common Mistakes (+ why)

- **Parallelizing dependent calls.** *Why: the second call needs the first's answer — running together gives wrong results.*
- **Losing track of ids across threads.** *Why: results get matched to the wrong request.*
- **Not sending all results together.** *Why: Claude waits with an incomplete picture.*
- **Ignoring one failed call among several.** *Why: a hidden error corrupts the combined answer.*

#### 11. Best Practices

- **Only parallelize truly independent** calls.
- **Carry each call's id** carefully through concurrent code.
- **Collect all results** before replying to Claude.
- **Handle each call's errors** individually (`is_error` per result).
- Keep **dependent steps sequential and ordered**.

#### 12. One-Page Summary

- **Key points:** Multiple independent tools in one turn, run concurrently for speed. Match each result by id; return them together. Dependent calls stay sequential.
- **Important terms:** parallel tool calls, independent, concurrent, sequential.
- **Quick revision:** Independent = parallel (fast). Dependent = sequential (ordered).
- **Mnemonic:** **"PIT"** — **P**arallel **I**f **T**ruly-independent.

> **Trainer Note:** Time it live: run three lookups sequentially, then in parallel, and show the stopwatch difference. Then show a dependent example breaking under parallelism so students feel *why* independence is the rule.

---

### Quick Recap

```
   THE TOOL-USE LOOP (the heart of Module 5)

   USER ---> YOUR APP ---(msg + tool schemas)---> CLAUDE
                                                    |
                          Claude ASKS (tool_use) <--+
                                |
             YOUR APP RUNS the tool (Claude never does)
                                |
             tool_result (match id, validate, flag errors)
                                |
                                v
                      CLAUDE reads it --> final answer
                                          OR another tool_use (loop)
```

| Topic | One-line takeaway | Mnemonic |
|---|---|---|
| 5.1 What are Tools? | Tools connect text-only Claude to the real world; Claude asks, your app acts. | Claude ASKS, App ACTS |
| 5.2 Function Calling | The ask→run→return→repeat loop; match `tool_use_id`, cap iterations. | ARRR |
| 5.3 Tool Schema | name + description + input_schema; description drives correct selection. | NDI |
| 5.4 Tool Results | Close the loop by id; validate output; flag failures with `is_error`. | MVE |
| 5.5 Parallel Tool Calls | Run independent calls at once for speed; keep dependent ones sequential. | PIT |

**The one thing to remember:** *Claude never runs a tool itself — it only asks. Your application runs the tool and returns the result.* Everything else in this module is detail on top of that single rule.

**Reliability tie-in (SPIDER):** *Isolate* (least-privilege tools), *Detect* (validate every result, check `is_error`), *Recover* (retries and loop caps like `max_iters`). Safe tool use is reliable tool use.


---

## Module 6 — Model Context Protocol (MCP)

This module explains **MCP (Model Context Protocol)** — the open standard that lets an AI app plug into outside tools and data the same way a **USB-C** port lets any device plug into any charger. By the end you will know what MCP is, why it exists, how it is built, and every one of its core building blocks.

---

### 6.1 What is MCP?

#### 1. Definition

**MCP (Model Context Protocol)** is an **open standard** — a shared set of rules — for connecting AI applications to **external tools, data sources, and prompts** in a uniform way. It was introduced by **Anthropic**. Think of it as a common language: it standardizes *how* an AI app talks to outside capabilities, so any compatible app can talk to any compatible tool.

Key word: **protocol**. A protocol is just an agreed way of communicating (like how "hello / goodbye" works on a phone call). MCP is built on **JSON-RPC**, a simple text format for "call this function, here are the arguments, here is the answer."

#### 2. Why do we need it?

Without a standard, every AI app has to build a **custom, one-off connector** for every tool it wants to use — Slack, GitHub, a database, your files. That is slow, repetitive, and breaks often. MCP replaces all those custom connectors with **one universal plug**.

> **MCP is the USB-C standard for AI.**
> Before USB-C, every device needed its own special cable and port — a drawer full of chargers. Before MCP, every AI app needed a custom integration for every tool. USB-C gave us **one universal port**. MCP gives AI **one universal protocol**: write a connector once, and any MCP-compatible app can use it.

#### 3. Office Analogy

Imagine a new employee (the AI) who needs to use the **printer, the filing cabinet, and the email system**. In a bad office, they'd need a different, hand-written instruction sheet for each machine. With MCP, the office adopts **one standard "how to request things" form**. Now the employee fills out the same form for any machine, and any machine understands it.

#### 4. Real-Life Analogy

A **power outlet on the wall**. You don't rewire your house for every new lamp. The lamp has a standard plug; the wall has a standard socket. MCP is that standard socket for AI capabilities — plug in and go.

#### 5. Internal Working (numbered)

1. The AI app (the **client**) starts up and connects to one or more **MCP servers**.
2. The client asks each server: *"What can you do?"* (this is called **discovery**).
3. Each server replies with a list of its **Resources**, **Tools**, and **Prompts**.
4. During a conversation, the model decides it needs a capability (e.g., read a file).
5. The client sends a **JSON-RPC request** to the right server.
6. The server does the work and sends back a **JSON-RPC response**.
7. The client feeds that result back to the model, which continues answering.

#### 6. Architecture Diagram (ASCII fenced)

```
     +-------------------+                      +--------------------+
     |   AI App (CLIENT) |   MCP protocol       |    MCP SERVER      |
     |  e.g. Claude Code | <==================>  |  (files / GitHub)  |
     |                   |   JSON-RPC messages  |                    |
     +-------------------+                      +--------------------+
        "What can you do?"  --------------->
        <---------------  "Resources, Tools, Prompts"
```

#### 7. Real Example

You ask **Claude Code**: *"Summarize the open issues in my GitHub repo."* Claude Code (client) talks to a **GitHub MCP server**, which exposes a `list_issues` tool. The server fetches the issues and returns them; Claude reads them and writes your summary. No custom GitHub code inside Claude — just the standard protocol.

#### 8. Live Demo

See **6.5 Live Demo** for a runnable walkthrough that lists a server's capabilities and calls one tool.

#### 9. Interview Questions

**Basic**
1. What does MCP stand for?
2. Is MCP open or proprietary, and who introduced it?
3. What three capability types does an MCP server expose?
4. What message format does MCP use under the hood?
5. Give one everyday analogy for MCP.

**Intermediate**
1. How does a client learn what a server offers?
2. Why is a *standard* protocol better than custom connectors?
3. What is the difference between a client and a server in MCP?
4. Why is MCP called "vendor-agnostic"?
5. What problem does MCP solve that plain function-calling does not?

**Scenario**
1. Your team has 3 AI apps and 4 tools. How does MCP reduce the work?
2. A new database needs to be reachable by all your AI apps. What do you build?
3. A vendor releases a new AI IDE. How can it reuse your existing servers?
4. You must swap the model provider but keep all integrations. Does MCP help?
5. A tool changes its API. Where do you make the fix so all apps benefit?

#### 10. Common Mistakes

- Thinking MCP *is* an AI model. It is a **connector standard**, not a model.
- Assuming it only works with Anthropic. It is **open** and vendor-neutral.
- Confusing "client" (the app) with "server" (the capability provider).

#### 11. Best Practices

- Prefer an **existing MCP server** before writing your own.
- Keep each server **small and single-purpose**.
- Treat the protocol as the contract — don't hard-code app-specific hacks.

#### 12. One-Page Summary

| Item | Answer |
|---|---|
| What | Open standard to connect AI apps to tools/data/prompts |
| Who | Introduced by Anthropic |
| Format | JSON-RPC messages |
| Analogy | USB-C for AI |
| Exposes | Resources, Tools, Prompts |

> **Trainer Note:** Start here by physically holding up a USB-C cable. The whole module clicks once learners see "one plug, many devices" = "one protocol, many tools."

---

### 6.2 Why was MCP created?

#### 1. Definition

MCP was created to **kill the N×M integration problem** — the explosion of custom connectors you get when **N apps** each need to connect to **M tools**. It gives everyone **one shared protocol** instead.

#### 2. Why do we need it?

Before MCP, connecting **N** AI apps to **M** tools meant writing up to **N × M** separate integrations. Add one tool and you rewrite it for every app. MCP turns that into **N + M**: each app speaks MCP once, each tool speaks MCP once, and they all interoperate.

#### 3. Office Analogy

Before: every manager (app) wrote a **custom memo format** for every department (tool) — chaos. After: the company adopts **one standard memo template**. Any manager can now message any department instantly.

#### 4. Real-Life Analogy

Before USB-C, your drawer held a **tangle of chargers** — one per phone, camera, and laptop. USB-C collapsed them into **one cable**. MCP collapses AI's tangle of custom connectors into one.

#### 5. Internal Working (numbered)

1. Identify the pain: too many custom, brittle, duplicated integrations.
2. Define **one open protocol** (messages, discovery, capability types).
3. Tool makers build **one MCP server** for their tool.
4. App makers add **one MCP client** to their app.
5. Now any client works with any server — no per-pair coding.
6. The community shares servers, so work is **reused**, not repeated.

#### 6. Architecture Diagram (ASCII fenced)

```
   WITHOUT MCP  (N x M custom wires)        WITH MCP  (N + M via one hub)

   App1 --\   /-- Slack                     App1 --\           /-- Slack
   App2 ---X-X--- GitHub                     App2 ---+--[MCP]--+--- GitHub
   App3 --/   \-- DBase                      App3 --/           \-- DBase
     (every line hand-built)                   (each speaks MCP once)
```

#### 7. Real Example

Your company runs Claude Desktop, an internal chatbot, and an IDE plugin (**3 apps**) that all need Slack, Jira, Postgres, and Google Drive (**4 tools**). Custom = up to **12** integrations. With MCP: **4 servers** + each app's built-in client = everything connects.

#### 8. Live Demo

In **6.5**, notice how the *same* client code can point at a filesystem server or a GitHub server with no rewrite — that's the N+M win in action.

#### 9. Interview Questions

**Basic**
1. What is the N×M problem?
2. How does MCP change N×M into something smaller?
3. Why are custom connectors considered "brittle"?
4. What does "reuse" mean in the MCP context?
5. Who builds servers vs. clients?

**Intermediate**
1. Why does adding one new tool used to require touching every app?
2. How does a shared standard encourage a community of servers?
3. What does "decoupling apps from integrations" mean?
4. How does MCP relate to being "vendor-agnostic"?
5. Why is N+M cheaper to maintain than N×M?

**Scenario**
1. You have 5 apps and 10 tools. Compare custom vs. MCP effort.
2. A tool's API version changes. How many places must you fix?
3. Leadership wants faster tool rollout. Pitch MCP in two sentences.
4. Your startup wants outside developers to extend your AI app. How does MCP help?
5. You must justify MCP's cost/benefit to a manager. What's your argument?

#### 10. Common Mistakes

- Underestimating maintenance cost of custom connectors.
- Building a bespoke integration when a public MCP server already exists.
- Forgetting that "N+M" only works if everyone truly speaks the standard.

#### 11. Best Practices

- Count your real N and M before deciding — the savings grow with scale.
- Contribute reusable servers back so the whole team benefits.
- Standardize early, before the connector tangle forms.

#### 12. One-Page Summary

| Item | Answer |
|---|---|
| Problem | N×M custom integrations |
| Solution | One open protocol → N+M |
| Payoff | Reuse, less maintenance, vendor-agnostic |
| Analogy | Drawer of chargers → one USB-C |

> **Trainer Note:** Draw the N×M spaghetti on the whiteboard, then erase it and draw N+M. The visual "aha" is the most memorable moment of the whole module.

---

### 6.3 MCP Architecture

#### 1. Definition

MCP architecture is a **host/client ↔ server** design. The **Host/Client** is the AI app (Claude Desktop, Claude Code, an IDE). The **Servers** are small programs that expose capabilities. Both sides speak the **MCP protocol (JSON-RPC)** over a **transport**.

#### 2. Why do we need it?

A clear split of roles keeps things **modular and safe**. The app doesn't need to know a tool's internals; the server doesn't need to know the app. Each server is an independent, replaceable **building block** — and a **trust boundary** you can lock down.

#### 3. Office Analogy

The **client is a manager** who delegates tasks. Each **server is a specialist department** (Legal, IT, Finance). The manager sends a standard request form; the department does the work and reports back. Clean chain of command.

#### 4. Real-Life Analogy

A **restaurant**: you (client) give the **waiter** a standard order; the **kitchen** (server) prepares it. You never enter the kitchen; the kitchen never seats guests. Standard order slips keep it smooth.

#### 5. Internal Working (numbered)

1. The **host app** launches its built-in **MCP client**.
2. The client opens a **transport** (stdio locally, or HTTP for remote).
3. Client and server **handshake** and agree on protocol details.
4. The client requests the server's **capabilities** (discovery).
5. During use, the client sends **requests** (call tool, read resource).
6. The server returns **responses** (results or errors).
7. Optionally the server sends a **sampling** request back (borrow the model).
8. On shutdown, the connection closes cleanly.

#### 6. Architecture Diagram (ASCII fenced)

```
+-----------------------------------------------------+
|                 HOST APP (AI application)           |
|                                                     |
|   +-----------+     +-----------+     +-----------+ |
|   | MCP Client|     | MCP Client|     | MCP Client| |
|   +-----+-----+     +-----+-----+     +-----+-----+ |
+---------|-----------------|-----------------|-------+
          | transport       | transport       | transport
          | (stdio)         | (HTTP/SSE)      | (stdio)
     +----v-----+      +----v-----+      +----v-----+
     | Server A |      | Server B |      | Server C |
     | (files)  |      | (GitHub) |      | (DBase)  |
     +----------+      +----------+      +----------+
       one client  :  one server  =  one MCP connection
```

#### 7. Real Example

Claude Code (host) runs **three clients** at once: one to a filesystem server (read your code), one to a GitHub server (open a PR), one to a Postgres server (query data). Each is a separate connection; each server is isolated from the others.

#### 8. Live Demo

**6.5** shows one client connecting over **stdio** to a local server, then listing and calling capabilities — the smallest complete version of this architecture.

#### 9. Interview Questions

**Basic**
1. Name the two main roles in MCP architecture.
2. What is a "host" in MCP?
3. What carries messages between client and server?
4. Can one host run multiple clients?
5. Which side exposes capabilities?

**Intermediate**
1. Why is one-client-to-one-server a useful rule?
2. What does the handshake step accomplish?
3. Why call each server a "trust boundary"?
4. How does the modular design make swapping tools easy?
5. What is discovery and why does it matter?

**Scenario**
1. One server crashes. Why don't the others go down?
2. You need both a local and a remote server. What transports fit?
3. A server must ask the model a question. Which flow is that?
4. You want to add a new capability without touching the app. How?
5. Two teams own two servers. How does the architecture keep them independent?

#### 10. Common Mistakes

- Letting one giant server do everything (loses isolation).
- Mixing client and server responsibilities in one blob.
- Ignoring the transport choice (local vs. remote needs differ).

#### 11. Best Practices

- **One responsibility per server**; compose many small ones.
- Treat each server as an **isolated trust boundary** (SPIDER "Isolate").
- Pick the transport that matches deployment (stdio local, HTTP remote).

#### 12. One-Page Summary

| Item | Answer |
|---|---|
| Roles | Host/Client and Server |
| Speaks | MCP protocol (JSON-RPC) |
| Carried by | Transport (stdio / HTTP) |
| Shape | 1 host → many clients → many servers |
| Principle | Modular, isolated, replaceable |

> **Trainer Note:** Use the restaurant analogy live — appoint a "waiter" and a "kitchen" volunteer and pass paper order slips. Learners physically feel the request/response boundary.

---

### 6.4 MCP Building Blocks — Deep Dive

Here are the pieces that make MCP work. Each gets a short definition, an office/real-life analogy, and where it fits.

```
+---------------------------- HOST APP ----------------------------+
|                                                                  |
|   MCP CLIENT  --[ AUTH ]--[ TRANSPORT: stdio | HTTP/SSE ]------+  |
|      |  requests: read resource / call tool / get prompt       |  |
|      |  <-- responses; server may ask <-- SAMPLING             |  |
+------|----------------------------------------------------------+ |
       v                                                            |
+----------------------------- MCP SERVER --------------------------+
|   [ RESOURCES ]   [ TOOLS ]   [ PROMPTS ]                         |
|   read-only data  actions     reusable templates                 |
|   -------------------- SECURITY: trust boundary ------------------|
+------------------------------------------------------------------+
```

#### MCP Client

**Definition:** The part inside the AI app that opens a connection to a server, discovers its capabilities, and sends requests. **Analogy:** the **manager** who delegates and collects results. **Fits:** lives inside the host app; one client per server connection.

#### MCP Server

**Definition:** A small standalone program that exposes capabilities (resources, tools, prompts) to clients. **Analogy:** a **specialist department** that does one job well. **Fits:** the other end of every connection; independent and lazy-loaded.

#### Resources

**Definition:** **Read-only data or context** the server can provide — files, database rows, documents. Think "**GET** this data." No side effects. **Analogy:** the **filing cabinet** you read from. **Fits:** server → client, feeds context into the model.

#### Tools

**Definition:** **Actions the model can invoke** — functions that *do* something, often with side effects (send an email, create a file, run a query). **Analogy:** the **office machines** (printer, shredder) that perform an action. **Fits:** model decides → client calls tool → server executes.

#### Prompts

**Definition:** **Reusable prompt templates** the server offers, so users/apps can trigger a well-crafted instruction with one click. **Analogy:** **pre-printed form letters** ready to fill in. **Fits:** server offers them; client surfaces them to the user.

#### Sampling

**Definition:** A server can **ask the CLIENT's model to run a completion on its behalf** — the server "borrows" the LLM. The **client stays in control** and can require **user approval**. **Analogy:** a department asking the manager to "make a quick judgment call for us." **Fits:** reverse direction — server → client → model.

#### Transport

**Definition:** **How** client and server exchange messages. Common options: **stdio** (a local subprocess) and **HTTP (Streamable HTTP / SSE)** for remote servers. **Analogy:** the **road** the memos travel on — a hallway (local) or the postal service (remote). **Fits:** the layer beneath every request/response.

#### Authentication

**Definition:** Proving **who** is allowed to connect. Remote servers can require auth such as **OAuth**; local **stdio** servers run with the **user's own permissions**. **Analogy:** the **security badge** at the office door. **Fits:** guards the connection before any capability is used.

#### Security

**Definition:** MCP servers are **trust boundaries**. Apply **least privilege**, **validate inputs**, be cautious with **untrusted servers**, require **user approval** for sensitive tools, and watch for **prompt-injection** hidden in returned data. **Analogy:** office **security policy** — locked rooms, ID checks, "don't trust a stranger's note." **Fits:** wraps every server; maps to **SPIDER "Isolate."**

| Block | One-liner | Direction |
|---|---|---|
| Client | Delegates & requests | in app |
| Server | Provides capabilities | standalone |
| Resources | Read-only data (GET) | server → client |
| Tools | Actions (side effects) | client → server |
| Prompts | Reusable templates | server → client |
| Sampling | Server borrows the model | server → client → model |
| Transport | The road (stdio / HTTP) | both ways |
| Authentication | Badge at the door | guards entry |
| Security | Trust-boundary discipline | around everything |

---

### 6.5 Live Demo

A minimal end-to-end flow: connect a client to a local server over **stdio**, list capabilities, then call one tool.

```
STEP 1  Launch server        $ (host starts server as a subprocess via stdio)
STEP 2  Handshake            client <---> server agree on protocol
STEP 3  Discover             client: "list your tools?"
                             server: ["read_file", "write_file"]
STEP 4  Call a tool          client -> read_file("notes.txt")
                             server -> "Buy milk, call Sam"
STEP 5  Model uses result    Claude summarizes the file for the user
```

Talking points while you run it:
1. The **same client** could point at a GitHub server instead — no rewrite (N+M win).
2. Ask for **user approval** before the `write_file` tool runs (Security).
3. Show the raw **JSON-RPC** request/response once so learners see the "language."
4. Swap **stdio** for an **HTTP** URL to demo a remote server and **auth**.

In this repo, explore the `mcp/` folder and run an MCP topic per the project README (`pip install -e ".[mcp]"`, then the topic's `demo.py`).

---

### 6.6 Interview Questions

**Basic**
1. What does MCP stand for and who introduced it?
2. Name the three capability types a server exposes.
3. What is the difference between a Resource and a Tool?
4. What are the two common transports?
5. What analogy best captures MCP?

**Intermediate**
1. Explain the N×M problem and how MCP solves it.
2. What is sampling, and who stays in control during it?
3. Why is each MCP server called a trust boundary?
4. How does authentication differ for local vs. remote servers?
5. Why is "one responsibility per server" a good rule?

**Scenario**
1. A server returns text containing hidden "ignore your rules" instructions. What risk is this and how do you defend?
2. You must connect one AI app to a remote server behind a login. Which transport and auth apply?
3. A tool can delete files. What safeguards do you add before enabling it?
4. Five AI apps need the same four tools. Estimate the effort with and without MCP.
5. A server needs the model to draft a reply mid-task. Which MCP feature enables this, and what approval step do you keep?

---

### 6.7 Common Mistakes

- **Confusing MCP with an AI model** — it's a connector standard, not a brain.
- **Mixing up Resources and Tools** — read-only data vs. side-effect actions.
- **Trusting any server blindly** — servers are trust boundaries; vet them.
- **Skipping user approval** on sensitive tools (delete, send, pay).
- **Ignoring prompt-injection** in data a server returns.
- **One giant do-everything server** instead of small, isolated ones.
- **Hard-coding a single vendor** and losing MCP's vendor-agnostic benefit.

---

### 6.8 Best Practices

- **Reuse before you build** — prefer existing MCP servers.
- **One responsibility per server**; compose many small ones.
- **Least privilege** — give each server only the access it needs.
- **Validate all inputs** and treat returned data as untrusted.
- **Require approval** for actions with real-world side effects.
- **Match the transport** to deployment: stdio local, HTTP remote.
- **Use proper auth** (e.g., OAuth) for remote servers.
- **Isolate** — lean on the trust-boundary design (SPIDER "Isolate").

---

### 6.9 One-Page Summary

| Topic | Key point |
|---|---|
| What | Open standard (by Anthropic) to connect AI apps to tools/data/prompts |
| Analogy | **USB-C for AI** — one universal plug |
| Problem solved | N×M custom integrations → N+M |
| Format | JSON-RPC over a transport |
| Roles | Host/Client ↔ Server |
| Capabilities | Resources (data), Tools (actions), Prompts (templates) |
| Sampling | Server borrows the client's model; client stays in control |
| Transports | stdio (local), HTTP / SSE (remote) |
| Auth | OAuth for remote; user permissions for local stdio |
| Security | Servers are trust boundaries; least privilege, validate, approve |
| SPIDER link | "Isolate" — each server is a boundary |

```
   ONE PROTOCOL  ->  MANY TOOLS
   +--------+     +--------+     +--------+
   | Client |=MCP=| Server |=====| Tool   |
   +--------+     +--------+     +--------+
   write once           connect to many
```

---

### Quick Recap

- **MCP** is the **open, USB-C-style standard** for connecting AI apps to tools, data, and prompts.
- It turns the messy **N×M** integration problem into a clean **N+M** — write once, connect to many.
- Architecture is **Host/Client ↔ Server**, speaking **JSON-RPC** over a **transport** (stdio or HTTP).
- Servers expose **Resources** (read), **Tools** (act), and **Prompts** (templates); **Sampling** lets a server borrow the model with the client in control.
- **Authentication** guards connections and **Security** treats every server as a **trust boundary** — least privilege, validate inputs, require approval.


---

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


---

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


---

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


---

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


---

## Glossary — Claude & Anthropic Terminology

A quick‑reference dictionary for every important term in this handbook. Terms are grouped so related ideas sit together; within each group they run roughly from most basic to more advanced.

### Core concepts
- **Anthropic** — The AI safety company that builds Claude.
- **Claude** — A family of large language model (LLM) AI assistants made by Anthropic. Reads text, writes helpful text back.
- **LLM (Large Language Model)** — An AI model trained on huge amounts of text that generates language by predicting the next token, over and over.
- **Token** — The small piece text is split into (~¾ of a word in English). Input and output are both counted in tokens; cost and limits are measured in tokens.
- **Helpful, Honest, Harmless (HHH)** — Anthropic's design goals for Claude's behavior.
- **Hallucination** — When the model states something false but sounds confident. The main risk to guard against with grounding and self‑checks.
- **Knowledge cutoff** — The date after which the model has no built‑in knowledge; fresh facts require tools/search.
- **Non‑determinism** — The same prompt can produce slightly different answers on different runs.

### Models
- **Model family / tier** — Different Claude models trading capability against speed and cost.
- **Opus** — The most capable tier; deepest reasoning (e.g., `claude-opus-4-8`). Best for the hardest tasks.
- **Sonnet** — The balanced, general‑purpose default (e.g., `claude-sonnet-5`).
- **Haiku** — The fastest, most economical tier (e.g., `claude-haiku-4-5`). Best for high‑volume, simpler work.
- **Fable** — A member of the Claude 5 family.
- **Model ID** — The exact string used to select a model in the API (e.g., `claude-opus-4-8`).

### The API
- **Claude API (Anthropic API)** — The developer interface for sending requests to Claude programmatically.
- **Messages API** — The core endpoint: you send a list of messages (roles: system/user/assistant) and receive an assistant reply.
- **Role** — The label on a message: **system** (global rules/persona), **user** (the human), **assistant** (Claude's reply).
- **`usage`** — The object in the API response reporting input/output token counts — the basis for cost.
- **`max_tokens`** — The cap you set on how many tokens the response may use.
- **Structured output** — Making Claude return machine‑readable output in a fixed shape (e.g., JSON matching a schema).

### Prompting
- **Prompt** — The text instruction you give Claude.
- **System Prompt** — Global instructions/persona/rules, usually set once at the top of a conversation.
- **User Prompt** — The human's actual request in a turn.
- **Assistant Response** — Claude's reply.
- **Prompt Engineering** — Designing prompts so the model reliably produces the wanted output.
- **PRECISE** — This course's prompting checklist: **P**ersona · **R**esult · **E**xamples · **C**ontext · **I**nstructions · **S**pecification · **E**valuation.
- **XML Prompting** — Wrapping prompt sections in tags (`<document>`, `<instructions>`, `<example>`) so Claude can separate them cleanly.
- **Few‑shot Prompting** — Including a few worked input→output examples to teach format and edge cases. (Zero‑shot = none; one‑shot = one.)
- **Role Prompting** — Assigning Claude a persona ("You are a senior tax accountant…") to steer tone and rigor.
- **Prompt Chaining** — Splitting a big task into a sequence of prompts where each step's output feeds the next.
- **Prompt hierarchy** — Building prompts in layers: Base → Role → Task → Output‑spec.

### Context
- **Context** — Everything sent to the model for one request: system prompt + history + retrieved docs + tool results + the current message. The model's entire working knowledge for that call.
- **Context Window** — The maximum number of tokens the model can consider at once (input + output). Finite (commonly up to ~200K, with 1M‑token windows on some tiers).
- **Conversation History** — The running list of prior turns re‑sent on every call so the model appears to "remember."
- **Long Context** — Tasks that load large inputs (whole documents/codebases); watch cost, latency, and "lost in the middle" effects.
- **Context Compression / Compaction** — Summarizing earlier history so it fits (risk: losing detail).
- **Context Editing** — Clearing stale tool results / thinking blocks from the window during long runs.
- **Context Overflow** — When total tokens exceed the window, causing errors or dropped content.
- **Token Limits** — The hard caps: the context‑window size and the `max_tokens` you set for the response.
- **CALM** — This course's context checklist: **C**ache · **A**ssemble selectively · **L**imit · **M**anage lifecycle.
- **Prompt Caching** — Reusing a stable prompt **prefix** so repeat tokens cost far less. Any change in the prefix invalidates the cache after that point; verify with `cache_read_input_tokens > 0`.
- **"Lost in the middle"** — The tendency for models to pay less attention to information buried in the middle of a very long context.

### Memory
- **Memory** — Information deliberately stored **outside** the model and reloaded later, so knowledge survives across calls/sessions.
- **Stateless** — Each request is independent; the server keeps no memory of previous requests. The Claude API is stateless underneath.
- **Stateful** — The system tracks state across interactions (e.g., a session or database‑backed app).
- **Persistent Memory** — Facts saved durably (files/database) that survive restarts and future sessions.
- **External Memory** — Knowledge stored outside the context window and retrieved on demand.
- **RAG (Retrieval‑Augmented Generation)** — Fetching only the relevant stored pieces (often from a vector database) and injecting them into the prompt.
- **Vector database** — A store that finds text by meaning/similarity, commonly used for RAG.

### Tools
- **Tool** — A capability that lets Claude do something it can't do alone (fetch data, call an API, run code, do exact math).
- **Function Calling / Tool Use** — The pattern where Claude requests a tool (name + JSON arguments), your code runs it, and you return the result.
- **Tool Schema** — A tool's `name`, `description`, and `input_schema` (JSON Schema of its parameters). Good descriptions drive correct tool selection.
- **`tool_use`** — The block Claude returns to request a tool. Claude never executes tools itself.
- **`tool_result`** — The block you send back containing the tool's output, tied to the request's `tool_use_id`.
- **`is_error`** — A flag on a tool result signalling failure so Claude can react/retry.
- **Parallel Tool Calls** — Requesting several independent tools in one turn so they can run concurrently.
- **Tool loop** — The repeat cycle: model requests → app executes → result returned → model continues.

### MCP (Model Context Protocol)
- **MCP** — An open standard for connecting AI applications to external tools, data, and prompts in a uniform way. "The USB‑C standard for AI."
- **MCP Host / Client** — The AI application (Claude Desktop, Claude Code, an IDE) that connects to servers.
- **MCP Server** — A small program that exposes capabilities to clients over the MCP protocol.
- **Resources (MCP)** — Read‑only data/context a server can provide (files, DB rows).
- **Tools (MCP)** — Actions the model can invoke through a server.
- **Prompts (MCP)** — Reusable prompt templates a server offers.
- **Sampling (MCP)** — When a server asks the client's model to run a completion on its behalf, with the client in control.
- **Transport (MCP)** — How client and server talk: **stdio** (local subprocess) or **HTTP/SSE** (remote).
- **Trust boundary** — A line across which you don't automatically trust input; MCP servers are trust boundaries to secure.

### Agents
- **Agent** — An LLM that pursues a goal in a **loop**: decide → act (tool) → observe → repeat, until done.
- **Agent Loop** — The cycle: Goal → Plan → Reason/Decide → Act → Observe → Reflect → (loop or) Respond.
- **Planning** — Breaking a goal into steps before acting.
- **Reasoning** — Thinking about what to do next given the current state.
- **Decision Making** — Choosing the next action / which tool to use.
- **Acting** — Taking the step (issuing a `tool_use`).
- **Observation** — Reading the tool result / new information.
- **Reflection** — Evaluating progress and adjusting the plan.
- **Max iterations (loop cap)** — A hard limit on loop turns to prevent infinite loops.
- **SPIDER** — This course's agent‑reliability checklist: **S**cope · **P**lan · **I**solate · **D**etect · **E**scalate · **R**ecover.
- **Approval gate / Human‑in‑the‑loop** — Routing risky or irreversible actions to a person for sign‑off (the "Escalate" in SPIDER).

### Subagents & orchestration
- **Subagent** — A separate, focused agent (its own prompt, tools, and context) that a main agent delegates a sub‑task to.
- **Orchestrator / Lead agent** — The agent that plans, delegates, and merges results.
- **Delegation** — Assigning a scoped task plus only the tools/context a subagent needs (least privilege).
- **Task Decomposition** — Breaking a big goal into independent or staged sub‑tasks.
- **Fan‑out / Parallel Execution** — Running independent subagents at the same time for speed.
- **Fan‑in / Result Aggregation** — Collecting, deduping, and synthesizing subagent outputs into one answer.
- **Router / Pipeline / Parallel** — Common multi‑agent patterns: pick a specialist · chain stages · run many at once.
- **Multi‑Agent Collaboration** — Multiple agents working together toward one goal.

### Claude Code & the exam
- **Claude Code** — Anthropic's agentic coding tool that runs in the terminal/IDE and uses tools, MCP, and project memory (`CLAUDE.md`).
- **Claude Agent SDK** — Anthropic's toolkit for building custom agents (agent loops, orchestration).
- **CLAUDE.md** — A project memory file Claude Code reads for standing instructions and conventions.
- **CCA‑F** — Community shorthand for the **Claude Certified Architect – Foundations** exam (the abbreviation itself is not officially confirmed).
- **Claude Partner Network** — The partner program that currently gates access to the certification.
- **Pearson VUE / OnVUE** — The proctoring provider/platform delivering the exam online.
- **Anthropic Partner Academy (Skilljar)** — Where registration, prep, and the authoritative Exam Guide PDF live.
- **Exam Guide PDF** — The single authoritative source for exam scope; reconcile all study material against it.

---

*End of handbook. Good luck on the exam — and welcome to building with Claude.*
