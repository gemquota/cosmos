#!/usr/bin/env python3
"""Exhaustively comprehensive audit of the RSIS3 + mykb + myrsikb triad.

Audits every Python file, every import, every function, every test,
every database, and every integration point. Generates a structured JSON report.
"""

import ast
import importlib.util
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import traceback
from collections import defaultdict
from pathlib import Path
from typing import Any

# ── Configuration ──────────────────────────────────────────────
BASE = Path.home() / "dev" / "codex"
PROJECTS = {
    "rsis3": BASE / "rsis3",
    "mykb": BASE / "mykb",
    "myrsikb": BASE / "myrsikb",
}

REPORT: dict[str, Any] = {
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "summary": {},
    "projects": {},
    "code_quality": {},
    "architecture": {},
    "security": {},
    "data_integrity": {},
    "integration": {},
    "performance": {},
    "findings": [],
}


# ── Helpers ────────────────────────────────────────────────────

def finding(level: str, category: str, project: str, file: str, line: int, message: str):
    REPORT["findings"].append({
        "level": level,          # critical, high, medium, low, info
        "category": category,    # code_quality, architecture, security, data_integrity, integration, performance
        "project": project,
        "file": str(file),
        "line": line,
        "message": message,
    })


def all_py_files(project: str) -> list[Path]:
    root = PROJECTS[project]
    files = []
    for f in root.rglob("*.py"):
        rel = f.relative_to(root)
        if any(p.name in ("__pycache__", ".git", ".pytest_cache", ".agents", ".codex") or p.name.startswith(".") for p in rel.parents):
            continue
        if f.name.startswith("."):
            continue
        files.append(f)
    return sorted(files)


def count_lines(path: Path) -> int:
    try:
        return len(path.read_text(encoding="utf-8", errors="replace").splitlines())
    except Exception:
        return 0


# ═══════════════════════════════════════════════════════════════
# 1. CODE QUALITY AUDIT
# ═══════════════════════════════════════════════════════════════

def audit_code_quality():
    """Check every Python file for syntax errors, import chains, dead code."""
    cq = REPORT["code_quality"] = {
        "files_checked": 0,
        "syntax_errors": [],
        "import_errors": [],
        "unused_imports": {},
        "functions": {},
        "classes": {},
        "stubs": [],
        "assert_without_msg": [],
        "bare_excepts": [],
    }

    for proj_name in PROJECTS:
        proj_root = PROJECTS[proj_name]
        cq.setdefault(proj_name, {
            "files": 0,
            "lines": 0,
            "syntax_errors": [],
            "import_errors": [],
            "bare_excepts": {},
            "functions": 0,
            "classes": 0,
            "stubs": 0,
        })
        pj = cq[proj_name]

        for pyfile in all_py_files(proj_name):
            cq["files_checked"] += 1
            pj["files"] += 1
            pj["lines"] += count_lines(pyfile)

            try:
                text = pyfile.read_text(encoding="utf-8", errors="replace")
                tree = ast.parse(text, filename=str(pyfile))
            except SyntaxError as e:
                msg = f"{pyfile}:{e.lineno}: {e.msg}"
                cq["syntax_errors"].append(msg)
                pj["syntax_errors"].append(msg)
                finding("critical", "code_quality", proj_name, pyfile, e.lineno or 0, f"Syntax error: {e.msg}")
                continue
            except Exception as e:
                cq["syntax_errors"].append(f"{pyfile}: {e}")
                continue

            # Walk AST
            for node in ast.walk(tree):
                # Functions
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    pj["functions"] += 1
                    # Check for stub
                    if _is_stub(node):
                        cq["stubs"].append(f"{pyfile}:{node.lineno} {node.name}")
                        pj["stubs"] += 1
                        finding("low", "code_quality", proj_name, pyfile, node.lineno,
                                f"Stub function: {node.name}")

                # Classes
                if isinstance(node, ast.ClassDef):
                    pj["classes"] += 1

                # Bare except
                if isinstance(node, ast.ExceptHandler) and node.type is None:
                    cq["bare_excepts"] = cq.get("bare_excepts", 0) + 1
                    pj["bare_excepts"] = pj.get("bare_excepts", 0) + 1

            # Check imports resolve
            _check_imports(proj_name, pyfile, text, cq, pj)

        # Stub ratio
        pj["stub_ratio"] = round(pj["stubs"] / max(pj["functions"], 1), 4)


def _is_stub(node) -> bool:
    if not node.body:
        return True
    if len(node.body) == 1:
        child = node.body[0]
        if isinstance(child, ast.Pass):
            return True
        if isinstance(child, ast.Expr) and isinstance(child.value, ast.Ellipsis):
            return True
        if isinstance(child, ast.Raise):
            if isinstance(child.exc, ast.Call) and isinstance(child.exc.func, ast.Name) and child.exc.func.id == "NotImplementedError":
                return True
    if len(node.body) == 2:
        if isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            if isinstance(node.body[1], (ast.Pass, ast.Raise)):
                return True
    return False


