# Projects — lightweight, reference-only

A **project** bundles *references* to shared components — a model, project-scoped context, and skills —
never copies of them (Constitution: Project Design). It stays small; the capability plane does the work.

## A project manifest (`project.json`)
```json
{
  "name": "DevRel Assistant",
  "description": "…",
  "model": "claude-opus-4-8",
  "context": ["context/project/devrel.md"],   // references, not copies
  "skills": ["changelog-writer"]               // references skills/
}
```
`core.load_project()` resolves it; `Project.context_text()` reads the referenced context.

## Projects vs the rest
| | Project | Skill | Agent |
|---|---|---|---|
| Holds | references + config | reusable expertise | one responsibility + tools |
| Owns logic? | no (composes) | no (guidance) | yes (a loop) |

## Claude ecosystem mapping
- **Claude.ai Projects:** persistent project context + knowledge you chat against — same idea, hosted.
- **Artifacts:** generated deliverables (docs, code, apps). In the API, rich file artifacts come from
  code execution / Agent Skills (Topic 03); simple text/markdown/HTML artifacts are just model output
  you save. Topic 04's demo generates and saves one.
