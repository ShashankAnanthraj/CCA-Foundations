"""Conversation — stateful multi-turn over the stateless Messages API (Context Management).

Purpose:    Manage history across turns and (optionally) cache the system prefix so repeated turns
            pay ~0.1x on the cached portion. Tracks cumulative token usage.
Usage:      `c = Conversation(provider, system); c.ask("hi"); print(c.totals)`
Depends on: core.providers.
Note:       The API is stateless — full history is resent each turn. Caching + selective context are
            how we keep that affordable (see the CALM framework).
"""

from __future__ import annotations

from core.providers import ChatMessage, LLMProvider, LLMResponse, Usage


class Conversation:
    """A multi-turn conversation with cumulative usage tracking and optional system caching."""

    def __init__(
        self,
        provider: LLMProvider,
        system: str,
        *,
        model: str | None = None,
        max_tokens: int | None = None,
        cache_system: bool = True,
    ) -> None:
        self.provider = provider
        self.system = system
        self.model = model
        self.max_tokens = max_tokens
        self.cache_system = cache_system
        self.history: list[ChatMessage] = []
        self._in = self._out = self._cr = self._cc = 0

    def ask(self, text: str) -> LLMResponse:
        self.history.append(ChatMessage("user", text))
        resp = self.provider.chat(
            self.history,
            system=self.system,
            model=self.model,
            max_tokens=self.max_tokens,
            cache=self.cache_system,
        )
        self.history.append(ChatMessage("assistant", resp.text))
        u = resp.usage
        self._in += u.input_tokens
        self._out += u.output_tokens
        self._cr += u.cache_read_input_tokens
        self._cc += u.cache_creation_input_tokens
        return resp

    @property
    def totals(self) -> Usage:
        """Cumulative usage across all turns so far."""
        return Usage(self._in, self._out, self._cr, self._cc)
