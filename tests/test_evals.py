"""evals.harness — assertion checks, LLM-as-judge, and the runner (key-free via FakeProvider)."""

from __future__ import annotations

from evals import (
    EvalCase,
    contains,
    is_json,
    llm_judge,
    matches,
    max_words,
    not_contains,
    run_evals,
    summarize,
)


def test_assertion_checks():
    assert contains("cat")("a CAT sat").passed
    assert not contains("dog")("a cat sat").passed
    assert not_contains("dog")("a cat sat").passed
    assert matches(r"\d{3}")("id 123").passed
    assert max_words(3)("one two three").passed
    assert not max_words(2)("one two three").passed
    assert is_json()('{"a": 1}').passed
    assert not is_json()("not json").passed


def test_run_evals_generates_and_scores(fake_provider):
    # FakeProvider.chat returns "echo: <prompt>", so `contains` on the prompt text passes.
    cases = [
        EvalCase("greet", checks=[contains("hello")], prompt="hello"),
        EvalCase("fixed", checks=[contains("world")], output="the world is round"),
    ]
    results = run_evals(fake_provider, cases)
    assert all(r.passed for r in results)
    s = summarize(results)
    assert s["cases"] == 2 and s["cases_passed"] == 2 and s["case_pass_rate"] == 1.0


def test_llm_judge_pass_and_fail(fake_provider):
    # FakeProvider.structured_chat picks the enum value whose label appears in the prompt.
    # The rubric text is echoed into the judge prompt, so we steer the verdict via keywords.
    judge_pass = llm_judge(fake_provider, "the answer is correct")
    judge_fail = llm_judge(fake_provider, "mark this fail")
    assert judge_pass("anything").passed          # no 'fail' token → first enum 'pass'
    assert not judge_fail("anything").passed       # 'fail' present in rubric → 'fail'


def test_case_without_prompt_or_output_raises(fake_provider):
    import pytest

    with pytest.raises(ValueError):
        run_evals(fake_provider, [EvalCase("bad", checks=[contains("x")])])
