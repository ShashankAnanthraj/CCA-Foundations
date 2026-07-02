"""Topic 09 — Subagents & Cowork (runnable demo).

A multi-agent research system (the classic exam scenario), built from the core orchestration layer:
  1. DECOMPOSE  — split the question into sub-questions        [SPIDER: Plan]
  2. FAN-OUT    — a researcher subagent answers each in parallel [SPIDER: Isolate]
  3. SYNTHESIZE — merge the answers into one grounded brief     [SPIDER: Detect]
  4. HUMAN GATE — approve before "publishing"                    [SPIDER: Escalate]

Run:  python topics/09-subagents-cowork/demo.py
Needs: .env with ANTHROPIC_API_KEY
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import (  # noqa: E402
    Agent,
    ChatMessage,
    approval_gate,
    assemble_system,
    fan_out,
    get_settings,
    read_prompt,
)
from providers.claude import ClaudeProvider  # noqa: E402

SHORT = 200
QUESTION = "What are the main trade-offs of microservices vs a monolith for a small startup?"

DECOMPOSE_SCHEMA = {
    "type": "object",
    "properties": {"subquestions": {"type": "array", "items": {"type": "string"}}},
    "required": ["subquestions"],
    "additionalProperties": False,
}


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main() -> None:
    settings = get_settings()
    if not settings.has_api_key:
        print("Set ANTHROPIC_API_KEY in .env to run this demo.")
        return
    provider = ClaudeProvider()
    model, base = settings.default_model, read_prompt("base", "base_system.md")

    # 1) DECOMPOSE ---------------------------------------------------------- #
    hr("1) DECOMPOSE the question into sub-questions  [SPIDER: Plan]")
    parsed, _ = provider.structured_chat(
        [ChatMessage("user", f"Break this into exactly 3 focused sub-questions: {QUESTION}")],
        schema=DECOMPOSE_SCHEMA,
        system=base,
        model=model,
        max_tokens=256,
    )
    subqs = parsed["subquestions"][:3]
    for i, q in enumerate(subqs, 1):
        print(f"  {i}. {q}")

    # 2) FAN-OUT to subagents (parallel) ------------------------------------ #
    hr("2) FAN-OUT — a researcher subagent answers each sub-question in parallel  [SPIDER: Isolate]")
    researcher = Agent(
        "researcher",
        provider,
        assemble_system(base, read_prompt("role", "researcher.md")),
        model=model,
        max_tokens=SHORT,
    )
    answers = fan_out(researcher, subqs)
    for q, res in zip(subqs, answers):
        print(f"  Q: {q}\n  A: {res.text.strip()}\n")

    # 3) SYNTHESIZE --------------------------------------------------------- #
    hr("3) SYNTHESIZE the answers into one grounded brief  [SPIDER: Detect]")
    qa = "\n".join(f"Q: {q}\nA: {r.text.strip()}" for q, r in zip(subqs, answers))
    synthesizer = Agent(
        "synthesizer",
        provider,
        assemble_system(base, read_prompt("role", "synthesizer.md")),
        model=model,
        max_tokens=SHORT,
    )
    brief = synthesizer.run(f"Original question: {QUESTION}\n\n{qa}")
    print("  " + brief.text.strip().replace("\n", "\n  "))

    # 4) HUMAN-IN-THE-LOOP GATE --------------------------------------------- #
    hr("4) HUMAN GATE — approve before publishing  [SPIDER: Escalate]")

    def policy(description: str) -> bool:
        # Stand-in for a human/UI: publish only if every subagent produced an answer.
        return all(r.text.strip() for r in answers)

    approved = approval_gate("Publish the research brief to the team wiki", policy)
    print(f"  gate decision: {'APPROVED — publishing' if approved else 'BLOCKED — needs human review'}")
    print("  (In production this is a real human or policy — the point is the agent does NOT auto-publish.)")

    hr("Done — Topic 09 complete")
    print("  Decompose -> fan-out subagents -> synthesize -> gate = a reliable multi-agent system.")


if __name__ == "__main__":
    main()
