"""Role profiles — a named persona bound to its least-privilege MCP toolset (compose, don't God-Agent).

Purpose:    A `RoleProfile` names a reusable specialist (software engineer, tech writer, …) as three
            references, never copies (Constitution: single responsibility, reuse):
              - a role system prompt   (`prompts/role/<file>`, layered on the base prompt),
              - the MCP servers it may use (coarse least privilege — e.g. filesystem + github),
              - an optional tool allowlist (fine least privilege) + skills to fold in.
Usage:      with open_toolset(PROFILES["tech-writer"]) as mc:
                agent = build_agent(PROFILES["tech-writer"], provider, mc)
                agent.run("Document the MCP bridge and open a docs PR.")
Depends on: core.agents, core.mcp_client, core.prompting, core.skills. No vendor SDK (ADR 0001).
Design:     Profiles are data; the helpers do the composition. Add a role = add a prompt + a row here.
"""

from __future__ import annotations

from dataclasses import dataclass

from core.agents import Agent
from core.mcp_client import MCPClient
from core.prompting import assemble_system, read_prompt
from core.providers import LLMProvider
from core.skills import SkillRegistry


@dataclass(frozen=True)
class RoleProfile:
    """A named specialist: role prompt + the MCP servers/tools it may use + skills to include."""

    name: str
    role_prompt: str  # filename under prompts/role/
    servers: tuple[str, ...] = ()  # manifest server names this role may connect to
    allow: tuple[str, ...] | None = None  # un-namespaced tool allowlist; None = all tools
    skills: tuple[str, ...] = ()  # skill names folded into the system prompt
    description: str = ""


# Registry — add a role by adding a prompt under prompts/role/ and a row here.
PROFILES: dict[str, RoleProfile] = {
    "software-engineer": RoleProfile(
        name="software-engineer",
        role_prompt="software_engineer.md",
        servers=("filesystem", "github-remote"),
        description="Reads and edits code through tools; proposes and opens pull requests.",
    ),
    "tech-writer": RoleProfile(
        name="tech-writer",
        role_prompt="tech_writer.md",
        servers=("filesystem", "github-remote"),
        skills=("changelog-writer",),
        description="Generates and updates project documentation; opens docs pull requests.",
    ),
}


# --------------------------------------------------------------------------- #
# Composition helpers
# --------------------------------------------------------------------------- #
def role_system(profile: RoleProfile, *, base: str | None = None) -> str:
    """Assemble the role's system prompt: base → role → any skill bodies (progressive disclosure)."""
    layers = [base if base is not None else read_prompt("base", "base_system.md")]
    layers.append(read_prompt("role", profile.role_prompt))
    if profile.skills:
        reg = SkillRegistry()
        layers.extend(reg.load_body(name) for name in profile.skills)
    return assemble_system(*layers)


def open_toolset(profile: RoleProfile, *, servers: tuple[str, ...] | None = None, **kwargs) -> MCPClient:
    """Open the role's MCP toolset (context manager) with its tool allowlist.

    `servers` overrides the profile's server list (e.g. to open only the startable ones for a dry
    run). Raises a clear error if a requested server is not startable (missing ${ENV}).
    """
    names = servers if servers is not None else profile.servers
    return MCPClient.from_manifest(names, allow=profile.allow, **kwargs)


def build_agent(
    profile: RoleProfile,
    provider: LLMProvider,
    mc: MCPClient,
    *,
    model: str | None = None,
    max_tokens: int | None = None,
) -> Agent:
    """Compose an Agent for this role, bound to an already-open MCP toolset."""
    return Agent(
        profile.name,
        provider,
        role_system(profile),
        model=model,
        max_tokens=max_tokens,
        tools=mc.tools,
        handlers=mc.handlers,
    )
