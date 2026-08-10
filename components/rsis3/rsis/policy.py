"""Policy-controlled governance — machine-readable autonomy bounds (Phase 9).

``rack/policy.json`` (env-templated) declares what the system may do
autonomously: allowed loop families, apply rules, approval-required
triggers, and budget ceilings. Policy-gated candidates are staged to
``rack/approvals/`` with a rendered diff; ``python -m rsis approve <id>
[--reject]`` completes or discards them. CI treats staged-but-unapproved
candidates as not-applied.

The human is one enforcement mechanism within the policy architecture:
approval gates are one of several policy instruments.
"""

from __future__ import annotations

import fnmatch
import json
import logging
import os
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_POLICY = {
    "version": 1,
    "allowed_loop_families": ["l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9"],
    "apply_rules": {
        "blocked_paths": [],
        "allowlist": [],
    },
    "approval_required": {
        "paths": [
            "rack/policy.json",
            "rack/bridge/server.mjs",
            "rack/approvals/",
            "rsis/policy.py",
        ],
        "patterns": [],
    },
    "budget_ceilings": {},
}


def _expand(value):
    if isinstance(value, str) and value.startswith("$"):
        return os.environ.get(value[1:].strip("{}"), value)
    return value


def policy_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "policy.json"


def load_policy(workspace: Path) -> dict:
    path = policy_path(workspace)
    if path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            logger.warning("policy.json unreadable (%s); using defaults", e)
    return dict(DEFAULT_POLICY)


def save_policy(workspace: Path, policy: dict) -> None:
    """Persist a policy dict to rack/policy.json."""
    path = policy_path(workspace)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(policy, fh, indent=2, sort_keys=True)
        fh.write("\n")


def ensure_policy(workspace: Path) -> dict:
    path = policy_path(workspace)
    if not path.is_file():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(DEFAULT_POLICY, indent=2) + "\n",
                        encoding="utf-8")
    return load_policy(workspace)


def approvals_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "approvals"


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _matches(path: str, patterns: list[str]) -> bool:
    for pat in patterns or []:
        if fnmatch.fnmatch(path, pat) or path.startswith(pat):
            return True
    return False


def _canonical(path) -> tuple[str, bool]:
    """Canonicalize a target path -> (canonical, escapes_workspace).

    ``escapes_workspace`` is True when the path is absolute or resolves
    above the workspace root via ``..`` segments. Canonicalization collapses
    ``.``/``..`` segments and normalises backslashes to forward slashes so
    that ``wiki/../.rsis/secrets`` gates exactly like ``.rsis/secrets`` and
    ``../../etc/passwd`` cannot dodge the policy gate.
    """
    raw = str(path).replace("\\", "/").strip()
    if not raw:
        return raw, False
    parts: list[str] = []
    escaped = raw.startswith("/")
    for seg in raw.split("/"):
        if seg in ("", "."):
            continue
        if seg == "..":
            if parts:
                parts.pop()
            else:
                escaped = True
        else:
            parts.append(seg)
    return "/".join(parts), escaped


def requires_approval(candidate, policy: Optional[dict] = None,
                      workspace: Optional[Path] = None) -> bool:
    """Whether a candidate's target files hit an approval-required gate."""
    policy = policy or (load_policy(workspace) if workspace else DEFAULT_POLICY)
    target_files = (list(candidate.get("target_files") or [])
                    if isinstance(candidate, dict)
                    else list(getattr(candidate, "target_files", []) or []))
    req = policy.get("approval_required", {})
    paths = req.get("paths", [])
    patterns = req.get("patterns", [])
    for f in target_files:
        canonical, escapes = _canonical(f)
        # Traversal attempts are always sensitive: absolute paths, paths
        # that resolve above the workspace root, or any ``..`` segment.
        if escapes or ".." in str(f).split("/"):
            return True
        if _matches(canonical, paths) or _matches(canonical, patterns) \
                or _matches(f, paths) or _matches(f, patterns):
            return True
    return False


def stage_candidate(workspace: Path, candidate: dict, reason: str,
                    actor: str = "system") -> dict:
    """Stage a policy-gated candidate for human approval."""
    out = approvals_dir(workspace)
    out.mkdir(parents=True, exist_ok=True)
    target_files = candidate.get("target_files") or []
    pre_state = {}
    for f in target_files:
        p = Path(workspace) / f
        if p.is_file():
            pre_state[f] = p.read_text(encoding="utf-8", errors="ignore")
    rec = {
        "id": uuid.uuid4().hex[:12],
        "ts": _now_ts(),
        "status": "staged",
        "actor": actor,
        "reason": reason,
        "description": candidate.get("description", ""),
        "goal": candidate.get("goal", ""),
        "target_files": target_files,
        "diff": candidate.get("diff_or_code", ""),
        "rationale": candidate.get("rationale", ""),
        "pre_state": pre_state,
    }
    path = out / f"{rec['id']}.json"
    path.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    return rec


