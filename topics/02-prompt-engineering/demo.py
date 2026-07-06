"""Topic 02 — Prompt Engineering (runnable demo).

Demonstrates, against the provider-agnostic core:
  1. Prompt hierarchy      (Base + Role + Task + Output-Spec, assembled from prompts/)
  2. Weak vs PRECISE       (free-form prose you must parse  ->  validated JSON object)
  3. Structured output     (JSON Schema constrains the response)
  4. Hallucination control (grounded prompt refuses to invent facts)

Run:  python topics/02-prompt-engineering/demo.py
Needs: .env with ANTHROPIC_API_KEY
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import assemble_system, get_settings, read_prompt  # noqa: E402
from core.providers import ChatMessage                        # noqa: E402
from core import get_provider                   # noqa: E402

# Machine-enforced contract for the triage task (matches prompts/output/support_ticket_triage.md).
TRIAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "category": {"type": "string", "enum": ["billing", "bug", "feature_request", "how_to", "other"]},
        "severity": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
        "needs_human": {"type": "boolean"},
        "summary": {"type": "string"},
    },
    "required": ["category", "severity", "needs_human", "summary"],
    "additionalProperties": False,
}

TICKET = "My app crashes every time I click Export and I just lost an hour of work. Please help!"


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main() -> None:
    settings = get_settings()
    model, max_tokens = settings.default_model, settings.max_tokens

    # 1) HIERARCHY ---------------------------------------------------------- #
    hr("1) Prompt hierarchy: Base -> Role -> Task -> Output-Spec (assembled once, reused)")
    system = assemble_system(
        read_prompt("base", "base_system.md"),
        read_prompt("role", "support_analyst.md"),
        read_prompt("task", "triage_support_ticket.md"),
        read_prompt("output", "support_ticket_triage.md"),
    )
    print(f"  composed system prompt = {len(system)} chars across 4 inherited layers")
    print("  preview:\n    " + system[:220].replace("\n", "\n    ") + " ...")

    if not settings.has_api_key:
        print("\n(Set ANTHROPIC_API_KEY in .env to run demos 2–4.)")
        return
    provider = get_provider()

    # 2) WEAK PROMPT -------------------------------------------------------- #
    hr("2) WEAK prompt (no hierarchy, no spec) -> unstructured prose you must parse")
    weak = provider.chat(
        [ChatMessage("user", f"Triage this ticket: {TICKET}")],
        model=model,
        max_tokens=max_tokens,
    )
    print("  " + weak.text.strip().replace("\n", "\n  "))

    # 3) PRECISE + STRUCTURED ---------------------------------------------- #
    hr("3) PRECISE + structured output -> validated JSON, every time")
    parsed, resp = provider.structured_chat(
        [ChatMessage("user", TICKET)],
        schema=TRIAGE_SCHEMA,
        system=system,
        model=model,
        max_tokens=max_tokens,
    )
    print("  parsed object (safe to use directly):")
    print("    " + json.dumps(parsed, indent=2).replace("\n", "\n    "))
    cost = provider.estimate_cost(resp.usage, resp.model)
    print(f"\n  [tokens in={resp.usage.input_tokens} out={resp.usage.output_tokens}] "
          f"[est. cost=${cost:.6f}]")

    # 4) HALLUCINATION CONTROL --------------------------------------------- #
    hr("4) Grounding: the model must NOT invent facts absent from the ticket")
    grounded = provider.chat(
        [ChatMessage("user", f"Ticket: {TICKET}\n\nWhat is the customer's account email?")],
        system=system,  # Base + Role forbid inventing details
        model=model,
        max_tokens=max_tokens,
    )
    print("  Q: What is the customer's account email?")
    print("  A: " + grounded.text.strip().replace("\n", "\n     "))
    print("\n  (Grounded prompt should say it's not provided — not fabricate an address.)")

    hr("Done — Topic 02 complete")
    print("  Weak prose vs validated object: same model, better prompt engineering.")


if __name__ == "__main__":
    main()
