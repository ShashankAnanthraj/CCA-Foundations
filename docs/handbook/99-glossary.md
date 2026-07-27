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
