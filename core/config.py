"""Configuration — environment-driven, secrets never in code (Constitution: Security).

Purpose:    Single place to read runtime settings from the environment / `.env`.
Usage:      `from core.config import get_settings; s = get_settings()`
Depends on: python-dotenv (optional; falls back to os.environ if absent).
Limits:     No secret storage — only reads. Never log `api_key`.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache

try:  # optional dependency; .env is a convenience, not a requirement
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # pragma: no cover
    pass


@dataclass(frozen=True)
class Settings:
    """Immutable runtime settings loaded from the environment."""

    api_key: str | None
    default_model: str
    max_tokens: int

    @property
    def has_api_key(self) -> bool:
        return bool(self.api_key)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return process-wide settings (cached). Reads env once."""
    return Settings(
        api_key=os.environ.get("ANTHROPIC_API_KEY") or None,
        default_model=os.environ.get("AI_OS_DEFAULT_MODEL", "claude-opus-4-8"),
        max_tokens=int(os.environ.get("AI_OS_MAX_TOKENS", "1024")),
    )
