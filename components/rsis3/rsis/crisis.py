"""Crisis response — act as infrastructure without dropping guardrails.

Phase 44 (Sequel IX): policy-defined crisis profiles flip defaults —
read paths open up, non-critical writes fail closed, budgets divert to
critical capability classes (extending the Phase 27 degradation ladder).
Crisis entry/exit events are high-priority and replicated immediately to
the federation ledger; foreign aid is quarantined until verified (14);
crisis drills run on a standing cadence with post-drill attestation.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
)

logger = logging.getLogger(__name__)


def crisis_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "crisis" / "state.json"


def drills_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "crisis" / "drills.jsonl"


def enter(workspace: Path, profile: str = "default",
          entered_by: str = "system") -> dict:
    """Enter a crisis mode: open reads, fail-closed writes, budget divert."""
    ws = Path(workspace)
    ensure_rack(ws, "crisis")
    profiles = load_json(Path(ws) / "rack" / "crisis" / "profiles.json",
                         {"version": 1, "profiles": {
                             "default": {"reads": "open", "writes": "fail-closed",
                                         "budget_divert": "policy-critical"}}})
    mode = profiles.get("profiles", {}).get(profile,
                                            profiles["profiles"]["default"])
    state = {"active": True, "profile": profile, "mode": mode,
             "entered_by": entered_by, "entered_at": now_ts()}
    save_json(crisis_path(ws), state)
    append_jsonl(Path(ws) / "rack" / "federation" / "ledger.jsonl",
                 {"type": "crisis.entered", "profile": profile,
                  "ts": now_ts()})
    emit(ws, "crisis_entered", profile=profile)
    return state


def exit_crisis(workspace: Path, exited_by: str = "system") -> dict:
    """Exit crisis; attest what ran."""
    ws = Path(workspace)
    state = load_json(crisis_path(ws), {"active": False})
    if not state.get("active"):
        return {"ok": False, "reason": "not in crisis"}
    from rsis.attestations import append as attest
    attest(ws, "crisis_exit", {"profile": state.get("profile"),
                               "entered": state.get("entered_at")})
    state["active"] = False
    state["exited_by"] = exited_by
    state["exited_at"] = now_ts()
    save_json(crisis_path(ws), state)
    append_jsonl(Path(ws) / "rack" / "federation" / "ledger.jsonl",
                 {"type": "crisis.exit", "ts": now_ts()})
    emit(ws, "crisis_exit", profile=state.get("profile"))
    return state


def drill(workspace: Path, scenario: str = "default",
          run_by: str = "system") -> tuple[bool, dict]:
    """Crisis drill: enter → verify policy-critical stays on → exit."""
    ws = Path(workspace)
    from rsis.capacity import degradation_ladder
    entered = enter(ws, profile=scenario, entered_by=run_by)
    ladder = degradation_ladder(ws, pressure=4)
    ok = "policy-critical" in ladder["always_on"]
    exited = exit_crisis(ws, exited_by=run_by)
    rec = {"scenario": scenario, "ok": ok, "policy_critical_kept": ok,
           "run_by": run_by, "ts": now_ts()}
    append_jsonl(drills_path(ws), rec)
    emit(ws, "crisis_drill", scenario=scenario, ok=ok)
    return ok, rec


def status(workspace: Path) -> dict:
    state = load_json(crisis_path(ws := workspace), {"active": False})
    drills = read_jsonl(drills_path(ws))
    return {"active": bool(state.get("active")),
            "profile": state.get("profile"),
            "drills": len(drills),
            "last_drill_ok": drills[-1].get("ok") if drills else None}
