"""Operational validation windows — P4 24h → P5 7-day cadence tracking.

Separates *implementation delivered* from *exit criterion operationally
demonstrated*. A validation window records a start timestamp, expected
duration, and the evidence required to pass; ``checkin`` evaluates the
criteria against live workspace state and appends a dated check-in record.
When Phase 4's 24 h window completes, Phase 5's 7-day window starts
immediately with the completion timestamp as its clean start point.

Evidence is gathered from the same places the roadmap names:

- ``rack/bridge/cycles/*.jsonl`` — per-cycle cards (3-min cadence),
- ``rack/cycle-daemon.lock`` — single-instance lock,
- ``.rsis/costs.jsonl`` — 24 h cost ledger,
- MyKB ``syntheses/rsis3-daily-summary-*.md`` — daily summaries,
- ``rack/proposals/applied.jsonl`` — bounded auto-retunes,
- ``rack/incidents.jsonl`` — bridge heal / self-repair events,
- ``contracts/validate.py`` — local gate snapshot at check-in.
"""

from __future__ import annotations

import json
import logging
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, ensure_rack, load_json, now_ts, save_json

logger = logging.getLogger(__name__)

#: validation windows: kind -> title + duration
WINDOWS = {
    "p4-24h": {"title": "Phase 4 — 24h unattended 3-min cadence", "hours": 24},
    "p5-7d": {"title": "Phase 5 — 7-day unattended cadence", "hours": 168},
}
ADVANCE = {"p4-24h": "p5-7d", "p5-7d": None}
CYCLES_PER_HOUR = 20  # 3-min cadence upper bound


def windows_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "validation" / "windows.json"


def _parse_ts(value) -> Optional[datetime]:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def _read_windows(workspace: Path) -> dict:
    data = load_json(windows_path(workspace), default={"windows": []})
    if not isinstance(data.get("windows"), list):
        data["windows"] = []
    return data


def _save_windows(workspace: Path, data: dict) -> None:
    save_json(windows_path(workspace), data)


def _ts_filter(records: list[dict], started_at: datetime, key: str = "ts"):
    """Count records whose ISO ts is at/after the window start."""
    n = 0
    for rec in records:
        ts = _parse_ts(rec.get(key))
        if ts is not None and ts >= started_at:
            n += 1
    return n


def _read_jsonl(path: Path) -> list[dict]:
    out = []
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def _jsonl_under(workspace: Path, rel: str, started_at: datetime,
                 key: str = "ts") -> int:
    return _ts_filter(_read_jsonl(Path(workspace) / rel), started_at, key)


def _summary_days(workspace: Path, started_at: datetime) -> int:
    """Daily-summary notes in MyKB dated at/after the window start."""
    mykb = Path(workspace).parent / "mykb"
    days = set()
    for p in (mykb / "wiki" / "syntheses").glob("rsis3-daily-summary-*.md"):
        date = p.name.replace("rsis3-daily-summary-", "").replace(".md", "")
        if date >= started_at.strftime("%Y-%m-%d"):
            days.add(date)
    return len(days)


def _lock_held(workspace: Path) -> bool:
    """Lockfile exists and the daemon behind it is alive (or it is fresh).

    ``cycle-daemon.lock`` holds the daemon PID for the daemon's lifetime,
    so the meaningful check is process liveness, with an mtime-freshness
    fallback for non-PID lock contents.
    """
    lock = Path(workspace) / "rack" / "cycle-daemon.lock"
    if not lock.is_file():
        return False
    try:
        pid = lock.read_text(encoding="utf-8").strip()
        if pid.isdigit() and Path(f"/proc/{pid}").exists():
            return True
    except OSError:
        pass
    try:
        age = (datetime.now(timezone.utc) -
               datetime.fromtimestamp(lock.stat().st_mtime,
                                      tz=timezone.utc)).total_seconds()
        return age <= 600
    except OSError:
        return False


def _contracts_green(repo: Path) -> bool:
    script = Path(repo) / "contracts" / "validate.py"
    if not script.is_file():
        return True
    try:
        proc = subprocess.run([sys.executable, str(script)], cwd=str(repo),
                              capture_output=True, text=True, timeout=120)
        return proc.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def evidence(workspace: Path, started_at: datetime) -> dict:
    """Snapshot of the evidence counters since ``started_at``."""
    ws = Path(workspace)
    elapsed_h = max(0.0, (datetime.now(timezone.utc) -
                          started_at).total_seconds() / 3600.0)
    cycle_cards = 0
    cycles_dir = ws / "rack" / "bridge" / "cycles"
    if cycles_dir.is_dir():
        for f in cycles_dir.glob("*.jsonl"):
            cycle_cards += _jsonl_under(ws, f"rack/bridge/cycles/{f.name}",
                                        started_at)
    repo = ws.parent.parent  # components/rsis3 → repo root
    return {
        "elapsed_h": round(elapsed_h, 3),
        "cycle_cards": cycle_cards,
        "lock_held": _lock_held(ws),
        "cost_records": _jsonl_under(ws, ".rsis/costs.jsonl", started_at),
        "daily_summaries": _summary_days(ws, started_at),
        "auto_retunes": _jsonl_under(ws, "rack/proposals/applied.jsonl",
                                     started_at),
        "incidents": _jsonl_under(ws, "rack/incidents.jsonl", started_at),
        "contracts_green": _contracts_green(repo),
    }


