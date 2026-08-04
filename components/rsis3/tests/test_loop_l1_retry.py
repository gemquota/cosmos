"""Unit tests for L1 retry policy (fatal fail-fast + budget enforcement)."""

import pytest

from rsis.config import CONFIG
from rsis.loop_l1 import L1ActionLoop


class StubTelemetry:
    def __init__(self):
        self.events = []

    def record(self, event):
        self.events.append(event)


class StubCheckpoint:
    def checkpoint(self, *args, **kwargs):
        return None


@pytest.fixture
def l1_env():
    old = {
        "tools_enabled": CONFIG.tools.enabled,
        "checkpoint": CONFIG.checkpoint_before_mutation,
        "max_retries": CONFIG.l1.max_retries,
    }
    CONFIG.tools.enabled = False          # use plain callable routing
    CONFIG.checkpoint_before_mutation = False
    CONFIG.l1.max_retries = 2
    yield
    CONFIG.tools.enabled = old["tools_enabled"]
    CONFIG.checkpoint_before_mutation = old["checkpoint"]
    CONFIG.l1.max_retries = old["max_retries"]


def make_loop(tools, max_retries=2):
    CONFIG.l1.max_retries = max_retries
    return L1ActionLoop(
        telemetry=StubTelemetry(),
        checkpoint_mgr=StubCheckpoint(),
        tools=tools,
        tool_manager=None,
    )


def test_transient_failure_recovers(l1_env):
    calls = {"n": 0}

    def run(**kwargs):
        calls["n"] += 1
        if calls["n"] < 3:
            raise RuntimeError("connection reset")
        return "ok"

    loop = make_loop({"run": run})
    result = loop.execute("run something")
    assert result.success is True
    assert result.final_output == "ok"
    assert calls["n"] == 3
    names = [c.name for c in result.tool_calls]
    assert names.count("retry") == 2     # one retry beat per failure


def test_fatal_failure_fails_fast(l1_env):
    def run(**kwargs):
        raise ValueError("invalid syntax")

    loop = make_loop({"run": run})
    result = loop.execute("run something")
    assert result.success is False
    assert len(result.tool_calls) == 1   # no retry beat, no second attempt
    assert result.tool_calls[0].name == "run"
    assert "invalid syntax" in result.tool_calls[0].error


def test_retry_budget_exhausted(l1_env):
    def run(**kwargs):
        raise RuntimeError("503 service unavailable")

    loop = make_loop({"run": run}, max_retries=2)
    result = loop.execute("run something")
    assert result.success is False
    names = [c.name for c in result.tool_calls]
    assert names.count("run") == 3       # initial + 2 retried attempts
    assert names.count("retry") == 2     # budget spent, then stop


def test_rate_limit_is_retryable(l1_env):
    calls = {"n": 0}

    def run(**kwargs):
        calls["n"] += 1
        if calls["n"] < 2:
            raise RuntimeError("429 rate limit")
        return "ok"

    loop = make_loop({"run": run}, max_retries=2)
    result = loop.execute("run something")
    assert result.success is True
    assert calls["n"] == 2
