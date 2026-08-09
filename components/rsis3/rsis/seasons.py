"""Long-horizon autonomy — seasonal goals, energy scheduling, self-repair.

Phase 15 (Sequel III): Phase 5's *bounded* autonomy extends into a
persistent lifecycle. Nothing here introduces new autonomy — it extends
what already exists:

- **Seasonal goal rotation**: the goal stack rotates through domain/tier
  seasons on a policy-defined cadence (``policy.json`` →
  ``season_rotation``), so L2 keeps finding new work instead of repeating
  plateaued patterns.
- **Energy-aware scheduling**: the daemon adapts cadence and LLM use to
  cost budgets (Phase 8) and forecast (Phase 10) — sprint during
  improvement phases, coast at plateau, pause under budget pressure.
- **Self-repair of configuration**: policy violations, broken state files
  and stale locks trigger defined recovery procedures (extending
  ``--supervise-bridge`` to the whole stack); every recovery is logged as
  an incident to ``rack/incidents.jsonl``.
- **Quarterly review loop**: a scheduled review synthesizes the quarter
  (nightlies, audits, forecasts, federation) into a policy-revision
  proposal staged for human approval — the only required human touchpoint.
"""

from __future__ import annotations

import json
import logging
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_DOMAINS = [
    "output", "communication", "envelopes", "bridge",
    "memory", "verification", "governance",
]
DEFAULT_ROTATION_DAYS = 7

#: energy mode → (interval factor, l2 budget factor)
ENERGY_MODES = {
    "sprint": (1.0, 1.0),   # improving forecast: full cadence + budget
    "coast": (1.3, 0.7),    # plateau: slow cadence, trim LLM enrichment
    "idle": (1.6, 0.3),     # declining: minimal cadence, low enrichment
    "pause": (0.0, 0.0),    # budget pressure: hold cycles entirely
}


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def seasons_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "seasons.json"


def incidents_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "incidents.jsonl"


def _season_config(workspace: Path) -> dict:
    from rsis.policy import load_policy
    cfg = load_policy(workspace).get("season_rotation") or {}
    return {
        "rotation_days": int(cfg.get("rotation_days",
                                     DEFAULT_ROTATION_DAYS)),
        "domains": list(cfg.get("domains") or DEFAULT_DOMAINS),
    }


