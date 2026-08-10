"""Failure understanding — root-cause corpus, clustering, near-misses.

Phase 48 (Sequel X): every incident gains a structured root-cause record
— symptoms, triggers, context, fix, verification — forming a searchable
failure corpus; incidents cluster by root cause across generations (35)
and populations (43); recurring clusters trigger prevention proposals;
telemetry records near-misses as first-class data.
"""

from __future__ import annotations

import json
import logging
import re
from collections import Counter
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
)

logger = logging.getLogger(__name__)


def corpus_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "failures" / "corpus.jsonl"


def nearmiss_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "failures" / "nearmiss.jsonl"


def _load_incidents(workspace: Path) -> list[dict]:
    return read_jsonl(Path(workspace) / "rack" / "incidents.jsonl")


def archive(workspace: Path, incident_id: str, root_cause: str,
            trigger: str, context: str, fix: str,
            verification: str = "verified") -> dict:
    """Archive one incident as a structured root-cause record."""
    ws = Path(workspace)
    ensure_rack(ws, "failures")
    rec = {"incident_id": incident_id, "root_cause": root_cause,
           "trigger": trigger, "context": context[:400], "fix": fix,
           "verification": verification, "ts": now_ts()}
    append_jsonl(corpus_path(ws), rec)
    emit(ws, "failure_archived", incident=incident_id,
         root_cause=root_cause[:40])
    return rec


def cluster(workspace: Path, threshold: float = 0.6) -> dict:
    """Cluster incidents by root-cause text similarity (word overlap)."""
    recs = read_jsonl(corpus_path(ws := workspace))
    by_id = {r.get("incident_id"): r for r in recs}
    clusters: list[list[str]] = []
    for rec in recs:
        words = set(re.findall(r"[a-z]+", rec.get("root_cause", "").lower()))
        placed = False
        for cluster in clusters:
            rep_rec = by_id.get(cluster[0]) or {}
            rep = set(re.findall(r"[a-z]+",
                                 rep_rec.get("root_cause", "").lower()))
            overlap = len(words & rep) / max(1, min(len(words), len(rep)))
            if overlap >= threshold:
                cluster.append(rec["incident_id"])
                placed = True
                break
        if not placed:
            clusters.append([rec["incident_id"]])
    recurring = [c for c in clusters if len(c) >= 2]
    result = {"clusters": len(clusters), "recurring": len(recurring),
              "recurring_ids": [c[0] for c in recurring]}
    save_json(Path(ws) / "rack" / "failures" / "clusters.json", result)
    emit(ws, "failure_clustered", clusters=len(clusters),
         recurring=len(recurring))
    return result


def prevention_proposal(workspace: Path, root_cause: str,
                        rationale: str) -> dict:
    """Stage a prevention proposal through the Phase 9/26 gates."""
    ws = Path(workspace)
    from rsis.goals import propose
    return propose(ws, f"Prevent recurrence: {root_cause[:60]}",
                   rationale, expected_value="reliability",
                   source="failure-cluster", proposer="system")


def record_nearmiss(workspace: Path, component: str, detail: str) -> dict:
    """Record a near-miss (recovered automatically, close to failure)."""
    ws = Path(workspace)
    ensure_rack(ws, "failures")
    rec = {"component": component, "detail": detail, "ts": now_ts()}
    append_jsonl(nearmiss_path(ws), rec)
    emit(ws, "nearmiss_recorded", component=component)
    return rec


def status(workspace: Path) -> dict:
    return {"corpus": len(read_jsonl(corpus_path(ws := workspace))),
            "nearmisses": len(read_jsonl(nearmiss_path(ws)))}
