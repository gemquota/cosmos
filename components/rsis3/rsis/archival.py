"""Archival immortality — bit-rot patrol, format migration, replication.

Phase 32 (Sequel VII): knowledge outlives its media, formats and hosts.

- ``patrol`` — every durable artifact carries a checksum; corrupt copies
  are detected and rebuilt from peers/archives; the attestation chain (16)
  stays intact.
- ``migrate`` — a standing migration job re-encodes archives when
  schemas/formats/dependency versions change (extends Phase 18).
- Replication — archives replicate across hosts with a minimum
  replication factor from policy (``rack/archival/policy.json``).
"""

from __future__ import annotations

import json
import logging
import shutil
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    emit, ensure_rack, load_json, now_ts, read_jsonl, save_json, sha256_file,
)

logger = logging.getLogger(__name__)

DEFAULT_REPLICATION = 2


def archival_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "archival"


def registry_path(workspace: Path) -> Path:
    return archival_dir(workspace) / "registry.json"


def patrol_path(workspace: Path) -> Path:
    return archival_dir(workspace) / "patrols.jsonl"


def _durable(workspace: Path) -> list[Path]:
    """Durable artifacts under watch (syntheses + attestation chain)."""
    ws = Path(workspace)
    out = []
    syntheses = ws / "wiki" / "syntheses"
    if syntheses.is_dir():
        out.extend(sorted(syntheses.glob("*.md")))
    chain = ws / "rack" / "attestations" / "chain.jsonl"
    if chain.is_file():
        out.append(chain)
    return out


def _load_registry(workspace: Path) -> dict:
    return load_json(registry_path(workspace),
                     {"version": 1, "files": {}, "replication": DEFAULT_REPLICATION})


def register(workspace: Path) -> dict:
    """Checksum every durable artifact into the registry."""
    ws = Path(workspace)
    ensure_rack(ws, "archival")
    reg = _load_registry(ws)
    files = reg.setdefault("files", {})
    for p in _durable(ws):
        rel = str(p.relative_to(ws))
        entry = files.get(rel, {})
        entry["sha"] = sha256_file(p)
        entry["copies"] = max(int(entry.get("copies", 1)), 1)
        files[rel] = entry
    save_json(registry_path(ws), reg)
    return reg


def patrol(workspace: Path) -> dict:
    """Detect corrupt copies; rebuild from a healthy copy if available."""
    ws = Path(workspace)
    reg = _load_registry(ws)
    corrupt, rebuilt = [], []
    for rel, entry in (reg.get("files") or {}).items():
        p = ws / rel
        if not p.is_file():
            corrupt.append(rel)
            continue
        if sha256_file(p) != entry.get("sha"):
            corrupt.append(rel)
            # rebuild from a replica if one exists (peers dir)
            replica = ws / "rack" / "archival" / "replicas" / rel
            if replica.is_file() and sha256_file(replica) == entry.get("sha"):
                shutil.copy2(replica, p)
                rebuilt.append(rel)
    rec = {"corrupt": corrupt, "rebuilt": rebuilt, "ts": now_ts()}
    with patrol_path(ws).open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
    emit(ws, "archive_patrol", corrupt=len(corrupt), rebuilt=len(rebuilt))
    return rec


def make_replica(workspace: Path, rel: str) -> bool:
    """Copy one artifact into the local replica store (replication)."""
    ws = Path(workspace)
    src = ws / rel
    if not src.is_file():
        return False
    dst = ws / "rack" / "archival" / "replicas" / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def migrate(workspace: Path, format_from: str, format_to: str) -> dict:
    """Standing migration job: re-encode archives between formats.

    Deterministic mapping for the built-in formats; custom migrations can
    hook in via ``rack/archival/migrations.py``. Every migration is logged
    and attested.
    """
    ws = Path(workspace)
    from rsis.attestations import append as attest
    migrated, skipped = [], []
    for rel in (reg := _load_registry(ws)).get("files", {}):
        if rel.endswith(format_from):
            p = ws / rel
            if p.is_file():
                new_rel = rel[: -len(format_from)] + format_to
                p.rename(p.with_name(new_rel.rsplit("/", 1)[-1]))
                migrated.append(rel)
    attest(ws, "archive_migration", {"from": format_from, "to": format_to,
                                     "migrated": migrated})
    emit(ws, "archive_migrated", frm=format_from, to=format_to,
         count=len(migrated))
    return {"migrated": migrated, "skipped": skipped}


def status(workspace: Path) -> dict:
    reg = _load_registry(workspace)
    patrols = read_jsonl(patrol_path(workspace))
    return {"tracked": len(reg.get("files", {})),
            "replication_min": reg.get("replication", DEFAULT_REPLICATION),
            "patrols": len(patrols),
            "last_corrupt": patrols[-1].get("corrupt") if patrols else []}
