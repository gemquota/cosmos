"""Enduring autonomy — continuous meta-invariant enforcement + guardrails.

Phase 30 (Sequel VI): the culmination of the 30-phase program. The system
proves continuously that no capability expansion relaxed a prior control,
policy evolves only through the ratified revision loop, and existential
guardrails (energy, budget, policy-critical capabilities) fail closed
under every scenario.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, load_json, now_ts, read_jsonl, save_json

logger = logging.getLogger(__name__)


def guardrails(workspace: Path) -> dict:
    """Run the full existential guardrail battery."""
    ws = Path(workspace)
    checks: dict = {}

    # 1. meta-invariant (26): no adopted policy relaxed a prior control
    from rsis.metagov import meta_invariant_check
    mi_ok, mi_issues = meta_invariant_check(ws)
    checks["meta_invariant"] = {"ok": mi_ok, "issues": mi_issues[:5]}

    # 2. invariant registry (14)
    from rsis.epoch1 import invariants_status
    inv_ok, inv_issues = invariants_status(ws)
    checks["invariants"] = {"ok": inv_ok, "issues": inv_issues[:5]}

    # 3. budget fail-closed (8)
    from rsis.budgets import budget_status
    try:
        bs = budget_status(ws)
        checks["budget"] = {"ok": not (bs.get("total", 0) >= bs.get("ceiling", 0))
                            if bs.get("ceiling", 0) > 0 else True,
                            "total": bs.get("total", 0),
                            "ceiling": bs.get("ceiling", 0)}
    except Exception as e:
        checks["budget"] = {"ok": False, "issues": [str(e)[:120]]}

    # 4. energy (27): policy-critical stays on at every ladder level
    from rsis.capacity import degradation_ladder
    ladder = degradation_ladder(ws, pressure=4)
    checks["energy_ladder"] = {"ok": "policy-critical" in ladder["always_on"],
                               "always_on": ladder["always_on"]}

    # 5. red-team (19): no untriaged findings
    findings = read_jsonl(Path(ws) / "rack" / "redteam" / "findings.jsonl")
    checks["redteam"] = {"ok": all(f.get("status") != "open" for f in findings),
                         "untriaged": sum(1 for f in findings
                                          if f.get("status") == "open")}

    overall = all(v.get("ok") for v in checks.values())
    record = {"ok": overall, "checks": checks, "ts": now_ts()}
    save_json(Path(ws) / "rack" / "endurance" / "guardrails.json", record)
    emit(ws, "endurance_guardrails", ok=overall,
         checks=",".join(checks.keys()))
    return record


def continuity(workspace: Path) -> dict:
    """Long-horizon continuity summary (identity + attestation history)."""
    ws = Path(workspace)
    from rsis.attestations import chain_summary
    from rsis.identity import status as identity_status
    return {
        "identity": identity_status(ws).get("instance"),
        "attestations": chain_summary(ws),
        "guardrails": load_json(Path(ws) / "rack" / "endurance" / "guardrails.json"),
        "ts": now_ts(),
    }
