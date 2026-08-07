"""Stub detector — scan a workspace for real improvement targets.

Produces a priority-ranked list of ``StubFind`` findings so L2 and the
RRP pulse tool generate goals from actual code state instead of canned
placeholders. Finding kinds:

  * ``missing_module`` — ``rsis.*`` module imported somewhere but absent
    on disk (highest priority: the codebase references it, so it is a
    concrete gap).
  * ``not_implemented`` — function/class body that raises
    ``NotImplementedError``.
  * ``pass_body`` — function/class body that is only ``pass``.
  * ``todo`` — ``TODO``/``FIXME``/``XXX`` comment markers.
"""

from __future__ import annotations

import ast
import logging
import re
import tokenize
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Iterable, Optional

logger = logging.getLogger(__name__)

DEFAULT_SCOPES = ("rsis", "rack", "dashboard")
TODO_RE = re.compile(r"\b(TODO|FIXME|XXX)\b")
_STUB_KINDS = {
    "missing_module": 1.0,
    "not_implemented": 0.8,
    "pass_body": 0.6,
    "todo": 0.3,
}


@dataclass
class StubFind:
    """One concrete improvement target found by :class:`StubDetector`."""

    file: str
    name: str
    kind: str
    pattern: str
    line: int
    priority: float

    def to_dict(self) -> dict:
        return {
            "file": self.file,
            "name": self.name,
            "kind": self.kind,
            "pattern": self.pattern,
            "line": self.line,
            "priority": self.priority,
        }

    def __str__(self) -> str:  # pragma: no cover - debugging aid
        return (f"StubFind({self.kind}: {self.name} @ {self.file}:{self.line}"
                f" — {self.pattern})")


