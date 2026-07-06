"""Topic 07 — Document-then-PR with role profiles (runnable, DRY-RUN safe).

The capability you asked for: point the app at a project and have it (1) generate documentation and
(2) open a pull request — using the MCP client bridge + role profiles, with nothing hard-coded per
vendor.

    tech-writer profile ─► filesystem MCP ─► reads real files ─► writes docs markdown
    software-engineer   ─► github (remote) MCP ─► opens a PR with those docs

Safety: this script is a **dry run**. It generates docs locally (into git-ignored `runtime/`) and,
for the PR step, only *plans* the pull request (and lists GitHub tools if a token is present) — it
never creates a branch, commit, or PR. Wire it live by adding `GITHUB_TOKEN` to `.env` and taking
the marked step (left as the explicit, authorized action).

Run:   python topics/07-advanced-mcp/document_and_pr.py
Needs: pip install -e ".[mcp]"  ·  Node/npx (filesystem server)  ·  ANTHROPIC_API_KEY (doc step)
       GITHUB_TOKEN is OPTIONAL here — without it you get the PR plan; with it, tool discovery too.
"""

from __future__ import annotations

import os
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    pass

from core import (  # noqa: E402
    MCPClient,
    PROFILES,
    ServerSpec,
    build_agent,
    get_provider,
    get_settings,
    load_manifest,
)

DOC_TITLE = "MCP Client Bridge"
DOC_OUT = ROOT / "runtime" / "generated-docs" / "MCP-CLIENT-BRIDGE.md"
PR_BRANCH = "docs/mcp-client-bridge"


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


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


def plan_pull_request(doc_rel: str) -> dict:
    """The PR this flow would open (data only — nothing is created)."""
    return {
        "base": "main",
        "head": PR_BRANCH,
        "title": f"docs: add {DOC_TITLE} guide",
        "body": (
            f"Adds generated documentation for the MCP client bridge.\n\n"
            f"- New page: `{doc_rel}`\n- Authored by the tech-writer role via the MCP bridge."
        ),
        "files": [doc_rel],
    }


def main() -> None:
    settings = get_settings()
    provider = get_provider() if settings.has_api_key else None
    target = pathlib.Path(os.environ.get("AI_OS_TARGET_DIR") or ROOT)
    print(f"Target project: {target}")
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
            print(f"\n  wrote {DOC_OUT.relative_to(ROOT)} (git-ignored dry-run artifact)")
            print(f"  preview:\n  {preview}\n  ...")

    # ---- Phase B: PULL REQUEST (dry run) ----------------------------------- #
    hr("2) PULL REQUEST — plan the PR (dry run: nothing is created)")
    doc_rel = str(DOC_OUT.relative_to(ROOT)).replace("\\", "/")
    plan = plan_pull_request(doc_rel)
    print("  PR plan:")
    for k in ("base", "head", "title"):
        print(f"    {k:6}: {plan[k]}")
    print(f"    files : {plan['files']}")
    print(f"    body  : {plan['body'].splitlines()[0]} …")

    gh = load_manifest().get("github-remote")
    if gh and gh.startable:
        print("\n  GITHUB_TOKEN detected — connecting to the remote GitHub MCP (read-only tool discovery):")
        try:
            with MCPClient.from_manifest(["github-remote"]) as gmc:
                names = [t.name.split("__", 1)[-1] for t in gmc.tools]
                pr_tool = next((n for n in names if "pull_request" in n or "pr" in n), None)
                print(f"    discovered {len(names)} GitHub tools; PR tool = {pr_tool or '(not found)'}")
                print("    (dry run — NOT calling it. To go live, add an authorized create-PR step.)")
        except Exception as exc:
            print(f"    could not connect: {exc}")
    else:
        missing = ", ".join(gh.missing_env) if gh else "github-remote (not in manifest)"
        print(f"\n  No live PR: set {missing} in .env to enable the remote GitHub MCP, then wire the")
        print("  authorized create-PR step. Until then this stays a safe plan.")

    hr("Done — document-then-PR flow (dry run)")
    print("  Same roles + bridge, with GITHUB_TOKEN set, become real docs PRs on any project.")


if __name__ == "__main__":
    main()