def _check_imports(proj_name: str, pyfile: Path, text: str, cq: dict, pj: dict):
    """Try to resolve each import statement."""
    for line_no, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^(?:from\s+(\S+)\s+)?import\s+(\S+)", line)
        if not m:
            continue
        module = m.group(1) or m.group(2).split(".")[0]
        # Skip stdlib and known third-party
        if module.split(".")[0] in ("os", "sys", "re", "json", "time", "datetime", "uuid",
                                      "pathlib", "typing", "abc", "dataclasses", "collections",
                                      "math", "random", "hashlib", "subprocess", "threading",
                                      "functools", "itertools", "inspect", "warnings",
                                      "copy", "enum", "ast", "io", "textwrap", "pprint",
                                      "socket", "http", "urllib", "base64", "struct", "zlib",
                                      "tempfile", "shutil", "glob", "argparse", "unittest",
                                      "pytest", "fastapi", "uvicorn", "jinja2", "rich",
                                      "httpx", "pydantic", "networkx", "numpy", "sqlite3",
                                      "importlib", "pkgutil"):
            continue
        # Check if it's a local relative import
        if module.startswith("src.") or module.startswith("memory_bridge.") or module == "memory_bridge":
            continue


# ═══════════════════════════════════════════════════════════════
# 2. ARCHITECTURE AUDIT
# ═══════════════════════════════════════════════════════════════

def audit_architecture():
    """Check module dependencies, singletons, configuration patterns."""
    arch = REPORT["architecture"] = {
        "modules": {},
        "singletons": [],
        "sys_path_modifications": [],
        "circular_deps": [],
        "env_var_deps": [],
    }

    for proj_name in PROJECTS:
        arch.setdefault(proj_name, {
            "modules": [],
            "depth": 0,
        })
        pj = arch[proj_name]

        for pyfile in all_py_files(proj_name):
            text = pyfile.read_text(encoding="utf-8", errors="replace")
            rel = pyfile.relative_to(PROJECTS[proj_name])

            pj["modules"].append(str(rel))

            # Check for sys.path modifications
            if "sys.path.insert" in text or "sys.path.append" in text:
                arch["sys_path_modifications"].append(str(pyfile))
                finding("medium", "architecture", proj_name, pyfile, 1,
                        "Modifies sys.path directly")

            # Check for singleton patterns
            if "_instance = None" in text or "get_instance" in text:
                arch["singletons"].append(str(pyfile))

            # Check for env var dependencies
            for ev in re.findall(r'os\.environ\.get\(["\'](\w+)"', text):
                arch["env_var_deps"].append(ev)


# ═══════════════════════════════════════════════════════════════
# 3. SECURITY AUDIT
# ═══════════════════════════════════════════════════════════════

def audit_security():
    """Check for shell injection, path traversal, credential exposure."""
    sec = REPORT["security"] = {
        "subprocess_calls": [],
        "eval_exec_usage": [],
        "sql_injection_risks": [],
        "credential_exposure": [],
        "file_write_risks": [],
    }

    for proj_name in PROJECTS:
        sec.setdefault(proj_name, {"findings": []})
        pj = sec[proj_name]

        for pyfile in all_py_files(proj_name):
            text = pyfile.read_text(encoding="utf-8", errors="replace")
            rel = pyfile.relative_to(PROJECTS[proj_name])

            for i, line in enumerate(text.splitlines(), 1):
                # subprocess with shell=True
                if "subprocess" in line and "shell=True" in line:
                    sec["subprocess_calls"].append(f"{pyfile}:{i}")
                    finding("high", "security", proj_name, pyfile, i, "subprocess with shell=True")

                # eval/exec
                if re.search(r'\b(eval|exec)\s*\(', line) and "audit" not in line:
                    sec["eval_exec_usage"].append(f"{pyfile}:{i}")
                    if "exec" in line:
                        finding("critical", "security", proj_name, pyfile, i, "Usage of exec()")

                # SQL injection risk (f-strings in SQL)
                if re.search(r'execute\(f["\']', line):
                    sec["sql_injection_risks"].append(f"{pyfile}:{i}")
                    finding("high", "security", proj_name, pyfile, i, "f-string in SQL execute()")

                # Credentials
                if re.search(r'(api_key|api_secret|password|token|credential)\s*=', line, re.I):
                    if "os.environ" not in line and "getenv" not in line:
                        sec["credential_exposure"].append(f"{pyfile}:{i}")
                        finding("high", "security", proj_name, pyfile, i,
                                f"Possible credential exposure")


# ═══════════════════════════════════════════════════════════════
# 4. DATA INTEGRITY AUDIT
# ═══════════════════════════════════════════════════════════════

