"""Inter-population diplomacy — treaties, disputes, trust levels.

Phase 43 (Sequel IX): populations negotiate shared rules and trust
without central authority. Treaties are signed records (Phase 21
identity), versioned like policy (24); conflicting shared rules resolve
through the Phase 24 quorum mechanisms or a policy-defined arbitrator;
peer trust (21) gains treaty-aware levels — allies, peers, observers,
quarantined — each with explicit capability bounds.
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

TREATY_LEVELS = ("allies", "peers", "observers", "quarantined")
#: capability bounds per treaty level
LEVEL_CAPS = {"allies": ("read", "propose", "approve", "dispatch"),
              "peers": ("read", "propose", "dispatch"),
              "observers": ("read",),
              "quarantined": ()}


def diplomacy_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "diplomacy"


def treaties_path(workspace: Path) -> Path:
    return diplomacy_dir(workspace) / "treaties.jsonl"


def sign_treaty(workspace: Path, population: str, terms: dict,
                level: str = "peers", signer: Optional[dict] = None) -> dict:
    """Sign a reciprocity treaty with another population."""
    if level not in TREATY_LEVELS:
        raise ValueError(f"bad level {level!r}")
    ws = Path(workspace)
    ensure_rack(ws, "diplomacy")
    rec = {
        "id": f"t{len(read_jsonl(treaties_path(ws)))}",
        "population": population, "terms": terms, "level": level,
        "capabilities": LEVEL_CAPS[level],
        "signed_by": signer, "status": "active", "ts": now_ts(),
        "sha": "",
    }
    rec["sha"] = sha256_text(json.dumps(
        {"population": population, "terms": terms, "level": level},
        sort_keys=True))
    append_jsonl(treaties_path(ws), rec)
    emit(ws, "treaty_signed", treaty=rec["id"], population=population,
         level=level)
    return rec


def trust_level(workspace: Path, population: str) -> dict:
    """Effective trust level + capability bounds for a population."""
    treaties = read_jsonl(treaties_path(ws := workspace))
    active = [t for t in treaties if t.get("population") == population
              and t.get("status") == "active"]
    if not active:
        return {"level": "quarantined", "capabilities": LEVEL_CAPS["quarantined"]}
    best = max(active, key=lambda t: TREATY_LEVELS.index(t.get("level", "peers")))
    return {"level": best["level"], "capabilities": LEVEL_CAPS[best["level"]],
            "treaty": best["id"]}


def dispute(workspace: Path, population: str, rule_sha: str,
            detail: str) -> dict:
    """Raise a treaty dispute; resolves via quorum or policy arbitrator."""
    ws = Path(workspace)
    ensure_rack(ws, "diplomacy")
    rec = {"population": population, "rule_sha": rule_sha, "detail": detail,
           "status": "open", "resolution": None, "ts": now_ts()}
    append_jsonl(Path(ws) / "rack" / "diplomacy" / "disputes.jsonl", rec)
    emit(ws, "treaty_violated", population=population, rule_sha=rule_sha[:12])
    return rec


def resolve(workspace: Path, population: str, rule_sha: str,
            resolution: str, arbitrator: str = "quorum") -> bool:
    """Resolve a dispute; outcome logged in every party's backlog."""
    ws = Path(workspace)
    path = Path(ws) / "rack" / "diplomacy" / "disputes.jsonl"
    recs = read_jsonl(path)
    hit = False
    for r in recs:
        if r.get("population") == population and r.get("rule_sha") == rule_sha:
            r["status"] = "resolved"
            r["resolution"] = resolution
            r["arbitrator"] = arbitrator
            r["resolved_at"] = now_ts()
            hit = True
    if hit:
        with path.open("w", encoding="utf-8") as fh:
            for r in recs:
                fh.write(json.dumps(r, sort_keys=True) + "\n")
        append_jsonl(Path(ws) / "rack" / "federation" / "backlog.jsonl",
                     {"type": "treaty_resolved", "population": population,
                      "rule_sha": rule_sha, "resolution": resolution,
                      "ts": now_ts()})
        emit(ws, "treaty_resolved", population=population,
             rule_sha=rule_sha[:12])
    return hit


def status(workspace: Path) -> dict:
    treaties = read_jsonl(treaties_path(ws := workspace))
    disputes = read_jsonl(Path(ws) / "rack" / "diplomacy" / "disputes.jsonl")
    return {"treaties": len(treaties),
            "active": sum(1 for t in treaties if t.get("status") == "active"),
            "open_disputes": sum(1 for d in disputes
                                 if d.get("status") == "open")}
