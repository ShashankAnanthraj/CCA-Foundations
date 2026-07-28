"""Topic 07 — Document-then-PR with role profiles (runnable).

Point the app at a project and have it (1) generate documentation and (2) open a real pull request —
using the MCP client bridge + role profiles, with nothing hard-coded per vendor.

    tech-writer profile ─► filesystem MCP ─► reads real files ─► writes docs markdown
    software-engineer   ─► GitHub (remote) MCP ─► branch + commit + open a PR with those docs

Two modes:
  • DEFAULT (dry run) — generates docs into git-ignored `runtime/` and only *plans* the PR. Safe:
    no branch, no commit, no PR.
  • `--live` — actually opens a PR via the remote GitHub MCP. Requires `GITHUB_TOKEN` in `.env`.
    Least privilege: the GitHub toolset is `allow`-filtered to branch/file/PR-create tools only —
    it cannot merge, close, or delete anything.

Run:   python topics/07-advanced-mcp/document_and_pr.py            # dry run
       python topics/07-advanced-mcp/document_and_pr.py --live     # open a real PR
Needs: pip install -e ".[mcp]"  ·  Node/npx (filesystem server)  ·  ANTHROPIC_API_KEY  ·
       GITHUB_TOKEN (only for --live; a fine-grained PAT with Contents + Pull requests: read/write).
"""

from __future__ import annotations

import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    pass

from core import (  # noqa: E402
    PROFILES,
    ChatMessage,
    MCPClient,
    ServerSpec,
    ToolCall,
    build_agent,
    get_provider,
    get_settings,
    load_manifest,
    role_system,
)

DOC_TITLE = "MCP Client Bridge"
DOC_OUT = ROOT / "runtime" / "generated-docs" / "MCP-CLIENT-BRIDGE.md"  # local dry-run artifact
REPO_DOC_PATH = "docs/generated/MCP-CLIENT-BRIDGE.md"                    # path committed in the PR
PR_BRANCH = "docs/mcpclient"

# Only these GitHub tools are exposed to the agent (least privilege — no merge/close/delete).
GH_ALLOW = {
    "get_me",
    "list_branches",
    "get_file_contents",
    "create_branch",
    "create_or_update_file",
    "create_pull_request",
}


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def repo_slug() -> tuple[str, str] | None:
    """Derive (owner, repo) from the git origin remote."""
    try:
        url = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"], cwd=str(ROOT), text=True
        ).strip()
    except Exception:
        return None
    if url.endswith(".git"):
        url = url[:-4]
    path = url.split(":", 1)[-1] if url.startswith("git@") else "/".join(url.split("/")[-2:])
    parts = [p for p in path.split("/") if p]
    return (parts[-2], parts[-1]) if len(parts) >= 2 else None


def generate_docs(provider, settings, target: pathlib.Path) -> str | None:
    """tech-writer role reads the real project via filesystem MCP and returns docs markdown."""
    if not shutil.which("npx"):
        print("  (skipped: Node/npx not found — the filesystem MCP server needs it)")
        return None
    fs = ServerSpec(
        name="filesystem",
        transport="stdio",
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", str(target)],
    )
    profile = PROFILES["tech-writer"]
    with MCPClient([fs]) as mc:
        print(f"  tech-writer toolset: {len(mc.tools)} filesystem tools")
        agent = build_agent(profile, provider, mc, model=settings.default_model, max_tokens=settings.max_tokens)
        task = (
            f"Read README.md and core/mcp_client.py in this project, then write a concise Markdown "
            f"docs page titled '{DOC_TITLE}' explaining what the MCP client bridge does and how to "
            f"use it (a short intro + a tiny usage example). Use the tools to read the real files. "
            f"Output ONLY the Markdown."
        )
        return agent.run(task).text.strip()


def plan_pull_request() -> dict:
    """The PR this flow would open (data only)."""
    return {
        "base": "the repo default branch (main/master)",
        "head": PR_BRANCH,
        "title": f"docs: add {DOC_TITLE} guide",
        "body": "Adds tech-writer-generated documentation for the MCP client bridge.",
        "file": REPO_DOC_PATH,
    }


