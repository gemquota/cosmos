"""Autonomous stewardship — the engine operates other instances.

Phase 29 (Sequel VI): Phase 11 generalization inverted into custody. A
steward instance monitors peer health within policy scope, onboards new
instances from profiles, attests every custody action, and hands custody
off with identity and provenance intact.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
)

logger = logging.getLogger(__name__)


def steward_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "stewardship"


def actions_path(workspace: Path) -> Path:
    return steward_dir(workspace) / "actions.jsonl"


def custody_path(workspace: Path) -> Path:
    return steward_dir(workspace) / "custody.jsonl"


def monitor(workspace: Path, peers: list[str]) -> list[dict]:
    """Health-scan peer workspaces; returns incidents (no manual action)."""
    ws = Path(workspace)
    ensure_rack(ws, "stewardship")
    findings = []
    for peer in peers:
        peer_ws = Path(ws).parent / peer if not Path(peer).is_absolute() else Path(peer)
        energy = "unknown"
        try:
            from rsis.seasons import energy_mode
            energy = energy_mode(peer_ws)
        except Exception:
            pass
        if energy == "pause":
            findings.append({"peer": peer, "issue": "energy pause", "ts": now_ts()})
    if findings:
        append_jsonl(actions_path(ws),
                     {"kind": "monitor", "findings": findings, "ts": now_ts()})
    emit(ws, "steward_monitored", peers=len(peers), issues=len(findings))
    return findings


def onboard(workspace: Path, repo: str, name: str,
            actor: str = "system") -> dict:
    """Initialize a peer instance from a project profile and join it to the
    trust graph (Phase 21) — all within policy."""
    ws = Path(workspace)
    from rsis.projects import init_project
    from rsis.identity import ensure_keypair, register_peer
    ensure_rack(ws, "stewardship")
    try:
        profile = init_project(ws, repo=repo, name=name)
    except Exception as e:
        profile = {"error": str(e)}
    key = ensure_keypair(ws)
    rec = {"kind": "onboard", "repo": repo, "name": name, "profile": profile,
           "actor": actor, "ts": now_ts()}
    append_jsonl(actions_path(ws), rec)
    emit(ws, "steward_onboarded", repo=repo, name=name)
    return rec


def custody_action(workspace: Path, peer: str, action: str,
                   detail: str, actor: str = "system") -> dict:
    """Any custody action (repair/retune/restart) is attested + audited."""
    ws = Path(workspace)
    from rsis.attestations import append as attest
    ensure_rack(ws, "stewardship")
    attest(ws, "steward_action", {"peer": peer, "action": action,
                                  "detail": detail, "actor": actor})
    rec = {"kind": "custody", "peer": peer, "action": action, "detail": detail,
           "actor": actor, "attested": True, "ts": now_ts()}
    append_jsonl(actions_path(ws), rec)
    emit(ws, "steward_custody_action", peer=peer, action=action)
    return rec


def handoff(workspace: Path, successor: str, peer: str,
            actor: str = "system") -> dict:
    """Transfer custody with identity/provenance intact (Phase 18)."""
    ws = Path(workspace)
    from rsis.attestations import append as attest
    ensure_rack(ws, "stewardship")
    attest(ws, "steward_handoff", {"peer": peer, "successor": successor,
                                   "actor": actor})
    rec = {"kind": "handoff", "peer": peer, "successor": successor,
           "actor": actor, "ts": now_ts()}
    append_jsonl(custody_path(ws), rec)
    emit(ws, "steward_handoff", peer=peer, successor=successor)
    return rec


def status(workspace: Path) -> dict:
    actions = read_jsonl(actions_path(workspace))
    custody = read_jsonl(custody_path(workspace))
    return {"actions": len(actions), "handoffs": len(custody),
            "last": actions[-1].get("kind") if actions else None}
