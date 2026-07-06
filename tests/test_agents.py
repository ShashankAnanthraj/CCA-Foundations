"""core.agents — Agent + orchestration patterns (router/pipeline/parallel/fan-out/gate)."""

from __future__ import annotations

from core.agents import Agent, approval_gate, fan_out, parallel_agents, pipeline, router
from core.tools import ToolSpec


def test_agent_plain_run(fake_provider):
    a = Agent("a", fake_provider, "sys")
    assert a.run("hi").text == "echo: hi"


def test_agent_with_tools_uses_tool_loop(fake_provider):
    tool = ToolSpec("greet", "greet", {"type": "object"})
    handlers = {"greet": lambda inp: "HELLO"}
    a = Agent("a", fake_provider, "sys", tools=[tool], handlers=handlers)
    res = a.run("please greet")
    assert res.text == "HELLO"


def test_router_dispatches_to_labelled_route(fake_provider):
    routes = {"math": Agent("math", fake_provider, "s"), "prose": Agent("prose", fake_provider, "s")}
    key, result, _usage = router(fake_provider, "do some math please", routes)
    assert key == "math"
    assert result.agent == "math"


def test_pipeline_feeds_output_forward(fake_provider):
    a, b = Agent("a", fake_provider, "s"), Agent("b", fake_provider, "s")
    results = pipeline("start", [a, b])
    assert len(results) == 2
    assert results[0].text == "echo: start"
    assert results[1].text == "echo: echo: start"


def test_parallel_runs_all(fake_provider):
    agents = [Agent(f"a{i}", fake_provider, "s") for i in range(3)]
    assert len(parallel_agents("t", agents)) == 3


def test_fan_out_covers_every_subtask(fake_provider):
    a = Agent("worker", fake_provider, "s")
    out = fan_out(a, ["q1", "q2", "q3"])
    assert [r.text for r in out] == ["echo: q1", "echo: q2", "echo: q3"]


def test_approval_gate_reflects_policy():
    assert approval_gate("ship it", lambda _d: True) is True
    assert approval_gate("ship it", lambda _d: False) is False
