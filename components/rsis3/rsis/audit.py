"""Audit trail — attributable, replayable activity log (Phase 9).

Every applied change, approval, rejection, and rollback appends to
``.rsis/audit.jsonl`` with actor, policy decision, verification record
reference, and pre-apply state digests.
"""

from __future__ import annotations

import hashlib
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def audit_path(workspace: Path) -> Path:
    return Path(workspace) / ".rsis" / "audit.jsonl"


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def digest(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def append(workspace: Path, entry: dict) -> dict:
    """Append an audit entry with a timestamp; returns the entry."""
    entry = dict(entry)
    entry.setdefault("ts", _now_ts())
    path = audit_path(workspace)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry) + "\n")
    return entry


def replay(workspace: Path, since: Optional[str] = None) -> list[dict]:
    """Replay audit entries, newest first, optionally from an ISO timestamp."""
    path = audit_path(workspace)
    out = []
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if since and rec.get("ts", "") < since:
                continue
            out.append(rec)
    return list(reversed(out))


def main(workspace: Path, since: Optional[str] = None,
         json_out: bool = False) -> int:
    entries = replay(workspace, since)
    if json_out:
        print(json.dumps(entries))
        return 0
    print(f"  audit: {len(entries)} entr{'y' if len(entries) == 1 else 'ies'}"
          + (f" since {since}" if since else ""))
    for e in entries[:20]:
        print(f"  - {e.get('ts')} {e.get('kind', '?')} "
              f"actor={e.get('actor', '-')} {e.get('detail', '')}")
    return 0
