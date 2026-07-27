"""core.tools + core.providers.Usage — vendor-neutral primitives."""

from __future__ import annotations

from core.providers import Usage
from core.tools import ToolCall, ToolLoopResult, ToolSpec


def test_toolspec_fields():
    t = ToolSpec(name="add", description="Add", input_schema={"type": "object"})
    assert t.name == "add"
    assert t.input_schema["type"] == "object"


def test_toolcall_and_loop_result_defaults():
    call = ToolCall(id="1", name="add", input={"a": 1})
    r = ToolLoopResult(final_text="done", usage=Usage(1, 2))
    assert r.steps == [] and r.iterations == 0
    assert call.input == {"a": 1}


def test_usage_total_tokens_sums_all_buckets():
    u = Usage(input_tokens=10, output_tokens=5, cache_read_input_tokens=3, cache_creation_input_tokens=2)
    assert u.total_tokens == 20
