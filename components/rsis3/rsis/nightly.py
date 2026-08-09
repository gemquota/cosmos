"""Nightly summary — aggregate the day's cycles into a MyKB synthesis note.

Runs once per day (CI cron or the cycle daemon) and writes an OKF note
into MyKB syntheses so every day leaves a durable, human-readable record
(Phase 5 exit criterion: a nightly summary note per day).

Usage:
    python -m rsis nightly-summary [--date YYYY-MM-DD] [--json]
"""

from __future__ import annotations

import json
import logging
import os
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

from rsis.forecast import predict as forecast_predict
from rsis.forecast import quality as forecast_quality

logger = logging.getLogger(__name__)

LOOP_LABELS = ("l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9")


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _day_bounds(day: str) -> tuple[datetime, datetime]:
    start = datetime.fromisoformat(day + "T00:00:00+00:00")
    return start, start + timedelta(days=1)


def read_telemetry(telemetry_dir: Path) -> list[dict]:
    events = []
    if not telemetry_dir.is_dir():
        return events
    for f in telemetry_dir.glob("*.jsonl"):
        try:
            for line in f.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    try:
                        events.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
        except OSError:
            continue
    return events


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def summarize_day(workspace: Path, mykb: Path,
                  day: Optional[str] = None) -> dict:
    """Aggregate one UTC day: cycles, health, costs, strategies, KG."""
    day = day or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    start, end = _day_bounds(day)
    events = read_telemetry(workspace / ".rsis" / "telemetry")
    in_day = [e for e in events if start <= _ts(e.get("timestamp")) < end]

    starts: dict[str, int] = {}
    completes: dict[str, int] = {}
    errors: dict[str, int] = {}
    noops = 0
    rc_failures = 0
    for e in in_day:
        t = e.get("type") or ""
        for loop in LOOP_LABELS:
            if t == f"{loop}_start":
                starts[loop] = starts.get(loop, 0) + 1
            elif t == f"{loop}_complete":
                completes[loop] = completes.get(loop, 0) + 1
                if e.get("changed") is False:
                    noops += 1
            elif t == f"{loop}_error":
                errors[loop] = errors.get(loop, 0) + 1
        if "error" in t or (t.startswith("l") and t.endswith("_error")):
            rc_failures += 1

    l3_cycles = completes.get("l3", 0)
    strategies = load_json(workspace / ".rsis" / "strategies.json", {})
    kg = load_json(workspace / ".rsis" / "knowledge_graph.json",
                   {"nodes": [], "edges": []})
    costs = _read_costs(workspace / ".rsis" / "costs.jsonl", start, end)

    git_summary = _git_summary(workspace, start, end)
    summary = {
        "day": day,
        "events": len(in_day),
        "cycles": l3_cycles,
        "loop_starts": starts,
        "loop_completes": completes,
        "loop_errors": errors,
        "noops": noops,
        "rc_failures": rc_failures,
        "strategies": {
            "generation": strategies.get("generation", 0),
            "best_fitness": max((s.get("fitness") or 0 for s in (strategies.get("population") or [])), default=None),
        },
        "kg": {"nodes": len(kg.get("nodes") or []), "edges": len(kg.get("edges") or [])},
        "costs": costs,
        "commits": git_summary,
        "forecast": _day_forecast(workspace),
        "attestation": _day_attestation(workspace),
        "federation": _federation_summary(workspace),
        "incidents": _incident_summary(workspace),
    }
    return summary


def _day_forecast(workspace: Path) -> dict:
    """Phase 10: self-model prediction for the day's summary."""
    fc = forecast_predict(workspace)
    if fc.get("available"):
        fc["quality"] = forecast_quality(workspace)
    return fc


