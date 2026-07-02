"""Claude implementation of `core.providers.LLMProvider`.

Purpose:    Translate the vendor-agnostic interface to the Anthropic Messages API.
Usage:      `from providers.claude import ClaudeProvider; p = ClaudeProvider()`
Depends on: anthropic (>=0.40). This is the only module permitted to import it.
Limits:     Text-first. Tools/vision/MCP are layered in their respective topics.
Best practice: default model `claude-opus-4-8`; adaptive thinking only (no budget_tokens).
"""

from __future__ import annotations

import json
from typing import Callable, Iterator

import anthropic

from core.providers import LLMProvider, LLMResponse, Messages, Usage
from core.tools import ToolCall, ToolLoopResult, ToolSpec


class ClaudeProvider(LLMProvider):
    """Anthropic Claude provider. Reads ANTHROPIC_API_KEY from the environment."""

    # $ per 1M tokens (input, output) — standard rates. Source: platform pricing.
    pricing = {
        "claude-fable-5": (10.0, 50.0),
        "claude-opus-4-8": (5.0, 25.0),
        "claude-opus-4-7": (5.0, 25.0),
        "claude-sonnet-5": (3.0, 15.0),
        "claude-sonnet-4-6": (3.0, 15.0),
        "claude-haiku-4-5": (1.0, 5.0),
    }

    DEFAULT_MODEL = "claude-opus-4-8"

    def __init__(self, api_key: str | None = None) -> None:
        # anthropic.Anthropic() resolves the key from the env when api_key is None.
        self._client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()

    # -- interface ---------------------------------------------------------- #
    def chat(
        self,
        messages: Messages,
        *,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
        thinking: bool = False,
        effort: str | None = None,
        cache: bool = False,
    ) -> LLMResponse:
        params: dict = {
            "model": model or self.DEFAULT_MODEL,
            "max_tokens": max_tokens or 1024,
            "messages": self._normalize(messages),
        }
        if system:
            # cache=True → mark the system prompt as a cacheable prefix (prompt caching).
            params["system"] = (
                [{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}]
                if cache
                else system
            )
        if thinking:
            params["thinking"] = {"type": "adaptive"}  # adaptive only on 4.7+/5/Fable
        if effort:
            params["output_config"] = {"effort": effort}

        resp = self._client.messages.create(**params)
        text = "".join(b.text for b in resp.content if b.type == "text")
        return LLMResponse(
            text=text,
            model=resp.model,
            stop_reason=resp.stop_reason,
            usage=self._usage(resp.usage),
            raw=resp,
        )

    def stream_chat(
        self,
        messages: Messages,
        *,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
    ) -> Iterator[str]:
        params: dict = {
            "model": model or self.DEFAULT_MODEL,
            "max_tokens": max_tokens or 1024,
            "messages": self._normalize(messages),
        }
        if system:
            params["system"] = system
        with self._client.messages.stream(**params) as stream:
            for text in stream.text_stream:
                yield text

    def count_tokens(
        self,
        messages: Messages,
        *,
        system: str | None = None,
        model: str | None = None,
    ) -> int:
        params: dict = {
            "model": model or self.DEFAULT_MODEL,
            "messages": self._normalize(messages),
        }
        if system:
            params["system"] = system
        return self._client.messages.count_tokens(**params).input_tokens

    def structured_chat(
        self,
        messages: Messages,
        *,
        schema: dict,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
    ) -> tuple[dict, LLMResponse]:
        # output_config.format constrains the response to valid JSON matching `schema`.
        params: dict = {
            "model": model or self.DEFAULT_MODEL,
            "max_tokens": max_tokens or 1024,
            "messages": self._normalize(messages),
            "output_config": {"format": {"type": "json_schema", "schema": schema}},
        }
        if system:
            params["system"] = system

        resp = self._client.messages.create(**params)
        text = "".join(b.text for b in resp.content if b.type == "text")
        parsed = json.loads(text)  # guaranteed valid JSON by output_config.format
        return parsed, LLMResponse(
            text=text,
            model=resp.model,
            stop_reason=resp.stop_reason,
            usage=self._usage(resp.usage),
            raw=resp,
        )

    def run_tools(
        self,
        messages: Messages,
        *,
        tools: list[ToolSpec],
        handlers: dict[str, Callable[[dict], str]],
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
        max_iters: int = 5,
        on_tool_call: Callable[[ToolCall], None] | None = None,
    ) -> ToolLoopResult:
        model = model or self.DEFAULT_MODEL
        max_tokens = max_tokens or 1024
        anth_tools = [
            {"name": t.name, "description": t.description, "input_schema": t.input_schema}
            for t in tools
        ]
        convo: list[dict] = self._normalize(messages)
        steps: list[ToolCall] = []
        tin = tout = 0

        for i in range(max_iters):
            params: dict = {
                "model": model,
                "max_tokens": max_tokens,
                "messages": convo,
                "tools": anth_tools,
            }
            if system:
                params["system"] = system
            resp = self._client.messages.create(**params)
            tin += resp.usage.input_tokens or 0
            tout += resp.usage.output_tokens or 0
            # Echo the assistant turn back verbatim so tool_use ids line up.
            convo.append({"role": "assistant", "content": resp.content})

            if resp.stop_reason != "tool_use":
                text = "".join(b.text for b in resp.content if b.type == "text")
                return ToolLoopResult(text, Usage(tin, tout), steps, i + 1)

            # Execute every requested tool; return ALL results in ONE user message.
            results: list[dict] = []
            for block in resp.content:
                if block.type != "tool_use":
                    continue
                call = ToolCall(id=block.id, name=block.name, input=dict(block.input))
                steps.append(call)
                if on_tool_call:
                    on_tool_call(call)
                handler = handlers.get(block.name)
                try:
                    output = handler(block.input) if handler else f"Error: no handler '{block.name}'"
                    is_error = handler is None
                except Exception as exc:  # tool failures are data, not crashes
                    output, is_error = f"Error: {exc}", True
                results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(output),
                        "is_error": is_error,
                    }
                )
            convo.append({"role": "user", "content": results})

        return ToolLoopResult("(stopped: max tool iterations reached)", Usage(tin, tout), steps, max_iters)

    # -- helpers ------------------------------------------------------------ #
    @staticmethod
    def _usage(u) -> Usage:
        return Usage(
            input_tokens=getattr(u, "input_tokens", 0) or 0,
            output_tokens=getattr(u, "output_tokens", 0) or 0,
            cache_read_input_tokens=getattr(u, "cache_read_input_tokens", 0) or 0,
            cache_creation_input_tokens=getattr(u, "cache_creation_input_tokens", 0) or 0,
        )
