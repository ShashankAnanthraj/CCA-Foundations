"""core.config.get_settings — env-driven, per-provider defaults."""

from __future__ import annotations

from core.config import get_settings

_ENV = ("AI_OS_PROVIDER", "AI_OS_DEFAULT_MODEL", "AI_OS_MAX_TOKENS", "ANTHROPIC_API_KEY", "GROQ_API_KEY")


def _clear(monkeypatch):
    for k in _ENV:
        monkeypatch.delenv(k, raising=False)


def test_defaults(monkeypatch):
    _clear(monkeypatch)
    s = get_settings()
    assert s.provider == "claude"
    assert s.default_model == "claude-opus-4-8"
    assert s.max_tokens == 1024
    assert s.has_api_key is False


def test_provider_switch_and_key(monkeypatch):
    _clear(monkeypatch)
    monkeypatch.setenv("AI_OS_PROVIDER", "groq")
    monkeypatch.setenv("GROQ_API_KEY", "secret")
    monkeypatch.setenv("AI_OS_MAX_TOKENS", "256")
    get_settings.cache_clear()
    s = get_settings()
    assert s.provider == "groq"
    assert s.default_model == "openai/gpt-oss-120b"
    assert s.max_tokens == 256
    assert s.has_api_key is True


def test_explicit_model_overrides_provider_default(monkeypatch):
    _clear(monkeypatch)
    monkeypatch.setenv("AI_OS_DEFAULT_MODEL", "claude-haiku-4-5")
    get_settings.cache_clear()
    assert get_settings().default_model == "claude-haiku-4-5"
