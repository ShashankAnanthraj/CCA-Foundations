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
