"""External evaluation & red-teaming — adversarial probe harness.

Phase 19 (Sequel IV): adversarial outsiders become a first-class input to
the improvement loop. The harness probes the controls established in
Phases 8, 9, 12 and 14 with adversarial inputs:

- policy gates (``requires_approval`` on gated paths, path traversal),
- budget fail-closes (over-limit spend must be blocked),
- invariant checks (tampered invariant registry must be detected),
- authz (role escalation attempts must be denied).

Every finding becomes a tracked incident (``rack/incidents.jsonl``) or a
policy gap (``rack/redteam/findings.jsonl``) with a resolution status.
CI mode (``--ci``) exits non-zero while any finding is untriaged.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
)
from rsis.epoch1 import invariants_status
from rsis.policy import requires_approval
from rsis.users import authorize

logger = logging.getLogger(__name__)

FINDING_STATUS = ("open", "triaged", "repaired", "accepted")


def findings_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "redteam" / "findings.jsonl"


def _staged(target_files):
    return {"description": "red-team probe", "target_files": list(target_files),
            "diff_or_code": "# probe", "goal": "red-team", "rationale": "probe"}


def run_probes(workspace: Path) -> list[dict]:
    """Run the adversarial probe battery; return findings (fresh)."""
    ws = Path(workspace)
    ensure_rack(ws, "redteam")
    findings: list[dict] = []

    # Probe 1 — policy gate: gated path must require approval.
    policy = load_json(ws / "rack" / "policy.json")
    gated = (policy.get("approval_required") or {}).get("paths") or []
    for path in gated[:1]:
        if not requires_approval(_staged([path]), policy=policy):
            findings.append(_finding("policy_gate", path,
                                     "gated path bypassed approval"))

    # Probe 2 — policy gate: traversal outside allowed roots must be blocked.
    for path in ("../../etc/passwd", "/etc/passwd", "wiki/../.rsis/secrets"):
        cand = _staged([path])
        try:
            blocked = requires_approval(cand, policy=policy)
        except Exception:
            blocked = False
        if not blocked:
            findings.append(_finding("path_traversal", path,
                                     "traversal path not approval-gated"))

    # Probe 3 — budget fail-close: over-limit spend must block.
    from rsis.budgets import check_budget
    try:
        budget = check_budget(ws, "evaluator")
        allowed = budget.get("allowed", True)
        over = budget.get("over", False) or \
            (budget.get("remaining", 1) is not None and budget.get("remaining", 1) < 0)
        if over and allowed:
            findings.append(_finding("budget_failclose", "evaluator",
                                     "spend over limit still allowed"))
    except Exception as e:
        findings.append(_finding("budget_failclose", "evaluator",
                                 f"budget check raised: {e}"))

    # Probe 4 — invariants: tampered registry must be detected.
    inv_ok, inv_issues = invariants_status(ws)
    # A registry that is missing or unparseable is itself a finding.
    inv_path = ws / "rack" / "invariants.json"
    inv_registry = None
    if inv_path.is_file():
        try:
            inv_registry = json.loads(inv_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    if inv_ok and not inv_registry:
        findings.append(_finding("invariant_missing", "rack/invariants.json",
                                 "invariant registry missing or unparseable"))

    # Probe 5 — authz: role escalation must be denied.
    for user_id, role, action, expect in (
        ("observer", "observer", "approve", False),
        ("contributor", "contributor", "rollback", False),
        ("approver", "approver", "rollback", True),
    ):
        user = {"id": user_id, "role": role, "projects": ["*"]}
        ok, _reason = authorize(ws, user=user, action=action, project="cosmos")
        if ok != expect:
            findings.append(_finding(
                "authz_escalation", f"{user_id}:{action}",
                f"expected deny={not expect}, got allow={ok}"))

    emit(ws, "redteam_probe", findings=len(findings))
    return findings


def _finding(kind: str, target: str, detail: str) -> dict:
    return {"kind": kind, "target": target, "detail": detail,
            "ts": now_ts(), "status": "open",
            "resolution": None, "incident": None}


def triage(workspace: Path, index: int, status: str,
           resolution: Optional[str] = None, actor: str = "redteam") -> bool:
    """Mark a finding open→triaged/repaired/accepted."""
    if status not in FINDING_STATUS:
        return False
    path = findings_path(workspace)
    recs = read_jsonl(path)
    if index < 0 or index >= len(recs):
        return False
    recs[index]["status"] = status
    recs[index]["resolution"] = resolution
    recs[index]["triaged_by"] = actor
    recs[index]["triaged_at"] = now_ts()
    # rewrite file
    with path.open("w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, sort_keys=True) + "\n")
    emit(workspace, "redteam_triaged", index=index, status=status)
    return True


def incident_for(workspace: Path, finding: dict) -> None:
    """Mirror a finding into the incident log (rack/incidents.jsonl)."""
    inc = {"id": f"redteam-{finding['ts']}", "source": "redteam",
           "severity": "medium", "status": "open",
           "summary": f"{finding['kind']}: {finding['detail']}",
           "ts": now_ts()}
    append_jsonl(Path(workspace) / "rack" / "incidents.jsonl", inc)


def main(workspace: Path, action: str = "run", index: Optional[int] = None,
         status: str = "triaged", resolution: Optional[str] = None,
         ci: bool = False, json_out: bool = False) -> int:
    ws = Path(workspace)
    if action == "run":
        fresh = run_probes(ws)
        existing = read_jsonl(findings_path(ws))
        new = [f for f in fresh if f not in existing]
        for f in new:
            append_jsonl(findings_path(ws), f)
            incident_for(ws, f)
        for f in fresh:
            print(f"  [{f['kind']}] {f['target']}: {f['detail']} "
                  f"({f['status']})")
        untriaged = [f for f in read_jsonl(findings_path(ws))
                     if f.get("status") == "open"]
        print(f"  red-team: {len(new)} new finding(s), "
              f"{len(untriaged)} untriaged")
        if ci and untriaged:
            return 1
        return 0
    if action == "triage":
        ok = triage(ws, index if index is not None else 0, status, resolution)
        print("  triage:", "ok" if ok else "not found")
        return 0 if ok else 1
    recs = read_jsonl(findings_path(ws))
    print(f"  red-team findings: {len(recs)} "
          f"({sum(1 for r in recs if r.get('status')=='open')} open)")
    if json_out:
        print(json.dumps(recs))
    return 0
