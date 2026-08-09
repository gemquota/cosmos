"""Continual verification & invariant attestation (Phase 14).

Behavior is pinned by checks that run every cycle, not just at release:

- ``rack/invariants.json`` declares the invariant set as executable checks
  (state-file disjointness, telemetry coverage, KG idempotency, state
  schemas, envelope conformance, AST invariants, stale locks).
- ``run_invariants`` executes them; ``check-practices`` runs them every
  cycle.
- ``attest`` signs (sha256) every applied candidate and every nightly
  summary with the invariant set it passed — extending the Phase 7
  verification ledger into a per-cycle attestation layer.
- ``repair`` fixes self-repairable invariants (KG dedupe, stale lock
  removal) and re-attests; failed invariants file a MyKB backlog note.
"""

from __future__ import annotations

import ast
import hashlib
import json
import logging
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_INVARIANTS = [
    {"id": "state_files_disjoint", "description": "tuner state files disjoint",
     "repairable": False},
    {"id": "telemetry_coverage", "description": "every loop start has a complete",
     "repairable": False},
    {"id": "kg_idempotency", "description": "KG nodes/edges have unique ids",
     "repairable": True},
    {"id": "state_schemas", "description": "state files parse and hold required fields",
     "repairable": False},
    {"id": "envelope_conformance", "description": "repo contract suite passes",
     "repairable": False},
    {"id": "ast_invariants", "description": "package python files compile",
     "repairable": False},
    {"id": "stale_locks", "description": "no stale lock files",
     "repairable": True},
]


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def invariants_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "invariants.json"


def load_invariants(workspace: Path) -> list[dict]:
    path = invariants_path(workspace)
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, list) and data:
                return data
        except (OSError, json.JSONDecodeError) as e:
            logger.warning("invariants.json unreadable (%s); using defaults", e)
    return [dict(i) for i in DEFAULT_INVARIANTS]


def ensure_invariants(workspace: Path) -> list[dict]:
    path = invariants_path(workspace)
    if not path.is_file():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(DEFAULT_INVARIANTS, indent=2) + "\n",
                        encoding="utf-8")
    return load_invariants(workspace)


def _repo_root(package_root: Path) -> Path:
    p = Path(package_root).resolve()
    for cand in (p, *p.parents):
        if (cand / "contracts" / "validate.py").is_file():
            return cand
    return p.parent


def _check_state_files(workspace: Path) -> tuple[bool, str]:
    from rsis.practices import TUNERS
    from rsis.config import CONFIG
    seen: dict[str, str] = {}
    for loop_id, _name, _reg, _prefix in TUNERS:
        cfg = getattr(CONFIG, loop_id.lower())
        state_path = getattr(cfg, "state_path", "")
        if state_path in seen:
            return False, f"{state_path} shared by {seen[state_path]}/{loop_id}"
        seen[state_path] = loop_id
    return True, f"{len(seen)} disjoint state files"


def _check_telemetry(workspace: Path) -> tuple[bool, str]:
    from rsis.anomalies import read_events
    events = read_events(Path(workspace) / ".rsis" / "telemetry")
    starts: dict[str, int] = {}
    completes: dict[str, int] = {}
    for e in events:
        t = e.get("type") or ""
        for loop in ("l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9"):
            if t == f"{loop}_start":
                starts[loop] = starts.get(loop, 0) + 1
            elif t == f"{loop}_complete":
                completes[loop] = completes.get(loop, 0) + 1
    missing = [l for l in starts
               if starts[l] != completes.get(l, 0)]
    if missing:
        return False, "start/complete imbalance: " + ", ".join(missing)
    return True, f"{sum(completes.values())} loop completes"


