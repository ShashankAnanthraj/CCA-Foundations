# Skills — reusable expertise, loaded on demand

A **skill** is a packaged unit of expertise the model can apply when relevant. Each lives in its own
folder as a `SKILL.md`:

```
skills/<name>/SKILL.md
```

## Anatomy of a SKILL.md
```
---
name: <kebab-case-id>
description: <one line — what it does + WHEN to use it. This is the trigger.>
---
# Body: Purpose · Responsibilities · Capabilities · Limitations ·
#       Thinking Strategy · Output Format · Best Practices
```

## Progressive disclosure (why skills scale)
- **Always loaded:** just the `name` + `description` (a few tokens each). The model sees the *menu*.
- **Loaded on demand:** the full body — **only** when that skill is selected for the task.

`core.SkillRegistry` implements exactly this: `discover()` returns metadata only; `load_body(name)`
fetches the instructions for the one skill you chose. 500 skills cost ~500 one-line descriptions in
context, not 500 full documents (Constitution: token & context economy).

## Two flavors
| Flavor | Where it runs | This repo |
|---|---|---|
| **Custom skill (as expertise)** | Injected into the prompt/agent by you | `skills/*/SKILL.md` + Topic 03 demo |
| **Anthropic Agent Skills (API-hosted)** | In a code-execution container (pptx/xlsx/pdf/docx…) | `topics/03-skills/prebuilt_agent_skills.md` |

**Rule:** skills are composable and never duplicate each other. Shared behavior belongs in `prompts/base`.
