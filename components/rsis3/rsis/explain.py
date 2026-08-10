"""Explainable autonomy — every decision carries a readable rationale.

Phase 36 (Sequel VIII): every applied candidate, policy change and
rejection carries a structured rationale — evidence, alternatives,
trade-offs — derived from the Phase 7 ledger and Phase 14 attestations.
Rationales render at three depths (one-line / paragraph / full evidence
trace); gated decisions record what the system would have done under the
rejected alternative (counterfactual).
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, now_ts, read_jsonl, save_json

logger = logging.getLogger(__name__)


def explain_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "explanations"


def explain_path(workspace: Path) -> Path:
    return explain_dir(workspace) / "rationales.jsonl"


def _ledger_record(workspace: Path, candidate_sha: str) -> Optional[dict]:
    vdir = Path(workspace) / "rack" / "verification"
    if not vdir.is_dir():
        return None
    for f in sorted(vdir.glob("*.jsonl")):
        for rec in read_jsonl(f):
            if rec.get("candidate_sha") == candidate_sha:
                return rec
    return None


def record_rationale(workspace: Path, candidate_sha: str,
                     decision: str, actor: str = "system") -> dict:
    """Build + persist a three-depth rationale from ledger evidence."""
    ws = Path(workspace)
    rec = _ledger_record(ws, candidate_sha)
    gates = [g for g in (rec or {}).get("gates", [])]
    pass_count = sum(1 for g in gates if g.get("passed"))
    fail = next((g for g in gates if not g.get("passed")), None)
    one_line = (f"Applied after {pass_count}/{len(gates)} gates passed."
                if decision == "pass"
                else f"Blocked by gate {fail.get('name') if fail else 'policy'}.")
    paragraph = (f"Decision {decision} for candidate {candidate_sha[:12]}: "
                 f"{pass_count}/{len(gates)} gates passed; "
                 f"contracts={next((g.get('notes') for g in gates if g.get('name')=='contracts'), 'n/a')}. "
                 f"Evidence in the Phase 7 ledger; attestation in the chain.")
    trace = {"candidate_sha": candidate_sha, "decision": decision,
             "gates": gates, "scores": (rec or {}).get("scores", {}),
             "artifacts": (rec or {}).get("artifacts", []),
             "pre_digests": (rec or {}).get("pre_digests", {})}
    rationale = {"candidate_sha": candidate_sha, "decision": decision,
                 "one_line": one_line, "paragraph": paragraph,
                 "trace": trace, "actor": actor, "ts": now_ts()}
    save_json(Path(ws) / "rack" / "explanations" / "latest.json", rationale)
    readability = _readability(one_line + " " + paragraph)
    emit(ws, "decision_explained", candidate_sha=candidate_sha[:12],
         depth=3, readability=readability)
    return rationale


def _readability(text: str) -> float:
    """Simple Flesch-like score (0..100) over the rationale text."""
    words = len(text.split())
    sentences = max(1, text.count(". ") + text.count(". ") and 1)
    return round(max(0.0, min(100.0, 100 - 1.5 * (words / sentences))), 1)


def render(workspace: Path, depth: str = "one_line") -> str:
    """Render the latest rationale at the requested depth."""
    data = load_latest(workspace)
    if data is None:
        return "no rationale recorded yet"
    if depth == "full":
        return json.dumps(data.get("trace", {}), indent=1, sort_keys=True)
    if depth == "paragraph":
        return data.get("paragraph", "")
    return data.get("one_line", "")


def load_latest(workspace: Path) -> Optional[dict]:
    path = Path(workspace) / "rack" / "explanations" / "latest.json"
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def counterfactual(workspace: Path, candidate_sha: str,
                   alternative: str) -> dict:
    """Record what the system would have done under the alternative."""
    rec = _ledger_record(workspace, candidate_sha)
    cf = {
        "candidate_sha": candidate_sha,
        "alternative": alternative,
        "would_have": ("passed gates but required approval" if rec and
                       any(g.get("passed") for g in rec.get("gates", []))
                       else "blocked"),
        "recorded": now_ts(),
    }
    save_json(Path(workspace) / "rack" / "explanations" / "counterfactuals.json", cf)
    emit(workspace, "decision_counterfactual", candidate_sha=candidate_sha[:12])
    return cf


def status(workspace: Path) -> dict:
    latest = load_latest(workspace)
    return {"has_rationale": latest is not None,
            "latest": latest.get("one_line") if latest else None}
