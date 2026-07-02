"""Agents & orchestration — single-responsibility agents + composition patterns.

Purpose:    A minimal `Agent` (provider + system prompt + optional tools) and the four orchestration
            patterns the CCA-F Agentic Architecture domain centers on: router, pipeline, parallel,
            and fan-out — plus a human-in-the-loop gate.
Usage:      `from core.agents import Agent, router, pipeline, parallel_agents, fan_out, approval_gate`
Depends on: core.providers, core.tools. Concurrency via threads (the sync client is per-call safe).
Design:     No God Agents — each Agent has one responsibility; orchestration composes them.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Callable

from core.providers import ChatMessage, LLMProvider, Usage
from core.tools import ToolSpec


@dataclass
class AgentResult:
    agent: str
    text: str
    usage: Usage


class Agent:
    """One responsibility. Runs a task via chat, or via the tool loop if given tools."""

    def __init__(
        self,
        name: str,
        provider: LLMProvider,
        system: str,
        *,
        model: str | None = None,
        max_tokens: int | None = None,
        tools: list[ToolSpec] | None = None,
        handlers: dict[str, Callable[[dict], str]] | None = None,
    ) -> None:
        self.name = name
        self.provider = provider
        self.system = system
        self.model = model
        self.max_tokens = max_tokens
        self.tools = tools
        self.handlers = handlers or {}

    def run(self, task: str) -> AgentResult:
        if self.tools:
            r = self.provider.run_tools(
                [ChatMessage("user", task)],
                tools=self.tools,
                handlers=self.handlers,
                system=self.system,
                model=self.model,
                max_tokens=self.max_tokens,
            )
            return AgentResult(self.name, r.final_text, r.usage)
        resp = self.provider.chat(
            [ChatMessage("user", task)],
            system=self.system,
            model=self.model,
            max_tokens=self.max_tokens,
        )
        return AgentResult(self.name, resp.text, resp.usage)


# --------------------------------------------------------------------------- #
# Orchestration patterns
# --------------------------------------------------------------------------- #
def pipeline(task: str, stages: list[Agent]) -> list[AgentResult]:
    """Sequential: each agent's output is the next agent's input."""
    results: list[AgentResult] = []
    current = task
    for agent in stages:
        res = agent.run(current)
        results.append(res)
        current = res.text
    return results


def parallel_agents(task: str, agents: list[Agent], *, max_workers: int = 4) -> list[AgentResult]:
    """Fan the SAME task to many agents concurrently (e.g., diverse perspectives)."""
    if not agents:
        return []
    with ThreadPoolExecutor(max_workers=max(1, min(max_workers, len(agents)))) as ex:
        return list(ex.map(lambda a: a.run(task), agents))


def fan_out(agent: Agent, tasks: list[str], *, max_workers: int = 4) -> list[AgentResult]:
    """Run ONE agent over many subtasks concurrently (subagent fan-out)."""
    if not tasks:
        return []
    with ThreadPoolExecutor(max_workers=max(1, min(max_workers, len(tasks)))) as ex:
        return list(ex.map(agent.run, tasks))


def router(
    provider: LLMProvider,
    task: str,
    routes: dict[str, Agent],
    *,
    model: str | None = None,
    max_tokens: int | None = None,
) -> tuple[str, AgentResult, Usage]:
    """Classify the task (constrained to the route labels), then dispatch to that agent."""
    labels = list(routes)
    schema = {
        "type": "object",
        "properties": {"route": {"type": "string", "enum": labels}},
        "required": ["route"],
        "additionalProperties": False,
    }
    parsed, resp = provider.structured_chat(
        [ChatMessage("user", task)],
        schema=schema,
        system="You are a router. Classify the task and choose the single best route.",
        model=model,
        max_tokens=max_tokens or 256,
    )
    key = parsed["route"]
    return key, routes[key].run(task), resp.usage


def approval_gate(description: str, approve: Callable[[str], bool]) -> bool:
    """Human-in-the-loop gate. `approve` is any policy/UI/CLI callable(description) -> bool."""
    return bool(approve(description))
