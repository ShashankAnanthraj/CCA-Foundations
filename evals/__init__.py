"""Evaluations capability — assertion + LLM-as-judge scoring (see harness.py).

Vendor-neutral: everything runs through `core.providers.LLMProvider`, so evals work with any
provider (and with a fake provider in tests — no API key needed for the assertion path).
"""

from evals.harness import (
    CheckResult,
    EvalCase,
    EvalResult,
    contains,
    is_json,
    llm_judge,
    matches,
    max_words,
    not_contains,
    run_evals,
    summarize,
)

__all__ = [
    "CheckResult",
    "EvalCase",
    "EvalResult",
    "contains",
    "not_contains",
    "matches",
    "max_words",
    "is_json",
    "llm_judge",
    "run_evals",
    "summarize",
]
