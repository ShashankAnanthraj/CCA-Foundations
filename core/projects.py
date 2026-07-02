"""Projects — lightweight configs that reference shared components (Constitution: Project Design).

Purpose:    A Project bundles *references* — model, project context files, skills — never copies. It
            stays lightweight and composes the shared capability plane.
Usage:      `p = load_project("projects/devrel_assistant/project.json"); sys = p.context_text()`
Depends on: stdlib only.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Project:
    """A project manifest: references to shared context + skills, plus a default model."""

    name: str
    description: str
    model: str | None
    context_files: list[str]
    skills: list[str]
    path: Path

    def context_text(self) -> str:
        """Concatenate the referenced project-context files (resolved from the repo root)."""
        parts: list[str] = []
        for rel in self.context_files:
            p = ROOT / rel
            if p.exists():
                parts.append(p.read_text(encoding="utf-8").strip())
        return "\n\n".join(parts)


def load_project(manifest_path: str | Path) -> Project:
    """Load a `project.json` manifest into a Project (references only, no duplication)."""
    p = Path(manifest_path)
    data = json.loads(p.read_text(encoding="utf-8"))
    return Project(
        name=data["name"],
        description=data.get("description", ""),
        model=data.get("model"),
        context_files=data.get("context", []),
        skills=data.get("skills", []),
        path=p,
    )
