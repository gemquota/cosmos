"""Anomaly policy — scan telemetry for regressions (Phase 8).

Sibling of the convergence monitor: instead of fitness plateaus, it scans
the telemetry window for operational regressions — success-rate drops,
duration spikes, and missing telemetry — and files MyKB backlog items.
Also owns telemetry retention (rolling window with compressed archives).
"""

from __future__ import annotations

import json
import logging
import shutil
import tarfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

LOOPS = ("l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9")


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_events(telemetry_dir: Path, limit: int = 100000) -> list[dict]:
    events = []
    if not telemetry_dir.is_dir():
        return events
    for f in sorted(telemetry_dir.glob("*.jsonl")):
        try:
            for line in f.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        except OSError:
            continue
        if len(events) >= limit:
            break
    return events


def scan(workspace: Path, noop_threshold: int = 8,
         min_events: int = 40) -> list[dict]:
    """Detect operational regressions in the telemetry window."""
    tel = Path(workspace) / ".rsis" / "telemetry"
    events = read_events(tel)
    anomalies = []
    starts: dict[str, int] = {}
    completes: dict[str, int] = {}
    durations: dict[str, list[float]] = {}
    for e in events:
        etype = e.get("type", "")
        meta = e.get("metadata") or {}
        loop = meta.get("loop") or next((l for l in LOOPS
                                         if etype.startswith(l)), None)
        if not loop:
            continue
        if etype.endswith("_start"):
            starts[loop] = starts.get(loop, 0) + 1
        elif etype.endswith("_complete"):
            completes[loop] = completes.get(loop, 0) + 1
            if etype.startswith(loop):
                durations.setdefault(loop, []).append(
                    float(meta.get("duration_s") or meta.get("elapsed_s") or 0))
    if not events:
        anomalies.append({"loop": "*", "kind": "missing_telemetry",
                          "severity": "high",
                          "detail": "no telemetry events in window"})
        return anomalies

    for loop in LOOPS:
        s, c = starts.get(loop, 0), completes.get(loop, 0)
        if s > 0 and c == 0:
            anomalies.append({"loop": loop, "kind": "missing_telemetry",
                              "severity": "high",
                              "detail": f"{s} start(s) without completion"})
        elif c > 0 and c < s:
            anomalies.append({"loop": loop, "kind": "success_drop",
                              "severity": "medium",
                              "detail": f"completion rate {c}/{s}"})
        elif s == 0 and len(events) >= min_events:
            anomalies.append({"loop": loop, "kind": "no_activity",
                              "severity": "low",
                              "detail": "no start events in window"})
        ds = durations.get(loop, [])
        if len(ds) >= 5:
            mean = sum(ds) / len(ds)
            spike = max(ds)
            if spike > mean * 3 and spike > 10:
                anomalies.append({"loop": loop, "kind": "duration_spike",
                                  "severity": "medium",
                                  "detail": f"max {spike:.1f}s vs mean {mean:.1f}s"})
    return anomalies


def file_backlog(mykb: Path, anomalies: list[dict]) -> Optional[Path]:
    """Mirror detected anomalies into the MyKB backlog."""
    if not anomalies:
        return None
    ts = _now_ts()
    date_part = ts[:10]
    out = mykb / "wiki" / "backlog"
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"anomalies-{date_part}.md"
    if path.exists():
        return path
    body = "\n".join([
        f"# Operational anomalies — {date_part}",
        "",
        f"- Detected: {ts}",
        *[f"- {a['loop']} {a['kind']} ({a['severity']}): {a['detail']}"
          for a in anomalies],
        "- Source: rsis anomalies",
    ])
    front = {
        "type": "backlog",
        "title": f"Operational anomalies — {date_part}",
        "description": f"{len(anomalies)} anomaly(ies)",
        "tags": ["backlog", "anomalies"],
        "timestamp": ts,
        "status": "open",
        "source": "anomalies",
    }
    path.write_text(
        "---\n" + "\n".join(f'{k}: "{v}"' for k, v in front.items()) + "\n---\n\n" + body + "\n",
        encoding="utf-8")
    return path


def prune(workspace: Path, retention_days: int = 7) -> dict:
    """Archive telemetry older than the retention window into rack/archive/."""
    tel = Path(workspace) / ".rsis" / "telemetry"
    archive = Path(workspace) / "rack" / "archive"
    now = datetime.now(timezone.utc).timestamp()
    cutoff = now - int(retention_days) * 86400
    old = [f for f in tel.glob("*.jsonl")
           if f.stat().st_mtime < cutoff] if tel.is_dir() else []
    archived = 0
    if old:
        archive.mkdir(parents=True, exist_ok=True)
        day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        tarball = archive / f"telemetry-{day}.tar.gz"
        with tarfile.open(tarball, "w:gz") as tf:
            for f in old:
                try:
                    tf.add(str(f), arcname=f.name)
                    f.unlink()
                    archived += 1
                except OSError as e:
                    logger.warning("prune failed for %s: %s", f, e)
    return {"archived": archived, "retention_days": retention_days,
            "archive": str(archive)}


def main(workspace: Path, mykb: Path, prune_days: int = 0,
         file_backlogs: bool = True, json_out: bool = False) -> int:
    anomalies = scan(workspace)
    result = {"ts": _now_ts(), "anomalies": anomalies}
    if file_backlogs:
        path = file_backlog(mykb, anomalies)
        result["backlog_note"] = str(path) if path else None
    if prune_days and prune_days > 0:
        result["prune"] = prune(workspace, prune_days)
    print(f"  anomalies: {len(anomalies)} "
          f"({sum(1 for a in anomalies if a['severity'] == 'high')} high)")
    for a in anomalies:
        print(f"  - {a['loop']:<4} {a['kind']:<18} {a['severity']:<6} {a['detail']}")
    if json_out:
        print(json.dumps(result))
    return 1 if any(a["severity"] in ("high", "medium") for a in anomalies) else 0
