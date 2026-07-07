# Exam Blueprint — What's Official vs. Unverified

> **Sourcing rule:** every claim below is tagged **[OFFICIAL]** (anthropic.com / Pearson VUE /
> Anthropic Skilljar) or **[UNVERIFIED]** (third-party prep sites). The single authoritative artifact
> is the partner-gated **"Claude Certified Architect – Foundations – Exam Guide" PDF**. Treat
> [UNVERIFIED] items as directional, not fact.

## What it is
- **[OFFICIAL]** A real, **Anthropic-administered** technical certification — "Claude Certified
  Architect, Foundations" — announced **2026-03-12** as Anthropic's first technical cert, for
  solution architects building production applications with Claude.
- **[OFFICIAL]** Delivered via **Pearson VUE** (OnVUE online-proctored); registration/prep on
  **Anthropic Partner Academy** (Skilljar).
- **[OFFICIAL]** **Access is gated to organizations in the Claude Partner Network.** It is not
  currently an open public exam.
- **[UNVERIFIED]** "CCA-F" is a community acronym, not confirmed official (one Pearson VUE rendering
  showed "CCAR-F"). Don't rely on the abbreviation in any official context.

## Domains
- **[OFFICIAL]** The exam validates practitioners across **four core technology areas**:
  **Claude Code · Claude Agent SDK · Claude API · Model Context Protocol (MCP)** — with an emphasis
  on making informed **tradeoff decisions** for real-world solutions.
- **[UNVERIFIED]** Prep sites consistently report a **five-domain** structure with these weights.
  The naming is corroborated across independent sources and is consistent with the official four
  areas, but **the percentages are not confirmed**:

  | Domain (third-party) | Reported weight | Status |
  |---|---|---|
  | Agentic Architecture & Orchestration | 27% | UNVERIFIED |
  | Claude Code Configuration & Workflows | 20% | UNVERIFIED |
  | Prompt Engineering & Structured Output | 20% | UNVERIFIED |
  | Tool Design & MCP Integration | 18% | UNVERIFIED |
  | Context Management & Reliability | 15% | UNVERIFIED |

  > AI-OS's `topics/README.md` is built to exactly these third-party weights. Useful as a study
  > spine, but do not treat the percentages as the real blueprint.

## Logistics
- **[OFFICIAL]** Proctored (OnVUE). Retake policy: 14 days after attempt 1, 30 after 2, 90 after 3;
  up to 4 attempts per rolling 12 months.
- **[OFFICIAL, conflicting]** Cost is in flux — reported as free for the first tranche of partner
  employees then ~$99/attempt; a $125 figure also appears. Treat exact price as unconfirmed.
- **[UNVERIFIED]** Widely reported: **~60 scenario-based multiple-choice questions**, **120 minutes**,
  passing **~720/1000**. Plausible but not confirmed on official pages.

## What's tested beyond architecture theory
The exam is **build-oriented around Anthropic's own tooling**, not vendor-neutral theory:
- **[OFFICIAL]** Claude API specifics, tool use + MCP configuration, and Claude's built-in tools.
- **[OFFICIAL]** Claude Code configuration and the Claude Agent SDK (agent loops, orchestration).
- **[UNVERIFIED]** Prompt engineering & structured output (few-shot, JSON schema, validation-retry),
  context management & reliability (summarization risks, escalation, provenance).

**Implication for this project:** AI-OS is deliberately vendor-*agnostic* and re-implements agent
loops/orchestration in its own `core/`. The exam rewards knowing the **real** Claude Agent SDK,
**real** Claude Code behaviors, and **real** API semantics. Study those from Anthropic's docs — see
[study-guide.md](study-guide.md) and [vendor-reconciliation.md](vendor-reconciliation.md).

## Sources
**Official:** anthropic.com/news/claude-partner-network (2026-03-12) · pearsonvue.com/us/en/anthropic
· anthropic-partners.skilljar.com (CCA Foundations page + gated Exam Guide PDF).
**Third-party (unverified):** claudecertifications.com, preporato.com, dev.to community posts,
GitHub community study guides. Use for exam "feel," never as the blueprint of record.
