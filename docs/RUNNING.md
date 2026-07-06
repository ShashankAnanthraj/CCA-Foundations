# Running & Validating AI-OS

How to install, run the demos, and validate the project. Windows PowerShell is shown first; POSIX
equivalents are noted inline.

## 1. Install

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1            # POSIX: source .venv/bin/activate

pip install -e ".[mcp,dev]"          # base + MCP servers + test tooling
#   base only:            pip install -e .
#   just the MCP topics:  pip install -e ".[mcp]"
```

## 2. Configure

```powershell
copy .env.example .env               # POSIX: cp .env.example .env
```
Then edit `.env`:
- `ANTHROPIC_API_KEY` — required for the LLM demos (Topics 01–05, 08–10, 12).
- `AI_OS_PROVIDER` — `claude` (default) · `openrouter` · `groq`. Switching providers needs the
  matching key (`OPENROUTER_API_KEY` / `GROQ_API_KEY`) and extra (`pip install -e ".[openrouter]"`).
- MCP vars (Topic 07, all optional): `AI_OS_TARGET_DIR`, `GITHUB_TOKEN`, `AI_OS_DOCS_DIR`,
  `AI_OS_DEPLOY_MCP_URL`/`AI_OS_DEPLOY_TOKEN`, `AI_OS_QUERYOPT_MCP_URL`/`AI_OS_QUERYOPT_TOKEN`.

Secrets live only in `.env`. The live MCP manifest is `mcp/servers.json` (git-ignored; copy from
`mcp/servers.example.json`) and pulls secrets from the environment via `${VAR}` expansion.

## 3. Run the demos

```powershell
# No API key needed (MCP protocol; needs the mcp extra):
python topics/06-mcp/demo.py
python topics/07-advanced-mcp/demo.py

# Needs ANTHROPIC_API_KEY — any topic except 06/07 (Topic 11 is config-only, no demo):
python topics/01-foundations/demo.py
python topics/05-tool-use/demo.py
python topics/09-subagents-cowork/demo.py

# The MCP client bridge, live — a real agent USES a real MCP server:
#   set AI_OS_TARGET_DIR in .env first (a project path to expose to the filesystem server)
python topics/07-advanced-mcp/agent_with_mcp.py
```
`agent_with_mcp.py` degrades gracefully: it uses the filesystem MCP server if Node/`npx` is present
(else the repo's echo server), and a live agent if `ANTHROPIC_API_KEY` is set (else a no-LLM bridge
check). See the tracker of all 12 topics in [../topics/README.md](../topics/README.md).

### Create PRs & generate documentation

```powershell
python topics/07-advanced-mcp/document_and_pr.py
```
The **tech-writer** role reads the project via the filesystem MCP, generates a docs page (into
git-ignored `runtime/generated-docs/`), then **plans a pull request** via the remote GitHub MCP. It
is **dry-run safe** — no branch, commit, or PR is created.

To go live (create real PRs):
1. Create a GitHub Personal Access Token with repo scope and set `GITHUB_TOKEN` in `.env`.
2. The remote GitHub MCP (`github-remote` in `mcp/servers.json`, HTTP → `api.githubcopilot.com/mcp/`)
   becomes *startable*; the script will then discover its PR tools.
3. Add the explicit, authorized create-PR step (kept out until you opt in).

Roles are defined in `core/profiles.py` (`PROFILES`) as a persona prompt + a least-privilege MCP
toolset; add one by adding a `prompts/role/<name>.md` and a row there.

## 4. Validate

Two levels, both **key-free and free of cost**:

```powershell
# a) Syntax check — fast, compiles every module
python -m compileall -q core providers topics mcp

# b) Test suite — offline, deterministic (uses a FakeProvider; no API key, no network)
pytest -q
```

What the suite covers (`tests/`):
- **core** — config, prompt assembly, skills registry, tool/usage types, provider helpers
  (`estimate_cost`, `_normalize`, adapter factory), projects, conversation, and the agent
  orchestration patterns (router / pipeline / parallel / fan-out / gate) via `FakeProvider`.
- **MCP bridge** — manifest `${ENV}` expansion, `missing_env`, `startable` rules, the actionable
  "not startable → set VAR" error, tool namespacing, and an integration test that spins up the echo
  server over stdio and drives the async→sync handler path end-to-end.

The MCP integration test needs the `mcp` extra; it auto-skips if the SDK is absent, so the base
suite still passes. LLM demos are intentionally **not** run by the suite (they cost tokens).

## 5. CI

`.github/workflows/ci.yml` runs the syntax check + `pytest` on every push/PR across Python 3.10 and
3.12. It needs **no secrets** — the whole suite is key-free.

## Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `MCP server(s) not startable — filesystem (set AI_OS_TARGET_DIR)` | A `${VAR}` in `mcp/servers.json` is unset. Set it in `.env` (this is the intended, explicit error). |
| MCP demos: `MCP SDK not installed` | `pip install -e ".[mcp]"` |
| `agent_with_mcp.py` falls back to the echo server | Node/`npx` not on PATH — install Node to use the filesystem server. |
| LLM demo prints `Set ANTHROPIC_API_KEY …` | Add the key to `.env` (or switch `AI_OS_PROVIDER`). |
| `pytest` collects 0 tests | Run from the repo root; `testpaths=["tests"]` is set in `pyproject.toml`. |
