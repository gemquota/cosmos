"""Self-directed learning goals — system-proposed, human-ratified.

Phase 28 (Sequel VI): the goal stack becomes system-proposed and
human-ratified. Gaps from self-assessment, red-team, federation and
external feedback become goal candidates with rationale and expected
value; unratified goals never run; plateaued goals retire automatically;
each proposed goal carries its own fitness/quality telemetry.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
)

logger = logging.getLogger(__name__)

PLATEAU_DAYS = 30


def goals_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "goals"


def proposals_path(workspace: Path) -> Path:
    return goals_dir(workspace) / "proposals.jsonl"


def _gap_sources(workspace: Path) -> list[dict]:
    """Gap candidates from red-team findings + confidence lows + backlog."""
    ws = Path(workspace)
    sources: list[dict] = []
    findings = read_jsonl(Path(ws) / "rack" / "redteam" / "findings.jsonl")
    for f in findings:
        if f.get("status") == "open":
            sources.append({"source": "redteam",
                            "title": f"Fix red-team gap: {f.get('kind')}",
                            "rationale": f.get("detail", ""),
                            "expected_value": "gate strength"})
    conf = load_json(Path(ws) / ".rsis" / "confidence.json")
    lows = [k for k, v in (conf.get("items") or {}).items()
            if float(v.get("confidence", 0)) < 0.4][:3]
    for k in lows:
        sources.append({"source": "federation",
                        "title": f"Resolve low-confidence knowledge {k[:12]}",
                        "rationale": "confidence below 0.4",
                        "expected_value": "knowledge reliability"})
    return sources


def propose_from_gaps(workspace: Path) -> list[dict]:
    """Turn open gaps into unratified goal candidates."""
    out = []
    for gap in _gap_sources(workspace):
        rec = propose(workspace, gap["title"], gap["rationale"],
                      expected_value=gap["expected_value"],
                      source=gap["source"], proposer="system")
        out.append(rec)
    return out


def propose(workspace: Path, title: str, rationale: str,
            expected_value: str = "unspecified", source: str = "manual",
            proposer: str = "system") -> dict:
    ws = Path(workspace)
    ensure_rack(ws, "goals")
    rec = {
        "id": f"g{len(read_jsonl(proposals_path(ws)))}",
        "title": title, "rationale": rationale,
        "expected_value": expected_value, "source": source,
        "proposer": proposer, "status": "proposed", "ratified_by": None,
        "fitness": None, "ts": now_ts(),
    }
    append_jsonl(proposals_path(ws), rec)
    emit(ws, "goals_proposed", goal=rec["id"], source=source)
    return rec


def ratify(workspace: Path, goal_id: str, actor: str = "approver",
           tier: int = 1) -> bool:
    """Human ratification; ratified goals merge into the goal stack."""
    recs = read_jsonl(proposals_path(workspace))
    target = next((r for r in recs if r.get("id") == goal_id), None)
    if target is None or target.get("status") != "proposed":
        return False
    with proposals_path(workspace).open("w", encoding="utf-8") as fh:
        for r in recs:
            if r.get("id") == goal_id:
                r["status"] = "ratified"
                r["ratified_by"] = actor
                r["ratified_at"] = now_ts()
                r["tier"] = tier
            fh.write(json.dumps(r, sort_keys=True) + "\n")
    # append to the goal stack as a system-proposed tier goal
    stack_path = Path(workspace) / "rack" / "goals_stack.json"
    stack = load_json(stack_path)
    tiers = stack.setdefault("system_proposed", [])
    tiers.append({"title": target["title"], "rationale": target["rationale"],
                  "expected_value": target["expected_value"],
                  "ratified_by": actor, "ts": now_ts()})
    save_json(stack_path, stack)
    emit(workspace, "goals_ratified", goal=goal_id, actor=actor)
    return True


def record_fitness(workspace: Path, goal_id: str, fitness: float,
                   cost: float = 0.0) -> bool:
    """Goal-quality telemetry: hit rate, novelty, cost."""
    recs = read_jsonl(proposals_path(workspace))
    for r in recs:
        if r.get("id") == goal_id:
            r["fitness"] = fitness
            r["cost"] = cost
            with proposals_path(workspace).open("w", encoding="utf-8") as fh:
                for rr in recs:
                    fh.write(json.dumps(rr, sort_keys=True) + "\n")
            emit(workspace, "goals_telemetry", goal=goal_id,
                 fitness=fitness, cost=cost)
            return True
    return False


def retire_plateaued(workspace: Path, plateau_days: int = PLATEAU_DAYS) -> list[str]:
    """Retire goals with no progress for the plateau window."""
    from datetime import timedelta
    cutoff = (datetime.now(timezone.utc) - timedelta(days=plateau_days))
    recs = read_jsonl(proposals_path(workspace))
    retired = []
    for r in recs:
        if r.get("status") == "ratified" and not r.get("fitness"):
            try:
                adopted = datetime.fromisoformat(r.get("ratified_at", "").replace("Z", "+00:00"))
            except ValueError:
                continue
            if adopted < cutoff:
                r["status"] = "retired"
                retired.append(r["id"])
    if retired:
        with proposals_path(workspace).open("w", encoding="utf-8") as fh:
            for r in recs:
                fh.write(json.dumps(r, sort_keys=True) + "\n")
        for gid in retired:
            emit(workspace, "goals_retired", goal=gid)
    return retired


def status(workspace: Path) -> dict:
    recs = read_jsonl(proposals_path(workspace))
    return {"proposals": len(recs),
            "ratified": sum(1 for r in recs if r.get("status") == "ratified"),
            "retired": sum(1 for r in recs if r.get("status") == "retired")}
