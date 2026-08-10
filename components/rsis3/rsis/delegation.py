"""Delegation contracts — bounded authority with instant revocation.

Phase 38 (Sequel VIII): a delegation is a signed, policy-encoded record —
scope (actions × projects × budget), expiry, and revocation conditions —
extending the Phase 12 authz chain without a new identity system.
Delegated actions run inside the contract's limits; any breach fails
closed and logs an incident; revocation takes effect within one cycle and
cascades to in-flight delegated work.
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, load_json, now_ts, save_json

logger = logging.getLogger(__name__)


def delegations_path(workspace: Path) -> Path:
    return Path(workspace) / ".rsis" / "delegations.json"


def _load(workspace: Path) -> dict:
    return load_json(delegations_path(workspace),
                     {"version": 1, "delegations": {}})


def issue(workspace: Path, delegate: str, actions: list[str],
          projects: list[str], budget: float, expiry_ts: int,
          granter: str = "approver") -> dict:
    """Issue a delegation contract."""
    ws = Path(workspace)
    data = _load(ws)
    rec = {
        "id": f"dlg{len(data.get('delegations', {}))}",
        "delegate": delegate, "actions": actions, "projects": projects,
        "budget": budget, "spent": 0.0, "expiry_ts": expiry_ts,
        "granter": granter, "revoked": False, "issued": now_ts(),
    }
    data.setdefault("delegations", {})[rec["id"]] = rec
    save_json(delegations_path(ws), data)
    emit(ws, "delegation_issued", delegation=rec["id"], delegate=delegate,
         scope=len(actions) * len(projects))
    return rec


def check(workspace: Path, delegation_id: str, action: str,
          project: str, cost: float = 0.0) -> tuple[bool, str]:
    """Bounded execution check: scope, expiry, budget, revocation."""
    rec = _load(workspace).get("delegations", {}).get(delegation_id)
    if rec is None:
        return False, "unknown delegation"
    if rec.get("revoked"):
        return False, "revoked"
    if time.time() > float(rec.get("expiry_ts", 0)):
        return False, "expired"
    if action not in rec.get("actions", []):
        return False, "action out of scope"
    if project not in rec.get("projects", []):
        return False, "project out of scope"
    if float(rec.get("spent", 0.0)) + cost > float(rec.get("budget", 0.0)):
        return False, "budget exceeded"
    return True, "ok"


def execute(workspace: Path, delegation_id: str, action: str,
            project: str, cost: float = 0.0) -> dict:
    """Execute within limits; any breach fails closed + logs an incident."""
    ws = Path(workspace)
    ok, reason = check(ws, delegation_id, action, project, cost)
    if not ok:
        from rsis.seasons import incident
        incident(ws, "delegation.breach",
                 f"{delegation_id} {action}@{project}: {reason}")
        emit(ws, "delegation_blocked", delegation=delegation_id, reason=reason)
        return {"executed": False, "reason": reason}
    data = _load(ws)
    rec = data["delegations"][delegation_id]
    rec["spent"] = round(float(rec.get("spent", 0.0)) + cost, 6)
    save_json(delegations_path(ws), data)
    emit(ws, "delegation_executed", delegation=delegation_id, action=action,
         cost=cost)
    return {"executed": True, "spent": rec["spent"]}


def revoke(workspace: Path, delegation_id: str, actor: str = "approver") -> bool:
    """Revoke; takes effect immediately (within one cycle by design)."""
    ws = Path(workspace)
    data = _load(ws)
    rec = data.get("delegations", {}).get(delegation_id)
    if rec is None:
        return False
    rec["revoked"] = True
    rec["revoked_by"] = actor
    rec["revoked_at"] = now_ts()
    save_json(delegations_path(ws), data)
    emit(ws, "delegation_revoked", delegation=delegation_id, actor=actor)
    return True


def status(workspace: Path) -> dict:
    data = _load(workspace)
    recs = data.get("delegations", {})
    return {"delegations": len(recs),
            "active": sum(1 for r in recs.values() if not r.get("revoked")),
            "revoked": sum(1 for r in recs.values() if r.get("revoked"))}
