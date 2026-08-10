"""Convergence monitor — fitness plateaus and L4–L9 bound no-ops.

Detects when the strategy search has stalled (best fitness flat over N
generations) or when meta-loops are no-ops at their parameter bounds, and
auto-proposes retuning through the existing identity/meta loops instead
of silent no-op runs (Phase 4 of the multi-phase roadmap).

Usage:
    python -m rsis convergence [--window 5] [--noop-window 10]
        [--noop-threshold 8] [--apply] [--json]
"""

from __future__ import annotations

import json
import logging
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from rsis.entity_states import EntityStateError, transition, validate_record

logger = logging.getLogger(__name__)

# loop key -> command that retunes it (the "existing identity/meta loops")
RETUNE_LOOP = {
    "l4": "optimize",
    "l5": "strategies",
    "l6": "identity",
    "l7": "metacog",
    "l8": "metameta",
    "l9": "mmm",
}
PLATEAU_LOOP = "identity"  # L6 tunes the L3 plateau timeout

_TS = lambda: datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def read_telemetry(telemetry_dir: Path, limit: Optional[int] = None) -> list[dict]:
    """Read telemetry events across all jsonl files (newest first)."""
    events: list[dict] = []
    if not telemetry_dir.is_dir():
        return events
    for f in sorted(telemetry_dir.glob("*.jsonl"), reverse=True):
        try:
            for line in f.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        except OSError:
            continue
    events.sort(key=lambda e: e.get("timestamp", ""))
    if limit:
        events = events[-limit:]
    return events


def detect(workspace: Path, plateau_window: int = 5,
           noop_window: int = 10, noop_threshold: int = 8,
           epsilon: float = 1e-9) -> dict:
    """Return a convergence report; writes nothing."""
    strategies = _load(workspace / ".rsis" / "strategies.json", {})
    history = strategies.get("history") or []
    report: dict = {
        "ts": _TS(),
        "generation": strategies.get("generation", 0),
        "plateau": None,
        "noops": {},
        "proposed_loop": None,
        "command": None,
        "detected": False,
    }
    recent = history[-plateau_window:]
    if len(recent) >= max(2, plateau_window - 1):
        bests = [float(h.get("best_fitness") or 0) for h in recent]
        flat = all(abs(b - bests[0]) <= epsilon for b in bests)
        if flat:
            report["plateau"] = {
                "generations": len(recent),
                "best_fitness": bests[0],
            }
    # L4–L9 bound no-ops from telemetry (changed: false on *_complete)
    events = read_telemetry(workspace / ".rsis" / "telemetry")
    events = events[-noop_window * 20:]
    counts: dict[str, int] = {}
    for e in events:
        t = e.get("type") or ""
        for loop in RETUNE_LOOP:
            if t == f"{loop}_complete" and e.get("changed") is False:
                counts[loop] = counts.get(loop, 0) + 1
    report["noops"] = {k: v for k, v in counts.items() if v > 0}
    over = {k: v for k, v in counts.items() if v >= noop_threshold}
    if report["plateau"]:
        report["proposed_loop"] = PLATEAU_LOOP
        report["detected"] = True
    elif over:
        worst = max(over, key=over.get)
        report["proposed_loop"] = RETUNE_LOOP[worst]
        report["detected"] = True
    if report["proposed_loop"]:
        report["command"] = f"python -m rsis {report['proposed_loop']}"
    return report


def proposals_dir(workspace: Path) -> Path:
    return workspace / "rack" / "proposals"


