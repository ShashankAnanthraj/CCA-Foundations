# AI‑OS Master Constitution (Canon)

> This is the governing contract for AI‑OS. Every artifact must comply. It is stored
> as canon so agents, contributors, and tooling can load it as authoritative context.

## Role
AI‑OS is a long-term, production-grade AI Engineering Platform — the operating system for
designing, building, testing, deploying, and managing AI systems. Not a demo. Every decision
is production-ready; never trade long-term maintainability for short-term convenience.

## Primary objective
Build AI‑OS with enterprise software-engineering principles. It must be: Modular · Extensible ·
Scalable · Maintainable · Token-Efficient · Cost-Efficient · Model-Agnostic · Cloud-Agnostic ·
Vendor-Agnostic · AI-First. Every artifact is reusable; nothing exists without a clear purpose.

## Core design priorities (in order)
1. Simplicity  2. Reusability  3. Maintainability  4. Performance  5. Token Efficiency
6. Context Efficiency  7. Cost Efficiency  8. Developer Experience  9. Scalability  10. Reliability

Never sacrifice architecture for speed.

## Token economy
Tokens are an expensive production resource. Never generate unnecessary text; never duplicate
prompts, skills, templates, or context. Reuse existing components. One responsibility per artifact.
Compose instead of duplicating. Default to concise output; expand only when explicitly requested.

## Context engineering
Context is the most valuable resource. Separate **Global · Domain · Project · Task · Runtime ·
Conversation · Persistent · Temporary** context. Load only the minimum required; design every
component for **selective** context loading.

## Knowledge architecture
Knowledge is modular — never one large file. Independent modules that support Semantic Search,
Vector DBs, RAG, and Knowledge Graphs without restructuring.

## Prompt engineering
Prompts are hierarchical: **Base → Role → Task → Output-Spec → User Request**. Shared behaviors
are inherited, never repeated.

## Skill design
Skills are reusable expertise. Each declares: Purpose · Responsibilities · Capabilities ·
Limitations · Thinking Strategy · Output Format · Coding Standards · Best Practices. Composable;
never duplicated.

## Agent design
One responsibility per agent — no God Agents (Planner, Architect, Developer, Reviewer, Tester,
Optimizer, Documentation, Security, Research, Deployment). Each receives only relevant context;
stateless whenever possible.

## MCP design
Every MCP server is independent and plug-and-play (Filesystem, GitHub, Browser, Docker, Database,
Snowflake, Databricks, Slack, Notion, Jira). Never tightly coupled; lazy-loaded only when required.

## Project design
Projects never duplicate Skills/Prompts/Knowledge/Templates/Workflows — they **reference** shared
components and stay lightweight.

## Documentation
Every component documents: Purpose · Usage · Examples · Dependencies · Limitations · Best Practices ·
Future Improvements.

## File design
Prefer many small, focused files. Split logically. Optimize for AI retrieval, human readability,
version control, and future RAG.

## Output standards
Any solution provides: Architecture · Folder Structure · Explanation · Implementation ·
Best Practices · Risks · Future Improvements · Optimization Opportunities · Security · Maintenance.

## Engineering principles
SOLID · DRY · KISS · YAGNI · Composition over Inheritance · Convention over Configuration ·
Separation of Concerns · Clean Code · Clean Architecture · DDD · Context Engineering · Token Economy · DX.

## Performance & cost
Optimize latency, memory, context size, token usage, model calls, caching, reuse, parallelism.
Assume every AI request costs money — prefer reusable components, templates, shared knowledge,
selective/incremental context loading.

## Security
Never expose secrets. Separate config from code. Support environment variables. Least privilege.
Design for auditability.

## Future compatibility
Support (without architectural change) Claude, OpenAI, Gemini, Ollama, DeepSeek, Qwen, Llama,
Mistral, HuggingFace, CrewAI, LangGraph, OpenAI Agents SDK, AutoGen, Semantic Kernel.

## Scale target
1000+ Projects · 1000+ Prompts · 500+ Skills · 500+ Agents · 200+ Workflows · 100+ MCP Servers ·
20+ Model Providers · Millions of AI requests — no redesign required.

## Final rule
Before generating any solution, ask internally: can it be **Simpler · More Modular · More Reusable ·
More Token-Efficient · More Maintainable · More Scalable?** If yes, improve first. Never settle for
the first solution.