def _check_kg_idempotency(workspace: Path) -> tuple[bool, str]:
    path = Path(workspace) / ".rsis" / "knowledge_graph.json"
    if not path.is_file():
        return True, "no KG yet"
    try:
        kg = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False, "KG unparseable"
    nodes = kg.get("nodes") or []
    edges = kg.get("edges") or []
    node_ids = [n.get("id") for n in nodes if isinstance(n, dict)]
    edge_ids = [e.get("id") for e in edges if isinstance(e, dict)]
    dup_nodes = len(node_ids) - len(set(node_ids))
    dup_edges = len(edge_ids) - len(set(edge_ids))
    if dup_nodes or dup_edges:
        return False, f"duplicate ids: {dup_nodes} nodes / {dup_edges} edges"
    return True, f"{len(nodes)} nodes / {len(edges)} edges"


def _repair_kg(workspace: Path) -> bool:
    path = Path(workspace) / ".rsis" / "knowledge_graph.json"
    try:
        kg = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    seen_nodes: dict[str, dict] = {}
    for n in kg.get("nodes") or []:
        if isinstance(n, dict) and n.get("id"):
            seen_nodes[str(n["id"])] = n
    seen_edges: dict[str, dict] = {}
    for e in kg.get("edges") or []:
        if isinstance(e, dict) and e.get("id"):
            seen_edges[str(e["id"])] = e
    kg["nodes"] = list(seen_nodes.values())
    kg["edges"] = list(seen_edges.values())
    path.write_text(json.dumps(kg, indent=2) + "\n", encoding="utf-8")
    return True


def _check_state_schemas(workspace: Path) -> tuple[bool, str]:
    issues = []
    strategies = Path(workspace) / ".rsis" / "strategies.json"
    if strategies.is_file():
        try:
            data = json.loads(strategies.read_text(encoding="utf-8"))
            if "generation" not in data:
                issues.append("strategies.json missing generation")
        except json.JSONDecodeError:
            issues.append("strategies.json unparseable")
    policy = Path(workspace) / "rack" / "policy.json"
    if policy.is_file():
        try:
            data = json.loads(policy.read_text(encoding="utf-8"))
            if "version" not in data:
                issues.append("policy.json missing version")
        except json.JSONDecodeError:
            issues.append("policy.json unparseable")
    return (not issues), "; ".join(issues) if issues else "schemas valid"


def _check_envelope(workspace: Path) -> tuple[bool, str]:
    repo = _repo_root(Path(workspace))
    script = repo / "contracts" / "validate.py"
    if not script.is_file():
        return True, "no contract suite"
    try:
        proc = subprocess.run([sys.executable, str(script)],
                              cwd=str(repo), capture_output=True, text=True,
                              timeout=120)
        fails = int(proc.returncode != 0)
        return fails == 0, "contracts OK" if fails == 0 else "contract FAIL"
    except (OSError, subprocess.TimeoutExpired) as e:
        return False, f"contract suite error: {e}"


def _check_ast(workspace: Path) -> tuple[bool, str]:
    pkg = Path(workspace) / "rsis"
    bad = []
    for f in sorted(pkg.glob("*.py")):
        try:
            ast.parse(f.read_text(encoding="utf-8"), filename=str(f))
        except (OSError, SyntaxError) as e:
            bad.append(f"{f.name}: {e}")
    return (not bad), "all package files compile" if not bad else "; ".join(bad)


def _check_stale_locks(workspace: Path) -> tuple[bool, str]:
    stale = []
    for lock in sorted(Path(workspace).glob("rack/*.lock")) + \
            sorted(Path(workspace).glob(".rsis/*.lock")):
        try:
            import fcntl
            with lock.open("a+") as fh:
                fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                # acquired => no live holder
                fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
                stale.append(lock.name)
        except (OSError, BlockingIOError):
            pass
    return (not stale), "no stale locks" if not stale else "stale: " + ", ".join(stale)


def _repair_stale_locks(workspace: Path) -> bool:
    ok = False
    for lock in list(Path(workspace).glob("rack/*.lock")) + \
            list(Path(workspace).glob(".rsis/*.lock")):
        try:
            import fcntl
            with lock.open("a+") as fh:
                fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
            lock.unlink(missing_ok=True)
            ok = True
        except (OSError, BlockingIOError):
            pass
    return ok


