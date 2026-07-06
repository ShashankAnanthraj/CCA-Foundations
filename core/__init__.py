"""AI-OS control plane (kernel).

Exposes the provider-agnostic interface and configuration. Nothing here imports a
vendor SDK — concrete adapters live under `providers/`.
"""

from core.agents import (
    Agent,
    AgentResult,
    approval_gate,
    fan_out,
    parallel_agents,
    pipeline,
    router,
)
from core.config import Settings, get_settings
from core.conversation import Conversation
from core.projects import Project, load_project
from core.mcp_client import MCPClient, ServerSpec, load_manifest
from core.profiles import PROFILES, RoleProfile, build_agent, open_toolset, role_system
from core.prompting import assemble_system, read_prompt
from core.providers import (
    ChatMessage,
    LLMProvider,
    LLMResponse,
    Usage,
    get_provider,
    get_provider_class,
)
from core.skills import SkillMeta, SkillRegistry
from core.tools import ToolCall, ToolLoopResult, ToolSpec

__all__ = [
    "Settings",
    "get_settings",
    "assemble_system",
    "read_prompt",
    "ChatMessage",
    "LLMProvider",
    "LLMResponse",
    "Usage",
    "get_provider",
    "get_provider_class",
    "SkillMeta",
    "SkillRegistry",
    "ToolSpec",
    "ToolCall",
    "ToolLoopResult",
    "Agent",
    "AgentResult",
    "router",
    "pipeline",
    "parallel_agents",
    "fan_out",
    "approval_gate",
    "Conversation",
    "Project",
    "load_project",
    "MCPClient",
    "ServerSpec",
    "load_manifest",
    "RoleProfile",
    "PROFILES",
    "role_system",
    "open_toolset",
    "build_agent",
]
