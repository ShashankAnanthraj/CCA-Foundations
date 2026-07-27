"""Groq provider — a thin subclass of the shared OpenAI-compatible base.

Groq serves open models on its LPU inference stack via an OpenAI-compatible API (one
`GROQ_API_KEY`, free tier, very fast). All behavior lives in
`providers.openai_compat.OpenAICompatibleProvider`; this class only pins the endpoint, key,
default model, and pricing.  Get a free key at https://console.groq.com/keys.
"""

from __future__ import annotations

from providers.openai_compat import OpenAICompatibleProvider


class GroqProvider(OpenAICompatibleProvider):
    """Groq provider. Reads GROQ_API_KEY from the environment."""

    LABEL = "groq"
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY_ENV = "GROQ_API_KEY"

    # Default supports BOTH tool-calling and strict json_schema structured output — required for
    # Topics 02/08/09. Note: Groq restricts json_schema to specific models (e.g. the gpt-oss ones);
    # llama-3.3-70b-versatile does tools but NOT json_schema. See
    # https://console.groq.com/docs/structured-outputs#supported-models. Override via AI_OS_DEFAULT_MODEL.
    DEFAULT_MODEL = "openai/gpt-oss-120b"

    # $ per 1M tokens (input, output). Free/preview tiers ≈ 0; unlisted models fall back to (0, 0).
    pricing = {
        "openai/gpt-oss-120b": (0.0, 0.0),
        "openai/gpt-oss-20b": (0.0, 0.0),
        "llama-3.3-70b-versatile": (0.0, 0.0),  # tools yes, json_schema NO
        "llama-3.1-8b-instant": (0.0, 0.0),
    }
