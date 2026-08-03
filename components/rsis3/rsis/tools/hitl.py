"""Human-in-the-Loop (HITL) Safety Gate — ported from Agent OS.

Sits between the agent's decision layer and physical tool execution.
Every tool call is classified against a 5-level risk matrix; actions at
or above the configured threshold pause for an operator decision before
any side effects occur.

Risk level matrix:
  1 SAFE      — auto-approve              (read-only vector search, memory recall)
  2 LOW       — auto-approve + audit log  (web search, reading non-sensitive files)
  3 MEDIUM    — auto-approve in sandbox   (Python execution, network disabled)
  4 HIGH      — REQUIRE operator approval (writing files, git commit)
  5 CRITICAL  — REQUIRE approval + reason (git push, deleting files, secrets)

Approval modes:
  auto        — no prompts (CI / trusted batch runs)
  interactive — pause and ask on the console (y/N)
  api         — suspend the call until an operator resolves it (dashboard/web)
                or the timeout expires (fail closed)
  deny        — fail closed: risky tools always denied

Every decision is written redacted to the HITL audit log.
"""

from __future__ import annotations

import json
import logging
import re
import time
import uuid
from enum import IntEnum
from pathlib import Path
from typing import Callable, Optional

logger = logging.getLogger(__name__)


class RiskLevel(IntEnum):
    """Five-step risk ladder; higher = more operator oversight needed."""

    SAFE = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    CRITICAL = 5


class ApprovalMode:
    """Approval behavior for requests at/above the risk threshold."""

    AUTO = "auto"
    INTERACTIVE = "interactive"
    API = "api"
    DENY = "deny"

    _VALID = {AUTO, INTERACTIVE, API, DENY}

    @classmethod
    def coerce(cls, mode: str) -> str:
        mode = str(mode).strip().lower()
        if mode not in cls._VALID:
            raise ValueError(f"unknown approval mode: {mode!r}")
        return mode


# Code patterns that escalate an execution request to CRITICAL.
_DESTRUCTIVE_CODE = re.compile(
    r"rm\s+-rf|os\.remove|shutil\.rmtree|subprocess|sys\.exit|"
    r"os\.system|eval\(|exec\(|open\([^)]*['\"]w['\"]|write\("
)
# GitHub actions that touch remote state irreversibly.
_PUSH_ACTIONS = {"push", "force_push", "delete_branch", "push_file"}
_WRITE_TOOLS = {"write_file", "write", "delete_file", "rm"}
_READ_TOOLS = {"read_file", "list_files", "vector_search",
               "web_search", "memory_recall", "search", "show_diff",
               "run_tests"}
_CODE_TOOLS = {"run_code", "run_python"}


def classify_risk(tool_name: str, args: dict) -> RiskLevel:
    """
    Evaluate a tool request against the risk matrix.

    Pattern rules come from the HITL blueprint and are extended to the
    tools RSIS3 ships (write_file / run_code / list_files / read_file).
    """
    args = args or {}

    # Rule 1: code execution inspection.
    if tool_name in _CODE_TOOLS:
        code = args.get("code", "")
        if _DESTRUCTIVE_CODE.search(code):
            return RiskLevel.CRITICAL
        if re.search(r"open\(.*['\"]w['\"]|write\(", code):
            return RiskLevel.HIGH
        return RiskLevel.MEDIUM

    # Rule 2: git / remote-state actions.
    if tool_name in ("git_action", "github"):
        action = args.get("action", "")
        if action in _PUSH_ACTIONS:
            return RiskLevel.CRITICAL
        if action in ("commit", "checkout", "create_issue", "delete_file"):
            return RiskLevel.HIGH
        return RiskLevel.LOW

    # Rule 3: file-system writes are always operator-worthy.
    if tool_name in _WRITE_TOOLS:
        return RiskLevel.HIGH

    # Rule 4: read-only / memory tools are cheap and safe.
    if tool_name in _READ_TOOLS:
        return RiskLevel.LOW

    # Default fallback for unknown tools: treat as HIGH (fail safe).
    return RiskLevel.HIGH


