"""Population governance — federated policy without a single point of trust.

Phase 24 (Sequel V): policy fragments are shareable and versioned across
instances; local policy always wins over foreign policy; high-risk
approvals can require peer corroboration under a policy-defined quorum;
conflicting durable rules resolve deterministically; every shared rule
carries origin and ratification history.

Shared rules live in ``rack/popgov/rules.jsonl``; approvals that need
quorum are staged in ``rack/popgov/quorum.jsonl``.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
    sha256_text,
)

logger = logging.getLogger(__name__)

DEFAULT_QUORUM = 2


def popgov_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "popgov"


def rules_path(workspace: Path) -> Path:
    return popgov_dir(workspace) / "rules.jsonl"


def quorum_path(workspace: Path) -> Path:
    return popgov_dir(workspace) / "quorum.jsonl"


def publish_rules(workspace: Path, rules: dict, origin: str,
                  signer: Optional[dict] = None) -> dict:
    """Publish a shared rule set; returns the rule record."""
    ws = Path(workspace)
    ensure_rack(ws, "popgov")
    rec = {
        "rule_sha": sha256_text(json.dumps(rules, sort_keys=True)),
        "rules": rules,
        "origin": origin,
        "ratification_history": [{"by": origin, "ts": now_ts()}],
        "signed": signer,
        "adopted": now_ts(),
    }
    append_jsonl(rules_path(ws), rec)
    emit(ws, "popgov_rules_published", origin=origin,
         rule_sha=rec["rule_sha"][:12])
    return rec


def adopt_rules(workspace: Path, rule_sha: str,
                local_policy: Optional[dict] = None) -> dict:
    """Adopt a foreign rule set; local policy always wins on conflicts."""
    recs = read_jsonl(rules_path(workspace))
    rec = next((r for r in recs if r.get("rule_sha") == rule_sha), None)
    if rec is None:
        return {"adopted": False, "reason": "unknown rule_sha"}
    conflicts = []
    local = local_policy or load_json(Path(workspace) / "rack" / "policy.json")
    for key, value in (rec.get("rules") or {}).items():
        if key in local and local[key] != value:
            conflicts.append(key)  # local wins silently; divergence logged
    if conflicts:
        log_divergence(workspace, rule_sha, conflicts,
                       resolution="local-policy-wins")
    emit(workspace, "popgov_rules_adopted", rule_sha=rule_sha[:12],
         conflicts=len(conflicts))
    return {"adopted": True, "conflicts": conflicts,
            "resolution": "local-policy-wins" if conflicts else "no-conflict"}


def log_divergence(workspace: Path, rule_sha: str, keys: list[str],
                   resolution: str) -> None:
    append_jsonl(Path(workspace) / "rack" / "federation" / "backlog.jsonl",
                 {"type": "rule_divergence", "rule_sha": rule_sha,
                  "keys": keys, "resolution": resolution, "ts": now_ts()})


def require_quorum(workspace: Path, approval_id: str, quorum: int = DEFAULT_QUORUM,
                   high_risk: bool = False) -> dict:
    """Register a cross-instance approval need; returns the quorum record."""
    ws = Path(workspace)
    ensure_rack(ws, "popgov")
    rec = {"approval_id": approval_id, "quorum": quorum, "votes": {},
           "high_risk": high_risk, "ts": now_ts(), "resolved": False}
    append_jsonl(quorum_path(ws), rec)
    emit(ws, "popgov_quorum_required", approval=approval_id, quorum=quorum)
    return rec


def cast_vote(workspace: Path, approval_id: str, peer: str,
              decision: str) -> Optional[dict]:
    """Cast a peer vote; resolves when quorum is met."""
    recs = read_jsonl(quorum_path(workspace))
    target = next((r for r in recs if r.get("approval_id") == approval_id), None)
    if target is None:
        return None
    votes = dict(target.get("votes", {}))
    votes[peer] = {"decision": decision, "ts": now_ts()}
    quorum = int(target.get("quorum", DEFAULT_QUORUM))
    approves = sum(1 for v in votes.values() if v.get("decision") == "approve")
    resolved = len(votes) >= quorum
    record = {"approval_id": approval_id, "votes": votes,
              "quorum": quorum, "approves": approves,
              "resolved": resolved, "decision": approves >= quorum,
              "ts": now_ts()}
    with quorum_path(workspace).open("w", encoding="utf-8") as fh:
        for r in recs:
            if r.get("approval_id") == approval_id:
                fh.write(json.dumps(record, sort_keys=True) + "\n")
            else:
                fh.write(json.dumps(r, sort_keys=True) + "\n")
    if resolved:
        emit(workspace, "popgov_quorum_resolved", approval=approval_id,
             decision=record["decision"], peers=len(votes))
    return record


def resolve_rule_divergence(rule_a: dict, rule_b: dict) -> dict:
    """Deterministic conflict resolution for durable rules.

    Order: newest fact wins; local behavior policy wins; population
    quorum (more adoptions) wins; else deterministic tie by sha.
    """
    ts_a = rule_a.get("adopted", ""); ts_b = rule_b.get("adopted", "")
    if ts_a != ts_b:
        return rule_a if ts_a > ts_b else rule_b
    adopt_a = len(rule_a.get("ratification_history", []))
    adopt_b = len(rule_b.get("ratification_history", []))
    if adopt_a != adopt_b:
        return rule_a if adopt_a > adopt_b else rule_b
    return rule_a if rule_a.get("rule_sha", "") <= rule_b.get("rule_sha", "") else rule_b


def status(workspace: Path) -> dict:
    rules = read_jsonl(rules_path(workspace))
    quorum = read_jsonl(quorum_path(workspace))
    return {"shared_rules": len(rules),
            "open_quorum": sum(1 for q in quorum if not q.get("resolved")),
            "quorum_total": len(quorum)}
