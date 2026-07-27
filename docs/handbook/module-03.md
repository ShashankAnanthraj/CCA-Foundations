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