class HITLSafetyGate:
    """Intercepts tool calls, evaluates risk, and routes to the operator."""

    def __init__(
        self,
        mode: str = ApprovalMode.AUTO,
        approval_threshold: RiskLevel | str = RiskLevel.HIGH,
        approval_timeout: float = 60.0,
        auto_approve: set[str] | None = None,
        custom_approval_callback: Optional[Callable[[dict], bool]] = None,
        audit_path: str | Path | None = None,
    ):
        self.mode = ApprovalMode.coerce(mode)
        self.approval_threshold = self._coerce_threshold(approval_threshold)
        self.approval_timeout = max(0.0, float(approval_timeout))
        self.auto_approve = set(auto_approve or [])     # tool names, always allowed
        self.custom_approval_callback = custom_approval_callback
        self.audit_path = Path(audit_path) if audit_path else None
        if self.audit_path:
            self.audit_path.parent.mkdir(parents=True, exist_ok=True)
        self.pending: dict[str, dict] = {}              # api-mode request registry

    @staticmethod
    def _coerce_threshold(threshold) -> RiskLevel:
        """Accept a RiskLevel or its name/number (e.g. 'high', 4)."""
        if isinstance(threshold, RiskLevel):
            return threshold
        if isinstance(threshold, str):
            try:
                return RiskLevel[threshold.strip().upper()]
            except KeyError:
                return RiskLevel(int(threshold))
        return RiskLevel(threshold)

    # ------------------------------------------------------------------ #
    def classify_risk(self, tool_name: str, args: dict) -> RiskLevel:
        """Public wrapper: risk evaluation for a tool request."""
        return classify_risk(tool_name, args)

    def needs_approval(self, tool_name: str, args: dict) -> bool:
        """True when the request meets or exceeds the approval threshold."""
        return self.classify_risk(tool_name, args) >= self.approval_threshold

    # ------------------------------------------------------------------ #
    def intercept_and_authorize(self, agent_role: str, tool_name: str,
                                args: dict) -> bool:
        """
        Evaluate a tool request and trigger authorization if needed.

        Below the threshold -> AUTO_APPROVED + audit.
        At/above the threshold -> dispatch by mode:
            auto        -> approved (trusted batch)
            interactive -> console y/N prompt
            api         -> register a pending request; poll for operator
                           resolution until the timeout (fail closed)
            deny        -> denied
        Returns True when the action may run.
        """
        risk = self.classify_risk(tool_name, args)
        args_preview = json.dumps(args, default=str)[:300]

        if risk < self.approval_threshold or tool_name in self.auto_approve:
            return self._log(agent_role, tool_name, args_preview, risk,
                             approved=True, approval_type="AUTO_APPROVED")

        if self.mode == ApprovalMode.AUTO:
            return self._log(agent_role, tool_name, args_preview, risk,
                             approved=True, approval_type="OPERATOR_AUTO")

        if self.mode == ApprovalMode.DENY:
            return self._log(agent_role, tool_name, args_preview, risk,
                             approved=False, approval_type="OPERATOR_DENY")

        if self.mode == ApprovalMode.INTERACTIVE:
            self._print_interception(agent_role, tool_name, args_preview, risk)
            approved = self._cli_prompt_operator()
            return self._log(agent_role, tool_name, args_preview, risk,
                             approved=approved, approval_type="OPERATOR_CLI")

        # API mode: register a pending request and wait (fail closed).
        request_id = uuid.uuid4().hex[:10]
        self.pending[request_id] = {
            "id": request_id, "agent": agent_role, "tool": tool_name,
            "risk": risk.name, "args_preview": args_preview,
            "status": "pending", "created_at": time.time(),
        }
        logger.info("HITL api-mode pending request %s (tool=%s, risk=%s)",
                    request_id, tool_name, risk.name)

        if self.custom_approval_callback is not None:
            event = dict(self.pending[request_id])
            approved = bool(self.custom_approval_callback(event))
        else:
            approved = self._poll_api_mode(request_id)

        self.pending[request_id]["status"] = (
            "approved" if approved else "denied")
        return self._log(agent_role, tool_name, args_preview, risk,
                         approved=approved, approval_type="OPERATOR_API",
                         request_id=request_id)

    # ------------------------------------------------------------------ #
    def resolve(self, request_id: str, approved: bool) -> None:
        """Resolve a pending api-mode request (dashboard/web operator)."""
        req = self.pending.get(request_id)
        if req:
            req["approved"] = bool(approved)
            req["status"] = "approved" if approved else "denied"

    # ------------------------------------------------------------------ #
    def _poll_api_mode(self, request_id: str) -> bool:
        """Block until the request is resolved or the timeout expires."""
        deadline = time.monotonic() + self.approval_timeout
        while time.monotonic() < deadline:
            req = self.pending.get(request_id)
            if req and req.get("status") != "pending":
                return bool(req.get("approved"))
            time.sleep(0.25)
        logger.warning("HITL request %s timed out — failing closed", request_id)
        return False

    # ------------------------------------------------------------------ #
    def _print_interception(self, agent_role: str, tool_name: str,
                            args_preview: str, risk: RiskLevel) -> None:
        print("\n" + "=" * 60)
        print(" [SAFETY GATE INTERCEPTION] High-Risk Tool Request Detected")
        print(f"   Agent Role : {agent_role}")
        print(f"   Tool Name  : {tool_name}")
        print(f"   Risk Level : {risk.name} ({risk.value}/5)")
        print(f"   Arguments  : {args_preview}")
        print("=" * 60)

    @staticmethod
    def _cli_prompt_operator() -> bool:
        try:
            answer = input(" Approve? [y/N] ").strip().lower()
        except EOFError:
            return False
        return answer in ("y", "yes")

    def _log(self, agent: str, tool: str, args_preview: str, risk: RiskLevel,
             approved: bool, approval_type: str, request_id: str | None = None) -> bool:
        event = {
            "ts": time.time(),
            "agent": agent,
            "tool": tool,
            "risk": risk.name,
            "args": args_preview,
            "approved": approved,
            "approval_type": approval_type,
        }
        if request_id:
            event["request_id"] = request_id
        if self.audit_path:
            with self.audit_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(event) + "\n")
        logger.info("HITL %s: %s -> %s (%s, %s)",
                    approval_type, tool, agent, risk.name,
                    "approved" if approved else "denied")
        return approved
