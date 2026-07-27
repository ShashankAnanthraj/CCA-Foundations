"""Shared base for OpenAI-compatible providers (capability plane).

Purpose:    One reusable `LLMProvider` implementation for every vendor that speaks the OpenAI
            Chat Completions protocol (OpenRouter, Groq, Together, Fireworks, OpenAI, Ollama,
            LM Studio, DeepSeek, …). A concrete provider is a ~10-line subclass that sets a base
            URL, a key env var, a default model, and a pricing table.
Usage:      subclass `OpenAICompatibleProvider`, override the class attributes, done.
Depends on: openai (>=1.0). Only the providers plane may import a vendor SDK (ADR 0001); this base
            lives here (not in `core`) so that rule holds.
Limits (shared, documented):
  - `count_tokens` is APPROXIMATE — the OpenAI protocol has no pre-send count endpoint.
  - `structured_chat` / `run_tools` require a model that supports JSON-schema / tool calling.
  - `thinking` / `effort` / `cache` hints are not portable and are silently ignored.
"""

from __future__ import annotations

import json
import os
import sys
import time
from typing import Callable, Iterator

from openai import OpenAI, RateLimitError

from core.providers import LLMProvider, LLMResponse, Messages, Usage
from core.tools import ToolCall, ToolLoopResult, ToolSpec


