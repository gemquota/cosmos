"""Succession planning — deliberate custody transfer.

Phase 33 (Sequel VII): stewardship passes to a chosen successor
deliberately, not by accident. Policy defines succession criteria; the
steward proposes an ordered heir list from the population (Phase 21);
custody transfers with a signed, audited record; predecessor and
successor dual-run through an overlap window so continuity is verified
before cutover.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
)
from rsis.identity import load_peers

logger = logging.getLogger(__name__)

DEFAULT_OVERLAP_CYCLES = 100


def succession_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "succession"


def plans_path(workspace: Path) -> Path:
    return succession_dir(workspace) / "plans.jsonl"


def plan(workspace: Path, criteria: Optional[dict] = None,
         actor: str = "system") -> dict:
    """Propose an ordered heir list from the trust graph (21)."""
    ws = Path(workspace)
    ensure_rack(ws, "succession")
    peers = load_peers(ws)
    candidates = [p for p in peers.get("peers", [])
                  if p.get("trust") in ("trusted", "allied")]
    # deterministic ordering: trust level then fingerprint
    order = {"allied": 0, "trusted": 1}
    candidates.sort(key=lambda p: (order.get(p.get("trust"), 9),
                                   p.get("fingerprint", "")))
    rec = {
        "id": f"s{len(read_jsonl(plans_path(ws)))}",
        "heirs": [{"id": p["id"], "fingerprint": p["fingerprint"],
                   "trust": p["trust"]} for p in candidates],
        "criteria": criteria or {"trust_min": "trusted",
                                 "overlap_cycles": DEFAULT_OVERLAP_CYCLES},
        "status": "proposed", "planned_by": actor, "ts": now_ts(),
    }
    append_jsonl(plans_path(ws), rec)
    emit(ws, "succession_planned", plan=rec["id"], heirs=len(candidates))
    return rec


def transfer(workspace: Path, plan_id: str, heir_id: str,
             actor: str = "system") -> dict:
    """Execute a signed custody transfer with audit + attestation."""
    ws = Path(workspace)
    recs = read_jsonl(plans_path(ws))
    target = next((r for r in recs if r.get("id") == plan_id), None)
    if target is None or not any(h["id"] == heir_id for h in target.get("heirs", [])):
        return {"ok": False, "reason": "plan/heir not found"}
    from rsis.attestations import append as attest
    from rsis.audit import append as audit
    attest(ws, "succession_transfer", {"plan": plan_id, "heir": heir_id,
                                       "actor": actor})
    audit(ws, {"type": "succession.transfer", "actor": actor,
               "detail": f"custody -> {heir_id} (plan {plan_id})"})
    rec = {"plan": plan_id, "heir": heir_id, "transferred_by": actor,
           "overlap_cycles": (target.get("criteria") or {}).get(
               "overlap_cycles", DEFAULT_OVERLAP_CYCLES),
           "status": "dual-running", "ts": now_ts()}
    append_jsonl(Path(ws) / "rack" / "succession" / "transfers.jsonl", rec)
    emit(ws, "succession_transferred", heir=heir_id, plan=plan_id)
    return {"ok": True, "transfer": rec}


def status(workspace: Path) -> dict:
    plans = read_jsonl(plans_path(workspace))
    transfers = read_jsonl(Path(workspace) / "rack" / "succession" / "transfers.jsonl")
    return {"plans": len(plans), "transfers": len(transfers),
            "open": [t for t in transfers if t.get("status") == "dual-running"]}
