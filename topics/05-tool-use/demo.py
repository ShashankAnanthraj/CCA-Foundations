"""Topic 05 — Tool Use (runnable demo).

Demonstrates an agentic tool loop with the shared core primitive:
  - Define user tools (ToolSpec) + Python handlers
  - The model decides which to call (and may call several in parallel)
  - run_tools executes them, feeds results back, and loops until done

Run:  python topics/05-tool-use/demo.py
Needs: .env with ANTHROPIC_API_KEY
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import ChatMessage, ToolCall, ToolSpec, get_settings  # noqa: E402
from providers.claude import ClaudeProvider                     # noqa: E402

# 1) Define tools (schema the model sees) ---------------------------------- #
TOOLS = [
    ToolSpec(
        name="add",
        description="Add two integers and return the sum.",
        input_schema={
            "type": "object",
            "properties": {"a": {"type": "integer"}, "b": {"type": "integer"}},
            "required": ["a", "b"],
        },
    ),
    ToolSpec(
        name="get_weather",
        description="Get the current weather for a city.",
        input_schema={
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    ),
]


# 2) Handlers (your code — the model never runs anything itself) ----------- #
def add(inp: dict) -> str:
    return str(int(inp["a"]) + int(inp["b"]))


def get_weather(inp: dict) -> str:  # mock: a real handler would call an API
    return f"{inp['city']}: 22°C, partly cloudy"


HANDLERS = {"add": add, "get_weather": get_weather}


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main() -> None:
    settings = get_settings()
    if not settings.has_api_key:
        print("Set ANTHROPIC_API_KEY in .env to run this demo.")
        return
    provider = ClaudeProvider()

    hr("Agentic tool loop — model calls tools, your code runs them, loop repeats")
    task = "What is 15 + 27, and what's the weather in Paris right now?"
    print(f"  task: {task}\n")

    def trace(call: ToolCall) -> None:  # live view of each tool call
        print(f"    -> model calls {call.name}({call.input})")

    result = provider.run_tools(
        [ChatMessage("user", task)],
        tools=TOOLS,
        handlers=HANDLERS,
        model=settings.default_model,
        max_tokens=settings.max_tokens,
        on_tool_call=trace,
    )

    print(f"\n  final answer: {result.final_text.strip()}")
    cost = provider.estimate_cost(result.usage, settings.default_model)
    print(
        f"\n  [tool calls={len(result.steps)}  loop iterations={result.iterations}]"
        f"\n  [tokens in={result.usage.input_tokens} out={result.usage.output_tokens}] "
        f"[est. cost=${cost:.6f}]"
    )
    print("\n  Note: both tools can be requested in one turn (parallel) — all results return together.")

    hr("Done — Topic 05 complete")
    print("  The loop is the heart of every agent (Topic 08 reuses this exact primitive).")


if __name__ == "__main__":
    main()
