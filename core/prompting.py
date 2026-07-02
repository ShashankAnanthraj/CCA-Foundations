"""Prompt assembly — hierarchical, inherited, no duplication (Constitution: Prompt Engineering).

Purpose:    Load prompt layers from `prompts/` and compose them Base → Role → Task → Output-Spec.
Usage:      `from core.prompting import read_prompt, assemble_system`
Depends on: stdlib only.
Limits:     File-based composition. A registry/RAG layer can replace `read_prompt` later unchanged.
"""

from __future__ import annotations

from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parents[1] / "prompts"


def read_prompt(*parts: str) -> str:
    """Read a prompt file under `prompts/`, e.g. read_prompt('role', 'support_analyst.md')."""
    return (PROMPTS_DIR.joinpath(*parts)).read_text(encoding="utf-8").strip()


def assemble_system(*layers: str) -> str:
    """Join prompt layers (Base → Role → Task → Output-Spec) into one system prompt.

    Empty/blank layers are skipped so callers can pass optional layers freely.
    """
    return "\n\n".join(layer.strip() for layer in layers if layer and layer.strip())
