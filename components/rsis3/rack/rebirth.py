#!/usr/bin/env python3
"""Rebirth Engine — archive pulses + workspace state, reset to a fresh start.

Mirrors the legacy rebirth mechanic (archive → reset → next pulse 001),
adapted to the file-based RSIS v0.4 workspace: state lives in
``rack/pulses/`` and ``.rsis/`` (no SQLite). Pulses are moved into
``rack/lifecycles/rebirth-<n>-<ts>/`` so the next pulse is 001; the
knowledge graph, identity and loop state are snapshotted but retained
(analytical-only mode, matching the legacy manifesto semantics).

Usage:
    python rack/rebirth.py
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

PULSES_DIR = Path("rack/pulses")
LIFECYCLES_DIR = Path("rack/lifecycles")
RSIS_STATE_DIR = Path(".rsis")
MANIFESTO_PATH = Path("rack/rebirth_manifesto.json")

SCHEMA_VERSION = "1.0"


def next_rebirth_number() -> int:
    """Derive the next rebirth number from the manifesto, else archives."""
    if MANIFESTO_PATH.exists():
        try:
            m = json.loads(MANIFESTO_PATH.read_text())
            return int(m.get("rebirth_number", 0)) + 1
        except (ValueError, OSError):
            pass
    if LIFECYCLES_DIR.is_dir():
        return len(list(LIFECYCLES_DIR.glob("rebirth-*"))) + 1
    return 1


def _copy_file(src: Path, dst_dir: Path) -> None:
    shutil.copy2(str(src), str(dst_dir / src.name))


def execute_rebirth() -> dict:
    """Archive pulses + state, reset pulses, write the manifesto."""
    rn = next_rebirth_number()
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    archive_dir = LIFECYCLES_DIR / f"rebirth-{rn:03d}-{ts}"
    archive_dir.mkdir(parents=True, exist_ok=True)

    # 1. Archive + move pulse artifacts (fresh start: next pulse is 001)
    pulses = sorted(PULSES_DIR.glob("pulse-*.json"))
    archived_pulses = []
    for pf in pulses:
        _copy_file(pf, archive_dir)
        pf.unlink()
        archived_pulses.append(pf.name)
    dash = PULSES_DIR / "dashboard-data.json"
    if dash.exists():
        _copy_file(dash, archive_dir)
    # Fresh dashboard payload so ecosystem telemetry stays contract-valid
    # (ints >= 0) and the dashboard reflects the fresh start.
    (PULSES_DIR / "dashboard-data.json").write_text(json.dumps({
        "pulses": [], "goals": [], "score_history": [],
        "telemetry_aggregates": {},
        "summary": {"tot": 0, "pass": 0, "hold": 0, "fail": 0,
                    "impl_count": 0, "ca": 0.0, "pulse_count": 0, "cd": {}},
    }, indent=2))

    # 2. Snapshot loop/identity/KG/telemetry state (retained, not cleared)
    state_files = []
    if RSIS_STATE_DIR.is_dir():
        for f in sorted(RSIS_STATE_DIR.iterdir()):
            if f.is_file():
                _copy_file(f, archive_dir)
                state_files.append(f.name)
        tele = RSIS_STATE_DIR / "telemetry"
        if tele.is_dir():
            shutil.copytree(str(tele), str(archive_dir / "telemetry"))

    first = archived_pulses[0] if archived_pulses else "none"
    last = archived_pulses[-1] if archived_pulses else "none"
    manifesto = {
        "schema_version": SCHEMA_VERSION,
        "rebirth_number": rn,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "pulses_archived": len(archived_pulses),
        "previous_pulse_range": f"{first} to {last}",
        "state_files_snapshotted": len(state_files),
        "archive_path": str(archive_dir),
        "next_pulse": "001",
        "mode": "analytical_only",
    }
    MANIFESTO_PATH.write_text(json.dumps(manifesto, indent=2))

    print(f"  ✓ Rebirth #{rn}: archived {len(archived_pulses)} pulses to {archive_dir}")
    print(f"  ✓ Next pulse: 001  (mode: analytical_only, "
          f"{len(state_files)} state files snapshotted)")
    return manifesto


if __name__ == "__main__":
    execute_rebirth()
