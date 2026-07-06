"""Topic 01 — Foundations (runnable demo).

Demonstrates, against the provider-agnostic core:
  1. Model catalog & pricing        (choosing a model — no API cost)
  2. Token counting BEFORE sending  (count_tokens)
  3. A basic Messages API call      (text, stop_reason, usage, $ cost)
  4. Streaming                      (tokens rendered live)
  5. Thinking + effort              (adaptive reasoning, cost trade-off)

Run:  python topics/01-foundations/demo.py
Needs: .env with ANTHROPIC_API_KEY  (keep AI_OS_MAX_TOKENS small to limit spend)
"""

from __future__ import annotations

import pathlib
import sys

# --- bootstrap: make the repo root importable (topic folders aren't packages) ---
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import get_provider, get_provider_class, get_settings  # noqa: E402
from core.providers import ChatMessage, LLMProvider, LLMResponse  # noqa: E402

BASE_SYSTEM = (ROOT / "prompts" / "base" / "base_system.md").read_text(encoding="utf-8")


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def show(provider: LLMProvider, resp: LLMResponse) -> None:
    """Uniformly print a response with its usage + estimated cost."""
    u = resp.usage
    cost = provider.estimate_cost(u, resp.model)
    print(resp.text.strip())
    print(
        f"\n  [model={resp.model}  stop_reason={resp.stop_reason}]"
        f"\n  [tokens: in={u.input_tokens} out={u.output_tokens} "
        f"total={u.total_tokens}]  [est. cost=${cost:.6f}]"
    )


def main() -> None:
    settings = get_settings()
    if not settings.has_api_key:
        print(
            "No ANTHROPIC_API_KEY found.\n"
            "  1) copy .env.example to .env   2) set ANTHROPIC_API_KEY   3) re-run.\n"
            "Showing the model catalog only (no API calls):\n"
        )

    provider = get_provider() if settings.has_api_key else None
    model = settings.default_model
    max_tokens = settings.max_tokens

    # 1) MODEL CATALOG & PRICING -------------------------------------------- #
    hr("1) Models & pricing ($ per 1M tokens)  —  choosing the right model")
    for m, (inp, out) in get_provider_class().pricing.items():
        marker = "  <- default" if m == model else ""
        print(f"  {m:20s}  in ${inp:<6}  out ${out}{marker}")

    if provider is None:
        print("\n(Set your API key to run demos 2–5.)")
        return

    # 2) TOKEN COUNTING (before sending) ------------------------------------ #
    hr("2) Count tokens BEFORE sending (never estimate with tiktoken)")
    q = "In one sentence, what is the Anthropic Messages API?"
    n = provider.count_tokens([ChatMessage("user", q)], system=BASE_SYSTEM, model=model)
    print(f"  prompt = {q!r}\n  input tokens (incl. system) = {n}")

    # 3) BASIC MESSAGE ------------------------------------------------------ #
    hr("3) Basic Messages API call")
    resp = provider.chat(
        [ChatMessage("user", q)], system=BASE_SYSTEM, model=model, max_tokens=max_tokens
    )
    show(provider, resp)

    # 4) STREAMING ---------------------------------------------------------- #
    hr("4) Streaming — tokens rendered as they arrive")
    print("  ", end="", flush=True)
    for delta in provider.stream_chat(
        [ChatMessage("user", "List 3 uses for streaming responses. Be terse.")],
        system=BASE_SYSTEM,
        model=model,
        max_tokens=max_tokens,
    ):
        print(delta, end="", flush=True)
    print()

    # 5) THINKING + EFFORT -------------------------------------------------- #
    hr("5) Adaptive thinking + effort (quality vs cost/latency)")
    reasoning_q = "A bat and ball cost $1.10. The bat costs $1 more than the ball. Ball price?"
    resp2 = provider.chat(
        [ChatMessage("user", reasoning_q)],
        system=BASE_SYSTEM,
        model=model,
        max_tokens=max_tokens,
        thinking=True,
        effort="high",
    )
    show(provider, resp2)
    print("\n  Note: thinking is adaptive (no fixed budget_tokens); higher effort => more tokens/$.")

    hr("Done — Topic 01 complete")
    print("  You just used the provider-agnostic core. Swapping models = change one string.")


if __name__ == "__main__":
    main()
