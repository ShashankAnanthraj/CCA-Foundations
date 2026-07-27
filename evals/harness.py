"""Evaluations — assertion + LLM-as-judge scoring for prompts and agents (Reliability domain).

Purpose:    Offline quality checks the CCA-F "Context Management & Reliability" domain expects but
            the topic demos don't cover: run a prompt/agent over cases, score each with cheap
            deterministic assertions and/or an LLM judge, and report a pass rate. This is *evaluation*
            (does the output meet a bar?), distinct from `tests/` (does the code run?).
Usage:      results = run_evals(provider, CASES, system=..., model=...); print(summarize(results))
Depends on: core.providers only (vendor-neutral — works with any LLMProvider, incl. the test fake).
Design:     Checks are `Callable[[str], CheckResult]`. Assertions are pure; the LLM judge takes a
            provider. Compose freely per case.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Callable

from core.providers import ChatMessage, LLMProvider

Check = Callable[[str], "CheckResult"]


@dataclass(frozen=True)
class CheckResult:
    """Outcome of one check against a single output."""

    name: str
    passed: bool
    detail: str = ""


@dataclass
class EvalCase:
    """One evaluation: either a `prompt` to run, or a fixed `output` to judge directly."""

    name: str
    checks: list[Check]
    prompt: str | None = None
    output: str | None = None  # supply to score an existing string without calling the model


@dataclass
class EvalResult:
    """Scored outcome for one case."""

    case: str
    output: str
    checks: list[CheckResult] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return bool(self.checks) and all(c.passed for c in self.checks)


# --------------------------------------------------------------------------- #
# Assertion checks (pure — no model, no key)
# --------------------------------------------------------------------------- #
def contains(substr: str, *, ignore_case: bool = True) -> Check:
    def check(out: str) -> CheckResult:
        hay = out.lower() if ignore_case else out
        needle = substr.lower() if ignore_case else substr
        ok = needle in hay
        return CheckResult(f"contains({substr!r})", ok, "" if ok else "substring not found")

    return check


def not_contains(substr: str, *, ignore_case: bool = True) -> Check:
    def check(out: str) -> CheckResult:
        inner = contains(substr, ignore_case=ignore_case)(out)
        return CheckResult(f"not_contains({substr!r})", not inner.passed,
                           "" if not inner.passed else "forbidden substring present")

    return check


def matches(pattern: str) -> Check:
    rx = re.compile(pattern)
    def check(out: str) -> CheckResult:
        ok = rx.search(out) is not None
        return CheckResult(f"matches({pattern!r})", ok, "" if ok else "regex did not match")

    return check


def max_words(n: int) -> Check:
    def check(out: str) -> CheckResult:
        count = len(out.split())
        return CheckResult(f"max_words({n})", count <= n, f"{count} words")

    return check


def is_json() -> Check:
    def check(out: str) -> CheckResult:
        try:
            json.loads(out)
            return CheckResult("is_json", True)
        except ValueError as exc:
            return CheckResult("is_json", False, str(exc))

    return check


# --------------------------------------------------------------------------- #
# LLM-as-judge (uses a provider's structured output)
# --------------------------------------------------------------------------- #
_JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["pass", "fail"]},
        "reason": {"type": "string"},
    },
    "required": ["verdict", "reason"],
    "additionalProperties": False,
}


def llm_judge(
    provider: LLMProvider,
    rubric: str,
    *,
    name: str = "llm_judge",
    model: str | None = None,
    max_tokens: int = 256,
) -> Check:
    """A check that asks the model to grade the output against `rubric` (constrained pass/fail)."""

    def check(out: str) -> CheckResult:
        parsed, _ = provider.structured_chat(
            [ChatMessage("user", f"RUBRIC:\n{rubric}\n\nOUTPUT TO JUDGE:\n{out}\n\n"
                                 "Judge whether the output satisfies the rubric; return a verdict "
                                 "and a brief reason.")],
            schema=_JUDGE_SCHEMA,
            system="You are a strict, fair evaluator. Judge only against the rubric.",
            model=model,
            max_tokens=max_tokens,
        )
        return CheckResult(name, parsed.get("verdict") == "pass", parsed.get("reason", ""))

    return check


# --------------------------------------------------------------------------- #
# Runner + summary
# --------------------------------------------------------------------------- #
def run_evals(
    provider: LLMProvider,
    cases: list[EvalCase],
    *,
    system: str | None = None,
    model: str | None = None,
    max_tokens: int | None = None,
) -> list[EvalResult]:
    """Run each case (generate output if `prompt` given, else use `output`) and apply its checks."""
    results: list[EvalResult] = []
    for case in cases:
        if case.output is not None:
            output = case.output
        elif case.prompt is not None:
            output = provider.chat(
                [ChatMessage("user", case.prompt)], system=system, model=model, max_tokens=max_tokens
            ).text
        else:
            raise ValueError(f"eval case {case.name!r} has neither prompt nor output")
        results.append(EvalResult(case.name, output, [chk(output) for chk in case.checks]))
    return results


def summarize(results: list[EvalResult]) -> dict:
    """Aggregate pass rate over cases and checks."""
    total = len(results)
    passed = sum(1 for r in results if r.passed)
    checks_total = sum(len(r.checks) for r in results)
    checks_passed = sum(1 for r in results for c in r.checks if c.passed)
    return {
        "cases": total,
        "cases_passed": passed,
        "case_pass_rate": (passed / total) if total else 0.0,
        "checks": checks_total,
        "checks_passed": checks_passed,
    }
