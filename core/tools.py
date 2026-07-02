"""Tool-use primitives — normalized across providers (Constitution: reusability, composition).

Purpose:    Vendor-neutral types for user-defined tools and the result of an agentic tool loop.
            The loop itself is provider-specific (each vendor's wire protocol differs) and lives on
            `LLMProvider.run_tools`; these types are the shared contract for callers + handlers.
Usage:      define a `ToolSpec`, a Python handler `Callable[[dict], str]`, call `provider.run_tools`.
Depends on: core.providers (Usage). stdlib only otherwise.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

from core.providers import Usage

#: A tool handler receives the model-supplied input dict and returns a string result.
ToolHandler = Callable[[dict], str]


@dataclass(frozen=True)
class ToolSpec:
    """A user-defined tool the model may call. `input_schema` is JSON Schema."""

    name: str
    description: str
    input_schema: dict


@dataclass(frozen=True)
class ToolCall:
    """One tool invocation the model requested."""

    id: str
    name: str
    input: dict


@dataclass
class ToolLoopResult:
    """Outcome of an agentic tool loop."""

    final_text: str
    usage: Usage
    steps: list[ToolCall] = field(default_factory=list)
    iterations: int = 0
