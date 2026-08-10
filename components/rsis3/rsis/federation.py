"""Federated memory — exchange distilled syntheses with provenance.

Phase 13 (Sequel III): multiple Cosmos instances exchange knowledge
without losing identity or creating conflicts.

- ``publish`` — only notes tagged ``publishable`` leave the instance; the
  outbound envelope carries explicit provenance (origin, source, project,
  session, producer, verification state, confidence, transformations,
  federation history).
- ``pull`` — foreign syntheses are adopted create-only, never overwriting
  local notes; name collisions are suffixed and recorded.
- Consensus: conflicting durable rules resolve deterministically —
  newest-by-timestamp wins for facts, local policy wins for behavior —
  and conflicts are logged to ``rack/federation/backlog.jsonl``.
- Every publish/pull/merge is recorded in ``rack/federation/ledger.jsonl``
  and summarized in the nightly note.
"""

from __future__ import annotations

import json
import logging
import re
import shutil
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.S)


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fed_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "federation"


def outbox_dir(workspace: Path) -> Path:
    return fed_dir(workspace) / "outbox"


def backlog_path(workspace: Path) -> Path:
    return fed_dir(workspace) / "backlog.jsonl"


def ledger_path(workspace: Path) -> Path:
    return fed_dir(workspace) / "ledger.jsonl"


def _parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.search(text)
    if not m:
        return {}
    front = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        front[k.strip()] = v.strip().strip('"')
    return front


def _tags_of(front: dict) -> set[str]:
    raw = front.get("tags", "")
    if isinstance(raw, list):
        return {str(t).strip() for t in raw}
    return {t.strip() for t in str(raw).split(",") if t.strip()}


def _verification_state(workspace: Path, rel: str) -> str:
    """Look up the note in the Phase 7 verification ledger, if present."""
    vdir = Path(workspace) / "rack" / "verification"
    if not vdir.is_dir():
        return "unverified"
    for f in sorted(vdir.glob("*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            artifacts = rec.get("artifacts") or []
            if any(rel in str(a) for a in artifacts):
                return rec.get("decision", "verified")
    return "unverified"


def publish(workspace: Path, mykb: Path, note_rel: str,
            producer: str = "system", origin: Optional[str] = None,
            confidence: float = 1.0,
            transformations: Optional[list[str]] = None) -> Optional[dict]:
    """Publish a MyKB synthesis note iff it is tagged ``publishable``.

    Returns the envelope (also persisted to the outbox) or None when the
    note is private or missing. Private notes never leave the instance.
    """
    note = Path(mykb) / note_rel
    if not note.is_file():
        logger.warning("federation: note not found: %s", note_rel)
        return None
    text = note.read_text(encoding="utf-8")
    front = _parse_frontmatter(text)
    tags = _tags_of(front)
    if "publishable" not in tags and front.get("publishable") != "true":
        logger.info("federation: %s is private (not tagged publishable)",
                    note_rel)
        return None
    envelope = {
        "id": uuid.uuid4().hex[:12],
        "ts": _now_ts(),
        "kind": "synthesis",
        "title": front.get("title") or note.stem,
        "rel": note_rel,
        "body": text,
        "provenance": {
            "origin": origin or str(note),
            "source": front.get("source", "mykb"),
            "project": next((t.split(":", 1)[1] for t in tags
                             if t.startswith("project:")), "cosmos"),
            "session": front.get("session", ""),
            "producer": producer,
            "verification_state": _verification_state(workspace, note_rel),
            "confidence": float(confidence),
            "transformations": list(transformations or []),
            "federation_history": [f"{producer}:{_now_ts()}"],
        },
    }
    out = outbox_dir(workspace)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{envelope['id']}.json"
    path.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
    _ledger(workspace, "publish", {"id": envelope["id"], "rel": note_rel,
                                   "title": envelope["title"]})
    return envelope


def _ledger(workspace: Path, op: str, detail: dict) -> None:
    p = ledger_path(workspace)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"ts": _now_ts(), "op": op, **detail}) + "\n")