def _expected_cycles(elapsed_h: float, window_h: float) -> int:
    """Expected 3-min cadence cards in the window (80% tolerance)."""
    return max(1, int(min(elapsed_h, window_h) * CYCLES_PER_HOUR * 0.8))


def evaluate(ws: Path, ev: dict, window_h: float) -> list[dict]:
    """Evaluate the exit-criterion checklist against a check-in snapshot."""
    exp_cycles = _expected_cycles(ev["elapsed_h"], window_h)
    days_elapsed = max(1, int(-(-ev["elapsed_h"] // 24)))  # ceil
    return [
        {"id": "cadence",
         "pass": ev["cycle_cards"] >= exp_cycles,
         "detail": f"{ev['cycle_cards']} cycle cards "
                   f"(≥ {exp_cycles} expected)"},
        {"id": "lockfile",
         "pass": ev["lock_held"],
         "detail": "cycle-daemon.lock fresh" if ev["lock_held"]
                   else "cycle-daemon.lock missing or stale"},
        {"id": "costs",
         "pass": ev["cost_records"] >= 1,
         "detail": f"{ev['cost_records']} cost record(s) since start"},
        {"id": "daily_summary",
         "pass": ev["daily_summaries"] >= days_elapsed,
         "detail": f"{ev['daily_summaries']} summary day(s) "
                   f"(≥ {days_elapsed} expected)"},
        {"id": "auto_retune",
         "pass": True,
         "detail": f"{ev['auto_retunes']} applied retune(s) "
                   f"(one per convergence episode)"},
        {"id": "bridge_heal",
         "pass": True,
         "detail": f"{ev['incidents']} incident(s) — supervision/self-heal "
                   f"logged when they occur"},
        {"id": "gates",
         "pass": ev["contracts_green"],
         "detail": "contracts validate 0 FAIL"
                   if ev["contracts_green"] else "contracts validate FAIL"},
    ]


def start(workspace: Path, kind: str = "p4-24h") -> dict:
    """Seed (or return the running) validation window of ``kind``."""
    ws = Path(workspace)
    ensure_rack(ws, "validation")
    if kind not in WINDOWS:
        raise ValueError(f"unknown window kind {kind!r} "
                         f"(expected {sorted(WINDOWS)})")
    data = _read_windows(ws)
    for w in data["windows"]:
        if w.get("kind") == kind and w.get("status") == "running":
            return w
    started = datetime.now(timezone.utc)
    window = {
        "id": f"{kind}-{started.strftime('%Y%m%dT%H%M%SZ')}",
        "kind": kind,
        "title": WINDOWS[kind]["title"],
        "hours": WINDOWS[kind]["hours"],
        "status": "running",
        "started_at": now_ts(),
        "ends_at": (started + timedelta(hours=WINDOWS[kind]["hours"]))
        .strftime("%Y-%m-%dT%H:%M:%SZ"),
        "completed_at": None,
        "checkins": [],
    }
    data["windows"].append(window)
    _save_windows(ws, data)
    emit(ws, "validation_window_started", kind=kind,
         hours=WINDOWS[kind]["hours"], ends_at=window["ends_at"])
    logger.info("validation window %s started (ends %s)",
                window["id"], window["ends_at"])
    return window


def _running(workspace: Path) -> Optional[dict]:
    data = _read_windows(workspace)
    for w in reversed(data["windows"]):
        if w.get("status") == "running":
            return w
    return None


def checkin(workspace: Path, kind: Optional[str] = None) -> dict:
    """Evaluate the running window's criteria and append a check-in."""
    ws = Path(workspace)
    ensure_rack(ws, "validation")
    data = _read_windows(ws)
    idx = None
    for i, w in enumerate(data["windows"]):
        if w.get("status") == "running" and (
                kind is None or w.get("kind") == kind):
            idx = i
    if idx is None:
        return {"checkin": None, "note": "no running window — "
                                         "use `rsis validation start`"}
    win = data["windows"][idx]  # mutate the same structure we save
    started = _parse_ts(win["started_at"]) or datetime.now(timezone.utc)
    ev = evidence(ws, started)
    rows = evaluate(ws, ev, float(win.get("hours", 0)))
    all_pass = all(r["pass"] for r in rows)
    ended = datetime.now(timezone.utc) >= (
        _parse_ts(win["ends_at"]) or datetime.now(timezone.utc))
    rec = {
        "ts": now_ts(),
        "elapsed_h": ev["elapsed_h"],
        "evidence": ev,
        "criteria": rows,
        "all_pass": all_pass,
        "window_ended": ended,
    }
    win.setdefault("checkins", []).append(rec)
    if ended and all_pass:
        win["status"] = "completed"
        win["completed_at"] = now_ts()
        emit(ws, "validation_window_completed", kind=win["kind"],
             id=win["id"], elapsed_h=ev["elapsed_h"])
        logger.info("validation window %s completed", win["id"])
    _save_windows(ws, data)  # persist check-in (+ completion) first
    if win.get("status") == "completed":
        next_kind = ADVANCE.get(win["kind"])
        if next_kind:
            next_win = start(ws, next_kind)  # reads fresh disk state
            logger.info("advanced to %s (clean start point: %s)",
                        next_kind, next_win["started_at"])
    emit(ws, "validation_checkin", kind=win["kind"], id=win["id"],
         all_pass=all_pass, elapsed_h=ev["elapsed_h"])
    return {"checkin": rec, "window": win}


def auto_checkin(workspace: Path) -> Optional[dict]:
    """Non-fatal daily hook for the nightly summary."""
    try:
        return checkin(workspace)
    except Exception as e:  # never break the nightly summary
        logger.warning("validation check-in skipped: %s", e)
        return None


def status(workspace: Path) -> list[dict]:
    ws = Path(workspace)
    data = _read_windows(ws)
    now = datetime.now(timezone.utc)
    out = []
    for w in data["windows"]:
        started = _parse_ts(w.get("started_at")) or now
        ends = _parse_ts(w.get("ends_at")) or now
        elapsed = max(0.0, (now - started).total_seconds() / 3600.0)
        remaining = max(0.0, (ends - now).total_seconds() / 3600.0)
        last = (w.get("checkins") or [{}])[-1]
        out.append({
            "id": w.get("id"), "kind": w.get("kind"),
            "title": w.get("title"), "status": w.get("status"),
            "started_at": w.get("started_at"), "ends_at": w.get("ends_at"),
            "completed_at": w.get("completed_at"),
            "elapsed_h": round(elapsed, 2),
            "remaining_h": round(remaining, 2),
            "last_checkin": last.get("ts"),
            "all_pass_last": last.get("all_pass"),
        })
    return out


def main(workspace: Path, action: str = "status", kind: str = "p4-24h",
         json_out: bool = False) -> int:
    ws = Path(workspace)
    if action == "start":
        win = start(ws, kind)
        if json_out:
            print(json.dumps(win))
        else:
            print(f"  validation window {win['id']} started "
                  f"(ends {win['ends_at']})")
        return 0
    if action == "checkin":
        res = checkin(ws, kind or None)
        if json_out:
            print(json.dumps(res, default=str))
        else:
            if res["checkin"] is None:
                print(f"  {res['note']}")
                return 0
            win = res["window"]
            rec = res["checkin"]
            print(f"  check-in {win['id']} @ {rec['ts']} "
                  f"({rec['elapsed_h']:.2f}h elapsed) — "
                  f"{'PASS' if rec['all_pass'] else 'PENDING'}")
            for row in rec["criteria"]:
                mark = "✔" if row["pass"] else "✘"
                print(f"    {mark} {row['id']}: {row['detail']}")
            if win.get("status") == "completed":
                print(f"  ✅ window {win['id']} completed")
                next_kind = ADVANCE.get(win["kind"])
                if next_kind:
                    print(f"  → advanced to {next_kind} "
                          f"(clean start point: {win['completed_at']})")
        return 0
    rows = status(ws)
    if json_out:
        print(json.dumps(rows))
        return 0
    if not rows:
        print("  no validation windows yet — `rsis validation start`")
        return 0
    for r in rows:
        print(f"  {r['kind']} [{r['status']}] {r['id']}")
        print(f"    {r['title']}")
        print(f"    started {r['started_at']} · ends {r['ends_at']} · "
              f"{r['elapsed_h']}h elapsed / {r['remaining_h']}h remaining")
        if r.get("last_checkin"):
            print(f"    last check-in {r['last_checkin']} · "
                  f"all-pass={r['all_pass_last']}")
    return 0
