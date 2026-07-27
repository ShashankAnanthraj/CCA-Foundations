"""OpenRouter provider — a thin subclass of the shared OpenAI-compatible base.

OpenRouter is an OpenAI-compatible gateway (one `OPENROUTER_API_KEY`) fronting many models,
including free ones. All behavior lives in `providers.openai_compat.OpenAICompatibleProvider`;
this class only pins the endpoint, key, default model, and pricing.
"""

from __future__ import annotations

from providers.openai_compat import OpenAICompatibleProvider


class OpenRouterProvider(OpenAICompatibleProvider):
    """OpenRouter provider. Reads OPENROUTER_API_KEY from the environment."""

    LABEL = "openrouter"
    BASE_URL = "https://openrouter.ai/api/v1"
    API_KEY_ENV = "OPENROUTER_API_KEY"

    # Default to a FREE, INSTRUCT-style model that supports BOTH tool-calling and structured output
    # (so every topic works) and gives clean prose without leaking chain-of-thought. Free-model
    # availability changes over time; browse https://openrouter.ai/models?max_price=0 and set
    # AI_OS_DEFAULT_MODEL. Capable free alternates: openai/gpt-oss-20b:free ·
    # nvidia/nemotron-3-super-120b-a12b:free (reasoning) · openrouter/free (auto-router).
    DEFAULT_MODEL = "google/gemma-4-31b-it:free"

    # Optional attribution header OpenRouter uses for ranking; harmless if unset.
    default_headers = {"X-Title": "AI-OS"}

    # $ per 1M tokens (input, output). Free tiers are (0, 0); unlisted models fall back to (0, 0).
    pricing = {
        "google/gemma-4-31b-it:free": (0.0, 0.0),
        "openai/gpt-oss-20b:free": (0.0, 0.0),
        "nvidia/nemotron-3-super-120b-a12b:free": (0.0, 0.0),
        "meta-llama/llama-3.3-70b-instruct:free": (0.0, 0.0),
        "meta-llama/llama-3.3-70b-instruct": (0.12, 0.30),  # cheap PAID: no rate limits
        "anthropic/claude-opus-4-8": (5.0, 25.0),  # same model, via OpenRouter, if you want it
    }
