"""Model provider adapters (capability plane).

The ONLY place allowed to import a vendor SDK. Each adapter implements
`core.providers.LLMProvider`, keeping AI-OS model/vendor-agnostic (ADR 0001).
"""