def ensure_seasons(workspace: Path) -> dict:
    path = seasons_path(workspace)
    if not path.is_file():
        cfg = _season_config(workspace)
        state = {
            "season_id": 0,
            "name": cfg["domains"][0],
            "started_at": _now_ts(),
            "rotations": 0,
            "domains": cfg["domains"],
            "rotation_days": cfg["rotation_days"],
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    return load_seasons(workspace)


def load_seasons(workspace: Path) -> dict:
    path = seasons_path(workspace)
    if path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            logger.warning("seasons.json unreadable (%s)", e)
    return {"season_id": 0, "name": "output", "started_at": _now_ts(),
            "rotations": 0, "domains": DEFAULT_DOMAINS,
            "rotation_days": DEFAULT_ROTATION_DAYS}


def current_season(workspace: Path) -> dict:
    return ensure_seasons(workspace)


def rotate(workspace: Path, force: bool = False) -> dict:
    """Advance the season on the policy-defined cadence."""
    state = ensure_seasons(workspace)
    cfg = _season_config(workspace)
    state["rotation_days"] = cfg["rotation_days"]
    state["domains"] = cfg["domains"]
    try:
        started = datetime.fromisoformat(
            str(state["started_at"]).replace("Z", "+00:00"))
    except ValueError:
        started = datetime.now(timezone.utc) - timedelta(days=999)
    if not force and datetime.now(timezone.utc) - started < timedelta(
            days=cfg["rotation_days"]):
        return state
    next_id = (int(state.get("season_id", 0)) + 1) % len(cfg["domains"])
    state["season_id"] = next_id
    state["name"] = cfg["domains"][next_id]
    state["started_at"] = _now_ts()
    state["rotations"] = int(state.get("rotations", 0)) + 1
    seasons_path(workspace).write_text(
        json.dumps(state, indent=2) + "\n", encoding="utf-8")
    _incident(workspace, "season-rotation",
              f"rotated to season {state['name']} "
              f"(rotation {state['rotations']})")
    return state


def season_goals(workspace: Path) -> list[str]:
    """L2 goal seeds for the current season's domain."""
    season = current_season(workspace)
    domain = season["name"]
    return [
        f"advance the {domain} domain — produce visible verifiable output "
        f"for the current season's goal tier",
        f"distill durable {domain} guidance into MyKB syntheses",
        f"find and fix the highest-value gap in the {domain} domain",
    ]


def energy_mode(workspace: Path) -> str:
    """Energy mode from forecast trend + budget pressure (Phase 8/10)."""
    try:
        from rsis.budgets import budget_status
        bs = budget_status(workspace)
        ceiling = float(bs.get("ceiling") or 0.0)
        total = float(bs.get("total") or 0.0)
        per_loop = bs.get("per_loop") or {}
        if (ceiling > 0 and total >= ceiling) or                 any(p.get("hit") for p in per_loop.values()):
            return "pause"
    except Exception:
        pass
    try:
        from rsis.forecast import load_history, _linear_fit
        history = load_history(workspace)[-10:]
        if not history:
            return "coast"
        gens = [float(h.get("generation", i)) for i, h in enumerate(history)]
        fits = [float(h["best_fitness"]) for h in history]
        slope, _ = _linear_fit(gens, fits)
        if slope > 1e-9:
            return "sprint"
        if slope < -1e-9:
            return "idle"
        return "coast"
    except Exception:
        return "coast"


def adaptive_sleep(workspace: Path, base_s: int,
                   min_s: int = 120, max_s: int = 300) -> int:
    """Phase 15 energy-aware cadence: forecast trend + budget pressure."""
    mode = energy_mode(workspace)
    factor, _ = ENERGY_MODES[mode]
    if mode == "pause":
        return min_s  # still poll: budget pressure lifts
    from rsis.forecast import adaptive_interval
    base = adaptive_interval(workspace, int(base_s), min_s=min_s, max_s=max_s)
    return min(max_s, max(min_s, int(base * factor)))


def self_repair(workspace: Path, mykb: Optional[Path] = None) -> list[dict]:
    """Recovery procedures for the whole stack; incidents logged."""
    from rsis.invariants import repair, run_invariants

    incidents: list[dict] = []
    rows = run_invariants(workspace)
    repaired = repair(workspace, rows, mykb=mykb)
    for rid in repaired:
        incidents.append(_incident(workspace, "self-repair",
                                   f"repaired invariant {rid}"))
    # policy violations: direct writes to gated paths trigger an incident
    try:
        from rsis.policy import check_unauthorized_writes
        violations = check_unauthorized_writes(workspace)
        for v in violations:
            incidents.append(_incident(
                workspace, "policy-violation",
                f"unauthorized write to gated path {v}"))
    except Exception as e:
        logger.warning("policy scan failed: %s", e)
    return incidents


def incident(workspace: Path, kind: str, detail: str) -> dict:
    return _incident(workspace, kind, detail)


def _incident(workspace: Path, kind: str, detail: str) -> dict:
    rec = {"ts": _now_ts(), "kind": kind, "detail": detail}
    p = incidents_path(workspace)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")
    return rec


def _quarter_boundaries() -> tuple[datetime, datetime]:
    now = datetime.now(timezone.utc)
    return now - timedelta(days=90), now


def quarterly_review(workspace: Path, mykb: Path,
                     actor: str = "quarterly-review") -> dict:
    """Synthesize the quarter into a policy-revision proposal (Phase 9)."""
    start, end = _quarter_boundaries()

    def _count_lines(path: Path) -> int:
        if not path.is_file():
            return 0
        try:
            return len([l for l in path.read_text(encoding="utf-8")
                        .splitlines() if l.strip()])
        except OSError:
            return 0

    nightlies = list((Path(mykb) / "wiki" / "syntheses").glob(
        "rsis3-daily-summary-*.md")) if Path(mykb).exists() else []
    quarter_nightlies = 0
    for f in nightlies:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", f.name)
        if m:
            try:
                d = datetime.fromisoformat(m.group(1) + "T00:00:00+00:00")
                if start <= d < end:
                    quarter_nightlies += 1
            except ValueError:
                continue
    audits = _count_lines(Path(workspace) / ".rsis" / "audit.jsonl")
    forecasts = _count_lines(Path(workspace) / "rack" / "forecasts" /
                             "forecasts.jsonl")
    federation = _count_lines(Path(workspace) / "rack" / "federation" /
                               "ledger.jsonl")
    incidents = _count_lines(incidents_path(workspace))
    body = (f"Quarterly review ({start.date()}..{end.date()}): "
            f"{quarter_nightlies} nightlies, {audits} audit entries, "
            f"{forecasts} forecasts, {federation} federation ops, "
            f"{incidents} incidents.")
    # Stage a policy-revision proposal for human approval (Phase 9).
    from rsis.policy import stage_candidate
    proposal = stage_candidate(
        workspace, {
            "description": "Quarterly policy review — revise season cadence "
                           "and capability bounds",
            "goal": body,
            "target_files": ["rack/policy.json"],
            "diff_or_code": body,
            "rationale": body,
        }, reason="quarterly-review", actor=actor)
    return {"proposal_id": proposal["id"], "summary": body,
            "nightlies": quarter_nightlies, "audits": audits,
            "forecasts": forecasts, "federation_ops": federation,
            "incidents": incidents}


def main(workspace: Path, mykb: Path, action: str = "status",
         force: bool = False, json_out: bool = False) -> int:
    if action == "status":
        s = current_season(workspace)
        mode = energy_mode(workspace)
        if json_out:
            print(json.dumps({"season": s, "energy_mode": mode}))
            return 0
        print(f"  season: {s['name']} (rotation {s['season_id']}, "
              f"rotated {s['rotations']}x, since {s['started_at']})")
        print(f"  energy mode: {mode}")
        return 0
    if action == "rotate":
        s = rotate(workspace, force=force)
        print(f"  ✓ season: {s['name']} (rotation {s['season_id']}, "
              f"total {s['rotations']})")
        return 0
    if action == "repair":
        incidents = self_repair(workspace, mykb)
        print(f"  ✓ self-repair: {len(incidents)} incident(s) logged "
              f"({[i['kind'] for i in incidents]})")
        return 0
    if action == "review":
        r = quarterly_review(workspace, mykb)
        print(f"  ✓ quarterly review → approval {r['proposal_id']}")
        print(f"    {r['summary']}")
        return 0
    print(f"  ✗ unknown seasons action {action!r}")
    return 2


if __name__ == "__main__":
    import sys
    sys.exit(main(Path(".").resolve(), Path("../mykb").resolve(),
                  sys.argv[1] if len(sys.argv) > 1 else "status"))
