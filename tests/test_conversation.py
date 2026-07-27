"""core.conversation.Conversation — multi-turn history + cumulative usage (FakeProvider)."""

from __future__ import annotations

from core.conversation import Conversation


def test_ask_accumulates_history_and_usage(fake_provider):
    convo = Conversation(fake_provider, system="be brief")
    convo.ask("hello")
    convo.ask("again")
    # 2 user + 2 assistant turns recorded.
    assert len(convo.history) == 4
    assert [m.role for m in convo.history] == ["user", "assistant", "user", "assistant"]
    # FakeProvider reports 10 in / 5 out per call → 20 / 10 over two turns.
    assert convo.totals.input_tokens == 20
    assert convo.totals.output_tokens == 10


def test_ask_returns_response_text(fake_provider):
    convo = Conversation(fake_provider, system="s")
    resp = convo.ask("ping")
    assert resp.text == "echo: ping"
