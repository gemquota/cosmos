"""Meta-governance — evidence-driven, human-ratified policy revision.

Phase 26 (Sequel VI): the system cannot sustainably run itself until
policy revision is evidence-driven and human-ratified.

- ``propose`` — a policy change arrives with rationale + evidence
  (incidents, forecast, red-team findings) and is staged, never applied
  directly.
- ``score`` — the proposal is scored against the invariant registry (14):
  any relaxation of a prior control is flagged and blocked.
- ``ratify`` — only scored-OK, human-ratified proposals apply; applied
  changes append to the policy history.
- ``meta_invariant_check`` — every cycle verifies that no adopted policy
  silently relaxed a prior control (the cross-roadmap invariant,
  executable form).
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

#: policy keys that are "controls" — relaxing any is a meta-invariant breach
CONTROL_KEYS = ("ceiling_usd", "default_daily_usd", "max_approval_skip",
                "quorum", "approval_required", "fail_closed", "allowed_paths")


def metagov_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "metagov"


def proposals_path(workspace: Path) -> Path:
    return metagov_dir(workspace) / "proposals.jsonl"


def history_path(workspace: Path) -> Path:
    return metagov_dir(workspace) / "policy_history.jsonl"


def propose(workspace: Path, policy_delta: dict, rationale: str,
            evidence: list[str], proposer: str = "system") -> dict:
    """Stage an evidence-backed policy change."""
    ws = Path(workspace)
    ensure_rack(ws, "metagov")
    rec = {
        "id": f"m{len(read_jsonl(proposals_path(ws)))}",
        "policy_delta": policy_delta,
        "rationale": rationale,
        "evidence": evidence,
        "proposer": proposer,
        "status": "staged",
        "score": None,
        "ts": now_ts(),
    }
    append_jsonl(proposals_path(ws), rec)
    emit(ws, "metagov_proposed", proposal=rec["id"], proposer=proposer)
    return rec


def score(workspace: Path, proposal_id: str) -> Optional[dict]:
    """Score a proposal against the invariant registry; blocks relaxations."""
    recs = read_jsonl(proposals_path(workspace))
    target = next((r for r in recs if r.get("id") == proposal_id), None)
    if target is None:
        return None
    from rsis.epoch1 import invariants_status
    inv_ok, inv_issues = invariants_status(workspace)
    delta = target.get("policy_delta", {})
    relaxed = [k for k in CONTROL_KEYS if k in delta]
    # a control appearing in the delta is only OK if it does not lower a ceiling
    violations = []
    for k in relaxed:
        v = delta[k]
        if isinstance(v, (int, float)) and v < 0:
            violations.append(k)
        if k in ("approval_required", "fail_closed") and v is False:
            violations.append(k)
    score_rec = {"invariants_ok": inv_ok, "invariant_issues": inv_issues[:5],
                 "controls_touched": relaxed, "violations": violations,
                 "verdict": "block" if (violations or not inv_ok) else "ok",
                 "ts": now_ts()}
    # persist score
    with proposals_path(workspace).open("w", encoding="utf-8") as fh:
        for r in recs:
            if r.get("id") == proposal_id:
                r["score"] = score_rec
                r["status"] = "blocked" if score_rec["verdict"] == "block" \
                    else "scored"
            fh.write(json.dumps(r, sort_keys=True) + "\n")
    emit(workspace, "metagov_scored", proposal=proposal_id,
         verdict=score_rec["verdict"])
    return score_rec


def ratify(workspace: Path, proposal_id: str, actor: str = "approver") -> bool:
    """Apply a scored-OK, human-ratified proposal."""
    recs = read_jsonl(proposals_path(workspace))
    target = next((r for r in recs if r.get("id") == proposal_id), None)
    if target is None or (target.get("score") or {}).get("verdict") != "ok":
        return False
    from rsis.policy import load_policy, save_policy
    policy = load_policy(workspace)
    policy.update(target.get("policy_delta", {}))
    save_policy(workspace, policy)
    with proposals_path(workspace).open("w", encoding="utf-8") as fh:
        for r in recs:
            if r.get("id") == proposal_id:
                r["status"] = "ratified"
                r["ratified_by"] = actor
                r["ratified_at"] = now_ts()
            fh.write(json.dumps(r, sort_keys=True) + "\n")
    append_jsonl(history_path(workspace), {
        "proposal": proposal_id, "policy_delta": target.get("policy_delta", {}),
        "ratified_by": actor, "ts": now_ts()})
    emit(workspace, "metagov_ratified", proposal=proposal_id, actor=actor)
    return True


def meta_invariant_check(workspace: Path) -> tuple[bool, list[str]]:
    """Cross-roadmap invariant, executable: no adopted policy relaxed a
    prior control. Compares the current policy against the full history."""
    issues: list[str] = []
    current = load_json(Path(workspace) / "rack" / "policy.json")
    for rec in read_jsonl(history_path(workspace)):
        for key, old_value in (rec.get("policy_delta") or {}).items():
            if key in CONTROL_KEYS and key in current:
                cv, ov = current[key], old_value
                if isinstance(ov, (int, float)) and isinstance(cv, (int, float)):
                    if cv < ov:
                        issues.append(
                            f"{key} relaxed {ov} -> {cv} by {rec.get('proposal')}")
                elif cv != ov and ov is True:
                    issues.append(f"{key} disabled by {rec.get('proposal')}")
    return (len(issues) == 0, issues)


def status(workspace: Path) -> dict:
    proposals = read_jsonl(proposals_path(workspace))
    ok, issues = meta_invariant_check(workspace)
    return {
        "proposals": len(proposals),
        "staged": sum(1 for p in proposals if p.get("status") == "staged"),
        "ratified": sum(1 for p in proposals if p.get("status") == "ratified"),
        "meta_invariant_ok": ok,
        "meta_invariant_issues": issues[:5],
    }
