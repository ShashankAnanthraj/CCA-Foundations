# One-pager — Topic 04: Projects & Artifacts

**Slide headline:** A project is lightweight references to your world; an artifact is a saved deliverable.

**Demo beats (`topics/04-projects-artifacts/demo.py`):**
1. Load a `project.json` → references to context + skills (stays lightweight).
2. Build a project-scoped system (Base + project context) → answer grounded in product facts.
3. Generate a markdown release-note **artifact** and save it under `runtime/artifacts/`.

**Say this:**
- "Projects reference shared skills/context/prompts — they never duplicate them (stay lightweight)."
- "Project context grounds the assistant in your world: version, support email, house style."
- "Artifacts = deliverables you persist. Simple ones are model output; rich files (pptx/xlsx/pdf) come
  from Agent Skills + code execution (Topic 03)."
- "Mirrors Claude.ai Projects (persistent knowledge) and Artifacts (generated deliverables)."

**Top pitfall:** copying skills/prompts into a project — it bloats and drifts. Reference, don't duplicate.

**CCA‑F:** Context Management (15%) + ties into Skills (Topic 03).