def pull(workspace: Path, mykb: Path, envelope: dict,
         actor: str = "federation") -> dict:
    """Adopt a foreign synthesis; resolve conflicts deterministically.

    Facts (non-policy notes): newest timestamp wins. Behavior (notes tagged
    ``policy`` / ``rule``): the local policy note wins. Name collisions are
    adopted create-only with a ``-federated-<id>`` suffix. Conflicts that
    cannot be auto-resolved are logged to the federation backlog.
    """
    prov = envelope.get("provenance") or {}
    title = envelope.get("title") or "federated-synthesis"
    body = envelope.get("body", "")
    front = _parse_frontmatter(body)
    tags = _tags_of(front)
    out = Path(mykb) / "wiki" / "syntheses"
    out.mkdir(parents=True, exist_ok=True)

    slug = re.sub(r"[^a-z0-9._-]+", "-", title.lower()).strip("-._") or "synthesis"
    target = out / f"{slug}.md"
    merged = False
    if target.is_file():
        existing = target.read_text(encoding="utf-8")
        existing_front = _parse_frontmatter(existing)
        is_behavior = bool({"policy", "rule"} & tags)
        new_ts = front.get("timestamp", "")
        old_ts = existing_front.get("timestamp", "")
        if is_behavior:
            # local policy wins; record the conflict
            _backlog(workspace, envelope, "local-policy-wins",
                     f"behavior note {title} conflicts with local note")
            _ledger(workspace, "merge", {"id": envelope.get("id"),
                                         "title": title, "outcome": "local-policy-wins"})
            return {"outcome": "local-policy-wins", "rel": str(target)}
        if new_ts and old_ts and new_ts > old_ts:
            # fact: newest wins — but never silently overwrite: adopt as
            # federated copy and record the merge
            target = out / f"{slug}-federated-{envelope.get('id', 'x')}.md"
            merged = True
        else:
            _backlog(workspace, envelope, "older-fact", None)
            _ledger(workspace, "merge", {"id": envelope.get("id"),
                                         "title": title,
                                         "outcome": "older-fact-skipped"})
            return {"outcome": "older-fact-skipped", "rel": str(target)}
    # append federation provenance to frontmatter without mutating body
    prov_marker = "\n".join(
        f"{k}: \"{v}\"" for k, v in prov.items() if isinstance(v, str))
    body = body.rstrip() + (f"\n\n<!-- federation: {json.dumps(prov)} -->\n")
    target.write_text(body + "\n", encoding="utf-8")
    _ledger(workspace, "pull", {"id": envelope.get("id"), "title": title,
                                "rel": str(target), "merged": merged,
                                "producer": prov.get("producer", "")})
    return {"outcome": "adopted", "rel": str(target), "merged": merged}


def _backlog(workspace: Path, envelope: dict, kind: str,
             detail: Optional[str]) -> None:
    p = backlog_path(workspace)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({
            "ts": _now_ts(), "kind": kind, "detail": detail,
            "envelope_id": envelope.get("id"), "title": envelope.get("title"),
        }) + "\n")


def status(workspace: Path, json_out: bool = False) -> int:
    ledger = []
    if ledger_path(workspace).is_file():
        for line in ledger_path(workspace).read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    ledger.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    ops: dict[str, int] = {}
    for rec in ledger:
        ops[rec.get("op", "?")] = ops.get(rec.get("op", "?"), 0) + 1
    outbox = sorted(p.name for p in outbox_dir(workspace).glob("*.json")) \
        if outbox_dir(workspace).is_dir() else []
    backlog = 0
    if backlog_path(workspace).is_file():
        backlog = len([l for l in
                       backlog_path(workspace).read_text(encoding="utf-8").splitlines()
                       if l.strip()])
    if json_out:
        print(json.dumps({"ops": ops, "outbox": len(outbox),
                          "backlog": backlog, "entries": len(ledger)}))
        return 0
    print(f"  federation ledger: {len(ledger)} entries — {ops or 'none'}")
    print(f"  outbox: {len(outbox)} envelope(s) pending")
    print(f"  backlog: {backlog} conflict(s)")
    return 0


def main(workspace: Path, mykb: Path, action: str,
         note_rel: Optional[str] = None, envelope_file: Optional[str] = None,
         producer: str = "system", json_out: bool = False) -> int:
    if action == "publish":
        assert note_rel
        env = publish(workspace, mykb, note_rel, producer=producer)
        if env is None:
            print(f"  ✗ {note_rel} not publishable or missing "
                  "(tag it `publishable`)")
            return 1
        print(f"  ✓ published {env['title']} → "
              f"rack/federation/outbox/{env['id']}.json")
        return 0
    if action == "pull":
        assert envelope_file
        env = json.loads(Path(envelope_file).read_text(encoding="utf-8"))
        result = pull(workspace, mykb, env)
        print(f"  ✓ {result['outcome']}: {result['rel']}")
        return 0
    if action == "status":
        return status(workspace, json_out=json_out)
    print(f"  ✗ unknown federation action {action!r}")
    return 2


if __name__ == "__main__":
    import sys
    sys.exit(main(Path(".").resolve(), Path("../mykb").resolve(),
                  sys.argv[1] if len(sys.argv) > 1 else "status"))
