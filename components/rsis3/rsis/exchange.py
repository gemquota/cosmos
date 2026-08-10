"""Knowledge economy & exchange at scale.

Phase 22 (Sequel V): distilled knowledge moves across the population with
confidence and value semantics, not just copies.

- Confidence propagation — an item's confidence updates as it is
  corroborated or contradicted across instances (``.rsis/confidence.json``).
- Canonicalization — duplicate detection (normalized title + content
  similarity) so the same durable rule is not adopted N times with
  divergent edits (``rack/exchange/canonical.json``).
- Exchange ledger — provider/consumer/item/confidence-delta records in
  ``rack/federation/exchange.jsonl``.
- Provenance intactness — envelopes with a federation history of three or
  more hops keep origin and full history; no silent rewriting.
"""

from __future__ import annotations

import difflib
import json
import logging
import re
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
    sha256_text,
)

logger = logging.getLogger(__name__)

CONFIDENCE_DEFAULT = 0.5
CONFIDENCE_STEP = 0.1


def confidence_path(workspace: Path) -> Path:
    return Path(workspace) / ".rsis" / "confidence.json"


def canonical_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "exchange" / "canonical.json"


def exchange_ledger_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "federation" / "exchange.jsonl"


def _load_confidence(workspace: Path) -> dict:
    return load_json(confidence_path(workspace),
                     {"version": 1, "items": {}})


def corroborate(workspace: Path, item_sha: str, agreement: bool,
                provider: str = "system") -> dict:
    """Update confidence for an item based on a peer verdict."""
    data = _load_confidence(workspace)
    items = data.setdefault("items", {})
    item = items.get(item_sha, {"confidence": CONFIDENCE_DEFAULT,
                                "corroborations": 0, "contradictions": 0,
                                "history": []})
    if agreement:
        item["corroborations"] = int(item.get("corroborations", 0)) + 1
        item["confidence"] = min(1.0, float(item.get("confidence", CONFIDENCE_DEFAULT))
                                 + CONFIDENCE_STEP)
    else:
        item["contradictions"] = int(item.get("contradictions", 0)) + 1
        item["confidence"] = max(0.0, float(item.get("confidence", CONFIDENCE_DEFAULT))
                                 - CONFIDENCE_STEP)
    item["history"].append({"ts": now_ts(), "provider": provider,
                            "agreement": agreement,
                            "confidence": round(item["confidence"], 3)})
    items[item_sha] = item
    save_json(confidence_path(workspace), data)
    append_jsonl(exchange_ledger_path(workspace), {
        "type": "confidence", "item": item_sha, "provider": provider,
        "agreement": agreement, "confidence_delta":
            CONFIDENCE_STEP if agreement else -CONFIDENCE_STEP, "ts": now_ts()})
    emit(workspace, "exchange_confidence", item=item_sha[:12],
         confidence=item["confidence"], provider=provider)
    return item


def confidence(workspace: Path, item_sha: str) -> float:
    items = _load_confidence(workspace).get("items", {})
    return float(items.get(item_sha, {}).get("confidence", CONFIDENCE_DEFAULT))


def _norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def canonical_key(title: str, content: str) -> str:
    """Deterministic canonical key: normalized title + content similarity."""
    head = " ".join(re.findall(r"[a-z0-9]+", content.lower()))[:200]
    return sha256_text(_norm_title(title) + "|" + head)


def find_canonical(workspace: Path, title: str, content: str,
                   threshold: float = 0.8) -> Optional[str]:
    """Return an existing canonical sha if title/content are near-dupes."""
    data = load_json(canonical_path(workspace),
                     {"version": 1, "items": {}})
    for sha, rec in data.get("items", {}).items():
        if _norm_title(title) == _norm_title(rec.get("title", "")):
            sim = difflib.SequenceMatcher(None, content[:500], rec.get("content", "")[:500])
            if sim.ratio() >= threshold:
                return sha
    return None


def adopt(workspace: Path, title: str, content: str, origin: str,
          item_sha: Optional[str] = None) -> dict:
    """Canonical adoption: dedupe against existing items, record the item."""
    sha = item_sha or canonical_key(title, content)
    existing = find_canonical(workspace, title, content)
    data = load_json(canonical_path(workspace),
                     {"version": 1, "items": {}})
    items = data.setdefault("items", {})
    if existing and existing != sha:
        # same durable rule already adopted — record a duplicate reference
        items[sha] = {"title": title, "content": content[:500],
                      "origin": origin, "duplicate_of": existing,
                      "adopted": now_ts()}
        save_json(canonical_path(workspace), data)
        append_jsonl(exchange_ledger_path(workspace), {
            "type": "dedup", "item": sha, "canonical": existing,
            "provider": origin, "ts": now_ts()})
        emit(workspace, "exchange_deduped", item=sha[:12],
             canonical=existing[:12])
        return {"deduped": True, "canonical": existing}
    items[sha] = {"title": title, "content": content[:500], "origin": origin,
                  "duplicate_of": None, "adopted": now_ts()}
    save_json(canonical_path(workspace), data)
    append_jsonl(exchange_ledger_path(workspace), {
        "type": "adopt", "item": sha, "provider": origin, "ts": now_ts()})
    emit(workspace, "exchange_adopted", item=sha[:12], origin=origin)
    return {"deduped": False, "canonical": sha}


def provenance_intact(envelope: dict, min_hops: int = 3) -> tuple[bool, list[str]]:
    """Verify an envelope's federation history is unbroken across hops."""
    issues: list[str] = []
    history = envelope.get("provenance", {}).get("federation_history", [])
    if len(history) + 1 < min_hops:
        issues.append(f"history too short ({len(history)+1} hops < {min_hops})")
    origin = envelope.get("origin", {})
    if not origin.get("instance") or not origin.get("fingerprint"):
        issues.append("missing origin")
    current = origin.get("instance")
    for hop in history:
        if hop.get("from") != current:
            issues.append(f"broken hop: {hop.get('from')} != {current}")
        current = hop.get("to")
    return (len(issues) == 0, issues)


def record_hop(workspace: Path, envelope: dict, to_instance: str) -> dict:
    """Record one federation hop (extend history, preserving origin)."""
    env = dict(envelope)
    prov = dict(env.get("provenance", {}))
    history = list(prov.get("federation_history", []))
    history.append({"from": env.get("origin", {}).get("instance"),
                    "to": to_instance, "ts": now_ts()})
    prov["federation_history"] = history
    env["provenance"] = prov
    append_jsonl(exchange_ledger_path(workspace), {
        "type": "hop", "item": env.get("content_sha", ""), "to": to_instance,
        "ts": now_ts()})
    return env


def status(workspace: Path) -> dict:
    conf = _load_confidence(workspace)
    canon = load_json(canonical_path(workspace), {"version": 1, "items": {}})
    ledger = read_jsonl(exchange_ledger_path(workspace))
    return {"items": len(conf.get("items", {})),
            "canonical_items": len(canon.get("items", {})),
            "ledger_records": len(ledger),
            "avg_confidence": round(sum(
                float(i.get("confidence", 0)) for i in conf.get("items", {}).values())
                / max(1, len(conf.get("items", {}))), 3)}
