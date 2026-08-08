#!/usr/bin/env python3
"""Aggregate RRP v2 pulse files into the cumulative dashboard payload.

Reads ``rack/pulses/pulse-*.json`` (current RRP v2 schema) and writes
``rack/pulses/dashboard-data.json`` — the cumulative payload consumed by
``dashboard/index.html`` and by ``gen-static-data.py`` (ecosystem
telemetry, contract-valid ints). Mirrors the legacy dashboard schema
(pulses / goals / score_history / telemetry_aggregates / summary).

Usage:
    python rack/build_dashboard_data.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

PULSES_DIR = Path(__file__).parent / "pulses"


def _pulse_num(path: Path) -> int:
    m = re.search(r"pulse-(\d+)\.json$", path.name)
    return int(m.group(1)) if m else 0


def build() -> dict:
    """Return the cumulative dashboard payload from the current pulses."""
    pulses = sorted(PULSES_DIR.glob("pulse-*.json"), key=_pulse_num)
    goals: list[dict] = []
    pulses_out: list[dict] = []
    score_history: dict[str, dict] = {}
    telemetry_aggregates: dict[str, dict] = {}
    cd: dict[str, dict] = {}

    for pf in pulses:
        p = json.loads(pf.read_text())
        pid = p.get("pulse") or f"{_pulse_num(pf):03d}"
        gs = p.get("goals", [])
        approved = impl = 0
        confs: list[float] = []
        for g in gs:
            ev = g.get("rrp_evaluation") or {}
            dec = ev.get("decision", "FAIL")
            conf = float(ev.get("confidence") or 0.0)
            confs.append(conf)
            gt = g.get("type", "improvement")
            if dec == "PASS":
                approved += 1
                if gt == "implementation":
                    impl += 1
            ref = g.get("rrp_refinement") or {}
            constraints = ref.get("constraints") or {}
            locked = set(ref.get("locked") or [])
            for name, state in constraints.items():
                entry = cd.setdefault(str(name), {"freq": 0, "locked": 0})
                entry["freq"] += 1
                if state == "LOCKED" or name in locked:
                    entry["locked"] += 1
            goals.append({
                "p": pid,
                "d": g.get("description", ""),
                "dec": dec,
                "conf": round(conf, 3),
                "file": g.get("file", ""),
                "func": g.get("function", ""),
                "type": gt,
                "conversation": [],
                "constraints": constraints,
                "telemetry": ev.get("rrp_telemetry") or {},
                "contradictions": [],
            })

        agg = p.get("rrp_telemetry_aggregate") or {}
        sm = p.get("summary") or {}
        pulses_out.append({
            "id": pid,
            "ts_start": p.get("timestamp_start", ""),
            "ts_end": p.get("timestamp_end", ""),
            "goals_count": len(gs),
            "approved": approved,
            "duration": sm.get("duration_seconds", 0),
            "scores": {},
            "type": p.get("type", "rrp_v2_full"),
            "num_goals": len(gs),
            "implementation_count": impl,
            "telemetry": agg,
            "avg_confidence": round(sum(confs) / max(len(confs), 1), 3),
        })
        score_history[pid] = {}
        telemetry_aggregates[pid] = agg

    tot = len(goals)
    passed = sum(1 for g in goals if g["dec"] == "PASS")
    return {
        "pulses": pulses_out,
        "goals": goals,
        "score_history": score_history,
        "telemetry_aggregates": telemetry_aggregates,
        "summary": {
            "tot": tot,
            "pass": passed,
            "hold": sum(1 for g in goals if g["dec"] == "HOLD"),
            "fail": sum(1 for g in goals if g["dec"] == "FAIL"),
            "impl_count": sum(p["implementation_count"] for p in pulses_out),
            "ca": round(passed / tot, 3) if tot else 0.0,
            "pulse_count": len(pulses_out),
            "cd": cd,
        },
    }


if __name__ == "__main__":
    out = build()
    (PULSES_DIR / "dashboard-data.json").write_text(json.dumps(out, indent=2))
    s = out["summary"]
    print(f"dashboard-data: {s['pulse_count']} pulse(s), {s['tot']} goal(s) "
          f"({s['pass']} PASS / {s['hold']} HOLD / {s['fail']} FAIL)")
