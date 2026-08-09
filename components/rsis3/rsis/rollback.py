"""Rollback — restore prior state for an applied candidate (Phase 9).

Uses the Phase 7 verification ledger (pre-apply digests + pre-apply
checkpoint commit) or the Phase 9 approval record (pre-state content) to
restore the prior versions, then files a MyKB incident note and an audit
entry.
"""

from __future__ import annotations

import json
import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _find_verification(workspace: Path, candidate_sha: str) -> Optional[dict]:
    ledger_dir = Path(workspace) / "rack" / "verification"
    if not ledger_dir.is_dir():
        return None
    for f in ledger_dir.glob("*.jsonl"):
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("candidate_sha", "").startswith(candidate_sha) \
                    or rec.get("candidate_sha") == candidate_sha:
                return rec
    return None


def _find_approval(workspace: Path, approval_id: str) -> Optional[dict]:
    path = Path(workspace) / "rack" / "approvals" / f"{approval_id}.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def rollback(workspace: Path, candidate_id: str,
             mykb: Optional[Path] = None) -> bool:
    """Restore the pre-apply state for a candidate/approval id."""
    ws = Path(workspace)
    rec = _find_approval(ws, candidate_id)
    if rec is None:
        rec = _find_verification(ws, candidate_id)
    if rec is None:
        logger.error("no approval or verification record for %s", candidate_id)
        return False

    target_files = rec.get("target_files") or []
    restored: list[str] = []
    pre_state = rec.get("pre_state") or {}
    if pre_state:
        for f in target_files:
            if f in pre_state:
                p = ws / f
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(pre_state[f], encoding="utf-8")
                restored.append(f)
    elif rec.get("pre_commit"):
        proc = subprocess.run(
            ["git", "checkout", rec["pre_commit"], "--", *target_files],
            cwd=str(ws), capture_output=True, text=True, timeout=60)
        if proc.returncode == 0:
            restored = list(target_files)

    from rsis.audit import append
    append(ws, {
        "kind": "rollback",
        "actor": "system",
        "candidate_id": candidate_id,
        "detail": f"restored {len(restored)} file(s): {', '.join(restored)}",
    })
    if mykb is not None and restored:
        _incident_note(mykb, candidate_id, restored)
    return bool(restored)


def _incident_note(mykb: Path, candidate_id: str, files: list[str]) -> Path:
    ts = _now_ts()
    date_part = ts[:10]
    out = mykb / "wiki" / "backlog"
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"rollback-{candidate_id}-{date_part}.md"
    if path.exists():
        return path
    body = "\n".join([
        f"# Rollback — {candidate_id}",
        "",
        f"- Rolled back: {ts}",
        f"- Restored files: {', '.join(files)}",
        "- Source: rsis rollback",
    ])
    front = {
        "type": "backlog",
        "title": f"Rollback — {candidate_id}",
        "description": f"restored {len(files)} file(s)",
        "tags": ["backlog", "rollback"],
        "timestamp": ts,
        "status": "open",
        "source": "rollback",
    }
    path.write_text(
        "---\n" + "\n".join(f'{k}: "{v}"' for k, v in front.items()) + "\n---\n\n" + body + "\n",
        encoding="utf-8")
    return path


def main(workspace: Path, mykb: Path, candidate_id: str) -> int:
    ok = rollback(workspace, candidate_id, mykb=mykb)
    print(f"  {'✓' if ok else '✗'} rollback {candidate_id}: "
          f"{'restored' if ok else 'not found / nothing to restore'}")
    return 0 if ok else 1