class OpenAICompatibleProvider(LLMProvider):
    """Base adapter for any OpenAI-compatible endpoint. Subclasses override the attributes below."""

    #: Short name used in stderr notes, e.g. "[groq] …". Override per provider.
    LABEL = "openai-compat"
    #: OpenAI-compatible base URL, e.g. "https://api.groq.com/openai/v1".
    BASE_URL = ""
    #: Environment variable holding the API key. Empty string => keyless (e.g. local Ollama).
    API_KEY_ENV = ""
    #: Model used when the caller passes none.
    DEFAULT_MODEL = ""
    #: Extra HTTP headers (e.g. attribution). Override with a dict if needed.
    default_headers: dict[str, str] = {}
    #: How many times to retry a transient failure (rate limit / empty body / empty JSON).
    MAX_RETRIES = 4
    #: model id -> (input $/1M, output $/1M). Unlisted models fall back to (0, 0).
    pricing: dict[str, tuple[float, float]] = {}

    def __init__(self, api_key: str | None = None) -> None:
        # Keyless local servers (Ollama, LM Studio) still need a non-empty placeholder for the SDK.
        key = api_key or (os.environ.get(self.API_KEY_ENV) if self.API_KEY_ENV else None)
        self._client = OpenAI(
            base_url=self.BASE_URL,
            api_key=key or "not-needed",
            default_headers=self.default_headers or None,
        )

    # -- rate-limit-aware request helper ------------------------------------ #
    def _create(self, **params):
        """`chat.completions.create` with retry/backoff for flaky (often free) endpoints.

        Retries three transient conditions: (1) HTTP 429 rate limits (honoring `Retry-After`, else
        ~2/4/8s backoff), (2) an HTTP-200 body carrying an upstream error so `choices` is empty.
        A per-day quota 429 is NOT retried (won't recover in-window) — it fails fast with guidance.
        Other terminal errors (e.g. 404 unknown model) surface immediately.
        """
        streaming = params.get("stream", False)
        for attempt in range(self.MAX_RETRIES + 1):
            try:
                resp = self._client.chat.completions.create(**params)
            except RateLimitError as exc:
                if "per-day" in str(exc) or "free-models-per-day" in str(exc):
                    raise RuntimeError(
                        f"{self.LABEL}: free daily quota exhausted. Add credit to raise the daily "
                        f"cap (still $0 on free models) or switch to a paid model via "
                        f"AI_OS_DEFAULT_MODEL."
                    ) from exc
                if attempt == self.MAX_RETRIES:
                    raise
                wait = self._retry_after(exc) or 2 * (2**attempt)
                self._warn_retry("rate-limited", wait, attempt)
                time.sleep(wait)
                continue
            # Non-streaming responses must carry choices; some gateways return 200 with an error
            # body (choices=None) when the upstream provider hiccups — treat as transient.
            if not streaming and not getattr(resp, "choices", None):
                if attempt == self.MAX_RETRIES:
                    detail = getattr(resp, "error", None) or resp
                    raise RuntimeError(f"{self.LABEL}: no choices after retries: {detail}")
                wait = 2 * (2**attempt)
                self._warn_retry("empty response", wait, attempt)
                time.sleep(wait)
                continue
            return resp

    def _warn_retry(self, reason: str, wait: float, attempt: int) -> None:
        print(
            f"  [{self.LABEL}] {reason}; retrying in {wait:.0f}s "
            f"(attempt {attempt + 1}/{self.MAX_RETRIES})",
            file=sys.stderr,
        )

    @staticmethod
    def _retry_after(exc: RateLimitError) -> float | None:
        try:
            value = exc.response.headers.get("retry-after")
            return float(value) if value is not None else None
        except (AttributeError, TypeError, ValueError):
            return None

    # -- interface ---------------------------------------------------------- #
    def chat(
        self,
        messages: Messages,
        *,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
        thinking: bool = False,  # not portable; ignored
        effort: str | None = None,  # ignored
        cache: bool = False,  # ignored
    ) -> LLMResponse:
        resp = self._create(
            model=model or self.DEFAULT_MODEL,
            max_tokens=max_tokens or 1024,
            messages=self._to_openai(messages, system),
        )
        choice = resp.choices[0]
        return LLMResponse(
            text=choice.message.content or "",
            model=resp.model,
            stop_reason=choice.finish_reason,
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
        stream = self._create(
            model=model or self.DEFAULT_MODEL,
            max_tokens=max_tokens or 1024,
            messages=self._to_openai(messages, system),
            stream=True,
        )
        for chunk in stream:
            if not chunk.choices:
                continue
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    def count_tokens(
        self,
        messages: Messages,
        *,
        system: str | None = None,
        model: str | None = None,
    ) -> int:
        """APPROXIMATE input-token count. The OpenAI protocol has no pre-send count endpoint, so
        this uses a ~4-chars-per-token heuristic. Exact counts come back in `usage` after a call.
        """
        print(
            f"  [{self.LABEL}] note: count_tokens is an estimate (~chars/4); no exact endpoint.",
            file=sys.stderr,
        )
        text = system or ""
        for m in self._normalize(messages):
            text += m["content"]
        return max(1, len(text) // 4)

    def structured_chat(
        self,
        messages: Messages,
        *,
        schema: dict,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
    ) -> tuple[dict, LLMResponse]:
        # response_format json_schema constrains output on models that support it. Models under
        # load occasionally return empty/invalid content despite it; retry a few times before
        # giving up (transport-level 429s/empty-body are already handled by _create).
        params = {
            "model": model or self.DEFAULT_MODEL,
            "max_tokens": max_tokens or 1024,
            "messages": self._to_openai(messages, system),
            "response_format": {
                "type": "json_schema",
                "json_schema": {"name": "response", "strict": True, "schema": schema},
            },
        }
        for attempt in range(self.MAX_RETRIES + 1):
            resp = self._create(**params)
            choice = resp.choices[0]
            text = choice.message.content or ""
            try:
                parsed = json.loads(text)
            except json.JSONDecodeError:
                if attempt == self.MAX_RETRIES:
                    raise
                wait = 2 * (2**attempt)
                self._warn_retry("empty/invalid JSON from structured output", wait, attempt)
                time.sleep(wait)
                continue
            return parsed, LLMResponse(
                text=text,
                model=resp.model,
                stop_reason=choice.finish_reason,
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
        oa_tools = [
            {
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description,
                    "parameters": t.input_schema,
                },
            }
            for t in tools
        ]
        convo: list[dict] = self._to_openai(messages, system)
        steps: list[ToolCall] = []
        tin = tout = 0

        for i in range(max_iters):
            resp = self._create(
                model=model,
                max_tokens=max_tokens,
                messages=convo,
                tools=oa_tools,
            )
            if resp.usage:
                tin += resp.usage.prompt_tokens or 0
                tout += resp.usage.completion_tokens or 0
            msg = resp.choices[0].message
            # Echo the assistant turn back verbatim so tool_call ids line up.
            convo.append(msg.model_dump(exclude_none=True))

            if not msg.tool_calls:
                return ToolLoopResult(msg.content or "", Usage(tin, tout), steps, i + 1)

            # Execute every requested tool; append one tool message per call.
            for tc in msg.tool_calls:
                try:
                    args = json.loads(tc.function.arguments or "{}")
                except json.JSONDecodeError:
                    args = {}
                call = ToolCall(id=tc.id, name=tc.function.name, input=args)
                steps.append(call)
                if on_tool_call:
                    on_tool_call(call)
                handler = handlers.get(tc.function.name)
                try:
                    output = handler(args) if handler else f"Error: no handler '{tc.function.name}'"
                except Exception as exc:  # tool failures are data, not crashes
                    output = f"Error: {exc}"
                convo.append({"role": "tool", "tool_call_id": tc.id, "content": str(output)})

        return ToolLoopResult(
            "(stopped: max tool iterations reached)", Usage(tin, tout), steps, max_iters
        )

    # -- helpers ------------------------------------------------------------ #
    def _to_openai(self, messages: Messages, system: str | None) -> list[dict]:
        """Normalize to OpenAI wire format: system folds into a leading system message."""
        out: list[dict] = []
        if system:
            out.append({"role": "system", "content": system})
        out.extend(self._normalize(messages))
        return out

    @staticmethod
    def _usage(u) -> Usage:
        if u is None:
            return Usage()
        return Usage(
            input_tokens=getattr(u, "prompt_tokens", 0) or 0,
            output_tokens=getattr(u, "completion_tokens", 0) or 0,
        )
