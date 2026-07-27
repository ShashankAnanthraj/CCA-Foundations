"""Provider-agnostic LLM interface + normalized types (Constitution: Model/Vendor-Agnostic).

Purpose:    One abstraction every capability/topic calls, so models and vendors are swappable.
Usage:      Subclass `LLMProvider` under `providers/<vendor>/`. Never import a vendor SDK above
            the capability plane — depend on this interface instead (see ADR 0001).
Depends on: stdlib only.
Limits:     Text-first normalization. Rich content blocks (images/PDF/tools) are added per topic.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterable, Iterator, Sequence


# --------------------------------------------------------------------------- #
# Normalized request / response types (identical across every provider)
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class ChatMessage:
    """A single turn. `role` is 'user' or 'assistant'."""

    role: str
    content: str


@dataclass(frozen=True)
class Usage:
    """Token accounting, normalized across providers."""

    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_input_tokens: int = 0
    cache_creation_input_tokens: int = 0

    @property
    def total_tokens(self) -> int:
        return (
            self.input_tokens
            + self.output_tokens
            + self.cache_read_input_tokens
            + self.cache_creation_input_tokens
        )


@dataclass(frozen=True)
class LLMResponse:
    """Normalized model response."""

    text: str
    model: str
    stop_reason: str | None
    usage: Usage
    raw: Any = field(default=None, repr=False)  # vendor-native object, if needed


# --------------------------------------------------------------------------- #
# The interface
# --------------------------------------------------------------------------- #
Messages = Sequence[ChatMessage] | Sequence[dict]


class LLMProvider(ABC):
    """Abstract model provider. Concrete adapters live under `providers/<vendor>/`.

    Cost estimation is generic here; only `pricing` is vendor-specific.
    """

    #: model id -> (input $/1M tokens, output $/1M tokens). Adapters override.
    pricing: dict[str, tuple[float, float]] = {}

    @abstractmethod
    def chat(
        self,
        messages: Messages,
        *,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
        thinking: bool = False,
        effort: str | None = None,
        cache: bool = False,
    ) -> LLMResponse:
        """One non-streaming completion. `effort` in {low,medium,high,xhigh,max}.

        `cache=True` marks the system prompt as a cacheable prefix (prompt caching) — reused
        across requests at ~0.1x cost when the prefix is byte-identical and above the model minimum.
        """

    @abstractmethod
    def stream_chat(
        self,
        messages: Messages,
        *,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
    ) -> Iterator[str]:
        """Yield text deltas as they arrive (for live rendering)."""

    @abstractmethod
    def count_tokens(
        self,
        messages: Messages,
        *,
        system: str | None = None,
        model: str | None = None,
    ) -> int:
        """Exact input-token count for the given request (never estimate client-side)."""

    # -- optional capability: structured output ----------------------------- #
    def structured_chat(
        self,
        messages: Messages,
        *,
        schema: dict,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
    ) -> tuple[dict, "LLMResponse"]:
        """Return (parsed_dict, response) validated against a JSON Schema.

        Optional: adapters that support constrained decoding override this. Default raises
        so a provider without the capability fails loudly rather than silently.
        """
        raise NotImplementedError(f"{type(self).__name__} does not support structured output")

    # -- optional capability: agentic tool loop ----------------------------- #
    def run_tools(
        self,
        messages: Messages,
        *,
        tools: "list",
        handlers: dict,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
        max_iters: int = 5,
        on_tool_call=None,
    ):
        """Drive an agentic loop: model → execute requested tools → feed results → repeat.

        `tools` is a list of `core.tools.ToolSpec`; `handlers` maps tool name → `Callable[[dict], str]`.
        Returns `core.tools.ToolLoopResult`. Optional: adapters override; base raises loudly.
        """
        raise NotImplementedError(f"{type(self).__name__} does not support tool use")

    # -- generic helpers (shared by all adapters) --------------------------- #
    def estimate_cost(self, usage: Usage, model: str) -> float:
        """USD cost estimate from usage + this provider's pricing table."""
        in_rate, out_rate = self.pricing.get(model, (0.0, 0.0))
        # Cache reads are ~0.1x input; cache writes ~1.25x input (approx, for display).
        return (
            usage.input_tokens * in_rate
            + usage.cache_read_input_tokens * in_rate * 0.1
            + usage.cache_creation_input_tokens * in_rate * 1.25
            + usage.output_tokens * out_rate
        ) / 1_000_000

    @staticmethod
    def _normalize(messages: Messages) -> list[dict]:
        """Accept ChatMessage or plain dicts; emit the wire format `{role, content}`."""
        out: list[dict] = []
        for m in messages:
            if isinstance(m, ChatMessage):
                out.append({"role": m.role, "content": m.content})
            else:
                out.append({"role": m["role"], "content": m["content"]})
        return out


# --------------------------------------------------------------------------- #
# Provider selection (factory) — keeps the model/vendor swap to one env var.
# Imports are lazy so `core` never imports a vendor SDK at module load (ADR 0001):
# each adapter module — the only place allowed to import its SDK — is imported on demand.
# --------------------------------------------------------------------------- #
# provider name -> (module path, class name). Imported lazily so `core` never loads a vendor SDK
# at module import (ADR 0001). Add a row to support a new provider.
_ADAPTERS = {
    "claude": ("providers.claude", "ClaudeProvider"),
    "openrouter": ("providers.openrouter", "OpenRouterProvider"),
    "groq": ("providers.groq", "GroqProvider"),
}


def get_provider_class(name: str | None = None) -> type[LLMProvider]:
    """Return the adapter CLASS for `name` (or the configured provider). No key required —
    use this for the offline model-catalog / pricing sections of demos."""
    import importlib

    from core.config import get_settings

    name = (name or get_settings().provider).lower()
    entry = _ADAPTERS.get(name)
    if entry is None:
        raise ValueError(
            f"unknown provider {name!r} (set AI_OS_PROVIDER to one of: {', '.join(_ADAPTERS)})"
        )
    module, cls = entry
    return getattr(importlib.import_module(module), cls)


def get_provider(name: str | None = None) -> LLMProvider:
    """Construct the configured provider. The adapter resolves its own key from the environment."""
    return get_provider_class(name)()