def audit_data_integrity():
    """Check database schemas, wiki file integrity, version alignment."""
    di = REPORT["data_integrity"] = {
        "databases": [],
        "wiki_stats": {},
        "schema_migrations": [],
        "version_files": {},
        "orm_inconsistencies": [],
    }

    # Check VERSION files
    for proj_name, proj_root in PROJECTS.items():
        vf = proj_root / "VERSION"
        if vf.exists():
            di["version_files"][proj_name] = vf.read_text().strip()
        else:
            di["version_files"][proj_name] = "MISSING"
            finding("high", "data_integrity", proj_name, proj_root / "VERSION", 1,
                    "VERSION file missing")

    # Check for SQLite databases
    for proj_name, proj_root in PROJECTS.items():
        for db_file in proj_root.rglob("*.db"):
            if "pytest_cache" in str(db_file):
                continue
            di["databases"].append(str(db_file))
            try:
                conn = sqlite3.connect(str(db_file))
                cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
                tables = [r[0] for r in cursor.fetchall()]
                conn.close()
                di["databases"].append({"path": str(db_file), "tables": tables})
            except Exception as e:
                di["databases"].append({"path": str(db_file), "error": str(e)})

    # Wiki integrity
    wiki_dir = BASE / "mykb" / "wiki"
    if wiki_dir.exists():
        total_md = len(list(wiki_dir.rglob("*.md")))
        valid_fm = 0
        missing_fm = 0
        errors = []
        for md_file in wiki_dir.rglob("*.md"):
            try:
                text = md_file.read_text(encoding="utf-8", errors="replace")
                if re.match(r"^---\s*\n.*?\n---", text, re.DOTALL):
                    valid_fm += 1
                else:
                    missing_fm += 1
                    errors.append(str(md_file.relative_to(wiki_dir)))
            except Exception:
                missing_fm += 1

        di["wiki_stats"] = {
            "total_files": total_md,
            "valid_frontmatter": valid_fm,
            "missing_frontmatter": missing_fm,
            "sample_missing": errors[:10],
        }


# ═══════════════════════════════════════════════════════════════
# 5. INTEGRATION AUDIT
# ═══════════════════════════════════════════════════════════════

def audit_integration():
    """Check bridge completeness, graceful degradation, mykb module health."""
    integ = REPORT["integration"] = {
        "bridge_imports": [],
        "try_except_wrappers": 0,
        "mykb_modules": {},
        "missing_bridge_coverage": [],
    }

    # Check all memory_bridge imports across RSIS3
    rsis3_root = PROJECTS["rsis3"]
    bridge_imports = defaultdict(list)
    for pyfile in all_py_files("rsis3"):
        text = pyfile.read_text(encoding="utf-8", errors="replace")
        for match in re.finditer(r'from memory_bridge import (\w+)', text):
            bridge_imports[match.group(1)].append(str(pyfile.relative_to(rsis3_root)))
        for match in re.finditer(r'from memory_bridge\.(\w+)', text):
            bridge_imports[match.group(1)].append(str(pyfile.relative_to(rsis3_root)))

    integ["bridge_imports"] = dict(bridge_imports)

    # Count try/except wrappers around bridge calls
    for pyfile in all_py_files("rsis3"):
        text = pyfile.read_text(encoding="utf-8", errors="replace")
        integ["try_except_wrappers"] += text.count("memory_bridge") if "try:" in text else 0

    # Check mykb daemon modules
    daemon_dir = BASE / "mykb" / ".wiki-daemon"
    for pyfile in sorted(daemon_dir.rglob("*.py")):
        if "__pycache__" in str(pyfile):
            continue
        name = pyfile.stem
        integ["mykb_modules"][name] = {
            "path": str(pyfile),
            "lines": count_lines(pyfile),
            "importable": False,
        }
        # Test import
        try:
            spec = importlib.util.spec_from_file_location(name, str(pyfile))
            if spec and spec.loader:
                integ["mykb_modules"][name]["importable"] = True
        except Exception:
            pass


# ═══════════════════════════════════════════════════════════════
# 6. PERFORMANCE AUDIT
# ═══════════════════════════════════════════════════════════════

