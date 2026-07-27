"""core.prompting — hierarchical prompt assembly."""

from __future__ import annotations

import pytest

from core.prompting import assemble_system, read_prompt


def test_read_prompt_loads_known_file():
    base = read_prompt("base", "base_system.md")
    assert base.strip()  # non-empty


def test_read_prompt_missing_raises():
    with pytest.raises(FileNotFoundError):
        read_prompt("role", "does_not_exist.md")


def test_assemble_joins_and_skips_blank_layers():
    out = assemble_system("A", "", "  ", "B")
    assert out == "A\n\nB"


def test_assemble_empty_is_empty_string():
    assert assemble_system("", None) == ""  # type: ignore[arg-type]
