# Topic 02 — Prompt Engineering

**Purpose:** Turn vague requests into reliable, machine-usable outputs — the highest-leverage skill
for production quality (CCA‑F *Prompt Engineering*, 20%).

## Concept
- **Hierarchy (no duplication):** `Base → Role → Task → Output-Spec → User Request`. Shared behavior is
  written once and inherited (`prompts/`), assembled with `core.assemble_system`.
- **Persona prompting:** the Role layer sets expertise and tone (`prompts/role/…`).
- **Few-shot:** examples in the Task layer teach format and edge cases faster than prose.
- **PRECISE framework:** Persona · Result · Examples · Context · Instructions · Specification ·
  Evaluation — a checklist for production prompts (`prompts/frameworks/precise.md`).
- **Structured output:** constrain the response to a JSON Schema (`structured_chat`) so it's always
  parseable — no regex, no "please return JSON".
- **Hallucination reduction:** ground in provided facts + "if unknown, say so" (the Evaluation letter).

## When to use what
| Need | Reach for |
|---|---|
| Consistent tone/expertise | Persona (Role layer) |
| Teach a format / edge cases | Few-shot examples (Task layer) |
| Machine-parseable result | Structured output + JSON Schema |
| Fewer made-up facts | Grounding + self-evaluation instruction |

## Talking points
1. A weak prompt returns prose you must parse and can't trust; a **PRECISE + structured** prompt returns
   a validated object every time. The demo shows both, side by side.
2. Prompt layers are **reused** across tasks (Base/Role stay cached → near-zero repeat cost).
3. Don't shout ("CRITICAL: YOU MUST"): modern Claude follows plain instructions; over-forcing back-fires.

## Run it
```bash
python topics/02-prompt-engineering/demo.py
```

## Reuses (DRY)
- `core.assemble_system`, `core.read_prompt` — hierarchy assembly
- `prompts/base|role|task|output/…` — the four layers
- `prompts/frameworks/precise.md` — the checklist
- `providers.claude.ClaudeProvider.structured_chat` — JSON-Schema-constrained output
