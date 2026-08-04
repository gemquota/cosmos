"""L1 — Per-Task Action Loop.

The innermost loop: plan → execute tool calls → observe → retry/adapt.
Collects workspace telemetry and creates checkpoints before destructive ops.
"""

import logging
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional

from rsis.checkpoint import CheckpointManager
from rsis.config import CONFIG
from rsis.error_classifier import is_retryable
from rsis.telemetry import TelemetryCollector, TelemetryEvent
from rsis.tools import ToolManager, default_tool_manager

logger = logging.getLogger(__name__)


@dataclass
class ToolCall:
    """A single tool invocation within an L1 step."""
    name: str
    arguments: dict
    result: Any = None
    error: Optional[str] = None
    duration_ms: int = 0


@dataclass
class L1Result:
    """Outcome of an L1 loop execution."""
    success: bool
    steps_taken: int = 0
    tool_calls: list[ToolCall] = field(default_factory=list)
    error: Optional[str] = None
    final_output: Any = None


class L1ActionLoop:
    """Per-task action loop with checkpointing and telemetry."""

    def __init__(
        self,
        telemetry: TelemetryCollector,
        checkpoint_mgr: Optional[CheckpointManager] = None,
        tools: Optional[dict[str, Callable]] = None,
        tool_manager: Optional[ToolManager] = None,
        agent_name: str = "l1",
    ):
        self.config = CONFIG.l1
        self.telemetry = telemetry
        self.checkpoint = checkpoint_mgr or CheckpointManager(CONFIG.workspace_dir)
        self.tools = tools or {}
        self.agent_name = agent_name
        # Sandboxed tool layer (allowlists + HITL). Falls back to the plain
        # callable dict when disabled or when an explicit manager is given.
        if tool_manager is not None:
            self.tool_manager = tool_manager
        elif CONFIG.tools.enabled:
            self.tool_manager = default_tool_manager(Path(CONFIG.workspace_dir))
        else:
            self.tool_manager = None
        self._task_description: str = ""

    def execute(self, task: str, context: Optional[dict] = None) -> L1Result:
        """Execute a task through the L1 loop.

        Steps:
        1. Record task start in telemetry
        2. Plan → tool call loop with retry
        3. Checkpoint before destructive operations
        4. Return result
        """
        self._task_description = task
        context = context or {}
        tool_calls: list[ToolCall] = []
        steps = 0

        logger.info("L1 executing task: %s", task[:80])

        self.telemetry.record(TelemetryEvent(
            event_type="l1_start",
            metadata={"task": task},
        ))

        for step_idx in range(self.config.max_tool_calls_per_step):
            steps = step_idx + 1
            logger.debug("L1 step %d/%d", step_idx + 1, self.config.max_tool_calls_per_step)

            # Determine which tool to call based on task
            tool_name, tool_args = self._plan_next_action(task, context, tool_calls)

            if tool_name is None:
                # Task is complete
                logger.info("L1 task complete after %d steps", steps)
                break

            # Execute tool call
            start = time.monotonic()
            call = self._execute_tool(tool_name, tool_args)
            call.duration_ms = int((time.monotonic() - start) * 1000)
            tool_calls.append(call)

            # Telemetry
            self.telemetry.record(TelemetryEvent(
                event_type="tool_call",
                path=tool_name,
                duration_ms=call.duration_ms,
                metadata={"error": call.error} if call.error else None,
            ))

            if call.error:
                logger.warning("Tool call failed: %s — %s", tool_name, call.error)
                # Checkpoint on failure so we can rollback
                if CONFIG.checkpoint_before_mutation:
                    self.checkpoint.checkpoint(f"after-tool-failure-{tool_name}")

            # Update context with result
            context["last_result"] = call.result
            context["last_error"] = call.error

        # A recovered retry is a success: the terminal attempt decides.
        # Tasks with no tool calls (nothing matched) count as complete.
        real_calls = [c for c in tool_calls if c.name not in ("retry", "noop")]
        if real_calls:
            success = not real_calls[-1].error
        else:
            success = True

        self.telemetry.record(TelemetryEvent(
            event_type="l1_complete",
            duration_ms=sum(c.duration_ms for c in tool_calls),
            metadata={"success": success, "steps": steps},
        ))

        return L1Result(
            success=success,
            steps_taken=steps,
            tool_calls=tool_calls,
            final_output=context.get("last_result"),
        )

    def _plan_next_action(
        self, task: str, context: dict, previous_calls: list[ToolCall]
    ) -> tuple[Optional[str], dict]:
        """Decide the next tool to call based on task and prior results.

        In production this would use an LLM to plan. This stub uses a simple
        keyword router for demonstration. With the sandboxed tool layer the
        task must name a tool; unmatched tasks complete instead of spinning
        on an arbitrary default.
        """
        # If the last call failed, retry only transient/rate-limit errors,
        # bounded by l1.max_retries (L4-tunable). Fatal errors fail fast.
        if previous_calls and previous_calls[-1].error:
            last = previous_calls[-1]
            retries = sum(1 for c in previous_calls if c.name == "retry")
            if retries >= self.config.max_retries:
                logger.info("L1 retry budget exhausted (%d)", retries)
                return None, {}
            if not is_retryable(last.error):
                logger.info("L1 non-retryable failure: %s", last.error[:80])
                return None, {}
            logger.info("Retrying after failure...")
            return "retry", {"previous_error": last.error}

        if self.tool_manager is not None:
            candidates = self.tool_manager.list_tools(self.agent_name)
            if not candidates:
                return None, {}
            task_lower = task.lower()
            for tool_name in candidates:
                if tool_name in task_lower:
                    # Stub planner: each tool runs at most once per task.
                    # Failed calls still retry (previous error -> retry beat).
                    if any(c.name == tool_name and not c.error
                           for c in previous_calls):
                        continue
                    return tool_name, self._arguments_for(
                        tool_name, task, context)
            logger.info("L1 task matched no tool; marking complete")
            return None, {}

        if not self.tools:
            return None, {}

        # Simple keyword routing for demo purposes: prefer keyword matches,
        # fall back to any tool, and run each tool at most once per task
        # (mirrors the sandboxed path, so a recovered retry stops cleanly
        # instead of re-running the tool until the step budget).
        task_lower = task.lower()
        matched = [name for name in self.tools if name in task_lower]
        if not matched:
            matched = list(self.tools)
        for tool_name in matched:
            if not any(c.name == tool_name and not c.error
                       for c in previous_calls):
                return tool_name, {"task": task, **context}
        return None, {}

    def _arguments_for(self, tool_name: str, task: str,
                       context: dict) -> dict:
        """Stub planner args for a sandboxed tool.

        Tools declare strict schemas (required params with types).  When a
        tool takes exactly one required string parameter, the stub planner
        hands it the task text; anything more complex falls back to the
        legacy `{"task": ...}` envelope and fails validation visibly.
        """
        tool = self.tool_manager.tools.get(tool_name)
        if tool is not None:
            # The matched keyword is consumed; the rest is the payload.
            payload = task.replace(tool_name, "").strip()
            # Free-text tools receive the task text as their payload.
            if tool_name == "run_code":
                return {"code": payload, **context}
            required_strings = [
                name for name, spec in tool.parameters.items()
                if spec.get("required") and spec.get("type") == "string"
            ]
            if len(required_strings) == 1:
                return {required_strings[0]: payload, **context}
        return {"task": task, **context}

    def _execute_tool(self, name: str, args: dict) -> ToolCall:
        """Execute a single tool call."""
        if name == "retry":
            return ToolCall(name="retry", arguments=args, result=None)
        if name == "noop":
            return ToolCall(name="noop", arguments=args, result=None)

        # Sandboxed tool layer: allowlists, validation, HITL, audit.
        if self.tool_manager is not None and name in self.tool_manager.tools:
            result = self.tool_manager.execute(self.agent_name, name, args)
            error = None if result.ok else f"{result.status.value}: {result.output}"
            return ToolCall(
                name=name, arguments=args,
                result=result.output if result.ok else None,
                error=error,
            )

        handler = self.tools.get(name)
        if not handler:
            return ToolCall(name=name, arguments=args, error=f"Unknown tool: {name}")

        try:
            result = handler(**args)
            return ToolCall(name=name, arguments=args, result=result)
        except Exception as e:
            return ToolCall(name=name, arguments=args, error=str(e))
