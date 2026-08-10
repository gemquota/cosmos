"""Cross-ecosystem standards — protocol versions, coexistence, sunset.

Phase 41 (Sequel IX): protocols stop being Cosmos-specific and become
community standards. This module tracks supported protocol versions, a
change process (proposals → conformance → deprecation), version
coexistence with capability negotiation, and a sunset calendar —
``rack/standards/registry.json``.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, load_json, now_ts, save_json

logger = logging.getLogger(__name__)

DEFAULT_REGISTRY = {
    "version": 1,
    "standards": [
        {"id": "cosmos-protocol", "versions": ["1"], "status": "current",
         "sunset": None, "conformance": "tests/test_protocol.py"},
    ],
    "change_process": [
        "proposal", "conformance-test", "review", "deprecation-window",
        "sunset",
    ],
}


def registry_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "standards" / "registry.json"


def registry(workspace: Path) -> dict:
    return load_json(registry_path(workspace), DEFAULT_REGISTRY)


def register_version(workspace: Path, standard: str, version: str,
                     status: str = "current", sunset: Optional[str] = None) -> dict:
    """Register a protocol version (coexistence allowed)."""
    ws = Path(workspace)
    reg = registry(ws)
    entry = next((s for s in reg.get("standards", [])
                  if s.get("id") == standard), None)
    if entry is None:
        entry = {"id": standard, "versions": [], "status": status,
                 "sunset": sunset, "conformance": None}
        reg.setdefault("standards", []).append(entry)
    versions = entry.setdefault("versions", [])
    if version not in versions:
        versions.append(version)
    entry["status"] = status
    entry["sunset"] = sunset
    save_json(registry_path(ws), reg)
    emit(ws, "standard_version", standard=standard, version=version,
         status=status)
    return entry


def deprecate(workspace: Path, standard: str, version: str,
              sunset: str) -> bool:
    """Open a deprecation window (sunset calendar entry)."""
    ws = Path(workspace)
    reg = registry(ws)
    entry = next((s for s in reg.get("standards", [])
                  if s.get("id") == standard), None)
    if entry is None or version not in entry.get("versions", []):
        return False
    entry["status"] = "deprecated"
    entry["sunset"] = sunset
    reg.setdefault("sunset_calendar", []).append(
        {"standard": standard, "version": version, "sunset": sunset,
         "ts": now_ts()})
    save_json(registry_path(ws), reg)
    emit(ws, "standard_deprecated", standard=standard, version=version,
         sunset=sunset)
    return True


def conformance_status(workspace: Path) -> dict:
    reg = registry(workspace)
    return {"standards": reg.get("standards", []),
            "sunset_calendar": reg.get("sunset_calendar", []),
            "change_process": reg.get("change_process", [])}
