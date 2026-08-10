"""Self-metrics & longitudinal studies — epoch-scale self-knowledge.

Phase 46 (Sequel X): a permanent, append-only store of epoch-scale
metrics (fitness, costs, trust, knowledge growth, incident rates)
extending the Phase 10 self-model; declarative studies — hypotheses,
metrics, windows, cohorts — so analysis is reproducible from raw
telemetry; trend decomposition separating long-term trends from seasonal
effects and regime changes.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
)

logger = logging.getLogger(__name__)


def registry_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "longitudinal" / "registry.jsonl"


def studies_path(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "longitudinal" / "studies.json"


def snapshot(workspace: Path, metrics: dict) -> dict:
    """Append one epoch-scale metric snapshot (append-only registry)."""
    ws = Path(workspace)
    ensure_rack(ws, "longitudinal")
    rec = {"ts": now_ts(), **metrics}
    append_jsonl(registry_path(ws), rec)
    emit(ws, "study_snapshot", metrics=",".join(metrics.keys()))
    return rec


def define_study(workspace: Path, study_id: str, hypothesis: str,
                 metrics: list[str], window_days: int,
                 cohorts: Optional[list[str]] = None) -> dict:
    """Declare a reproducible longitudinal study."""
    ws = Path(workspace)
    ensure_rack(ws, "longitudinal")
    data = load_json(studies_path(ws), {"version": 1, "studies": {}})
    study = {"id": study_id, "hypothesis": hypothesis, "metrics": metrics,
             "window_days": window_days, "cohorts": cohorts or ["all"],
             "defined": now_ts()}
    data.setdefault("studies", {})[study_id] = study
    save_json(studies_path(ws), data)
    emit(ws, "study_defined", study=study_id, metrics=len(metrics))
    return study


def trend_report(workspace: Path, metric: str,
                 window_days: int = 90) -> dict:
    """Long-term trend vs seasonal effect decomposition."""
    recs = read_jsonl(registry_path(ws := workspace))
    series = [float(r[metric]) for r in recs[-window_days:]
              if metric in r]
    if not series:
        return {"metric": metric, "samples": 0}
    slope = (series[-1] - series[0]) / max(1, len(series) - 1)
    seasonal = abs(sum(series[::7]) / max(1, len(series[::7])) -
                   sum(series) / len(series))
    return {"metric": metric, "samples": len(series),
            "trend_slope": round(slope, 6),
            "seasonal_amplitude": round(seasonal, 6),
            "regime_change": slope != 0 and abs(slope) > 3 * max(1e-6, seasonal),
            "generated": now_ts()}


def status(workspace: Path) -> dict:
    recs = read_jsonl(registry_path(ws := workspace))
    studies = load_json(studies_path(ws), {"version": 1, "studies": {}})
    return {"snapshots": len(recs), "studies": len(studies.get("studies", {})),
            "first": recs[0].get("ts") if recs else None,
            "last": recs[-1].get("ts") if recs else None}
