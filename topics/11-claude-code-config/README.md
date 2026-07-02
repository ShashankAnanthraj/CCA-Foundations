# Topic 11 — Claude Code Configuration

**Purpose:** Configure the Claude Code harness itself — memory, permissions, commands, hooks, MCP —
so the agent works *your* way, safely (CCA‑F *Claude Code Configuration*, 20%).

> This topic is exercised **inside Claude Code**, not via the API. The demo *is* the config files.

## Concept
- **`CLAUDE.md`** = persistent project memory auto-loaded each session (conventions, commands, layout).
  Scopes: **project** (`./CLAUDE.md`, shared) vs **user** (`~/.claude/CLAUDE.md`, personal). More
  specific wins. This repo ships a real one at the root.
- **`settings.json` permissions:** `allow` / `ask` / `deny` gate tool calls (e.g. `deny: Read(.env)`).
  Scopes: project (`.claude/settings.json`) · local (`.claude/settings.local.json`) · user.
- **Slash commands:** custom commands in `.claude/commands/*.md`. This repo ships `/topic` — try
  `/topic 05`. `$ARGUMENTS` passes input into the command's prompt.
- **Hooks:** shell commands the harness runs at lifecycle points (PreToolUse, PostToolUse, Stop…).
  Deterministic, token-free automation. See `hooks-example.md`.
- **MCP integration:** wire servers via `.mcp.json` or `claude mcp add` — see
  [../06-mcp/claude-code-setup.md](../06-mcp/claude-code-setup.md).

## When to use what
| Need | Reach for |
|---|---|
| Team-wide conventions the agent should always know | `CLAUDE.md` (project) |
| Prevent risky actions | `permissions.deny` (+ `ask`) |
| Reusable prompt you invoke often | Slash command |
| Guaranteed format/compile/test every edit | `PostToolUse` hook |
| Give the agent external tools | MCP server (`.mcp.json`) |

## Talking points
1. `CLAUDE.md` is memory, `settings.json` is policy, commands are shortcuts, hooks are guarantees.
2. `deny` beats prompting — a hook/permission the model *cannot* bypass (great for security & SPIDER).
3. Project vs user scope: share via project files, personalize via user files.
4. The `/topic` command and root `CLAUDE.md` in this repo are live — try them now.

## Files (real + templates)
- `CLAUDE.md` (repo root) — live project memory
- `.claude/commands/topic.md` — live slash command (`/topic <n>`)
- `settings.example.json` — permissions + hooks template (copy into `.claude/settings.json`)
- `hooks-example.md` — hook events + a working example
- MCP wiring → `topics/06-mcp/claude-code-setup.md`
