"""Topic 04 — Projects & Artifacts (runnable demo).

  1. Load a PROJECT manifest — references to shared context + skills (lightweight)
  2. Build a project-scoped system (Base + project context) and answer a grounded question
  3. Generate an ARTIFACT (a markdown release note) and save it to disk

Run:  python topics/04-projects-artifacts/demo.py
Needs: .env with ANTHROPIC_API_KEY (steps 2–3)
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import ChatMessage, assemble_system, get_settings, load_project, read_prompt  # noqa: E402
from providers.claude import ClaudeProvider                                             # noqa: E402

MANIFEST = ROOT / "projects" / "devrel_assistant" / "project.json"
ARTIFACT_DIR = ROOT / "runtime" / "artifacts"  # gitignored


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main() -> None:
    settings = get_settings()

    # 1) LOAD PROJECT (references only) ------------------------------------ #
    hr("1) Load the project manifest — references to shared components (stays lightweight)")
    project = load_project(MANIFEST)
    print(f"  name:    {project.name}")
    print(f"  model:   {project.model}")
    print(f"  context: {project.context_files}   (references, not copies)")
    print(f"  skills:  {project.skills}")

    if not settings.has_api_key:
        print("\n(Set ANTHROPIC_API_KEY in .env to run steps 2–3.)")
        return
    provider = ClaudeProvider()
    model = project.model or settings.default_model
    system = assemble_system(read_prompt("base", "base_system.md"), project.context_text())

    # 2) GROUNDED ANSWER (project context) --------------------------------- #
    hr("2) Answer a question grounded in the PROJECT context")
    q = "A developer filing a bug asks which version to cite and where to email support. Answer briefly."
    resp = provider.chat([ChatMessage("user", q)], system=system, model=model, max_tokens=settings.max_tokens)
    print("  " + resp.text.strip().replace("\n", "\n  "))

    # 3) GENERATE + SAVE AN ARTIFACT --------------------------------------- #
    hr("3) Generate an ARTIFACT (markdown release note) and save it to disk")
    artifact = provider.chat(
        [ChatMessage("user", "Write a short markdown release note for AI-OS v0.1.0 in our house style.")],
        system=system,
        model=model,
        max_tokens=settings.max_tokens,
    )
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    out = ARTIFACT_DIR / "release-notes-v0.1.0.md"
    out.write_text(artifact.text.strip() + "\n", encoding="utf-8")
    print(f"  saved artifact -> {out.relative_to(ROOT)}")
    preview = "\n  ".join(artifact.text.strip().splitlines()[:4])
    print(f"  preview:\n  {preview}")

    hr("Done — Topic 04 complete")
    print("  Project = references (light). Artifact = a saved deliverable the model produced.")
    print("  Rich file artifacts (pptx/xlsx/pdf) come from Agent Skills — see Topic 03.")


if __name__ == "__main__":
    main()