def _day_attestation(workspace: Path) -> dict:
    """Phase 14: attest the day's summary against the invariant set."""
    try:
        from rsis.invariants import attest, run_invariants
        rows = run_invariants(workspace)
        rec = attest(workspace, f"nightly:{datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
                     rows, actor="nightly")
        return {"sha256": rec["sha256"],
                "passed": len([r for r in rows if r["ok"]]),
                "total": len(rows)}
    except Exception as e:
        return {"error": str(e), "passed": 0, "total": 0}


def _federation_summary(workspace: Path) -> dict:
    """Phase 13: today's federation publishes/pulls/merges."""
    path = Path(workspace) / "rack" / "federation" / "ledger.jsonl"
    ops: dict[str, int] = {}
    if not path.is_file():
        return {"ops": ops}
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            if str(rec.get("ts", "")).startswith(today):
                op = rec.get("op", "?")
                ops[op] = ops.get(op, 0) + 1
    except (OSError, json.JSONDecodeError):
        pass
    return {"ops": ops}


def _incident_summary(workspace: Path) -> dict:
    """Phase 15: today's self-repair incidents."""
    path = Path(workspace) / "rack" / "incidents.jsonl"
    kinds: dict[str, int] = {}
    if not path.is_file():
        return {"kinds": kinds}
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            if str(rec.get("ts", "")).startswith(today):
                k = rec.get("kind", "?")
                kinds[k] = kinds.get(k, 0) + 1
    except (OSError, json.JSONDecodeError):
        pass
    return {"kinds": kinds}


def _ts(raw) -> Optional[datetime]:
    if not raw:
        return None
    try:
        return datetime.fromisoformat(str(raw).replace("Z", "+00:00"))
    except ValueError:
        pass
    try:
        return datetime.fromtimestamp(float(raw), tz=timezone.utc)
    except (ValueError, OSError):
        return None


def _read_costs(path: Path, start: datetime, end: datetime) -> dict:
    total_cost = 0.0
    tokens_in = 0
    tokens_out = 0
    traces = 0
    if path.is_file():
        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                ts = _ts(rec.get("ts"))
                if ts is None or not (start <= ts < end):
                    continue
                total_cost += float(rec.get("cost") or 0)
                tokens_in += int(rec.get("tokens_in") or 0)
                tokens_out += int(rec.get("tokens_out") or 0)
                traces += 1
        except OSError:
            pass
    return {"traces": traces, "tokens_in": tokens_in,
            "tokens_out": tokens_out, "cost": round(total_cost, 6)}


def _git_summary(workspace: Path, start: datetime, end: datetime) -> dict:
    try:
        repo = workspace.parent
        proc = subprocess.run(
            ["git", "log", "--since", start.isoformat(), "--until", end.isoformat(),
             "--pretty=format:%h %s", "--no-merges"],
            cwd=str(repo), capture_output=True, text=True, timeout=30)
        lines = [l for l in proc.stdout.splitlines() if l.strip()]
        return {"count": len(lines), "sample": lines[:8]}
    except Exception:
        return {"count": 0, "sample": []}


