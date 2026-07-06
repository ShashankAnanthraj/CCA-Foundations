"""core.skills.SkillRegistry — discovery + progressive disclosure."""

from __future__ import annotations

import pytest

from core.skills import SkillRegistry, _split_frontmatter


def test_discover_finds_repo_skills():
    names = {m.name for m in SkillRegistry().discover()}
    assert {"sql-reviewer", "changelog-writer"} <= names


def test_metadata_has_description_but_body_not_loaded():
    metas = SkillRegistry().discover()
    sql = next(m for m in metas if m.name == "sql-reviewer")
    assert sql.description  # lightweight surface is populated
    assert sql.path.name == "SKILL.md"


def test_load_body_returns_full_instructions():
    body = SkillRegistry().load_body("sql-reviewer")
    assert "SQL Reviewer" in body


def test_load_body_unknown_raises():
    with pytest.raises(KeyError):
        SkillRegistry().load_body("nope")


def test_split_frontmatter_parses_meta_and_body():
    meta, body = _split_frontmatter("---\nname: x\ndescription: y\n---\nHELLO")
    assert meta == {"name": "x", "description": "y"}
    assert body == "HELLO"


def test_split_frontmatter_no_fence_returns_all_body():
    meta, body = _split_frontmatter("just text")
    assert meta == {}
    assert body == "just text"
