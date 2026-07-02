# Anthropic Agent Skills (API-hosted) — reference

Two distinct things share the word "skill":

| | Custom skill (this repo, Topic 03 demo) | Anthropic Agent Skills (API) |
|---|---|---|
| What | Your `SKILL.md` expertise, injected into the prompt | Anthropic-managed skills that run **in a code-execution container** |
| Examples | `sql-reviewer`, `changelog-writer` | `pptx`, `xlsx`, `pdf`, `docx` |
| Produces | Text guidance | Real files (a `.pptx`, `.xlsx`, …) |
| Enable via | `assemble_system(base, skill_body)` | `container.skills` + `code_execution` tool + beta headers |

## Enabling an Anthropic Agent Skill (Messages API)
Requires **both** beta flags and the code-execution tool. The skill runs server-side in a container;
generated files come back as file IDs to download via the Files API.

```python
import anthropic
client = anthropic.Anthropic()

resp = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={"skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]},
    tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
    messages=[{"role": "user", "content": "Create a 3-slide deck introducing AI-OS to a team."}],
)

# Find the generated file's id in resp.content, then:
#   data = client.beta.files.download(file_id)   # needs beta: files-api-2025-04-14
#   data.write_to_file("ai-os-intro.pptx")
```

Notes:
- `skill_id` for Anthropic skills: `pptx`, `xlsx`, `docx`, `pdf`. Custom (org) skills use their `skill_id`
  from the Skills API + a `version`.
- This is **not** the Managed Agents surface — it's the Messages API with a container attached.
- Cost/latency: code execution runs real code — keep demos small; download artifacts, then clean up files.

This file is a reference (not run by `demo.py`) to keep the topic cheap and offline-friendly.
