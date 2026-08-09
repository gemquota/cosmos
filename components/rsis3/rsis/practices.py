"""Usage-practice enforcement for RSIS3 workspaces.

Implements the checks described in `docs/usage-practices.md`:

1. Registry invariants — the +3 ownership diagonal is disjoint, each tuner
   writes only its target's keys, and the top three loops (L7-L9) are
   untuned fixed points.
2. State-file disjointness — no two loops share a write file.
3. Telemetry coverage — every loop with persisted state has emitted
   start + complete events, with no errors.
4. Checkpoint hygiene — a workspace with state has a git repo and at least
   one `rsis-checkpoint:` commit.

Run standalone with `python3 ops/check_practices.py` or through the CLI with
`python -m rsis check-practices`. Exits non-zero on any FAIL.
"""

import json
import logging
import re
import subprocess
from pathlib import Path
from typing import Optional

from rsis.config import (
    CONFIG,
    L1_TUNABLES,
    L2_TUNABLES,
    L3_TUNABLES,
    L4_TUNABLES,
    L5_TUNABLES,
    L6_TUNABLES,
)

logger = logging.getLogger(__name__)

# Tuner -> (loop id, name, its target's registry, target key prefix)
TUNERS = [
    ("L4", "Optimizer", L1_TUNABLES, "l1"),
    ("L5", "Evolution", L2_TUNABLES, "l2"),
    ("L6", "Identity", L3_TUNABLES, "l3"),
    ("L7", "Meta-Cog", L4_TUNABLES, "l4"),
    ("L8", "Meta-Meta", L5_TUNABLES, "l5"),
    ("L9", "MMM", L6_TUNABLES, "l6"),
]
LOOPS = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9"]


class CheckRow:
    """One practice check result."""

    def __init__(self, name: str, status: str, detail: str = ""):
        self.name = name
        self.status = status  # PASS | FAIL | WARN | INFO
        self.detail = detail

    def __str__(self) -> str:
        return f"{self.name:<34} {self.status:<5} {self.detail}"


def _git(repo_root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo_root), *args],
        capture_output=True, text=True, timeout=30,
    )


def check_registry() -> list[CheckRow]:
    """Registry invariants: ownership prefixes, disjoint keys, fixed points."""
    rows = []
    all_keys: dict[str, str] = {}
    for loop_id, _name, registry, prefix in TUNERS:
        wrong = [k for k in registry if not k.startswith(prefix + ".")]
        rows.append(CheckRow(
            f"{loop_id} owns {prefix}.*",
            "PASS" if not wrong else "FAIL",
            "" if not wrong else f"off-prefix keys: {wrong}",
        ))
        for key in registry:
            if key in all_keys:
                rows.append(CheckRow(
                    f"unique write key {key}",
                    "FAIL",
                    f"also owned by {all_keys[key]}",
                ))
            else:
                all_keys[key] = loop_id
    fixed_keys = [k for k in all_keys if k.startswith(("l7.", "l8.", "l9."))]
    rows.append(CheckRow(
        "top-3 loops untuned (fixed points)",
        "PASS" if not fixed_keys else "FAIL",
        "" if not fixed_keys else f"forbidden keys: {fixed_keys}",
    ))
    rows.append(CheckRow(
        "registry keys disjoint",
        "PASS",
        f"{len(all_keys)} unique keys across {len(TUNERS)} tuners",
    ))
    return rows


def check_state_files() -> list[CheckRow]:
    """State-file disjointness: each loop writes its own file."""
    rows = []
    paths: dict[str, str] = {}
    for loop_id, _name, _registry, _prefix in TUNERS:
        state_path = getattr(getattr(CONFIG, loop_id.lower()), "state_path")
        if state_path in paths:
            rows.append(CheckRow(
                f"state file {state_path}", "FAIL",
                f"shared by {paths[state_path]} and {loop_id}",
            ))
        else:
            paths[state_path] = loop_id
    rows.append(CheckRow(
        "state files disjoint",
        "PASS",
        f"{len(paths)} files ({', '.join(sorted(paths.values()))})",
    ))
    return rows


