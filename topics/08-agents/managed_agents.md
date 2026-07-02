# Managed Agents (server-hosted) — reference

Two ways to run an agent:

| | Self-hosted (Topics 08–09) | Managed Agents |
|---|---|---|
| Who runs the loop | You (our `run_tools` / orchestration) | Anthropic's orchestration layer |
| Where tools execute | Your process | A per-session container Anthropic provisions |
| State | You hold it | Server-managed session + event stream |
| Best for | Full control, custom compute | Stateful agents with a workspace, less infra |

## The mandatory flow: Agent (once) → Session (every run)
`model`/`system`/`tools` live on the **Agent** (a persisted, versioned object). Sessions only reference it.

```python
import anthropic
client = anthropic.Anthropic()

# 1) Create the agent ONCE (store agent.id; reuse across runs)
agent = client.beta.agents.create(
    name="Repo Assistant",
    model="claude-opus-4-8",
    system="You are a careful coding assistant.",
    tools=[{"type": "agent_toolset_20260401"}],   # built-in bash/read/write/edit/grep/web
)

# 2) Start a Session per run, then stream events
session = client.beta.sessions.create(agent=agent.id, environment_id=ENV_ID)
with client.beta.sessions.events.stream(session_id=session.id) as stream:
    client.beta.sessions.events.send(
        session_id=session.id,
        events=[{"type": "user.message", "content": [{"type": "text", "text": "Review the auth module"}]}],
    )
    for event in stream:
        if event.type == "agent.message":
            for b in event.content:
                if b.type == "text":
                    print(b.text, end="")
        elif event.type == "session.status_idle":
            break
```

## Key points (exam-relevant)
- **Never** put `model`/`system`/`tools` on the session — they belong to the agent. Session = pointer.
- Agents are **versioned**; pin a session to a version for reproducibility.
- Sessions stream events; custom tools round-trip via `agent.custom_tool_use` → `user.custom_tool_result`.
- Credentials for MCP servers live in **vaults** attached via `vault_ids` (Topic 07).
- Multiagent: an agent can declare a coordinator roster to delegate to (Topic 09).

This is a reference (not run by `demo.py`) — Managed Agents needs an environment and incurs cost.