def write_nightly_note(mykb: Path, summary: dict, ts: Optional[str] = None) -> Optional[Path]:
    """Write the OKF synthesis note (create-only) + log.md entry."""
    day = summary["day"]
    out = mykb / "wiki" / "syntheses"
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"rsis3-daily-summary-{day}.md"
    ts = ts or _now_ts()
    title = f"RSIS3 daily summary — {day}"
    desc = (f"{summary['cycles']} cycle(s), {summary['events']} telemetry events, "
            f"gen {summary['strategies']['generation']} "
            f"(best fitness {summary['strategies']['best_fitness']}), "
            f"KG {summary['kg']['nodes']}n/{summary['kg']['edges']}e")
    body = "\n".join([
        f"# {title}",
        "",
        f"- Cycles (L3 completes): {summary['cycles']}",
        f"- Telemetry events: {summary['events']}",
        f"- Loop completes: {json.dumps(summary['loop_completes'])}",
        f"- Loop errors: {json.dumps(summary['loop_errors']) or 'none'}",
        f"- No-ops (changed=false): {summary['noops']}",
        f"- rc failures: {summary['rc_failures']}",
        f"- Strategies: generation {summary['strategies']['generation']}, "
        f"best fitness {summary['strategies']['best_fitness']}",
        f"- KG: {summary['kg']['nodes']} nodes / {summary['kg']['edges']} edges",
        f"- LLM costs: ${summary['costs']['cost']} "
        f"({summary['costs']['traces']} traces, "
        f"{summary['costs']['tokens_in'] + summary['costs']['tokens_out']} tokens)",
        f"- Commits: {summary['commits']['count']}",
    ])
    if summary["commits"]["sample"]:
        body += "\n\nLatest commits:\n\n" + "\n".join(
            f"- `{c}`" for c in summary["commits"]["sample"])
    if summary.get("forecast"):
        fc = summary["forecast"]
        if fc.get("available"):
            f = fc["fitness"]
            body += (f"\n\nForecast (self-model):\n"
                     f"- Next-cycle best fitness {f['predicted']} "
                     f"(band ±{f['band']}, {f['low']}..{f['high']}) — "
                     f"{fc['trend']}\n"
                     f"- Success rate {fc['success_rate']}, "
                     f"daily cost ${fc['cost_usd']}\n")
        if fc.get("quality"):
            q = fc["quality"]
            body += (f"- Forecast quality: {q['verified']} verified, "
                     f"coverage {q['coverage']} "
                     f"(hits {q['hits']}, misses {q['misses']})\n")
    att = summary.get("attestation")
    if att and att.get("sha256"):
        body += (f"\nAttestation: {att['passed']}/{att['total']} invariants "
                 f"passed, sha256 {att['sha256'][:16]}...\n")
    fed = summary.get("federation")
    if fed and fed.get("ops"):
        body += (f"\nFederation: {json.dumps(fed['ops'])} "
                 f"publish/pull/merge op(s) today\n")
    inc = summary.get("incidents")
    if inc and inc.get("kinds"):
        body += (f"\nIncidents (self-recovered): "
                 f"{json.dumps(inc['kinds'])}\n")
    if path.exists():
        return path
    front = {
        "type": "synthesis",
        "title": title,
        "description": desc,
        "tags": ["rsis3", "daily-summary", "ops"],
        "timestamp": ts,
        "status": "growing",
    }
    path.write_text(
        "---\n" + "\n".join(f'{k}: "{v}"' for k, v in front.items())
        + "\n---\n\n" + body + "\n", encoding="utf-8")
    _append_log(mykb, day, path.name, summary)
    return path


def _append_log(mykb: Path, day: str, note_name: str, summary: dict) -> None:
    log = mykb / "log.md"
    if not log.is_file():
        return
    entry = (f"\n## {day} (RSIS3 nightly summary — automatic)\n"
             f"- {summary['cycles']} cycle(s), {summary['events']} telemetry "
             f"events, gen {summary['strategies']['generation']} "
             f"(best {summary['strategies']['best_fitness']}), "
             f"KG {summary['kg']['nodes']}n/{summary['kg']['edges']}e, "
             f"${summary['costs']['cost']} llm cost, "
             f"{summary['commits']['count']} commits.\n"
             f"- Synthesis: `{note_name}`.\n")
    with log.open("a", encoding="utf-8") as fh:
        fh.write(entry)


def main(workspace: Path, mykb: Path, day: Optional[str] = None,
         json_out: bool = False) -> int:
    summary = summarize_day(workspace, mykb, day)
    path = write_nightly_note(mykb, summary)
    print(f"  ✓ nightly summary for {summary['day']}: "
          f"{summary['cycles']} cycles, {summary['events']} events, "
          f"gen {summary['strategies']['generation']}")
    if path:
        print(f"  note: {path}")
    if json_out:
        print(json.dumps(summary))
    return 0
