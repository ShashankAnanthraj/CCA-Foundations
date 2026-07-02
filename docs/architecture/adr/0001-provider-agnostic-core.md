# ADR 0001 — Provider-agnostic core

- **Status:** Accepted
- **Date:** 2026-07-02

## Context
The Constitution requires AI‑OS to be model-, vendor-, and cloud-agnostic and to support 20+
providers without architectural change. Demos and capabilities must not bind to one SDK.

## Decision
All model access flows through a single abstraction, `core.providers.LLMProvider` (an ABC with
normalized request/response types: `ChatMessage`, `LLMResponse`, `Usage`). Concrete adapters live
under `providers/<vendor>/` and are the *only* code allowed to import a vendor SDK. Cost estimation
lives on the provider via a pricing registry, keyed by model id.

## Consequences
- **+** Swap `claude` → `openai`/`ollama`/… by adding an adapter; nothing above the capability plane changes.
- **+** Uniform usage/cost telemetry across providers.
- **−** A thin translation layer per adapter (accepted; small and isolated).

## Alternatives rejected
- Calling `anthropic` SDK directly from topics/demos → violates vendor-agnostic + DRY.
- A heavy framework (LangChain-style) → conflicts with Simplicity/KISS and token economy.