class StubDetector:
    """Scan a workspace for stubs and improvement gaps."""

    def __init__(self, workspace: str | Path = ".",
                 scopes: Iterable[str] = DEFAULT_SCOPES):
        self.root = Path(workspace)
        self.scopes = tuple(scopes)

    # ── public API ───────────────────────────────────────────────────── #

    def scan(self) -> list[StubFind]:
        """Return all findings, highest priority first."""
        findings: list[StubFind] = []
        for py in sorted(self.root.rglob("*.py")):
            rel = self._relative(py)
            if not rel or not self._in_scope(rel):
                continue
            try:
                findings.extend(self._scan_file(py, rel))
            except (SyntaxError, tokenize.TokenError, OSError) as e:
                logger.debug("skipping %s: %s", rel, e)
        findings.extend(self._scan_dangling_imports())
        findings.sort(key=lambda f: (f.priority, f.file, f.line), reverse=True)
        return findings

    def scan_by_priority(self, top_n: Optional[int] = None) -> list[StubFind]:
        """Return the top-N highest-priority findings (all if top_n is None)."""
        findings = self.scan()
        if top_n is not None:
            findings = findings[: max(0, int(top_n))]
        return findings

    # ── file scanning ────────────────────────────────────────────────── #

    def _scan_file(self, path: Path, rel: str) -> list[StubFind]:
        source = path.read_text(encoding="utf-8")
        findings = self._scan_ast(rel, source)
        findings.extend(self._scan_comments(rel, source))
        return findings

    def _scan_ast(self, rel: str, source: str) -> list[StubFind]:
        findings: list[StubFind] = []
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                                     ast.ClassDef)):
                continue
            if self._is_abstract(node):
                continue
            if isinstance(node, ast.ClassDef) and not node.body:
                continue
            body = [n for n in node.body
                    if not isinstance(n, ast.Expr) or not self._is_docstring(n)]
            if len(body) == 1 and isinstance(body[0], ast.Pass):
                if isinstance(node, ast.ClassDef) and self._is_exception(node):
                    continue
                findings.append(StubFind(
                    file=rel, name=node.name, kind="pass_body",
                    pattern="pass-only body", line=node.lineno,
                    priority=_STUB_KINDS["pass_body"]))
                continue
            if self._raises_not_implemented(node):
                findings.append(StubFind(
                    file=rel, name=node.name, kind="not_implemented",
                    pattern="raises NotImplementedError", line=node.lineno,
                    priority=_STUB_KINDS["not_implemented"]))
        return findings

    @staticmethod
    def _is_abstract(node) -> bool:
        """Skip abstract methods (raise NotImplementedError is idiomatic)."""
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for dec in node.decorator_list:
                if isinstance(dec, ast.Name) and dec.id == "abstractmethod":
                    return True
                if (isinstance(dec, ast.Attribute)
                        and dec.attr == "abstractmethod"):
                    return True
        return False

    @staticmethod
    def _is_docstring(node: ast.Expr) -> bool:
        return isinstance(node.value, ast.Constant) and isinstance(
            node.value.value, str)

    @staticmethod
    def _is_exception(node: ast.ClassDef) -> bool:
        if node.name.endswith(("Error", "Exception")):
            return True
        for base in node.bases:
            if isinstance(base, ast.Name) and base.id in (
                    "Exception", "BaseException", "ValueError", "RuntimeError"):
                return True
        return False

    @staticmethod
    def _raises_not_implemented(node) -> bool:
        for child in ast.walk(node):
            if not isinstance(child, ast.Raise):
                continue
            exc = child.exc
            if isinstance(exc, ast.Name):
                if exc.id == "NotImplementedError":
                    return True
            elif isinstance(exc, ast.Call) and isinstance(exc.func,
                                                          ast.Name):
                if exc.func.id == "NotImplementedError":
                    return True
        return False

    def _scan_comments(self, rel: str, source: str) -> list[StubFind]:
        findings: list[StubFind] = []
        try:
            tokens = tokenize.generate_tokens(StringIO(source).readline)
            for tok in tokens:
                if tok.type != tokenize.COMMENT:
                    continue
                m = TODO_RE.search(tok.string)
                if m:
                    findings.append(StubFind(
                        file=rel, name=m.group(1), kind="todo",
                        pattern=tok.string.strip("# ")[:80], line=tok.start[0],
                        priority=_STUB_KINDS["todo"]))
        except (tokenize.TokenError, IndentationError, OSError):
            pass
        return findings

    # ── dangling imports ─────────────────────────────────────────────── #

    def _scan_dangling_imports(self) -> list[StubFind]:
        imported: dict[str, set[str]] = {}
        for py in sorted(self.root.rglob("*.py")):
            rel = self._relative(py)
            if not rel or not self._in_scope(rel):
                continue
            try:
                tree = ast.parse(py.read_text(encoding="utf-8"))
            except (SyntaxError, OSError):
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imported.setdefault(alias.name, set()).add(rel)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imported.setdefault(node.module, set()).add(rel)

        findings: list[StubFind] = []
        for module, importers in sorted(imported.items()):
            if not module.startswith("rsis") or module == "rsis":
                continue
            if not self._module_exists(module):
                for importer in sorted(importers):
                    findings.append(StubFind(
                        file=importer, name=module, kind="missing_module",
                        pattern=f"imported but module missing: {module}",
                        line=0, priority=_STUB_KINDS["missing_module"]))
        return findings

    def _module_exists(self, dotted: str) -> bool:
        parts = dotted.split(".")
        cur = self.root / parts[0]
        if not cur.is_dir():
            return False
        for part in parts[1:-1]:
            cur = cur / part
            if not cur.is_dir():
                return False
        last = parts[-1]
        return (cur / f"{last}.py").is_file() or (cur / last).is_dir()

    # ── helpers ──────────────────────────────────────────────────────── #

    def _relative(self, path: Path) -> Optional[str]:
        try:
            return path.relative_to(self.root).as_posix()
        except ValueError:
            return None

    def _in_scope(self, rel: str) -> bool:
        if "__pycache__" in rel or "/tests/" in rel or rel.startswith("tests/"):
            return False
        return any(rel == s or rel.startswith(f"{s}/") for s in self.scopes)
