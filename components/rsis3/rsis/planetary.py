"""Planetary stewardship — coordinated global resource operation.

Phase 45 (Sequel IX, Epoch-1 commons capstone): the commons operates as
coordinated global infrastructure. Energy/compute/storage budgets (27)
coordinate across the commons with local policy sovereign (24);
sustainability accounting (27) extends to global footprints; population-
level invariants (14) monitor commons health — replication (32),
attribution (42), trust (43) — with drift repaired by stewards (29).
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, ensure_rack, load_json, now_ts, save_json

logger = logging.getLogger(__name__)


def planetary_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "planetary" / "state.json"


def resource_plan(workspace: Path, allocations: dict,
                  planned_by: str = "system") -> dict:
    """Coordinate a shared resource plan; local policy stays sovereign."""
    ws = Path(workspace)
    ensure_rack(ws, "planetary")
    from rsis.policy import load_policy
    local = load_policy(ws)
    plan = {"allocations": allocations, "planned_by": planned_by,
            "local_policy_sovereign": bool(local),
            "planned_at": now_ts()}
    save_json(planetary_path(ws), plan)
    emit(ws, "commons_resource", populations=len(allocations))
    return plan


def health(workspace: Path) -> dict:
    """Commons health: replication (32), attribution (42), trust (43)."""
    ws = Path(workspace)
    from rsis.archival import status as archival_status
    from rsis.commons import attribution_report
    from rsis.diplomacy import status as diplomacy_status
    arch = archival_status(ws)
    att = attribution_report(ws)
    dip = diplomacy_status(ws)
    checks = {
        "replication": arch.get("tracked", 0) > 0,
        "attribution": att.get("attribution_ok", False),
        "trust": dip.get("active", 0) > 0,
    }
    h = {"checks": checks,
         "health_ok": all(checks.values()),
         "replication_min": arch.get("replication_min"),
         "commons_items": att.get("items", 0),
         "treaties": dip.get("active", 0),
         "ts": now_ts()}
    save_json(Path(ws) / "rack" / "planetary" / "health.json", h)
    emit(ws, "commons_health", ok=h["health_ok"])
    return h


def status(workspace: Path) -> dict:
    return {"plan": load_json(planetary_path(ws := workspace)),
            "health": load_json(Path(ws) / "rack" / "planetary" / "health.json")}
