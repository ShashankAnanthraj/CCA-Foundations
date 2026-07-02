# One-pager — Topic 03: Skills

**Slide headline:** 500 skills fit in context because the model only sees the menu, not the cookbook.

**Demo beats (`topics/03-skills/demo.py`):**
1. Discover skills → prints just name + description (the always-loaded metadata).
2. Route a SQL task → picks `sql-reviewer` (body still not loaded).
3. Load body on demand → only the chosen skill's instructions enter context.
4. Apply → Base prompt + skill body produces a guided review.

**Say this:**
- "A skill is a `SKILL.md`: frontmatter (name, description) + a body of expertise."
- "Progressive disclosure = descriptions always loaded, bodies loaded on demand. That's how it scales."
- "The description IS the trigger — write 'what it does + *when* to use it.'"
- "Anthropic Agent Skills (pptx/xlsx/pdf/docx) run server-side in a container and emit real files —
  same idea, hosted." (see prebuilt_agent_skills.md)

**Top pitfall:** a vague `description` → the skill never triggers (or triggers wrongly). Be specific about *when*.

**CCA‑F:** Claude Code / Skills (part of the 20% Claude Code Config domain); reused in Topic 11.
