"""Swarm coordination & distributed cycles.

Phase 23 (Sequel V): workloads dispatch across the population with
corroborated results.

- ``dispatch`` — a task/candidate goes to trusted peers under a result
  contract (``rack/swarm/dispatch.jsonl``, status pending → accepted →
  verified | failed).
- ``corroborate`` — a candidate's verification is corroborated when two
  or more instances independently agree; confidence (22) updates.
- ``reconcile`` — divergent results resolve deterministically
  (majority + provenance) and every reconciliation is logged.
- Failure containment — a peer that fails mid-dispatch never blocks the
  population: the work re-dispatches or degrades to local verification.
"""

from __future__ import annotations

import json
import logging
from collections import Counter
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, now_ts, read_jsonl, save_json,
)
from rsis.exchange import corroborate

logger = logging.getLogger(__name__)

DISPATCH_STATUS = ("pending", "accepted", "verified", "failed", "redistributed")
CORROBORATION_QUORUM = 2


def dispatch_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "swarm"


def dispatch_path(workspace: Path) -> Path:
    return dispatch_dir(workspace) / "dispatch.jsonl"


def dispatch(workspace: Path, task: dict, peers: list[str]) -> dict:
    """Dispatch a task to trusted peers; returns the dispatch record."""
    ws = Path(workspace)
    ensure_rack(ws, "swarm")
    rec = {
        "id": f"d{len(read_jsonl(dispatch_path(ws)))}",
        "task": task,
        "peers": list(peers),
        "status": "pending",
        "verdicts": {},
        "ts": now_ts(),
    }
    append_jsonl(dispatch_path(ws), rec)
    emit(ws, "swarm_dispatched", dispatch=rec["id"], peers=len(peers))
    return rec


def _update(workspace: Path, dispatch_id: str, **changes) -> Optional[dict]:
    path = dispatch_path(workspace)
    recs = read_jsonl(path)
    for rec in recs:
        if rec.get("id") == dispatch_id:
            rec.update(changes)
            with path.open("w", encoding="utf-8") as fh:
                for r in recs:
                    fh.write(json.dumps(r, sort_keys=True) + "\n")
            return rec
    return None


def accept(workspace: Path, dispatch_id: str, peer: str) -> Optional[dict]:
    return _update(workspace, dispatch_id, **{
        "status": "accepted", "accepted_by": peer, "accepted_at": now_ts()})


def report_verdict(workspace: Path, dispatch_id: str, peer: str,
                   candidate_sha: str, verdict: str,
                   evidence: Optional[dict] = None) -> Optional[dict]:
    """Record a peer verdict; corroborate when the quorum agrees."""
    recs = read_jsonl(dispatch_path(workspace))
    target = next((r for r in recs if r.get("id") == dispatch_id), None)
    if target is None:
        return None
    verdicts = dict(target.get("verdicts", {}))
    verdicts[peer] = {"verdict": verdict, "candidate_sha": candidate_sha,
                      "evidence": evidence or {}, "ts": now_ts()}
    agree = sum(1 for v in verdicts.values() if v.get("verdict") == "pass")
    total = len(verdicts)
    rec = _update(workspace, dispatch_id, verdicts=verdicts)
    if total >= CORROBORATION_QUORUM and agree >= CORROBORATION_QUORUM:
        rec = _update(workspace, dispatch_id, status="verified",
                      corroborated_by=list(verdicts.keys()), reconciled=None)
        corroborate(workspace, candidate_sha, True, provider=peer)
        emit(workspace, "swarm_corroborated", dispatch=dispatch_id,
             candidate_sha=candidate_sha[:12], peers=list(verdicts.keys()))
    elif total >= CORROBORATION_QUORUM:
        rec = reconcile(workspace, dispatch_id, verdicts)
    return rec


def reconcile(workspace: Path, dispatch_id: str,
              verdicts: Optional[dict] = None) -> Optional[dict]:
    """Deterministic divergence resolution: majority + provenance."""
    recs = read_jsonl(dispatch_path(workspace))
    target = next((r for r in recs if r.get("id") == dispatch_id), None)
    if target is None:
        return None
    verdicts = verdicts or target.get("verdicts", {})
    tally = Counter(v.get("verdict") for v in verdicts.values())
    majority = tally.most_common(1)[0][0] if tally else "fail"
    # tie-break by earliest timestamp (provenance)
    if len(tally) > 1 and len({k for k, c in tally.items() if c == max(tally.values())}) > 1:
        earliest = min(verdicts, key=lambda p: verdicts[p].get("ts", ""))
        majority = verdicts[earliest].get("verdict", "fail")
    rec = _update(workspace, dispatch_id, status="verified", verdict=majority,
                  reconciled={"method": "majority+provenance", "tally": dict(tally),
                              "ts": now_ts()})
    append_jsonl(dispatch_path(workspace) if False else
                 Path(workspace) / "rack" / "federation" / "exchange.jsonl",
                 {"type": "reconcile", "dispatch": dispatch_id,
                  "tally": dict(tally), "result": majority, "ts": now_ts()})
    emit(workspace, "swarm_reconciled", dispatch=dispatch_id, result=majority)
    return rec


def fail_peer(workspace: Path, dispatch_id: str, peer: str) -> Optional[dict]:
    """Contain a mid-dispatch peer failure: mark failed + redistribute."""
    recs = read_jsonl(dispatch_path(workspace))
    target = next((r for r in recs if r.get("id") == dispatch_id), None)
    if target is None:
        return None
    remaining = [p for p in target.get("peers", []) if p != peer]
    rec = _update(workspace, dispatch_id, status="failed" if not remaining
                  else "redistributed", peers=remaining, failed_peer=peer)
    if remaining:
        emit(workspace, "swarm_redistributed", dispatch=dispatch_id,
             peers=len(remaining))
    else:
        emit(workspace, "swarm_degraded", dispatch=dispatch_id)
    return rec


def status(workspace: Path) -> dict:
    recs = read_jsonl(dispatch_path(workspace))
    by_status: dict = {}
    for r in recs:
        s = r.get("status", "?")
        by_status[s] = by_status.get(s, 0) + 1
    return {"dispatches": len(recs), "by_status": by_status,
            "verified": by_status.get("verified", 0)}
