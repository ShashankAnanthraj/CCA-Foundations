"""Groq provider package (capability plane).

Exposes `GroqProvider`, a thin subclass of the shared OpenAI-compatible base. Groq's inference API
is OpenAI-compatible, so it reuses the `openai` SDK — no new dependency. Free tier, very fast (LPU).
"""

from providers.groq.adapter import GroqProvider

__all__ = ["GroqProvider"]