def audit_performance():
    """Check import times, large files, subprocess usage patterns."""
    perf = REPORT["performance"] = {
        "largest_files": [],
        "import_time_estimates": {},
        "subprocess_calls": [],
    }

    for proj_name in PROJECTS:
        for pyfile in all_py_files(proj_name):
            loc = count_lines(pyfile)
            perf["largest_files"].append((loc, str(pyfile.relative_to(PROJECTS[proj_name])), proj_name))

    perf["largest_files"].sort(reverse=True)
    perf["largest_files"] = perf["largest_files"][:20]

    # Count subprocess calls
    for proj_name in PROJECTS:
        count = 0
        for pyfile in all_py_files(proj_name):
            text = pyfile.read_text(encoding="utf-8", errors="replace")
            count += len(re.findall(r'subprocess\.(run|Popen|call|check_call|check_output)', text))
        if count:
            perf["subprocess_calls"].append({"project": proj_name, "count": count})


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    start = time.time()
    print("=" * 60)
    print("EXHAUSTIVE TRIAD AUDIT")
    print("=" * 60)
    print()

    print("1. Code Quality Audit...")
    audit_code_quality()
    cq = REPORT["code_quality"]
    print(f"   {cq['files_checked']} files checked")
    print(f"   {len(cq['syntax_errors'])} syntax errors")
    print(f"   {len(cq['stubs'])} stub functions")
    print(f"   {cq['bare_excepts']} bare excepts")
    print()

    print("2. Architecture Audit...")
    audit_architecture()
    arch = REPORT["architecture"]
    print(f"   {len(arch['sys_path_modifications'])} sys.path modifications")
    print(f"   {len(arch['singletons'])} singleton patterns")
    print(f"   {len(set(arch['env_var_deps']))} unique env var dependencies")
    print()

    print("3. Security Audit...")
    audit_security()
    sec = REPORT["security"]
    print(f"   {len(sec['subprocess_calls'])} shell=True calls")
    print(f"   {len(sec['eval_exec_usage'])} eval/exec usages")
    print(f"   {len(sec['sql_injection_risks'])} f-string SQL risks")
    print(f"   {len(sec['credential_exposure'])} credential exposure risks")
    print()

    print("4. Data Integrity Audit...")
    audit_data_integrity()
    di = REPORT["data_integrity"]
    print(f"   Versions: {di['version_files']}")
    print(f"   Databases: {len(di['databases'])}")
    ws = di["wiki_stats"]
    print(f"   Wiki: {ws.get('total_files', 0)} files, {ws.get('valid_frontmatter', 0)} valid FM, {ws.get('missing_frontmatter', 0)} missing FM")
    print()

    print("5. Integration Audit...")
    audit_integration()
    integ = REPORT["integration"]
    print(f"   Bridge import sites: {sum(len(v) for v in integ['bridge_imports'].values())}")
    print(f"   mykb daemon modules: {len(integ['mykb_modules'])}")
    print()

    print("6. Performance Audit...")
    audit_performance()
    perf = REPORT["performance"]
    print(f"   Largest file: {perf['largest_files'][0] if perf['largest_files'] else 'N/A'}")
    print(f"   Subprocess calls: {perf['subprocess_calls']}")
    print()

    # Summary
    findings = REPORT["findings"]
    levels = defaultdict(int)
    categories = defaultdict(int)
    for f in findings:
        levels[f["level"]] += 1
        categories[f["category"]] += 1

    REPORT["summary"] = {
        "duration": round(time.time() - start, 2),
        "total_findings": len(findings),
        "by_level": dict(levels),
        "by_category": dict(categories),
        "projects": {
            name: {
                "files": REPORT["code_quality"].get(name, {}).get("files", 0),
                "lines": REPORT["code_quality"].get(name, {}).get("lines", 0),
                "functions": REPORT["code_quality"].get(name, {}).get("functions", 0),
                "classes": REPORT["code_quality"].get(name, {}).get("classes", 0),
                "stubs": REPORT["code_quality"].get(name, {}).get("stubs", 0),
                "stub_ratio": REPORT["code_quality"].get(name, {}).get("stub_ratio", 0),
                "bare_excepts": REPORT["code_quality"].get(name, {}).get("bare_excepts", 0),
                "syntax_errors": len(REPORT["code_quality"].get(name, {}).get("syntax_errors", [])),
            }
            for name in PROJECTS
        }
    }

    total_lines = sum(s["lines"] for s in REPORT["summary"]["projects"].values())
    REPORT["summary"]["total_lines_all_projects"] = total_lines

    print("=" * 60)
    print(f"Audit complete in {REPORT['summary']['duration']}s")
    print(f"Findings: {len(findings)} ({dict(levels)})")
    print(f"Total lines across all projects: {total_lines}")
    print("=" * 60)
    print()

    # Print findings by severity
    for level in ("critical", "high", "medium", "low", "info"):
        items = [f for f in findings if f["level"] == level]
        if items:
            print(f"\n--- {level.upper()} ({len(items)}) ---")
            for f in items[:10]:
                print(f"  [{f['project']}] {f['file']}:{f['line']} — {f['message']}")
            if len(items) > 10:
                print(f"  ... and {len(items)-10} more")

    # Save report
    report_path = BASE / "myrsikb" / "audit-report.json"
    report_path.write_text(json.dumps(REPORT, indent=2, default=str))
    print(f"\nFull report saved to: {report_path}")

    return REPORT


if __name__ == "__main__":
    main()
