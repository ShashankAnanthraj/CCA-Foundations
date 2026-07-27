"""core.mcp_client — manifest parsing, env resolution, and pure bridge helpers (no SDK needed)."""

from __future__ import annotations

import json

import pytest

from core.mcp_client import (
    MCPClient,
    ServerSpec,
    _as_predicate,
    _result_text,
    load_manifest,
)


def _write_manifest(tmp_path, servers: dict):
    p = tmp_path / "servers.json"
    p.write_text(json.dumps({"mcpServers": servers}), encoding="utf-8")
    return p


def test_env_expansion_and_missing_env(tmp_path, monkeypatch):
    monkeypatch.setenv("MY_DIR", "/work/proj")
    monkeypatch.delenv("NO_SUCH", raising=False)
    p = _write_manifest(
        tmp_path,
        {
            "fs": {"command": "npx", "args": ["-y", "srv", "${MY_DIR}"]},
            "broken": {"command": "npx", "args": ["${NO_SUCH}"]},
        },
    )
    m = load_manifest(p)
    assert m["fs"].args == ["-y", "srv", "/work/proj"]
    assert m["fs"].missing_env == ()
    assert m["fs"].startable is True
    assert m["broken"].missing_env == ("NO_SUCH",)
    assert m["broken"].startable is False  # unresolved placeholder → not startable


def test_startable_rules():
    assert ServerSpec("s", "stdio", command="python", args=["ok"]).startable is True
    assert ServerSpec("s", "stdio", command="python", args=[""]).startable is False
    assert ServerSpec("s", "stdio", command=None).startable is False
    assert ServerSpec("h", "http", url="https://x/mcp").startable is True
    assert ServerSpec("h", "http", url="not-a-url").startable is False
    assert ServerSpec("h", "http", url=None).startable is False


def test_from_manifest_raises_with_actionable_message(tmp_path, monkeypatch):
    monkeypatch.delenv("TOKEN", raising=False)
    p = _write_manifest(tmp_path, {"gh": {"transport": "http", "url": "https://x", "headers": {"Authorization": "Bearer ${TOKEN}"}}})
    with pytest.raises(ValueError, match="TOKEN"):
        MCPClient.from_manifest(["gh"], path=p)


def test_from_manifest_unknown_server_raises(tmp_path):
    p = _write_manifest(tmp_path, {"a": {"command": "x", "args": ["y"]}})
    with pytest.raises(KeyError):
        MCPClient.from_manifest(["missing"], path=p)


def test_as_predicate_forms():
    assert _as_predicate(None)("anything") is True
    only = _as_predicate({"read", "write"})
    assert only("read") is True and only("delete") is False
    assert _as_predicate(lambda n: n.startswith("get"))("get_x") is True


def test_exposed_name_namespacing_and_length():
    c = MCPClient([])  # no connection needed for the pure helper
    assert c._exposed_name("github-remote", "create_pr") == "github-remote__create_pr"
    long = c._exposed_name("srv", "x" * 100)
    assert len(long) <= 64
    c_flat = MCPClient([], namespace=False)
    assert c_flat._exposed_name("srv", "tool") == "tool"


class _FakeResult:
    def __init__(self, texts, is_error=False, structured=None):
        self.content = [type("B", (), {"text": t})() for t in texts]
        self.isError = is_error
        self.structuredContent = structured


def test_result_text_extraction():
    assert _result_text(_FakeResult(["hello", "world"])) == "hello world"
    assert _result_text(_FakeResult(["boom"], is_error=True)) == "Error: boom"
    assert _result_text(_FakeResult([], structured={"n": 1})) == '{"n": 1}'
