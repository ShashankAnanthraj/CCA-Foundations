# Topic 04 — Projects & Artifacts

**Purpose:** Package persistent, project-scoped context so an assistant answers "in your world," and
produce **artifacts** — saved deliverables (CCA‑F *Context Management*, 15%).

## Concept
- **Project = references, not copies.** A `project.json` points at shared context files + skills + a
  default model. It stays lightweight; the capability plane does the work (`core.load_project`).
- **Project context** lives in `context/project/…` and is loaded on top of the Base prompt — the
  assistant now knows your product facts and house style.
- **Artifacts** are deliverables the model produces: markdown/HTML/code you save (this demo), or rich
  files (`.pptx`/`.xlsx`/`.pdf`) via **Agent Skills** + code execution (Topic 03).
- **Claude ecosystem:** mirrors **Claude.ai Projects** (persistent knowledge you chat against) and
  **Artifacts** (generated, viewable/editable deliverables).

## When to use
| Need | Reach for |
|---|---|
| Persistent facts/style across many chats | A **Project** (context references) |
| A saved text/markdown/HTML deliverable | Artifact = save model output (this demo) |
| A real Office/PDF file | Agent Skills + code execution (Topic 03) |

## Talking points
1. Projects stay lightweight — they *reference* skills/context/prompts, never duplicate them.
2. Project context grounds answers in your world (version, support email, house style).
3. An artifact is just a deliverable you persist — from a one-line note to a full document.
4. Rich file artifacts are the API's Agent Skills; simple ones are model output you write to disk.

## Run it
```bash
python topics/04-projects-artifacts/demo.py    # saves an artifact under runtime/artifacts/
```

## Reuses (DRY)
- `core.load_project` / `Project.context_text()` — manifest + project context
- `core.assemble_system` + `prompts/base/base_system.md` — compose project context onto Base
- `context/project/devrel.md`, `projects/devrel_assistant/project.json`
