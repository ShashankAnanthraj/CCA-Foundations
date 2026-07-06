"""core.profiles — role registry + prompt composition (key-free)."""

from __future__ import annotations

import pytest

from core.profiles import PROFILES, RoleProfile, build_agent, role_system


def test_registry_has_expected_roles():
    assert {"software-engineer", "tech-writer"} <= set(PROFILES)
    for name, p in PROFILES.items():
        assert p.name == name
        assert p.role_prompt.endswith(".md")


def test_role_system_layers_base_role_and_skills():
    sys_prompt = role_system(PROFILES["tech-writer"])
    # base prompt + the tech-writer role + the folded-in changelog-writer skill body.
    assert "technical writer" in sys_prompt.lower()
    assert "Changelog Writer" in sys_prompt  # skill body was appended
    assert sys_prompt.strip()


def test_role_system_without_skills():
    sys_prompt = role_system(PROFILES["software-engineer"])
    assert "software engineer" in sys_prompt.lower()


def test_profile_is_immutable():
    with pytest.raises(Exception):
        PROFILES["tech-writer"].name = "x"  # frozen dataclass


def test_build_agent_binds_toolset(fake_provider):
    # A tiny stand-in for an open MCPClient: just needs .tools and .handlers.
    class _MC:
        tools = []
        handlers: dict = {}

    profile = RoleProfile(name="r", role_prompt="software_engineer.md")
    agent = build_agent(profile, fake_provider, _MC())
    assert agent.name == "r"
    assert "software engineer" in agent.system.lower()
    assert agent.run("hi").text == "echo: hi"
