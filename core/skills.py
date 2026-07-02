"""Skills registry — reusable expertise with progressive disclosure (Constitution: Skill Design).

Purpose:    Discover skills by their lightweight metadata, and load a skill's full body ONLY when
            it's selected — mirroring how Claude Agent Skills work (metadata always in context;
            body loaded on demand).
Usage:      `reg = SkillRegistry(); metas = reg.discover(); body = reg.load_body("sql-reviewer")`
Depends on: stdlib only.
Limits:     File-based (`skills/<name>/SKILL.md`). A DB/registry backend can replace it unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parents[1] / "skills"


@dataclass(frozen=True)
class SkillMeta:
    """Lightweight, always-loadable skill descriptor (the 'progressive disclosure' surface)."""

    name: str
    description: str
    path: Path


def _split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (metadata, body) from a `---`-delimited YAML-ish frontmatter block."""
    meta: dict[str, str] = {}
    lines = text.splitlines()
    fences = [i for i, ln in enumerate(lines) if ln.strip() == "---"]
    if len(fences) >= 2 and fences[0] == 0:
        for ln in lines[fences[0] + 1 : fences[1]]:
            if ":" in ln:
                key, val = ln.split(":", 1)
                meta[key.strip()] = val.strip()
        body = "\n".join(lines[fences[1] + 1 :]).strip()
        return meta, body
    return meta, text.strip()


class SkillRegistry:
    """Discovers `skills/<name>/SKILL.md` files and loads bodies on demand."""

    def __init__(self, skills_dir: Path = SKILLS_DIR) -> None:
        self.dir = skills_dir

    def discover(self) -> list[SkillMeta]:
        """Return metadata only for every skill (cheap; body NOT loaded)."""
        metas: list[SkillMeta] = []
        for skill_file in sorted(self.dir.glob("*/SKILL.md")):
            meta, _ = _split_frontmatter(skill_file.read_text(encoding="utf-8"))
            name = meta.get("name", skill_file.parent.name)
            metas.append(SkillMeta(name=name, description=meta.get("description", ""), path=skill_file))
        return metas

    def load_body(self, name: str) -> str:
        """Load the FULL instructions for one skill (progressive disclosure: on demand)."""
        for meta in self.discover():
            if meta.name == name:
                _, body = _split_frontmatter(meta.path.read_text(encoding="utf-8"))
                return body
        raise KeyError(f"skill not found: {name}")
