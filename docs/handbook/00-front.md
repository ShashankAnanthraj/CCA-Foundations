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
