"""Tool & Access Manager — registry + secrets vault + audit (ported from Agent OS).

Security model:
  * secrets live in a vault, never in the agent's context window
  * tools declare the env vars they need; only those are injected
  * every call is checked against the calling agent's allowlist
  * every call is audited (redacted) to the audit log
  * risky calls pause for operator approval via the HITL gate
"""

from __future__ import annotations

import concurrent.futures
import json
import logging
import os
import re
import time
from pathlib import Path

from rsis.tools.base import Tool, ToolResult, ToolStatus
from rsis.tools.hitl import HITLSafetyGate

logger = logging.getLogger(__name__)


class SecretVault:
    """Holds credentials out of band (env vars or OS keyring)."""

    def __init__(self, backend: str = "env", service: str = "rsis"):
        self.backend = backend
        self.service = service
        self._cache: dict[str, str | None] = {}

    def get(self, name: str) -> str | None:
        """Fetch a secret. Result is cached and can be used for redaction."""
        if name in self._cache:
            return self._cache[name]
        value: str | None = None
        if self.backend == "keyring":
            try:
                import keyring
                value = keyring.get_password(self.service, name)
            except Exception as exc:
                logger.warning("keyring backend failed (%s); trying env", exc)
        if value is None:
            value = os.getenv(name)
        self._cache[name] = value
        return value

    # Sensitive-value patterns caught even when the exact secret was never
    # loaded into the vault (belt-and-suspenders beyond exact-match masking).
    _SECRET_PATTERNS = [
        (r"github_pat_[A-Za-z0-9_]{10,}", "github_pat"),
        (r"gh[pousr]_[A-Za-z0-9]{20,}", "github_token"),
        (r"sk-[A-Za-z0-9]{16,}", "openai_key"),
        (r"AIza[0-9A-Za-z_\-]{20,}", "google_key"),
        (r"AKIA[0-9A-Z]{16}", "aws_access_key"),
        (r"xox[baprs]-[A-Za-z0-9-]{10,}", "slack_token"),
        (r"eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}",
         "jwt"),
        (r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", "private_key"),
    ]

    def redact(self, text: str) -> str:
        """Mask every known secret and sensitive pattern (logs, output)."""
        for name, value in self._cache.items():
            if value and len(value) >= 4 and value in text:
                text = text.replace(value, f"<redacted:{name}>")
        for pattern, label in self._SECRET_PATTERNS:
            text = re.sub(pattern, f"<redacted:{label}>", text)
        return text


class ToolManager:
    """Registry + authorization + audit for all tool execution."""

    def __init__(self, sandbox, config, audit_path: Path | None = None):
        self.sandbox = sandbox
        self.config = config
        self.vault = SecretVault(backend=getattr(config, "secret_backend", "env"))
        self.tools: dict[str, Tool] = {}
        self.audit_path = Path(audit_path or config.audit_log)
        self.audit_path.parent.mkdir(parents=True, exist_ok=True)
        self.telemetry_hook = None   # optional callable(agent, tool, status, latency_s)
        self.hitl_gate: HITLSafetyGate | None = None
        self._executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="rsis-tool")

    # ------------------------------------------------------------------ #
    def register(self, tool: Tool) -> None:
        self.tools[tool.name] = tool
        # Preload declared secrets into the vault cache so redaction
        # covers them even before the tool is ever called.
        for name in tool.requires_secrets:
            self.vault.get(name)
        logger.info("tool registered: %s (secrets=%s)",
                    tool.name, tool.requires_secrets)

    def list_tools(self, agent_name: str | None = None) -> list[str]:
        """Names of tools the agent may call (or all, when agent is None)."""
        if agent_name is None:
            return sorted(self.tools)
        return sorted(name for name, t in self.tools.items()
                      if not t.agent_allowlist or agent_name in t.agent_allowlist)

    # ------------------------------------------------------------------ #
    def execute(self, agent_name: str, tool_name: str,
                args: dict) -> ToolResult:
        """Validate, authorize, execute, and audit one tool call."""
        tool = self.tools.get(tool_name)
        if tool is None:
            return self._audit(agent_name, tool_name, args, ToolResult(
                ToolStatus.ERROR, f"unknown tool: {tool_name}"))

        # --- authorization ------------------------------------------- #
        if tool.agent_allowlist and agent_name not in tool.agent_allowlist:
            return self._audit(agent_name, tool_name, args, ToolResult(
                ToolStatus.DENIED,
                f"agent '{agent_name}' is not allowed to use '{tool_name}'"))

        # --- validation ----------------------------------------------- #
        validation_error = self._validate(tool, args)
        if validation_error:
            return self._audit(agent_name, tool_name, args, ToolResult(
                ToolStatus.ERROR, validation_error))

        # --- HITL: operator approval for risky actions ------------------ #
        if self.config.hitl_enabled and self.hitl_gate is not None:
            if not self.hitl_gate.intercept_and_authorize(
                    agent_name, tool_name, args):
                return self._audit(agent_name, tool_name, args, ToolResult(
                    ToolStatus.DENIED,
                    "blocked by operator approval (HITL)"))

        # --- execution (worker thread + hard timeout) ----------------- #
        started = time.monotonic()
        try:
            future = self._executor.submit(tool.run, self, args)
            result = future.result(timeout=self.config.sandbox_timeout)
        except concurrent.futures.TimeoutError:
            result = ToolResult(
                ToolStatus.TIMEOUT,
                f"tool '{tool_name}' exceeded {self.config.sandbox_timeout}s")
        except Exception as exc:  # defensive: tool bugs must not kill L1
            logger.exception("tool %s crashed", tool_name)
            result = ToolResult(ToolStatus.ERROR, f"tool crashed: {exc}")

        result.metadata["latency_s"] = round(time.monotonic() - started, 3)
        # Never leak secrets back into the agent's context.
        result.output = self.vault.redact(result.output)
        return self._audit(agent_name, tool_name, args, result)

    # ------------------------------------------------------------------ #
    def scoped_env(self, tool: Tool) -> dict[str, str]:
        """Minimal env containing ONLY the secrets this tool declared."""
        env: dict[str, str] = {}
        for name in tool.requires_secrets:
            value = self.vault.get(name)
            if value:
                env[name] = value
        return env

    # ------------------------------------------------------------------ #
    @staticmethod
    def _validate(tool: Tool, args: dict) -> str | None:
        """Lightweight JSON-schema-ish validation for tool arguments."""
        types = {"string": str, "integer": int, "number": (int, float),
                 "boolean": bool, "array": list, "object": dict}
        for name, spec in tool.parameters.items():
            if spec.get("required") and name not in args:
                return f"missing required argument '{name}'"
            if name in args and "type" in spec:
                expected = types.get(spec["type"])
                if expected and not isinstance(args[name], expected):
                    return f"argument '{name}' must be {spec['type']}"
        return None

    def _audit(self, agent: str, tool_name: str, args: dict,
               result: ToolResult) -> ToolResult:
        """Append a redacted record of the call to the audit log."""
        record = {
            "ts": time.time(),
            "agent": agent,
            "tool": tool_name,
            "args": self.vault.redact(json.dumps(args, default=str))[:300],
            "risk": getattr(self.tools.get(tool_name), "risk", "write"),
            "status": result.status.value,
            "output": result.output[:400],
            "latency_s": result.metadata.get("latency_s"),
        }
        with self.audit_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record) + "\n")
        if self.telemetry_hook is not None:
            try:
                self.telemetry_hook(agent, tool_name, result.status.value,
                                    result.metadata.get("latency_s", 0.0))
            except Exception as exc:
                logger.warning("telemetry hook failed: %s", exc)
        logger.info("tool %s by %s -> %s (%.2fs)", tool_name, agent,
                    result.status.value, record["latency_s"] or 0)
        return result
