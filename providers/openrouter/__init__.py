"""OpenRouter provider package (capability plane).

Exposes `OpenRouterProvider`, an OpenAI-compatible adapter for the OpenRouter gateway
(https://openrouter.ai). One key, many models — including free ones. Per ADR 0001, the
adapter module is the only place permitted to import the vendor SDK (`openai`).
"""

from providers.openrouter.adapter import OpenRouterProvider

__all__ = ["OpenRouterProvider"]
