# One-pager — Topic 02: Prompt Engineering

**Slide headline:** Same model, better prompt → prose you distrust becomes a validated object.

**Demo beats (`topics/02-prompt-engineering/demo.py`):**
1. Show the composed system prompt = 4 inherited layers (Base·Role·Task·Output) — written once, reused.
2. Weak prompt → free-form prose (must parse, can't trust).
3. PRECISE + structured output → JSON validated against a schema, every time.
4. Grounding → the model says "not provided" instead of inventing an email.

**Say this:**
- "Prompts are a hierarchy, not a paragraph. Base and Role are shared and cached — near-zero repeat cost."
- "PRECISE = Persona·Result·Examples·Context·Instructions·Specification·Evaluation. The last E — self-
  evaluation/grounding — is the biggest hallucination lever."
- "Structured outputs remove the fragile 'please return JSON' dance."

**Top pitfall to call out:** shouting at the model ("CRITICAL: YOU MUST…") over-triggers on modern Claude —
state the rule once, plainly.

**CCA‑F:** Prompt Engineering domain (20%).
