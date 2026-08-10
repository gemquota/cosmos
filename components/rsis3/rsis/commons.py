"""Global knowledge commons — shared pool with attribution norms.

Phase 42 (Sequel IX): syntheses publish to a shared pool under explicit
terms (license, attribution, confidence) extending the Phase 13 envelope
and Phase 22 exchange. Every item tracks origin, contributor and
provenance permanently — nothing enters anonymously. Consumption credits
the producer in the exchange ledger; free-riding is surfaced, not
punished silently.
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


def commons_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "commons"


def items_path(workspace: Path) -> Path:
    return commons_dir(workspace) / "items.json"


def ledger_path(workspace: Path) -> Path:
    return commons_dir(workspace) / "attribution.jsonl"


def publish(workspace: Path, title: str, content: str, origin: str,
            license: str = "cc-by-4.0", confidence: float = 0.5,
            contributor: str = "system") -> dict:
    """Publish a synthesis to the commons with permanent attribution."""
    ws = Path(workspace)
    ensure_rack(ws, "commons")
    item = {
        "sha": sha256_text(title + "|" + content),
        "title": title, "content": content[:2000],
        "origin": origin, "contributor": contributor, "license": license,
        "confidence": confidence, "adopted_by": [], "published": now_ts(),
    }
    data = load_json(items_path(ws), {"version": 1, "items": {}})
    items = data.setdefault("items", {})
    if item["sha"] in items:
        return {"duplicate": True, "sha": item["sha"]}
    items[item["sha"]] = item
    save_json(items_path(ws), data)
    append_jsonl(ledger_path(ws), {"type": "publish", "sha": item["sha"],
                                   "contributor": contributor,
                                   "origin": origin, "ts": now_ts()})
    emit(ws, "commons_published", sha=item["sha"][:12], origin=origin)
    return item


def adopt(workspace: Path, sha: str, adopter: str) -> dict:
    """Adopt a commons item; credits the producer in the ledger."""
    ws = Path(workspace)
    data = load_json(items_path(ws), {"version": 1, "items": {}})
    item = data.get("items", {}).get(sha)
    if item is None:
        return {"adopted": False, "reason": "unknown item"}
    if adopter not in item.setdefault("adopted_by", []):
        item["adopted_by"].append(adopter)
    save_json(items_path(ws), data)
    append_jsonl(ledger_path(ws), {"type": "adopt", "sha": sha,
                                   "adopter": adopter,
                                   "credit_to": item.get("contributor"),
                                   "ts": now_ts()})
    emit(ws, "commons_adopted", sha=sha[:12], adopter=adopter)
    return {"adopted": True, "sha": sha}


def attribution_report(workspace: Path) -> dict:
    """Attribution integrity: no item entered anonymously."""
    items = load_json(items_path(ws := workspace), {"version": 1, "items": {}})
    anonymous = [s for s, i in items.get("items", {}).items()
                 if not i.get("contributor") or not i.get("origin")]
    ledger = read_jsonl(ledger_path(ws))
    return {"items": len(items.get("items", {})),
            "anonymous": anonymous,
            "attribution_ok": len(anonymous) == 0,
            "ledger_records": len(ledger)}


def status(workspace: Path) -> dict:
    return attribution_report(workspace)
