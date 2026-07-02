# PRECISE — a prompt-engineering checklist

A repeatable structure for production prompts. Walk the seven letters top-to-bottom; each maps to a
layer of the prompt hierarchy (`Base → Role → Task → Output-Spec`).

| Letter | Element | Question it answers | Hierarchy layer |
|---|---|---|---|
| **P** | **Persona** | Who is the model acting as? | Role |
| **R** | **Result** | What exact outcome do we want? | Task |
| **E** | **Examples** | What do good inputs/outputs look like? (few-shot) | Task |
| **C** | **Context** | What grounding/background is relevant — and only that? | Task / Runtime |
| **I** | **Instructions** | What steps, rules, and constraints govern the work? | Task |
| **S** | **Specification** | What is the exact output shape (schema/format)? | Output-Spec |
| **E** | **Evaluation** | How does the model check itself and avoid hallucination? | Output-Spec |

## How each letter reduces failure
- **P/R** kill vagueness — the model stops guessing intent.
- **E (examples)** teach format and edge cases faster than prose.
- **C** grounds answers in facts → fewer hallucinations. Include *only* what's needed (token economy).
- **I** makes behavior deterministic and testable.
- **S** guarantees machine-parseable output (pair with structured outputs).
- **E (evaluation)** — instruct "if unsure, say so; cite sources" → the single biggest hallucination lever.

## Anti-patterns
- Aggressive shouting ("CRITICAL: YOU MUST…") — modern Claude follows plain instructions; over-forcing
  causes over-triggering. State the rule once, plainly.
- Dumping the whole knowledge base into Context — load selectively.

> **Note:** PRECISE is AI-OS's working checklist for the CCA‑F *Prompt Engineering* domain. If the
> exam vendor publishes a different letter expansion, reconcile here — the *practice* (persona, result,
> examples, grounded context, instructions, output spec, self-evaluation) is what matters and is stable.
