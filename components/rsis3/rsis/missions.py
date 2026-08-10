"""Mission continuity — long-horizon missions outlive any single instance.

Phase 34 (Sequel VII): missions (goal-stack level goals) carry explicit
state — objective, progress, constraints, next actions — that travels
with inheritance (31) and succession (33), not with any instance.
Generation checkpoints are attestable (14) every cycle so a successor can
resume at the exact logical point; progress is contiguous (no lost or
double-applied steps).
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


def missions_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "missions"


def state_path(workspace: Path) -> Path:
    return missions_dir(workspace) / "missions.json"


def checkpoints_path(workspace: Path) -> Path:
    return missions_dir(workspace) / "checkpoints.jsonl"


def create(workspace: Path, mission_id: str, objective: str,
           constraints: list[str] | None = None, steward: str = "system") -> dict:
    ws = Path(workspace)
    ensure_rack(ws, "missions")
    state = load_json(state_path(ws), {"version": 1, "missions": {}})
    if mission_id in state.get("missions", {}):
        raise ValueError(f"mission {mission_id!r} exists")
    mission = {
        "id": mission_id, "objective": objective,
        "constraints": constraints or [], "progress": 0.0,
        "next_actions": [], "steward": steward, "status": "active",
        "started": now_ts(),
    }
    state.setdefault("missions", {})[mission_id] = mission
    save_json(state_path(ws), state)
    checkpoint(ws, mission_id, "created")
    emit(ws, "mission_created", mission=mission_id)
    return mission


def checkpoint(workspace: Path, mission_id: str, note: str,
               progress: Optional[float] = None) -> dict:
    """Attestable generation checkpoint (progress ledger is contiguous)."""
    ws = Path(workspace)
    from rsis.attestations import append as attest
    state = load_json(state_path(ws), {"version": 1, "missions": {}})
    mission = state.get("missions", {}).get(mission_id)
    if mission is None:
        raise ValueError(f"no mission {mission_id}")
    if progress is not None:
        mission["progress"] = round(float(progress), 4)
    seq = len(read_jsonl(checkpoints_path(ws)))
    rec = {"seq": seq, "mission": mission_id, "note": note,
           "progress": mission["progress"], "steward": mission.get("steward"),
           "ts": now_ts()}
    append_jsonl(checkpoints_path(ws), rec)
    attest(ws, "mission_checkpoint", {"mission": mission_id, "seq": seq,
                                      "progress": mission["progress"]})
    save_json(state_path(ws), state)
    emit(ws, "mission_progress", mission=mission_id, seq=seq,
         progress=mission["progress"])
    return rec


def handoff(workspace: Path, mission_id: str, new_steward: str,
            resume_seq: Optional[int] = None) -> dict:
    """Resume by a successor at the exact logical point."""
    ws = Path(workspace)
    state = load_json(state_path(ws), {"version": 1, "missions": {}})
    mission = state.get("missions", {}).get(mission_id)
    if mission is None:
        raise ValueError(f"no mission {mission_id}")
    mission["steward"] = new_steward
    checkpoints = read_jsonl(checkpoints_path(ws))
    last = max((c["seq"] for c in checkpoints if c.get("mission") == mission_id),
               default=-1)
    if resume_seq is not None and resume_seq != last:
        raise ValueError(
            f"contiguity violation: resume {resume_seq} != last {last}")
    save_json(state_path(ws), state)
    emit(ws, "mission_handoff", mission=mission_id, steward=new_steward,
         resume=last)
    return {"mission": mission_id, "steward": new_steward,
            "resume_seq": last, "contiguous": True}


def status(workspace: Path) -> dict:
    state = load_json(state_path(ws := workspace), {"version": 1, "missions": {}})
    missions = state.get("missions", {})
    return {"missions": len(missions),
            "active": sum(1 for m in missions.values()
                          if m.get("status") == "active"),
            "checkpoints": len(read_jsonl(checkpoints_path(ws)))}
