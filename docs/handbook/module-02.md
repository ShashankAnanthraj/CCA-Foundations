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
