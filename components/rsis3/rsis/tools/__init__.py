"""RSIS3 tool layer — sandboxed execution with allowlists + HITL approvals.

Ported from the Agent OS project (`~/dev/codex/ao`). See
`docs/ao-assessment.md` for the inclusion rationale.
"""

from __future__ import annotations

from pathlib import Path

from rsis.tools.base import Tool, ToolResult, ToolStatus
from rsis.tools.hitl import (
    ApprovalMode,
    HITLSafetyGate,
    RiskLevel,
    classify_risk,
)
from rsis.tools.manager import SecretVault, ToolManager
from rsis.tools.sandbox import Sandbox, SandboxResult
from rsis.tools.workspace_tools import (
    ListFilesTool,
    ReadFileTool,
    RunCodeTool,
    WriteFileTool,
)

__all__ = [
    "ApprovalMode",
    "HITLSafetyGate",
    "ListFilesTool",
    "ReadFileTool",
    "RiskLevel",
    "RunCodeTool",
    "Sandbox",
    "SandboxResult",
    "SecretVault",
    "Tool",
    "ToolManager",
    "ToolResult",
    "ToolStatus",
    "WriteFileTool",
    "classify_risk",
]


def default_tool_manager(workspace_dir: str | Path, config=None) -> ToolManager:
    """Build a ToolManager with the standard workspace tools.

    Sandbox root is the RSIS workspace; only files under it are reachable.
    The HITL gate is wired when config.tools.hitl_enabled is set.
    """
    if config is None:
        from rsis.config import CONFIG
        config = CONFIG.tools

    sandbox = Sandbox(
        workdir=Path(workspace_dir),
        default_timeout=config.sandbox_timeout,
        allow_network=config.sandbox_allow_network,
        max_memory_mb=config.sandbox_max_memory_mb,
        mem_limit=config.sandbox_mem_limit,
        backend=config.sandbox_backend,
        docker_image=config.sandbox_docker_image,
        docker_mem_limit=config.sandbox_docker_mem_limit,
        docker_nano_cpus=config.sandbox_docker_nano_cpus,
    )
    manager = ToolManager(sandbox=sandbox, config=config,
                          audit_path=Path(workspace_dir) / config.audit_log)
    manager.register(ListFilesTool())
    manager.register(ReadFileTool())
    manager.register(WriteFileTool())
    manager.register(RunCodeTool())

    if config.hitl_enabled:
        manager.hitl_gate = HITLSafetyGate(
            mode=config.approval_mode,
            approval_threshold=config.approval_threshold,
            approval_timeout=config.approval_timeout,
            auto_approve=set(config.auto_approve_tools),
            audit_path=Path(workspace_dir) / config.hitl_log,
        )
    return manager
