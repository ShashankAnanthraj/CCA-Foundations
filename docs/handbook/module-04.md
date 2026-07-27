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