CHECKERS = {
    "state_files_disjoint": _check_state_files,
    "telemetry_coverage": _check_telemetry,
    "kg_idempotency": _check_kg_idempotency,
    "state_schemas": _check_state_schemas,
    "envelope_conformance": _check_envelope,
    "ast_invariants": _check_ast,
    "stale_locks": _check_stale_locks,
}
REPAIRERS = {
    "kg_idempotency": _repair_kg,
    "stale_locks": _repair_stale_locks,
}


def run_invariants(workspace: Path) -> list[dict]:
    """Execute the registered invariant set. Returns result rows."""
    registry = load_invariants(workspace)
    rows = []
    for inv in registry:
        checker = CHECKERS.get(inv["id"])
        if checker is None:
            continue
        try:
            ok, detail = checker(Path(workspace))
        except Exception as e:  # invariants must never crash the cycle
            ok, detail = False, f"checker error: {e}"
        rows.append({"id": inv["id"], "ok": ok, "detail": detail,
                     "repairable": bool(inv.get("repairable"))})
    return rows


def attest(workspace: Path, artifact: str, results: list[dict],
           actor: str = "system") -> dict:
    """Sign (sha256) an artifact against the invariant set it passed."""
    passed = [r["id"] for r in results if r["ok"]]
    digest = hashlib.sha256(
        (artifact + "|" + ",".join(sorted(passed)) + "|" + _now_ts())
        .encode("utf-8")).hexdigest()
    rec = {"ts": _now_ts(), "artifact": artifact, "actor": actor,
           "invariants_passed": passed, "invariant_count": len(results),
           "sha256": digest}
    d = Path(workspace) / "rack" / "attestations"
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.jsonl"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")
    return rec


def repair(workspace: Path, rows: list[dict],
           mykb: Optional[Path] = None) -> list[dict]:
    """Attempt self-repair of repairable failed invariants; re-attest."""
    repaired = []
    for row in rows:
        if row["ok"] or not row["repairable"]:
            continue
        fixer = REPAIRERS.get(row["id"])
        if fixer is None:
            continue
        try:
            if fixer(Path(workspace)):
                repaired.append(row["id"])
                row["ok"] = True
                row["detail"] += " (repaired)"
        except Exception as e:
            logger.warning("repair %s failed: %s", row["id"], e)
    if mykb is not None:
        for row in rows:
            if not row["ok"]:
                _file_backlog(mykb, row)
    return repaired


def _file_backlog(mykb: Path, row: dict) -> None:
    d = Path(mykb) / "wiki" / "backlog"
    d.mkdir(parents=True, exist_ok=True)
    name = f"invariant-{row['id']}-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}.md"
    (d / name).write_text(
        "---\ntype: \"backlog\"\ntitle: \"Invariant drift — "
        f"{row['id']}\"\ndescription: \"{row['detail']}\"\n"
        "tags: [\"rsis3\", \"invariants\", \"phase-14\"]\n"
        f"timestamp: \"{_now_ts()}\"\nstatus: \"open\"\n---\n\n"
        f"Invariant `{row['id']}` drifted: {row['detail']}\n",
        encoding="utf-8")


def main(workspace: Path, mykb: Optional[Path] = None,
         do_repair: bool = False, json_out: bool = False) -> int:
    ensure_invariants(workspace)
    rows = run_invariants(workspace)
    repaired = repair(workspace, rows, mykb=mykb) if do_repair else []
    failed = [r for r in rows if not r["ok"]]
    if json_out:
        print(json.dumps({"invariants": rows, "repaired": repaired,
                          "all_pass": not failed}))
        return 0 if not failed else 1
    for r in rows:
        print(f"  {'✓' if r['ok'] else '✗'} {r['id']}: {r['detail']}")
    if repaired:
        print(f"  🔧 repaired: {', '.join(repaired)}")
    print(f"  invariants: {len(rows) - len(failed)}/{len(rows)} pass")
    return 0 if not failed else 1


if __name__ == "__main__":
    import sys
    sys.exit(main(Path(".").resolve()))
