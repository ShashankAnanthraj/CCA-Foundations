"""core.providers — generic helpers + adapter factory (all offline, no key)."""

from __future__ import annotations

import pytest

from core.providers import ChatMessage, LLMProvider, Usage, get_provider_class


class _Bare(LLMProvider):
    """Minimal concrete provider to exercise the base-class helpers."""

    pricing = {"m": (2.0, 4.0)}  # $/1M in, out

    def chat(self, *a, **k):  # pragma: no cover - not used here
        raise NotImplementedError

    def stream_chat(self, *a, **k):  # pragma: no cover
        raise NotImplementedError

    def count_tokens(self, *a, **k):  # pragma: no cover
        raise NotImplementedError


def test_estimate_cost_includes_cache_multipliers():
    p = _Bare()
    usage = Usage(
        input_tokens=1_000_000,
        output_tokens=1_000_000,
        cache_read_input_tokens=1_000_000,
        cache_creation_input_tokens=1_000_000,
    )
    # 2 (in) + 4 (out) + 2*0.1 (cache read) + 2*1.25 (cache write) = 8.7
    assert p.estimate_cost(usage, "m") == pytest.approx(8.7)


def test_estimate_cost_unknown_model_is_zero():
    assert _Bare().estimate_cost(Usage(10, 10), "unknown") == 0.0


def test_normalize_accepts_chatmessage_and_dict():
    out = LLMProvider._normalize([ChatMessage("user", "hi"), {"role": "assistant", "content": "yo"}])
    assert out == [{"role": "user", "content": "hi"}, {"role": "assistant", "content": "yo"}]


def test_get_provider_class_resolves_offline():
    cls = get_provider_class("claude")
    assert cls.__name__ == "ClaudeProvider"


def test_get_provider_class_unknown_raises():
    with pytest.raises(ValueError):
        get_provider_class("nope")
