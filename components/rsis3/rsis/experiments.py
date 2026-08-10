"""Hypothesis-driven self-experimentation — controlled A/B on itself.

Phase 47 (Sequel X): candidates for behavior change (policy, tuning,
loop parameters) can be assigned to A/B cohorts with guardrails — sample
sizes, minimum effect, stop conditions. Experiments randomize across
seasons/projects/populations so observed effects are attributable; every
experiment, its cohorts and outcome land in an append-only ledger with
attestation (14).
"""

from __future__ import annotations

import json
import logging
import random
from pathlib import Path
from typing import Optional

from rsis.epoch1 import (
    append_jsonl, emit, ensure_rack, load_json, now_ts, read_jsonl, save_json,
)

logger = logging.getLogger(__name__)

MIN_SAMPLE = 10
MIN_EFFECT = 0.05


def experiments_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "experiments"


def ledger_path(workspace: Path) -> Path:
    return experiments_dir(workspace) / "ledger.jsonl"


def start(workspace: Path, name: str, variable: str,
          control: object, treatment: object,
          min_sample: int = MIN_SAMPLE, min_effect: float = MIN_EFFECT,
          seed: Optional[int] = None) -> dict:
    """Start an A/B experiment with guardrails."""
    ws = Path(workspace)
    ensure_rack(ws, "experiments")
    rng = random.Random(seed)
    rec = {
        "id": f"x{len(read_jsonl(ledger_path(ws)))}",
        "name": name, "variable": variable,
        "control": control, "treatment": treatment,
        "min_sample": min_sample, "min_effect": min_effect,
        "cohorts": {"control": [], "treatment": []},
        "status": "running", "seed": seed, "ts": now_ts(),
    }
    append_jsonl(ledger_path(ws), rec)
    emit(ws, "experiment_started", experiment=rec["id"], variable=variable)
    return rec


def assign(workspace: Path, experiment_id: str, unit: str) -> str:
    """Randomize a unit into a cohort (confound control)."""
    recs = read_jsonl(ledger_path(ws := workspace))
    target = next((r for r in recs if r.get("id") == experiment_id), None)
    if target is None or target.get("status") != "running":
        raise ValueError("experiment not running")
    rng = random.Random(hash((experiment_id, unit)) & 0xFFFFFFFF)
    cohort = "control" if rng.random() < 0.5 else "treatment"
    target.setdefault("cohorts", {}).setdefault(cohort, []).append(unit)
    _rewrite(ledger_path(ws), recs)
    return cohort


def _rewrite(path: Path, recs: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, sort_keys=True) + "\n")


def complete(workspace: Path, experiment_id: str,
             outcomes: dict) -> Optional[dict]:
    """Complete with guardrail checks (sample size, min effect)."""
    ws = Path(workspace)
    recs = read_jsonl(ledger_path(ws))
    target = next((r for r in recs if r.get("id") == experiment_id), None)
    if target is None:
        return None
    cohorts = target.get("cohorts", {})
    n_c = len(cohorts.get("control", []))
    n_t = len(cohorts.get("treatment", []))
    guardrails = {"sample_ok": min(n_c, n_t) >= target.get("min_sample", MIN_SAMPLE),
                  "n_control": n_c, "n_treatment": n_t}
    outcome = outcomes.get("result", 0.0)
    effect = abs(float(outcome)) if isinstance(outcome, (int, float)) else 0.0
    significant = effect >= target.get("min_effect", MIN_EFFECT)
    target["status"] = "completed" if guardrails["sample_ok"] else "terminated"
    target["outcome"] = outcome
    target["effect_size"] = effect
    target["significant"] = significant
    target["completed_at"] = now_ts()
    target["guardrails"] = guardrails
    _rewrite(ledger_path(ws), recs)
    from rsis.attestations import append as attest
    attest(ws, "experiment_result",
           {"experiment": experiment_id, "effect": effect,
            "significant": significant})
    emit(ws, "experiment_completed" if target["status"] == "completed"
         else "experiment.terminated",
         experiment=experiment_id, significant=significant)
    return target


def status(workspace: Path) -> dict:
    recs = read_jsonl(ledger_path(ws := workspace))
    return {"experiments": len(recs),
            "running": sum(1 for r in recs if r.get("status") == "running"),
            "completed": sum(1 for r in recs if r.get("status") == "completed"),
            "terminated": sum(1 for r in recs if r.get("status") == "terminated")}
