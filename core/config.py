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


# Per-provider config: which env var holds the key, and the default model. Add a row to support
# a new provider (also register its adapter in core.providers._ADAPTERS).
_PROVIDERS = {
    "claude": {"key_env": "ANTHROPIC_API_KEY", "default_model": "claude-opus-4-8"},
    "openrouter": {"key_env": "OPENROUTER_API_KEY", "default_model": "google/gemma-4-31b-it:free"},
    "groq": {"key_env": "GROQ_API_KEY", "default_model": "openai/gpt-oss-120b"},
}


@dataclass(frozen=True)
class Settings:
    """Immutable runtime settings loaded from the environment."""

    provider: str
    api_key: str | None  # key for the SELECTED provider (None if unset)
    default_model: str
    max_tokens: int

    @property
    def has_api_key(self) -> bool:
        return bool(self.api_key)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return process-wide settings (cached). Reads env once."""
    provider = os.environ.get("AI_OS_PROVIDER", "claude").lower()
    meta = _PROVIDERS.get(provider, _PROVIDERS["claude"])
    return Settings(
        provider=provider,
        api_key=os.environ.get(meta["key_env"]) or None,
        default_model=os.environ.get("AI_OS_DEFAULT_MODEL") or meta["default_model"],
        max_tokens=int(os.environ.get("AI_OS_MAX_TOKENS", "1024")),
    )
