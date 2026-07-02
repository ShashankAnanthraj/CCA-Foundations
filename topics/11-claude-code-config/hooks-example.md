# Hooks — deterministic automation around tool calls

Hooks run **your** shell commands at fixed points in Claude Code's lifecycle. The harness executes
them — not the model — so they're deterministic guarantees, not suggestions.

## Common events
| Event | Fires… | Use for |
|---|---|---|
| `PreToolUse` | before a tool runs | block/validate/gate an action |
| `PostToolUse` | after a tool runs | format, lint, compile, test |
| `Stop` | when the assistant finishes | notify, log, summarize |
| `UserPromptSubmit` | when you send a message | inject context, redact secrets |

## Example (from `settings.example.json`)
Compile-check the project every time a file is edited:
```json
"hooks": {
  "PostToolUse": [
    { "matcher": "Edit|Write",
      "hooks": [ { "type": "command", "command": "python -m compileall -q core providers topics mcp" } ] }
  ]
}
```

## Why hooks (vs asking the model)
- **Guaranteed:** a formatter/compile check that *always* runs can't be forgotten mid-task.
- **Fast + free:** no tokens spent.
- **Policy:** a `PreToolUse` deny is a hard gate (great with the SPIDER "Escalate" idea).

## Try it
Copy the `hooks` block into `.claude/settings.json`, then edit any file — the compile check runs
automatically. Remove it when done.

> Hooks are configured in `settings.json` (project or user scope). Keep destructive commands out of
> hooks; pair with `permissions.deny` for safety.