def create_pr_live(provider, settings, doc_text: str, owner: str, repo: str) -> str:
    """LIVE: software-engineer agent opens a real PR via the allow-filtered GitHub MCP toolset."""
    with MCPClient.from_manifest(["github-remote"], allow=GH_ALLOW, connect_timeout=45) as mc:
        exposed = sorted(t.name.split("__", 1)[-1] for t in mc.tools)
        print(f"  GitHub toolset (allow-filtered): {exposed}")
        system = role_system(PROFILES["software-engineer"])
        task = (
            f"Open a documentation pull request on the GitHub repository {owner}/{repo} using the "
            f"available tools. Do exactly this, in order:\n"
            f"1. Determine the repository's default branch (use list_branches; it is 'main' or 'master').\n"
            f"2. Create a new branch named '{PR_BRANCH}' from that default branch.\n"
            f"3. Create a new file at path '{REPO_DOC_PATH}' on branch '{PR_BRANCH}', commit message "
            f"'docs: add {DOC_TITLE} guide', with EXACTLY the content between the <<<DOC>>> and "
            f"<<<END>>> markers below (do not alter it).\n"
            f"4. Open a pull request from '{PR_BRANCH}' into the default branch, title "
            f"'docs: add {DOC_TITLE} guide', body noting the docs were generated by the tech-writer "
            f"role via the MCP bridge.\n"
            f"Then report the pull request number and URL.\n\n"
            f"<<<DOC>>>\n{doc_text}\n<<<END>>>"
        )

        def trace(call: ToolCall) -> None:  # show tool + arg keys only (not the doc content)
            print(f"    -> {call.name}({', '.join(sorted(call.input))})")

        result = provider.run_tools(
            [ChatMessage("user", task)],
            tools=mc.tools,
            handlers=mc.handlers,
            system=system,
            model=settings.default_model,
            max_tokens=4096,
            max_iters=10,
            on_tool_call=trace,
        )
        return result.final_text


def main() -> None:
    live = "--live" in sys.argv
    settings = get_settings()
    provider = get_provider() if settings.has_api_key else None
    target = pathlib.Path(os.environ.get("AI_OS_TARGET_DIR") or ROOT)
    print(f"Target project: {target}   mode: {'LIVE (will open a real PR)' if live else 'dry run'}")
    print(f"Roles available: {', '.join(PROFILES)}")

    # ---- Phase A: DOCUMENT ------------------------------------------------- #
    hr("1) DOCUMENT — tech-writer reads the project and generates a docs page")
    doc = None
    if provider is None:
        print("  (skipped: set ANTHROPIC_API_KEY to generate docs with the LLM)")
    else:
        doc = generate_docs(provider, settings, target)
        if doc:
            DOC_OUT.parent.mkdir(parents=True, exist_ok=True)
            DOC_OUT.write_text(doc + "\n", encoding="utf-8")
            preview = "\n  ".join(doc.splitlines()[:8])
            print(f"\n  wrote {DOC_OUT.relative_to(ROOT)} (local artifact)")
            print(f"  preview:\n  {preview}\n  ...")

    # ---- Phase B: PULL REQUEST --------------------------------------------- #
    gh = load_manifest().get("github-remote")
    plan = plan_pull_request()

    if not live:
        hr("2) PULL REQUEST — plan only (dry run: nothing is created)")
        print("  PR plan:")
        for k in ("base", "head", "title", "file"):
            print(f"    {k:5}: {plan[k]}")
        if gh and gh.startable:
            print("\n  GITHUB_TOKEN detected — re-run with --live to open this PR for real.")
        else:
            missing = ", ".join(gh.missing_env) if gh else "github-remote (not in manifest)"
            print(f"\n  No live PR: set {missing} in .env, then re-run with --live.")
        hr("Done — dry run")
        return

    # LIVE
    hr("2) PULL REQUEST — LIVE (opening a real PR via the GitHub MCP)")
    if not (gh and gh.startable):
        missing = ", ".join(gh.missing_env) if gh else "github-remote (not in manifest)"
        print(f"  Aborting --live: set {missing} in .env first.")
        return
    if not doc:
        print("  Aborting --live: need a generated doc (requires ANTHROPIC_API_KEY + npx).")
        return
    slug = repo_slug()
    if not slug:
        print("  Aborting --live: could not determine owner/repo from the git origin remote.")
        return
    owner, repo = slug
    print(f"  repo: {owner}/{repo}   branch: {PR_BRANCH}   file: {REPO_DOC_PATH}\n")
    final = create_pr_live(provider, settings, doc, owner, repo)
    print("\n  result:\n  " + final.strip().replace("\n", "\n  "))
    hr("Done — live PR flow")


if __name__ == "__main__":
    main()
