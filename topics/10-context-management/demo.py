"""Topic 10 — Context Management (runnable demo).

Proves the core context-economy ideas with the shared Conversation:
  1. Token budgeting   — count the system prompt before sending           [CALM: Limit]
  2. Multi-turn        — stateless API, full history resent each turn      [CALM: Assemble]
  3. Prompt caching    — a large cached prefix: turn 1 WRITES, turn 2 READS [CALM: Cache]

Uses a cheap model (haiku) + a padded knowledge base to reliably exceed the cache minimum.

Run:  python topics/10-context-management/demo.py
Needs: .env with ANTHROPIC_API_KEY
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core import Conversation, get_provider, get_settings  # noqa: E402
from core.providers import ChatMessage                     # noqa: E402

# Claude path uses cheap haiku (cacheable ~4K min); other providers use their default model.
# Note: prompt caching is a Claude feature — on OpenRouter the cache flags are ignored and
# the demo prints its "no cache read" branch, which is expected.
MODEL = "claude-haiku-4-5" if get_settings().provider == "claude" else get_settings().default_model

FACTS = (
    "AI-OS is an enterprise AI engineering platform. The current release is version 0.1.0. "
    "Support is reachable at support@ai-os.dev. It is model-agnostic, vendor-agnostic, and MCP-native. "
)
FILLER = (
    "The platform emphasizes modularity, reusability, token efficiency, and context engineering. "
    "Every component has a single responsibility and is documented and composable. "
)
# Pad to a large, STABLE knowledge base so it exceeds the model's cache minimum.
KNOWLEDGE = "# AI-OS Handbook\n\n" + (FACTS + FILLER) * 45


def hr(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def usage_line(resp) -> str:
    u = resp.usage
    return (f"input={u.input_tokens}  cache_write={u.cache_creation_input_tokens}  "
            f"cache_read={u.cache_read_input_tokens}  output={u.output_tokens}")


def main() -> None:
    settings = get_settings()
    if not settings.has_api_key:
        print("Set ANTHROPIC_API_KEY in .env to run this demo.")
        return
    provider = get_provider()

    # 1) BUDGET ------------------------------------------------------------- #
    hr("1) Token budget — measure the system prefix before sending  [CALM: Limit]")
    n = provider.count_tokens([ChatMessage("user", "hi")], system=KNOWLEDGE, model=MODEL)
    print(f"  knowledge-base system prompt ≈ {n} tokens (large + stable → cacheable)")

    # 2/3) MULTI-TURN + CACHING -------------------------------------------- #
    hr("2) Multi-turn with a CACHED system prefix  [CALM: Assemble + Cache]")
    convo = Conversation(provider, KNOWLEDGE, model=MODEL, max_tokens=80, cache_system=True)

    r1 = convo.ask("Which version of AI-OS is current? One short sentence.")
    print(f"  turn 1: {r1.text.strip()}")
    print(f"          usage -> {usage_line(r1)}   (expect cache_write > 0)")

    r2 = convo.ask("And what's the support email? One short sentence.")
    print(f"  turn 2: {r2.text.strip()}")
    print(f"          usage -> {usage_line(r2)}   (expect cache_read > 0)")

    t = convo.totals
    print(f"\n  cumulative: input={t.input_tokens} cache_read={t.cache_read_input_tokens} "
          f"output={t.output_tokens}")
    if t.cache_read_input_tokens > 0:
        print("  ✅ cache HIT on turn 2 — the big prefix was reused at ~0.1x cost.")
    else:
        print("  (no cache read — prefix may be below this model's minimum; try a longer KNOWLEDGE.)")

    # Lifecycle (the M in CALM) -------------------------------------------- #
    hr("Lifecycle tools (CALM: Manage) — for longer runs")
    print("  - context editing: CLEAR stale tool results/thinking  (clear_tool_uses_20250919)")
    print("  - compaction:      SUMMARIZE old history server-side   (compact_20260112)")
    print("  - memory:          PERSIST facts across sessions        (memory tool / files)")

    hr("Done — Topic 10 complete")
    print("  Cache · Assemble selectively · Limit · Manage = CALM (Context Management, 15%).")


if __name__ == "__main__":
    main()
