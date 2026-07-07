"""Topic 09 — Evaluations harness (runnable demo).

Reliability is a CCA-F domain, and "does the output meet a bar?" is a different question from "does
the code run?" (that's `tests/`). This demo scores model/agent output with:
  1. ASSERTION checks — deterministic, no API key (contains / regex / word cap / JSON)
  2. LLM-AS-JUDGE   — a constrained pass/fail verdict against a rubric (needs a key)

Run:  python topics/09-subagents-cowork/evals_demo.py
Needs: nothing for the assertion section; ANTHROPIC_API_KEY for the judge/generation section.
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import get_provider, get_settings  # noqa: E402
from evals import (  # noqa: E402
    EvalCase,
    contains,
    is_json,
    llm_judge,
    max_words,
    not_contains,
    run_evals,
    summarize,
)


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main() -> None:
    settings = get_settings()

    # 1) ASSERTION EVALS — no key: score fixed sample outputs against a bar.
    hr("1) ASSERTION EVALS — deterministic, no API key")
    fixture = [
        EvalCase("has_answer", checks=[contains("42"), max_words(20)],
                 output="The answer to the question is 42."),
        EvalCase("no_pii", checks=[not_contains("ssn"), not_contains("password")],
                 output="Contact the team via the support portal."),
        EvalCase("valid_json", checks=[is_json()], output='{"ok": true, "count": 3}'),
    ]
    # No provider needed — every case supplies a fixed `output`.
    results = run_evals(get_provider() if settings.has_api_key else _NoProvider(), fixture)
    for r in results:
        mark = "PASS" if r.passed else "FAIL"
        print(f"  [{mark}] {r.case}: " + ", ".join(f"{c.name}={'ok' if c.passed else 'x'}" for c in r.checks))
    print(f"  summary: {summarize(results)}")

    # 2) LLM-AS-JUDGE — needs a key: generate then grade against a rubric.
    hr("2) LLM-AS-JUDGE — grade generated output against a rubric")
    if not settings.has_api_key:
        print("  (skipped: set ANTHROPIC_API_KEY to generate + judge with the model)")
    else:
        provider = get_provider()
        rubric = "A one-sentence, factual definition of MCP (Model Context Protocol); no marketing."
        cases = [
            EvalCase(
                "define_mcp",
                checks=[max_words(40), llm_judge(provider, rubric, model=settings.default_model)],
                prompt="In one factual sentence, define the Model Context Protocol (MCP).",
            )
        ]
        judged = run_evals(provider, cases, model=settings.default_model, max_tokens=settings.max_tokens)
        for r in judged:
            print(f"  case: {r.case}\n  output: {r.output.strip()}")
            for c in r.checks:
                print(f"    - {c.name}: {'PASS' if c.passed else 'FAIL'}"
                      + (f" — {c.detail}" if c.detail else ""))
        print(f"  summary: {summarize(judged)}")

    hr("Done — evals score OUTPUT quality (tests score code). Both belong in a reliable pipeline.")


class _NoProvider:
    """Placeholder so the assertion section runs with no configured provider (fixed outputs only)."""


if __name__ == "__main__":
    main()
