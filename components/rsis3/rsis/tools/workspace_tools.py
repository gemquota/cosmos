"""Workspace tools: safe file I/O and sandboxed code execution.

Path traversal is blocked: tools can only touch files under the
sandbox workdir.
"""

from __future__ import annotations

from pathlib import Path

from rsis.tools.base import Tool, ToolResult, ToolStatus

_READ_AGENTS = ["l1", "coder", "reviewer"]     # may inspect + run tests
_WRITE_AGENTS = ["l1", "coder"]                # only implementers mutate files

_READ_LIMIT_CHARS = 20_000                     # keep context bounded


def _resolve_inside(root: Path, rel_path: str) -> Path | None:
    """Return an absolute path inside root, or None if it escapes."""
    root_resolved = root.resolve()
    candidate = (root_resolved / rel_path).resolve()
    if candidate != root_resolved and root_resolved not in candidate.parents:
        return None
    return candidate


class ListFilesTool(Tool):
    name = "list_files"
    description = "List files inside the sandbox workspace."
    agent_allowlist = _READ_AGENTS
    risk = "read"
    parameters = {
        "path": {"type": "string", "required": False},
    }

    def run(self, tm, args: dict) -> ToolResult:
        rel = args.get("path", ".")
        target = _resolve_inside(tm.sandbox.workdir, rel)
        if target is None:
            return ToolResult(ToolStatus.DENIED,
                              f"path escapes workspace: {rel}")
        files = [str(p.relative_to(tm.sandbox.workdir))
                 for p in target.rglob("*") if p.is_file()]
        return ToolResult(ToolStatus.OK, "\n".join(files[:200]),
                          {"file_count": len(files)})


class ReadFileTool(Tool):
    name = "read_file"
    description = "Read text content of a file inside the sandbox workspace."
    agent_allowlist = _READ_AGENTS
    risk = "read"
    parameters = {
        "path": {"type": "string", "required": True},
    }

    def run(self, tm, args: dict) -> ToolResult:
        target = _resolve_inside(tm.sandbox.workdir, args["path"])
        if target is None:
            return ToolResult(ToolStatus.DENIED,
                              f"path escapes workspace: {args['path']}")
        if not target.is_file():
            return ToolResult(ToolStatus.ERROR, f"not a file: {args['path']}")
        text = target.read_text(encoding="utf-8", errors="replace")
        truncated = len(text) > _READ_LIMIT_CHARS
        if truncated:
            text = text[:_READ_LIMIT_CHARS] + "\n...[truncated]"
        return ToolResult(ToolStatus.OK, text, {"truncated": truncated})


class WriteFileTool(Tool):
    name = "write_file"
    description = "Write text content to a file inside the sandbox workspace."
    agent_allowlist = _WRITE_AGENTS        # reviewer is blocked: read-only
    risk = "write"
    parameters = {
        "path": {"type": "string", "required": True},
        "content": {"type": "string", "required": True},
    }

    def run(self, tm, args: dict) -> ToolResult:
        target = _resolve_inside(tm.sandbox.workdir, args["path"])
        if target is None:
            return ToolResult(ToolStatus.DENIED,
                              f"path escapes workspace: {args['path']}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(args["content"], encoding="utf-8")
        return ToolResult(
            ToolStatus.OK,
            f"wrote {target.relative_to(tm.sandbox.workdir)}")


class RunCodeTool(Tool):
    name = "run_code"
    description = "Run untrusted pure-Python code inside the restricted sandbox."
    agent_allowlist = _READ_AGENTS
    risk = "write"          # execution can have side effects -> audited as write
    parameters = {
        "code": {"type": "string", "required": False},
        "file": {"type": "string", "required": False},
    }

    def run(self, tm, args: dict) -> ToolResult:
        code = args.get("code")
        if not code:
            path = args.get("file")
            if not path:
                return ToolResult(ToolStatus.ERROR, "provide 'code' or 'file'")
            target = _resolve_inside(tm.sandbox.workdir, path)
            if target is None:
                return ToolResult(ToolStatus.DENIED,
                                  f"path escapes workspace: {path}")
            code = target.read_text(encoding="utf-8")
        return tm.sandbox.run_python(code).as_tool_result()
