"""Trust calibration — ask-vs-act, per human and context.

Phase 39 (Sequel VIII): the system knows when to ask and when to act,
per human and context. Extending the Phase 10 self-model, it predicts
for each (human, action, project) whether to ask first — trained on
approval outcomes and post-hoc corrections. Over-trust (acted when they
wanted to be asked) and under-trust (asked when they wanted autonomy)
are first-class metrics with policy-defined targets; periodic
recalibration adjusts ask thresholds from measured outcomes.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, load_json, now_ts, read_jsonl, save_json,
)

logger = logging.getLogger(__name__)

DEFAULT_OVERTRUST_TARGET = 0.10
DEFAULT_UNDERTRUST_TARGET = 0.10


def trust_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "trust"


def outcomes_path(workspace: Path) -> Path:
    return trust_dir(workspace) / "outcomes.jsonl"


def thresholds_path(workspace: Path) -> Path:
    return trust_dir(workspace) / "thresholds.json"


def record_outcome(workspace: Path, human: str, action: str, project: str,
                   asked: bool, wanted_ask: bool) -> dict:
    """Log one ask-vs-act outcome."""
    ws = Path(workspace)
    rec = {"human": human, "action": action, "project": project,
           "asked": bool(asked), "wanted_ask": bool(wanted_ask),
           "ts": now_ts()}
    append_jsonl(outcomes_path(ws), rec)
    emit(ws, "trust_asked" if asked else "trust_acted",
         human=human, action=action)
    return rec


def metrics(workspace: Path) -> dict:
    """Over-trust / under-trust rates per human (policy-defined targets)."""
    outcomes = read_jsonl(outcomes_path(workspace))
    by_human: dict = {}
    for o in outcomes:
        h = o.get("human", "?")
        d = by_human.setdefault(h, {"n": 0, "over": 0, "under": 0})
        d["n"] += 1
        if not o.get("asked") and o.get("wanted_ask"):
            d["over"] += 1          # acted when they wanted to be asked
        elif o.get("asked") and not o.get("wanted_ask"):
            d["under"] += 1         # asked when they wanted autonomy
    per = {h: {"n": d["n"],
               "over_trust": round(d["over"] / d["n"], 3) if d["n"] else 0.0,
               "under_trust": round(d["under"] / d["n"], 3) if d["n"] else 0.0}
           for h, d in by_human.items()}
    return {"per_human": per,
            "over_trust_target": DEFAULT_OVERTRUST_TARGET,
            "under_trust_target": DEFAULT_UNDERTRUST_TARGET}


def recalibrate(workspace: Path) -> dict:
    """Adjust ask thresholds from measured outcomes (evidence-driven)."""
    ws = Path(workspace)
    m = metrics(ws)
    thresholds = load_json(thresholds_path(ws),
                           {"version": 1, "ask_threshold": 0.5, "by_human": {}})
    for human, d in m.get("per_human", {}).items():
        # over-trust -> ask more (raise threshold); under-trust -> ask less
        adjust = 0.0
        if d["over_trust"] > DEFAULT_OVERTRUST_TARGET:
            adjust = +0.05
        if d["under_trust"] > DEFAULT_UNDERTRUST_TARGET:
            adjust = -0.05
        cur = thresholds.setdefault("by_human", {}).get(human,
                                                        thresholds.get("ask_threshold", 0.5))
        thresholds["by_human"][human] = round(max(0.0, min(1.0, cur + adjust)), 3)
    save_json(thresholds_path(ws), thresholds)
    emit(ws, "trust_recalibrated", humans=len(m.get("per_human", {})))
    return thresholds


def status(workspace: Path) -> dict:
    return {"metrics": metrics(workspace),
            "thresholds": load_json(thresholds_path(workspace),
                                    {"version": 1})}