def _telemetry_counts(telemetry_dir: Path) -> dict[str, dict]:
    counts = {loop: {"start": 0, "complete": 0, "error": 0, "evaluation": 0}
              for loop in LOOPS}
    if not telemetry_dir.exists():
        return counts
    for f in telemetry_dir.glob("*.jsonl"):
        try:
            for line in f.read_text().splitlines():
                try:
                    ev = json.loads(line)
                except json.JSONDecodeError:
                    continue
                t = ev.get("type", "")
                for loop in LOOPS:
                    prefix = loop.lower() + "_"
                    if t.startswith(prefix):
                        kind = t[len(prefix):]
                        if kind in counts[loop]:
                            counts[loop][kind] += 1
        except OSError:
            continue
    return counts


def check_telemetry(workspace: Path) -> list[CheckRow]:
    """Every loop with persisted state has start + complete, no errors."""
    rows = []
    telemetry_dir = Path(workspace) / CONFIG.telemetry_dir
    counts = _telemetry_counts(telemetry_dir)
    for loop_id in LOOPS:
        state = getattr(getattr(CONFIG, loop_id.lower()), "state_path", None) \
            if loop_id != "L1" and loop_id != "L2" and loop_id != "L3" else None
        # L1-L3 have no state file; they are covered when run (telemetry only)
        c = counts[loop_id]
        if loop_id in ("L1", "L2", "L3"):
            if c["start"] or c["complete"]:
                status = "PASS" if c["start"] and c["complete"] else "FAIL"
                rows.append(CheckRow(
                    f"{loop_id} telemetry", status,
                    f"{c['start']} start / {c['complete']} complete / {c['error']} error",
                ))
            else:
                rows.append(CheckRow(
                    f"{loop_id} telemetry", "WARN", "never run (no events)",
                ))
            continue
        state_path = Path(workspace) / getattr(
            getattr(CONFIG, loop_id.lower()), "state_path")
        if not state_path.exists():
            rows.append(CheckRow(
                f"{loop_id} telemetry", "WARN", "never run (no state file)",
            ))
            continue
        ok = c["start"] >= 1 and c["complete"] >= 1
        err = f" / {c['error']} error" if c["error"] else ""
        rows.append(CheckRow(
            f"{loop_id} telemetry", "PASS" if ok and not c["error"] else "FAIL",
            f"{c['start']} start / {c['complete']} complete{err}",
        ))
    return rows


EVENT_TYPE_RE = re.compile(r"^[a-z][a-z0-9_]*$")
LOOP_EVENT_RE = re.compile(r"^l[1-9]_[a-z_]+$")
ISO_TS_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$"
)


def check_telemetry_contract(workspace: Path) -> list[CheckRow]:
    """Telemetry JSONL shape contract (mirrors contracts/validate.py section 5).

    Every line is one JSON object with a snake_case `type` (loop events
    must be `l{1..9}_*`) and an ISO-8601 `timestamp`.
    """
    rows = []
    tel = Path(workspace) / CONFIG.telemetry_dir
    if not tel.exists():
        rows.append(CheckRow("telemetry contract", "WARN", "no telemetry dir"))
        return rows
    files = events = bad = 0
    for p in tel.glob("*.jsonl"):
        files += 1
        for ln, line in enumerate(p.read_text(encoding="utf-8",
                                              errors="ignore").splitlines()):
            if not line.strip():
                continue
            events += 1
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                bad += 1
                continue
            et = ev.get("type", "")
            if not isinstance(et, str) or not EVENT_TYPE_RE.match(et):
                bad += 1
                continue
            if et.startswith("l") and not LOOP_EVENT_RE.match(et):
                bad += 1
                continue
            ts = ev.get("timestamp", "")
            if not isinstance(ts, str) or not ISO_TS_RE.match(ts):
                bad += 1
    rows.append(CheckRow(
        "telemetry contract", "PASS" if not bad else "FAIL",
        f"{files} files / {events} events / {bad} malformed"))
    return rows


