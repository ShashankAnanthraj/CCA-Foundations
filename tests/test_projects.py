"""core.projects.load_project — reference-only manifests."""

from __future__ import annotations

import json
from pathlib import Path

from core.projects import Project, load_project


def test_load_project_reads_manifest(tmp_path):
    manifest = tmp_path / "project.json"
    manifest.write_text(
        json.dumps(
            {
                "name": "demo",
                "description": "d",
                "model": "claude-haiku-4-5",
                "context": [],
                "skills": ["sql-reviewer"],
            }
        ),
        encoding="utf-8",
    )
    p = load_project(manifest)
    assert isinstance(p, Project)
    assert p.name == "demo"
    assert p.model == "claude-haiku-4-5"
    assert p.skills == ["sql-reviewer"]


def test_context_text_concatenates_existing_files_only():
    # References are resolved from the repo ROOT; a real file + a missing one.
    p = Project(
        name="x",
        description="",
        model=None,
        context_files=["README.md", "does/not/exist.md"],
        skills=[],
        path=Path("."),
    )
    text = p.context_text()
    assert "AI" in text  # README content present; missing file silently skipped
