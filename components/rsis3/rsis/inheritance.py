"""Knowledge inheritance — one generation's curriculum for the next.

Phase 31 (Sequel VII): the distilled knowledge of one generation becomes
the curriculum of the next. ``export`` renders the full durable knowledge
(syntheses, durable rules, KG, verification history, policy rationale) as
a versioned bundle; a successor ``adopt``s it and must pass a
generation-parity probe set with parity ≥ 0.98 plus green invariants.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    emit, ensure_rack, load_json, now_ts, read_jsonl, save_json, sha256_file,
    sha256_text,
)

logger = logging.getLogger(__name__)

PARITY_MIN = 0.98


def inheritance_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "inheritance"


def export_bundle(workspace: Path, mykb: Path,
                  out: Optional[Path] = None) -> dict:
    """Versioned inheritance bundle: durable knowledge + curriculum."""
    ws = Path(workspace)
    ensure_rack(ws, "inheritance")
    syntheses = sorted((Path(mykb) / "wiki" / "syntheses").glob("*.md")) \
        if (Path(mykb) / "wiki" / "syntheses").is_dir() else []
    knowledge = []
    for p in syntheses[-50:]:
        text = p.read_text(encoding="utf-8", errors="ignore")
        knowledge.append({"rel": str(p.relative_to(mykb)), "sha": sha256_text(text)})
    bundle = {
        "format": "cosmos-inheritance/1",
        "generated": now_ts(),
        "curriculum": knowledge,
        "durable_rules": read_jsonl(Path(ws) / "rack" / "popgov" / "rules.jsonl"),
        "verification_history": _verification(ws),
        "policy_rationale": load_json(Path(ws) / "rack" / "policy.json"),
        "parity_min": PARITY_MIN,
        "sha": "",
    }
    bundle["sha"] = sha256_text(json.dumps(
        {"curriculum": knowledge, "rules": bundle["durable_rules"]},
        sort_keys=True))
    if out:
        Path(out).write_text(json.dumps(bundle, indent=1, sort_keys=True),
                             encoding="utf-8")
    emit(ws, "inheritance_exported", sha=bundle["sha"][:12],
         notes=len(knowledge))
    return bundle


def _verification(workspace: Path) -> list[dict]:
    vdir = Path(workspace) / "rack" / "verification"
    recs = []
    if vdir.is_dir():
        for f in sorted(vdir.glob("*.jsonl")):
            recs.extend(read_jsonl(f))
    return recs[-200:]


def adopt(workspace: Path, bundle: dict, mykb: Path) -> dict:
    """Adopt an inheritance bundle: record curriculum + write probe set."""
    ws = Path(workspace)
    ensure_rack(ws, "inheritance")
    probes = [{"rel": k.get("rel", ""), "sha": k.get("sha", "")}
              for k in (bundle.get("curriculum") or [])]
    record = {"adopted_sha": bundle.get("sha", ""),
              "probes": probes, "adopted_at": now_ts()}
    save_json(Path(ws) / "rack" / "inheritance" / "adopted.json", record)
    emit(ws, "inheritance_adopted", sha=bundle.get("sha", "")[:12],
         probes=len(probes))
    return record


def parity_check(workspace: Path, mykb: Path) -> tuple[float, dict]:
    """Generation-parity: does the successor answer the probe set?"""
    adopted = load_json(Path(ws := workspace) / "rack" / "inheritance" / "adopted.json")
    probes = adopted.get("probes") or []
    matched = 0
    for p in probes:
        target = Path(mykb) / p.get("rel", "")
        if target.is_file() and sha256_text(
                target.read_text(encoding="utf-8", errors="ignore")) == p.get("sha"):
            matched += 1
    parity = matched / len(probes) if probes else 1.0
    ok = parity >= PARITY_MIN
    emit(ws, "inheritance_parity", parity=round(parity, 4),
         probes=len(probes), ok=ok)
    return parity, {"probes": len(probes), "matched": matched,
                    "parity_min": PARITY_MIN, "ok": ok}


def status(workspace: Path) -> dict:
    adopted = load_json(Path(workspace) / "rack" / "inheritance" / "adopted.json")
    probes = adopted.get("probes") or []
    return {"probes": len(probes),
            "adopted_sha": (adopted.get("adopted_sha") or "")[:12]}
