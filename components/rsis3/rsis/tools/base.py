"""Tool protocol — the actuator interface (ported from Agent OS).

A Tool is a named, schema-declared capability that runs *outside* the
model's context.  Tools never see raw secret material themselves: they
request scoped secrets from the ToolManager at call time.
"""

from __future__ import annotations

import abc
from dataclasses import dataclass, field
from enum import Enum


class ToolStatus(str, Enum):
    OK = "ok"
    ERROR = "error"
    DENIED = "denied"
    TIMEOUT = "timeout"


@dataclass
class ToolResult:
    status: ToolStatus
    output: str
    metadata: dict = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return self.status == ToolStatus.OK


class Tool(abc.ABC):
    """Base class for all tools."""

    name: str = "unnamed"
    description: str = ""
    parameters: dict = {}              # {name: {"type": ..., "required": bool, "desc": ...}}
    requires_secrets: list[str] = []   # env var names requested from the vault
    agent_allowlist: list[str] = []    # agents allowed to call; [] = everyone
    risk: str = "write"                # "read" | "write" | "destructive" (audited)

    @abc.abstractmethod
    def run(self, tm, args: dict) -> ToolResult:
        """Execute with scoped access. `tm` is the ToolManager."""
        raise NotImplementedError
