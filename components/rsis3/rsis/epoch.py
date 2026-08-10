"""Epoch capstone — Enduring Intelligence, decade program, epoch registry.

Phase 50 (Sequel X): the system commits to a decade-scale horizon and
closes Epoch 1. A 10-year operational program replaces the 365-day
horizon; ``rack/epochs.json`` records both epochs with per-phase status,
arc maps and the cross-roadmap invariant; the capstone validates that the
epoch's implementation status is complete (exit criteria remain live
validation).
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, ensure_rack, load_json, now_ts, save_json

logger = logging.getLogger(__name__)

PROGRAM_YEARS = 10


def epochs_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "epochs.json"


def decade_program(workspace: Path, ratified_by: str = "approver") -> dict:
    """Ratify the decade-scale program charter."""
    ws = Path(workspace)
    ensure_rack(ws, "epochs")
    program = {
        "id": "epoch-1-decade-program",
        "years": PROGRAM_YEARS,
        "horizon": "2026-2036",
        "charter": [
            "autonomy is cumulative but never unconditional",
            "quarterly human ratification remains the only standing touchpoint",
            "every expansion inherits memory, verification, cost, policy, "
            "provenance and observability controls",
        ],
        "ratified_by": ratified_by,
        "ratified_at": now_ts(),
        "status": "active",
    }
    save_json(Path(ws) / "rack" / "epochs" / "decade-program.json", program)
    emit(ws, "epoch_decade_ratified", years=PROGRAM_YEARS)
    return program


def registry(workspace: Path, phases: list[dict],
             arcs: list[dict]) -> dict:
    """Write rack/epochs.json: both epochs, phase status, arc maps."""
    ws = Path(workspace)
    ensure_rack(ws, "epochs")
    reg = {
        "epochs": [
            {"id": 1, "name": "Epoch 1 — one lineage to decade-scale maturity",
             "phases": "1–50", "sequels": "I–X",
             "status": "implemented (live exit validation pending)"},
            {"id": 2, "name": "Epoch 2 — the Age of Living Systems",
             "phases": "51–100", "sequels": "XI–XX",
             "status": "queued"},
        ],
        "invariant": "autonomy is cumulative but never unconditional",
        "phases": phases,
        "arcs": arcs,
        "generated": now_ts(),
    }
    save_json(epochs_path(ws), reg)
    emit(ws, "epoch_reported", phases=len(phases), epochs=2)
    return reg


def capstone_check(workspace: Path) -> dict:
    """Epoch-1 capstone validation: implementation status + guardrails."""
    ws = Path(workspace)
    from rsis.endurance import guardrails
    from rsis.attestations import chain_summary
    g = guardrails(ws)
    chain = chain_summary(ws)
    result = {
        "guardrails_ok": g.get("ok"),
        "attestation_chain": chain,
        "decade_program": load_json(Path(ws) / "rack" / "epochs" /
                                    "decade-program.json"),
        "epochs_registry": load_json(epochs_path(ws)),
        "ts": now_ts(),
    }
    save_json(Path(ws) / "rack" / "epochs" / "capstone.json", result)
    emit(ws, "epoch_enduring", ok=bool(g.get("ok")))
    return result


def status(workspace: Path) -> dict:
    ws = Path(workspace)
    return {
        "decade": load_json(Path(ws) / "rack" / "epochs" / "decade-program.json"),
        "registry": load_json(epochs_path(ws)),
        "capstone": load_json(Path(ws) / "rack" / "epochs" / "capstone.json"),
    }