def write_proposal(workspace: Path, report: dict,
                   ts: Optional[str] = None) -> Path:
    """Persist a convergence proposal (create-only)."""
    ts = ts or _TS()
    out = proposals_dir(workspace)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"convergence-{ts.replace(':', '').replace('T', '-').split('.')[0]}.json"
    if path.exists():
        return path
    payload = dict(report)
    payload["type"] = "convergence-proposal"
    try:
        # Series 2 entity_constraints: proposals carry required fields and
        # start in the "proposed" lifecycle state.
        validate_record("proposal", payload)
        payload["applied"] = False
        payload["state"] = "proposed"
    except EntityStateError as e:
        logger.warning("proposal record invalid: %s", e)
        payload["applied"] = False
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def file_backlog_note(mykb: Path, report: dict, ts: Optional[str] = None) -> Optional[Path]:
    """Mirror a convergence proposal into the MyKB backlog (create-only)."""
    if not report.get("detected"):
        return None
    ts = ts or _TS()
    date_part = ts[:10]
    slug = f"convergence-{date_part}"
    out = mykb / "wiki" / "backlog"
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{slug}.md"
    if path.exists():
        return path
    reason = "fitness plateau" if report.get("plateau") else "bound no-ops"
    detail = report["plateau"] if report.get("plateau") else report["noops"]
    body = "\n".join([
        f"# Convergence detected — {reason}",
        "",
        f"- Detected: {report['ts']}",
        f"- Generation: {report['generation']}",
        f"- Evidence: {json.dumps(detail)}",
        f"- Proposed retune: {report['command'] or '—'}",
        "- Source: rsis convergence",
    ])
    front = {
        "type": "backlog",
        "title": f"Convergence — {reason}",
        "description": json.dumps(detail)[:240],
        "tags": ["backlog", "convergence"],
        "timestamp": ts,
        "status": "open",
        "source": "convergence",
        "proposed_loop": report.get("proposed_loop"),
    }
    path.write_text(
        "---\n" + "\n".join(f'{k}: "{v}"' for k, v in front.items()) + "\n---\n\n" + body + "\n",
        encoding="utf-8")
    return path


def apply_proposal(workspace: Path, report: dict, package_root: Path) -> int:
    """Run the proposed retune loop once (bounded by the caller)."""
    loop = report.get("proposed_loop")
    if not loop:
        return 0
    print(f"  ▶ applying retune: python -m rsis {loop}")
    proc = subprocess.run(
        [sys.executable, "-m", "rsis", loop], cwd=str(package_root))
    if proc.returncode == 0:
        _mark_applied(workspace, report)
    return proc.returncode


def _mark_applied(workspace: Path, report: dict, ts: Optional[str] = None) -> None:
    ts = ts or _TS()
    out = proposals_dir(workspace)
    out.mkdir(parents=True, exist_ok=True)
    applied = out / "applied.jsonl"
    record = {
        "ts": ts,
        "loop": report.get("proposed_loop"),
        "generation": report.get("generation"),
    }
    try:
        # Series 2 entity_lifecycles: only a "proposed" retune may become
        # "applied", and each proposal applies at most once.
        validate_record("proposal", record)
        transition("proposal", "proposed", "applied")
    except EntityStateError as e:
        logger.warning("skipping invalid application record: %s", e)
        return
    if applied.is_file():
        for line in applied.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            prior = json.loads(line)
            if (prior.get("loop") == record["loop"]
                    and prior.get("generation") == record["generation"]):
                logger.warning(
                    "retune %s gen %s already applied — skipping duplicate",
                    record["loop"], record["generation"])
                return
    with applied.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")


def last_applied(workspace: Path) -> Optional[dict]:
    """Most recent retune application, or None."""
    applied = proposals_dir(workspace) / "applied.jsonl"
    if not applied.is_file():
        return None
    recs = [json.loads(l) for l in applied.read_text(encoding="utf-8").splitlines() if l.strip()]
    return recs[-1] if recs else None


def main(workspace: Path, mykb: Path, package_root: Path,
         plateau_window: int = 5, noop_window: int = 10,
         noop_threshold: int = 8, apply: bool = False,
         json_out: bool = False) -> int:
    report = detect(workspace, plateau_window, noop_window, noop_threshold)
    if report["detected"]:
        path = write_proposal(workspace, report)
        note = file_backlog_note(mykb, report)
        print(f"  ⚠ Convergence detected at generation {report['generation']}: "
              f"{report['command']}")
        print(f"  proposal: {path}")
        if note:
            print(f"  backlog:  {note}")
        if apply:
            code = apply_proposal(workspace, report, package_root)
            if code != 0:
                return code
    else:
        print("  ✓ No convergence detected (no plateau, no bound no-ops).")
    if json_out:
        print(json.dumps(report))
    return 0
