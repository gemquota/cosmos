"""Interface to the immutable AI Evaluator subprocess.

The evaluator runs as a separate process with read-only code. This module
manages calling it and returning structured results.
"""

import hashlib
import json
import logging
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from rsis.config import CONFIG
from rsis.telemetry import CostLedger, default_ledger
from rsis.budgets import check_budget

logger = logging.getLogger(__name__)


@dataclass
class EvalResult:
    decision: str  # "PASS" | "FAIL"
    scores: dict = field(default_factory=dict)
    rationale: str = ""
    suggestions: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return self.decision == "PASS"

    @property
    def score_avg(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)


class EvaluatorClient:
    """Client for the immutable evaluator subprocess."""

    def __init__(self, evaluator_path: Optional[str] = None,
                 ledger: Optional[CostLedger] = None):
        self._evaluator_path = Path(
            evaluator_path or CONFIG.evaluator.evaluator_path
        ).resolve()
        self.ledger = ledger or default_ledger()

    def verify_integrity(self) -> str:
        """Compute and return the evaluator's SHA-256 digest."""
        h = hashlib.sha256()
        with open(self._evaluator_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()

    def evaluate(self, candidate: dict) -> EvalResult:
        """Send a candidate to the evaluator and return the result."""
        logger.info("Submitting candidate to evaluator: %s",
                     candidate.get("description", "no description"))

        input_json = json.dumps(candidate)
        # Token estimate (chars/4) — exact counts are unknowable client-side;
        # the ledger needs a baseline for budget pre-flight and cost records.
        in_tokens = max(1, (len(input_json) + 1200) // 4)
        out_tokens = 200

        # Hard cost cap: refuse the call when the budget is spent.
        if not self.ledger.guard_budget(
                CONFIG.evaluator.model, in_tokens, out_tokens):
            logger.error("Evaluator call refused: LLM budget cap exceeded")
            return EvalResult(
                decision="FAIL",
                rationale="LLM budget cap exceeded — evaluator call refused")

        # Phase 8: per-loop daily budget — fail-close when the ledger exists.
        ws = Path(CONFIG.workspace_dir)
        if (ws / ".rsis" / "budgets.json").is_file():
            budget = check_budget(ws, "evaluator")
            if not budget["allowed"]:
                logger.error(
                    "Evaluator call refused: daily budget fail-close "
                    "($%.4f of $%.4f)", budget["spend"], budget["limit"])
                return EvalResult(
                    decision="FAIL",
                    rationale=(f"daily budget fail-close for evaluator "
                               f"(${budget['spend']:.4f} of "
                               f"${budget['limit']:.4f})"))

        try:
            started = time.monotonic()
            r = subprocess.run(
                [sys.executable, str(self._evaluator_path)],
                input=input_json,
                capture_output=True, text=True, timeout=60,
            )
            latency_s = time.monotonic() - started
            self.ledger.record_llm(
                "evaluator", CONFIG.evaluator.model,
                latency_s=latency_s,
                usage={"prompt_tokens": in_tokens,
                       "completion_tokens": out_tokens})
        except subprocess.TimeoutExpired:
            logger.error("Evaluator timed out")
            self.ledger.record_llm(
                "evaluator", CONFIG.evaluator.model,
                usage={"prompt_tokens": in_tokens, "completion_tokens": 0},
                error=True)
            return EvalResult(decision="FAIL", rationale="Evaluator timed out")
        except Exception as e:
            logger.error("Evaluator process error: %s", e)
            self.ledger.record_llm(
                "evaluator", CONFIG.evaluator.model,
                usage={"prompt_tokens": in_tokens, "completion_tokens": 0},
                error=True)
            return EvalResult(decision="FAIL", rationale=f"Process error: {e}")

        if r.returncode != 0:
            logger.error("Evaluator exited with code %d: %s",
                         r.returncode, r.stderr.strip())
            self.ledger.record_llm(
                "evaluator", CONFIG.evaluator.model,
                usage={"prompt_tokens": in_tokens, "completion_tokens": 0},
                error=True)
            return EvalResult(decision="FAIL", rationale=r.stderr.strip())

        try:
            data = json.loads(r.stdout)
        except json.JSONDecodeError as e:
            logger.error("Evaluator output parse error: %s", e)
            return EvalResult(decision="FAIL", rationale="Output parse error")

        if "error" in data:
            logger.error("Evaluator error: %s", data["error"])
            return EvalResult(decision="FAIL", rationale=data["error"])

        return EvalResult(
            decision=data.get("decision", "FAIL"),
            scores=data.get("scores", {}),
            rationale=data.get("rationale", ""),
            suggestions=data.get("suggestions", []),
        )
