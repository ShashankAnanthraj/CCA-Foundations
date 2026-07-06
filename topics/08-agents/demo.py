"""Topic 08 — Agents (runnable demo).

Shows the three core orchestration patterns on single-responsibility agents, each mapped to SPIDER:
  1. ROUTER    — classify the task, dispatch to the right specialist
  2. PIPELINE  — sequential stages (output feeds the next)
  3. PARALLEL  — same task to many agents at once (diverse perspectives)

Run:  python topics/08-agents/demo.py
Needs: .env with ANTHROPIC_API_KEY
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import Agent, get_settings, parallel_agents, pipeline, router  # noqa: E402
from core import get_provider                             # noqa: E402

SHORT = 150  # keep demo outputs (and cost) small


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main() -> None:
    settings = get_settings()
    if not settings.has_api_key:
        print("Set ANTHROPIC_API_KEY in .env to run this demo.")
        return
    provider = get_provider()

    def agent(name: str, system: str) -> Agent:
        return Agent(name, provider, system, model=settings.default_model, max_tokens=SHORT)

    # 1) ROUTER (SPIDER: Scope — send each input to the right specialist) --- #
    hr("1) ROUTER — classify, then dispatch to one specialist  [SPIDER: Scope]")
    routes = {
        "code": agent("code", "You are a senior engineer. Answer in one concise code-focused sentence."),
        "writing": agent("writing", "You are an editor. Answer in one concise sentence."),
        "math": agent("math", "You are a mathematician. Answer in one concise sentence."),
    }
    task = "How do I turn a nested for-loop that builds a list into a list comprehension?"
    key, result, route_usage = router(provider, task, routes, model=settings.default_model)
    print(f"  task: {task}")
    print(f"  routed to -> {key}")
    print(f"  answer: {result.text.strip()}")

    # 2) PIPELINE (SPIDER: Plan — decompose into ordered stages) ------------ #
    hr("2) PIPELINE — sequential stages, each output feeds the next  [SPIDER: Plan]")
    para = (
        "Our new caching layer cut median API latency from 800ms to 120ms, but memory use rose 30%, "
        "so we added an LRU eviction policy to keep it bounded."
    )
    stages = [
        agent("extractor", "Extract the single most important fact from the input. Output one line."),
        agent("headline", "Rewrite the input as a punchy 8-word headline."),
    ]
    for res in pipeline(para, stages):
        print(f"  [{res.agent}] {res.text.strip()}")

    # 3) PARALLEL (SPIDER: Isolate — independent views, no cross-contamination) #
    hr("3) PARALLEL — same task to many agents at once  [SPIDER: Isolate]")
    proposal = "Proposal: ship the feature now and fix edge cases in a fast-follow."
    perspectives = [
        agent("optimist", "Give the single strongest argument FOR the proposal. One sentence."),
        agent("skeptic", "Give the single strongest argument AGAINST the proposal. One sentence."),
    ]
    for res in parallel_agents(proposal, perspectives):
        print(f"  [{res.agent}] {res.text.strip()}")

    hr("Done — Topic 08 complete")
    print("  Router/Pipeline/Parallel + SPIDER = the Agentic Architecture domain (27%).")
    print("  Detect/Escalate/Recover and multi-agent synthesis: Topic 09.")


if __name__ == "__main__":
    main()
