"""Topic 12 — Production & Platform (runnable demo).

A tiny COST & OBSERVABILITY tool: count a prompt's tokens once, then compare projected cost across
models — and show what batching and caching save. Cost is a first-class production metric.

Run:  python topics/12-production-platform/demo.py
Needs: .env with ANTHROPIC_API_KEY (count_tokens is free of token charges)
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import ChatMessage, get_provider, get_provider_class, get_settings  # noqa: E402
from core.providers import Usage                                              # noqa: E402

ASSUMED_OUTPUT = 500  # tokens; a typical medium response
SAMPLE = (
    "Summarize the quarterly engineering report: latency improvements, the new caching layer, "
    "the incident on the 14th, and the roadmap for next quarter. Include risks and next steps."
)


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main() -> None:
    settings = get_settings()

    hr("Model pricing ($ per 1M tokens)")
    for m, (inp, out) in get_provider_class().pricing.items():
        print(f"  {m:20s}  in ${inp:<6} out ${out}")

    if not settings.has_api_key:
        print("\n(Set ANTHROPIC_API_KEY to compute per-model cost for a real prompt.)")
        return

    provider = get_provider()
    n_in = provider.count_tokens([ChatMessage("user", SAMPLE)], model=settings.default_model)

    hr(f"Projected cost per request  (input={n_in} tokens, assumed output={ASSUMED_OUTPUT})")
    print(f"  {'model':20s}  {'standard':>10}  {'batch(-50%)':>12}  {'cached-in(~0.1x)':>16}")
    for m in get_provider_class().pricing:
        std = provider.estimate_cost(Usage(n_in, ASSUMED_OUTPUT), m)
        batch = std * 0.5
        cached = provider.estimate_cost(Usage(0, ASSUMED_OUTPUT, cache_read_input_tokens=n_in), m)
        print(f"  {m:20s}  ${std:>9.5f}  ${batch:>11.5f}  ${cached:>15.5f}")

    hr("Production levers (see README + reference files)")
    print("  - Batches API:  50% cheaper, async (up to 24h)  -> batches_and_files.md")
    print("  - Prompt cache: cached input ~0.1x               -> Topic 10")
    print("  - Right model:  Haiku for simple/high-volume, Opus/Fable for hardest")
    print("  - Files API:    upload once, reference by id     -> batches_and_files.md")
    print("  - Platforms:    Bedrock / Vertex / Foundry / AWS -> platform_availability.md")

    hr("Done — Topic 12 complete")
    print("  Measure cost like any prod metric; pick model + batch + cache to hit your budget.")


if __name__ == "__main__":
    main()
