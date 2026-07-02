# Topic 03 — Skills

**Purpose:** Package expertise so it's reusable and loads only when relevant — the mechanism behind
scaling to 500+ skills without drowning the context window.

## Concept
- **`SKILL.md`** = frontmatter (`name`, `description`) + body (Purpose·Responsibilities·Capabilities·
  Limitations·Thinking Strategy·Output Format·Best Practices). See `skills/*/SKILL.md`.
- **Progressive disclosure:** only `name` + `description` stay in context; the body loads **on demand**
  when a skill is selected. Implemented by `core.SkillRegistry` (`discover()` vs `load_body()`).
- **Two flavors:** custom skills (injected as expertise — this demo) and Anthropic **Agent Skills**
  (API-hosted, run in a code-execution container: `pptx`/`xlsx`/`pdf`/`docx`). See
  [prebuilt_agent_skills.md](prebuilt_agent_skills.md).

## When to use
| Need | Reach for |
|---|---|
| Reusable domain expertise across tasks | A custom `SKILL.md` |
| Many skills, keep context small | Progressive disclosure (registry) |
| Generate real documents (deck/sheet/doc/pdf) | Anthropic Agent Skills + code execution |

## Talking points
1. The model sees a **menu** (descriptions), not the whole cookbook — that's how 500 skills fit.
2. A skill's `description` is its **trigger**: write it as "what it does + *when* to use it."
3. Skills are composable and never duplicate `prompts/base` — shared behavior stays in the Base layer.
4. Claude Code loads project skills the same way (`.claude/skills/`), which we wire up in Topic 11.

## Run it
```bash
python topics/03-skills/demo.py
```
Discovery + routing + on-demand load run offline; the final "apply" step needs your API key.

## Reuses (DRY)
- `core.SkillRegistry` — discover (metadata) / load_body (on demand)
- `core.assemble_system` + `prompts/base/base_system.md` — compose skill onto the Base layer
- `providers.claude.ClaudeProvider` — run the guided task