def check_checkpoints(workspace: Path) -> list[CheckRow]:
    """Workspaces with loop state must be git repos with rsis checkpoints."""
    rows = []
    has_state = any(
        (Path(workspace) / getattr(getattr(CONFIG, l.lower()), "state_path")).exists()
        for l in ("l4", "l5", "l6", "l7", "l8", "l9")
    )
    if not has_state:
        rows.append(CheckRow("checkpoint hygiene", "WARN", "no loop state yet"))
        return rows
    # Workspace may be its own repo (nested local checkout) or a directory
    # inside the COSMOS repo (CI) — resolve the enclosing work tree either way.
    git_ok = False
    try:
        r = _git(Path(workspace), "rev-parse", "--is-inside-work-tree")
        git_ok = r.returncode == 0 and r.stdout.strip() == "true"
    except Exception:
        git_ok = False
    if not git_ok:
        rows.append(CheckRow("checkpoint hygiene", "FAIL", "workspace is not a git repo"))
        return rows
    r = _git(Path(workspace), "log", "--oneline", "--grep=rsis-checkpoint:")
    n = len([l for l in r.stdout.splitlines() if l.strip()])
    rows.append(CheckRow(
        "checkpoint hygiene", "PASS" if n >= 1 else "FAIL",
        f"{n} rsis-checkpoint commit(s)" if n else "no rsis-checkpoint commits found",
    ))
    return rows


def check_workspace(workspace: Optional[Path] = None) -> tuple[list[CheckRow], bool]:
    """Run all practice checks. Returns (rows, all_pass)."""
    workspace = Path(workspace or CONFIG.workspace_dir).resolve()
    rows = check_registry() + check_state_files() + check_checkpoints(workspace)
    rows += check_telemetry(workspace) + check_telemetry_contract(workspace)
    rows += check_policy(workspace)
    rows += check_invariants(workspace)
    all_pass = all(r.status != "FAIL" for r in rows)
    return rows, all_pass


def check_policy(workspace: Path) -> list[CheckRow]:
    """Phase 9: staged approvals are not applied; no unauthorized writes."""
    from rsis.policy import check_unauthorized_writes, list_staged

    rows = []
    staged = list_staged(workspace)
    rows.append(CheckRow(
        "policy approvals",
        "WARN" if staged else "PASS",
        f"{len(staged)} staged approval(s) pending" if staged else "none pending"))
    violations = check_unauthorized_writes(workspace)
    rows.append(CheckRow(
        "policy unauthorized writes",
        "FAIL" if violations else "PASS",
        ", ".join(violations) if violations else "no direct writes to gated paths"))
    return rows


def check_invariants(workspace: Path) -> list[CheckRow]:
    """Phase 14: executable invariant registry runs every cycle."""
    from rsis.invariants import run_invariants

    rows = []
    for r in run_invariants(workspace):
        rows.append(CheckRow(
            f"invariant {r['id']}",
            "PASS" if r["ok"] else "FAIL",
            r["detail"]))
    return rows


def run_checks(workspace: Optional[Path] = None) -> int:
    rows, all_pass = check_workspace(workspace)
    print("RSIS3 usage-practice check")
    print(f"  workspace: {Path(workspace or CONFIG.workspace_dir).resolve()}")
    print()
    for r in rows:
        print(f"  {r}")
    print()
    fails = [r for r in rows if r.status == "FAIL"]
    if fails:
        print(f"  FAIL — {len(fails)} practice violation(s); see docs/usage-practices.md")
        return 1
    print("  OK — all usage practices satisfied")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(run_checks())
