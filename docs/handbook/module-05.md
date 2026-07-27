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
