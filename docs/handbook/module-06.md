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
