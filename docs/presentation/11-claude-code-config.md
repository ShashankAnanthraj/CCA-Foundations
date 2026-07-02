# One-pager — Topic 11: Claude Code Configuration

**Slide headline:** CLAUDE.md is memory, settings.json is policy, commands are shortcuts, hooks are guarantees.

**Demo beats (live in Claude Code — no API script):**
1. `CLAUDE.md` (repo root) → auto-loaded conventions the agent follows every session.
2. `settings.example.json` → `allow`/`ask`/`deny` permissions (e.g. `deny: Read(.env)`).
3. `/topic 05` → a real custom slash command (from `.claude/commands/topic.md`).
4. `hooks-example.md` → a `PostToolUse` hook that compile-checks on every edit.
5. `.mcp.json` → plug in the Topic 06 MCP server.

**Say this:**
- "`CLAUDE.md` = persistent memory; project scope is shared, user scope is personal; specific wins."
- "Permissions gate tools: `deny` is a hard stop the model can't talk its way past — security + SPIDER."
- "Slash commands are reusable prompts; `$ARGUMENTS` passes input."
- "Hooks run *your* shell commands deterministically — format/compile/test with zero tokens."

**Top pitfall:** relying on prompt instructions for safety — use `permissions.deny` / a `PreToolUse` hook; those can't be bypassed.

**CCA‑F:** Claude Code Configuration (20%).
