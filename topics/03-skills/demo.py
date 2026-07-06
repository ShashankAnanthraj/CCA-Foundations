"""Topic 03 — Skills (runnable demo).

Demonstrates progressive disclosure with the shared SkillRegistry:
  1. Discover skills        (metadata ONLY — the cheap 'menu' always in context)
  2. Select for a task      (route by description; body still not loaded)
  3. Load body on demand    (full instructions for the ONE chosen skill)
  4. Apply the skill         (Base prompt + skill body -> guided answer)

Run:  python topics/03-skills/demo.py
Needs: .env with ANTHROPIC_API_KEY (step 4 only)
See:  prebuilt_agent_skills.md for Anthropic's API-hosted skills (pptx/xlsx/pdf/docx).
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import SkillMeta, SkillRegistry, assemble_system, get_settings, read_prompt  # noqa: E402
from core.providers import ChatMessage                                                 # noqa: E402
from core import get_provider                                            # noqa: E402

TASK = (
    "Review this SQL query for issues:\n"
    "    SELECT * FROM users WHERE email = '\" + user_input + \"'"
)


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def select_skill(task: str, metas: list[SkillMeta]) -> SkillMeta | None:
    """Cheap router: score each skill by description-word overlap with the task.

    (In production you can let the model route — this stays deterministic and free.)
    """
    task_words = {w.strip(".,:'\"()").lower() for w in task.split()}
    best, best_score = None, 0
    for m in metas:
        words = {w.strip(".,:'\"()").lower() for w in m.description.split() if len(w) > 3}
        score = len(task_words & words)
        if score > best_score:
            best, best_score = m, score
    return best


def main() -> None:
    settings = get_settings()
    reg = SkillRegistry()

    # 1) DISCOVER (metadata only) ------------------------------------------ #
    hr("1) Discover skills — only name + description load (progressive disclosure)")
    metas = reg.discover()
    for m in metas:
        print(f"  - {m.name}: {m.description}")
    print(f"\n  Context cost so far: {len(metas)} one-line descriptions (not full bodies).")

    # 2) SELECT ------------------------------------------------------------- #
    hr("2) Route the task to a skill (body still NOT loaded)")
    print(f"  task: {TASK.splitlines()[0]} ...")
    chosen = select_skill(TASK, metas)
    if not chosen:
        print("  no matching skill.")
        return
    print(f"  selected -> {chosen.name}")

    # 3) LOAD ON DEMAND ----------------------------------------------------- #
    hr("3) Load ONLY the chosen skill's body")
    body = reg.load_body(chosen.name)
    print(f"  loaded '{chosen.name}' body = {len(body)} chars (this is what enters context now)")

    if not settings.has_api_key:
        print("\n(Set ANTHROPIC_API_KEY in .env to run step 4.)")
        return

    # 4) APPLY -------------------------------------------------------------- #
    hr("4) Apply the skill: Base prompt + skill body -> guided answer")
    provider = get_provider()
    system = assemble_system(read_prompt("base", "base_system.md"), body)
    resp = provider.chat(
        [ChatMessage("user", TASK)],
        system=system,
        model=settings.default_model,
        max_tokens=settings.max_tokens,
    )
    print("  " + resp.text.strip().replace("\n", "\n  "))
    cost = provider.estimate_cost(resp.usage, resp.model)
    print(f"\n  [tokens in={resp.usage.input_tokens} out={resp.usage.output_tokens}] "
          f"[est. cost=${cost:.6f}]")

    hr("Done — Topic 03 complete")
    print("  500 skills = 500 one-line descriptions in context, not 500 documents.")


if __name__ == "__main__":
    main()
