"""Epoch 1 (Phases 16–50) shared plumbing.

All epoch-1 phases emit telemetry through one append-only JSONL channel
(``.rsis/telemetry/epoch1.jsonl``) so ``gen-static-data.py`` and the
dashboard Roadmap tab can surface per-phase activity without each phase
implementing its own pipeline. Event shape follows the telemetry contract
enforced by ``contracts/validate.py``: snake_case ``type`` and an ISO-8601
``timestamp``.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def now_ts() -> str:
    """UTC timestamp matching the telemetry ISO format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def epoch1_telemetry_path(workspace: Path) -> Path:
    return Path(workspace) / ".rsis" / "telemetry" / "epoch1.jsonl"


def emit(workspace: Path, event_type: str, **meta) -> None:
    """Append one epoch-1 telemetry event (contract-safe, append-only)."""
    path = epoch1_telemetry_path(workspace)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        ev = {"type": event_type, "timestamp": now_ts(), **meta}
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(ev, sort_keys=True) + "\n")
    except OSError as e:
        logger.warning("epoch1 telemetry write failed: %s", e)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def sha256_file(path: Path) -> str:
    """Streaming sha256 of a file; empty string if unreadable."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return ""


def read_jsonl(path: Path) -> list[dict]:
    """Read JSONL lines, skipping malformed ones."""
    out = []
    if not Path(path).is_file():
        return out
    for line in Path(path).read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def append_jsonl(path: Path, record: dict) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")


def load_json(path: Path, default=None) -> dict:
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else default or {}
    except (OSError, json.JSONDecodeError):
        return default or {}


def save_json(path: Path, data: dict) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1, sort_keys=True)
        fh.write("\n")


def ensure_rack(workspace: Path, *names: str) -> None:
    """Create rack/<name> dirs (idempotent)."""
    root = Path(workspace) / "rack"
    for name in names:
        (root / name).mkdir(parents=True, exist_ok=True)


def invariants_status(workspace: Path) -> tuple[bool, list[str]]:
    """Run the Phase 14 invariant registry; returns (ok, issues)."""
    from rsis.invariants import run_invariants
    rows = run_invariants(workspace)
    issues = [f"{r.get('id')}: {r.get('detail')}" for r in rows
              if not r.get("ok")]
    return (len(issues) == 0, issues)
