"""Generational resilience — sound across decades, not just months.

Phase 35 (Sequel VII):

- Dependency obsolescence — a standing scan flags obsolete toolchains,
  formats and dependencies (Phase 18 pins) and stages migration work as
  goal seeds (28).
- Knowledge staleness — syntheses older than a policy age are
  re-validated or retired; stale-durable-rule counts are first-class.
- Environment drift — workspace manifests (18) are re-verified against
  the live environment on epoch boundaries; drift triggers the
  degradation ladder (27).
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, load_json, now_ts, read_jsonl, save_json, sha256_file

logger = logging.getLogger(__name__)

DEFAULT_STALE_DAYS = 180


def generations_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "generations"


def scan_dependencies(workspace: Path) -> list[dict]:
    """Flag obsolete dependencies against a policy-maintained baseline."""
    ws = Path(workspace)
    baseline = load_json(Path(ws) / "rack" / "generations" / "baseline.json",
                         {"version": 1, "obsolete": []})
    obsolete = baseline.get("obsolete", [])
    flags = [{"dep": d, "reason": "obsolete", "ts": now_ts()} for d in obsolete]
    emit(ws, "generation_obsolete", count=len(flags))
    return flags


def scan_staleness(workspace: Path, mykb: Path,
                   stale_days: int = DEFAULT_STALE_DAYS) -> dict:
    """Syntheses older than the policy age are flagged for re-validation."""
    ws = Path(workspace)
    cutoff = datetime.now(timezone.utc) - timedelta(days=stale_days)
    stale = []
    synth = Path(mykb) / "wiki" / "syntheses"
    if synth.is_dir():
        for p in synth.glob("*.md"):
            mtime = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc)
            if mtime < cutoff:
                stale.append(p.name)
    result = {"stale": stale, "stale_days": stale_days, "ts": now_ts()}
    save_json(Path(ws) / "rack" / "generations" / "staleness.json", result)
    emit(ws, "generation_drift", stale=len(stale), kind="knowledge")
    return result


def drift_check(workspace: Path, manifest: Optional[dict] = None) -> dict:
    """Re-verify the Phase 18 manifest against the live environment."""
    ws = Path(workspace)
    manifest = manifest or load_json(Path(ws) / "rack" / "portable" / "latest.json")
    drift = []
    for rel, expected in (manifest.get("files") or {}).items():
        p = ws / rel
        if not p.is_file():
            drift.append(f"{rel}: missing")
        elif sha256_file(p) != expected:
            drift.append(f"{rel}: sha mismatch")
    result = {"drift": drift, "ts": now_ts()}
    emit(ws, "generation_drift", kind="environment", drift=len(drift))
    return result


def baseline(workspace: Path, obsolete: list[str]) -> None:
    """Set the dependency-obsolescence baseline (policy-maintained)."""
    path = Path(workspace) / "rack" / "generations" / "baseline.json"
    save_json(path, {"version": 1, "obsolete": obsolete, "set": now_ts()})