def list_staged(workspace: Path) -> list[dict]:
    out = approvals_dir(workspace)
    recs = []
    if out.is_dir():
        for f in sorted(out.glob("*.json")):
            try:
                rec = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if rec.get("status") == "staged":
                recs.append(rec)
    return recs


def load_staged(workspace: Path, approval_id: str) -> Optional[dict]:
    path = approvals_dir(workspace) / f"{approval_id}.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _save_staged(workspace: Path, rec: dict) -> None:
    path = approvals_dir(workspace) / f"{rec['id']}.json"
    path.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")


def approve(workspace: Path, approval_id: str, actor: str = "approver") -> bool:
    """Apply a staged candidate: write target files, mark applied."""
    from rsis.audit import append, digest

    rec = load_staged(workspace, approval_id)
    if rec is None or rec.get("status") != "staged":
        logger.warning("approval %s not found or not staged", approval_id)
        return False
    written = []
    for f in rec.get("target_files", []):
        p = Path(workspace) / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(rec.get("diff", ""), encoding="utf-8")
        written.append(f)
    rec["status"] = "applied"
    rec["applied_at"] = _now_ts()
    rec["actor"] = actor
    _save_staged(workspace, rec)
    append(workspace, {
        "kind": "approval.applied",
        "actor": actor,
        "candidate_id": approval_id,
        "detail": f"applied {len(written)} file(s): {', '.join(written)}",
        "digests": {f: digest(Path(workspace) / f) for f in written},
    })
    return True


def reject(workspace: Path, approval_id: str, actor: str = "approver") -> bool:
    """Discard a staged candidate."""
    rec = load_staged(workspace, approval_id)
    if rec is None or rec.get("status") != "staged":
        logger.warning("approval %s not found or not staged", approval_id)
        return False
    rec["status"] = "rejected"
    rec["rejected_at"] = _now_ts()
    rec["actor"] = actor
    _save_staged(workspace, rec)
    from rsis.audit import append
    append(workspace, {
        "kind": "approval.rejected",
        "actor": actor,
        "candidate_id": approval_id,
        "detail": rec.get("description", "")[:120],
    })
    return True


def check_unauthorized_writes(workspace: Path) -> list[str]:
    """Detect direct writes to approval-required paths without an approval.

    Scans the git worktree for modified files matching the policy gates and
    reports any that lack a matching applied approval record.
    """
    policy = load_policy(workspace)
    req = policy.get("approval_required", {})
    paths = req.get("paths", [])
    patterns = req.get("patterns", [])
    if not paths and not patterns:
        return []
    approved = set()
    out = approvals_dir(workspace)
    if out.is_dir():
        for f in out.glob("*.json"):
            try:
                rec = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if rec.get("status") == "applied":
                approved.update(rec.get("target_files", []))
    proc = subprocess.run(["git", "status", "--porcelain"],
                          cwd=str(Path(workspace)),
                          capture_output=True, text=True, timeout=30)
    violations = []
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        p = line[3:].strip().strip('"')
        if p.endswith("/"):  # untracked dir — any gated path inside it?
            gated_inside = [g for g in (paths + patterns)
                            if g.startswith(p) or p in g]
            unapproved = [g for g in gated_inside if g not in approved]
            if unapproved:
                violations.append(p)
        elif (_matches(p, paths) or _matches(p, patterns)
               or _matches(_canonical(p)[0], paths)
               or _matches(_canonical(p)[0], patterns)) \
                and p not in approved:
            violations.append(p)
    return sorted(set(violations))


def main(workspace: Path, json_out: bool = False) -> int:
    policy = ensure_policy(workspace)
    staged = list_staged(workspace)
    violations = check_unauthorized_writes(workspace)
    if json_out:
        print(json.dumps({"policy": policy_path(workspace).as_posix(),
                          "staged": len(staged),
                          "unauthorized_writes": violations}))
        return 1 if violations else 0
    print(f"  policy: {policy_path(workspace)}")
    print(f"  approval-required paths: "
          f"{policy.get('approval_required', {}).get('paths', [])}")
    print(f"  staged approvals: {len(staged)}")
    for s in staged:
        print(f"    - {s['id']} {s['description'][:80]}")
    print(f"  unauthorized writes: {len(violations)}")
    for v in violations:
        print(f"    - {v}")
    return 1 if violations else 0
