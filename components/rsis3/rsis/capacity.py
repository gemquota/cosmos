"""Resource sovereignty & sustainability — capacity planning.

Phase 27 (Sequel VI): the system operates within its means indefinitely.

- ``plan`` — a 90-day cost/energy forecast from the cost ledger (8) and
  Phase 15 seasonal profile; sprint/coast/pause become a plan.
- ``sustainability`` — the cost ledger tracks budget, energy and storage;
  per-instance sustainability is reported.
- ``degradation_ladder`` — under sustained pressure the system degrades
  gracefully by capability class: observability → memory → verification →
  policy-critical always on.
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, load_json, now_ts, read_jsonl

logger = logging.getLogger(__name__)

PLAN_HORIZON_DAYS = 90
LADDER = ("observability", "memory", "verification", "policy-critical")
#: which capability classes may be shed at each pressure level
SHED_AT = {1: ("observability",), 2: ("observability", "memory"),
           3: ("observability", "memory", "verification"),
           4: ("observability", "memory", "verification")}


def cost_daily(workspace: Path, days: int = 30) -> list[float]:
    """Daily LLM cost totals from the cost ledger."""
    path = Path(workspace) / ".rsis" / "costs.jsonl"
    daily: dict = {}
    if path.is_file():
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            day = str(rec.get("ts", ""))[:10]
            daily[day] = daily.get(day, 0.0) + float(rec.get("cost", 0.0))
    out = [v for _, v in sorted(daily.items())][-days:]
    return out or [0.0]


def plan(workspace: Path) -> dict:
    """90-day capacity plan: extrapolated spend + seasonal profile."""
    from rsis.seasons import current_season
    daily = cost_daily(workspace)
    avg = sum(daily) / len(daily) if daily else 0.0
    trend = daily[-1] - daily[0] if len(daily) > 1 else 0.0
    projected = max(0.0, avg + trend / max(1, len(daily)) * PLAN_HORIZON_DAYS)
    season = current_season(workspace)
    season_name = season.get("season", "sprint") if isinstance(season, dict) else "sprint"
    mode = {"sprint": "sprint", "coast": "coast", "pause": "pause"}.get(
        season_name, "coast")
    p = {
        "horizon_days": PLAN_HORIZON_DAYS,
        "daily_avg": round(avg, 6),
        "projected_90d": round(projected, 6),
        "season": season_name,
        "planned_mode": mode,
        "generated": now_ts(),
    }
    save = Path(workspace) / "rack" / "capacity" / "plan.json"
    save.parent.mkdir(parents=True, exist_ok=True)
    save.write_text(json.dumps(p, indent=1, sort_keys=True), encoding="utf-8")
    emit(workspace, "capacity_plan", horizon=PLAN_HORIZON_DAYS,
         projected=round(projected, 6), mode=mode)
    return p


def sustainability(workspace: Path) -> dict:
    """Sustainability accounting from ledgers."""
    costs = read_jsonl(Path(workspace) / ".rsis" / "costs.jsonl")
    total = sum(float(c.get("cost", 0.0)) for c in costs)
    budget = load_json(Path(workspace) / ".rsis" / "budgets.json")
    ceiling = budget.get("ceiling_usd", 0.0)
    s = {
        "total_spend": round(total, 6),
        "ceiling_usd": ceiling,
        "pct_of_ceiling": round(total / ceiling * 100, 2) if ceiling else None,
        "energy_mode": None,
        "storage_kb": 0,
    }
    try:
        from rsis.seasons import energy_mode
        s["energy_mode"] = energy_mode(workspace)
    except Exception:
        pass
    telemetry = Path(workspace) / ".rsis" / "telemetry"
    if telemetry.is_dir():
        s["storage_kb"] = sum(f.stat().st_size for f in telemetry.rglob("*")
                              if f.is_file()) // 1024
    emit(workspace, "capacity_sustainability", total=round(total, 6),
         mode=s["energy_mode"])
    return s


def degradation_ladder(workspace: Path, pressure: int = 1) -> dict:
    """What stays on at each pressure level (1..4)."""
    pressure = max(1, min(4, int(pressure)))
    shed = set(SHED_AT.get(pressure, ()))
    on = [c for c in LADDER if c not in shed]
    d = {"pressure": pressure, "shed": sorted(shed), "always_on": on,
         "ts": now_ts()}
    emit(workspace, "capacity_degraded", pressure=pressure, shed=list(shed))
    return d


def status(workspace: Path) -> dict:
    return {"plan": load_json(Path(workspace) / "rack" / "capacity" / "plan.json"),
            "sustainability": sustainability(workspace)}
