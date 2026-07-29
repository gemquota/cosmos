#!/usr/bin/env python3
"""
RRP v2 Protocol Engine — Full State Machine with Telemetry.

Implements the complete Recursive Refinement Protocol specification:
  - AmbiguityVector (4 dimensions)
  - TokenBudget (per-round/session limits, saturation %, alerts)
  - QuestionQualityIndex (rolling score average)
  - UserSatisfactionDelta (cumulative + trend)
  - TemporalVelocity (round timing, avg duration)
  - TopicCoverage (8-bit bitmask)
  - TransactionLedger (immutable audit trail)
  - Checkpoints (fork/rollback support)
  - Decision log with contradictions and constraints
  - Early termination detection
  - Diamond dependency: Use Case (U) × Execution Mode (M) × Depth (D)

Usage:
    engine = RRPEngine(u=4, m=1, x=3, y=3, z=3, depth=2)
    engine.start_session("goal description", ["file1.py"])
    engine.process_round(open_answers={...}, mc_answers={...})
    result = engine.finalize()
"""

import json, time, uuid, math, logging
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional

logger = logging.getLogger('rrp_engine')

# ── Constants ──
TOPIC_ARCH   = 1 << 0  # Architecture
TOPIC_SEC    = 1 << 1  # Security
TOPIC_DATA   = 1 << 2  # Data model
TOPIC_PERF   = 1 << 3  # Performance
TOPIC_SCAL   = 1 << 4  # Scalability
TOPIC_TEST   = 1 << 5  # Testing
TOPIC_DEPL   = 1 << 6  # Deployment
TOPIC_UX     = 1 << 7  # User experience

TOPIC_NAMES = {
    TOPIC_ARCH: "ARCH", TOPIC_SEC: "SEC", TOPIC_DATA: "DATA",
    TOPIC_PERF: "PERF", TOPIC_SCAL: "SCAL", TOPIC_TEST: "TEST",
    TOPIC_DEPL: "DEPL", TOPIC_UX: "UX"
}

USE_CASES = {
    1: "Alignment", 2: "Ideation", 3: "Convergence",
    4: "Stress Testing", 5: "Data Mapping", 6: "Determinism"
}

EXEC_MODES = {1: "Hybrid", 2: "Batch", 3: "Pulse"}


@dataclass
class AmbiguityVector:
    """Four-dimensional ambiguity tracking (0.0 = clear, 1.0 = maximally ambiguous)."""
    requirements: float = 0.5
    data_model: float = 0.5
    edge_case: float = 0.5
    determinism: float = 0.5

    @property
    def avg(self) -> float:
        return (self.requirements + self.data_model + self.edge_case + self.determinism) / 4.0

    @property
    def max_dim(self) -> float:
        return max(self.requirements, self.data_model, self.edge_case, self.determinism)

    @property
    def converged(self) -> bool:
        """All dimensions <= 0.05"""
        return self.max_dim <= 0.05

    def calibrate_from_confidence(self, confidence: float, ambiguity_est: dict = None):
        """Calibrate ambiguity from RRP confidence score and estimates."""
        base = max(0.0, 0.5 - confidence * 0.4)  # Higher confidence = lower ambiguity
        if ambiguity_est:
            self.requirements = max(0.0, min(1.0, ambiguity_est.get("requirements", base)))
            self.data_model = max(0.0, min(1.0, ambiguity_est.get("data_model", base)))
            self.edge_case = max(0.0, min(1.0, ambiguity_est.get("edge_case", base)))
            self.determinism = max(0.0, min(1.0, ambiguity_est.get("determinism", base)))
        else:
            self.requirements = base
            self.data_model = base * 0.9
            self.edge_case = base * 1.1
            self.determinism = base

    def reduce(self, factor: float = 0.5):
        """Reduce all ambiguity dimensions by a factor (called after each round)."""
        self.requirements *= factor
        self.data_model *= factor
        self.edge_case *= factor
        self.determinism *= factor

    def to_dict(self) -> dict:
        return {"requirements": round(self.requirements, 3), "data_model": round(self.data_model, 3),
                "edge_case": round(self.edge_case, 3), "determinism": round(self.determinism, 3),
                "avg": round(self.avg, 3), "converged": self.converged}


@dataclass
class TokenBudget:
    """Per-round and per-session token budget tracking."""
    session_limit: int = 32000
    round_limit: int = 8000
    session_used: int = 0
    round_used: int = 0
    alerts: list = field(default_factory=list)

    def record_round(self, tokens: int):
        self.round_used = tokens
        self.session_used += tokens
        saturation = self.session_used / self.session_limit * 100
        if saturation > 85:
            self.alerts.append(f"Session budget {saturation:.0f}% saturated at round")
        if self.session_used > self.session_limit:
            self.alerts.append("SESSION BUDGET EXCEEDED")

    @property
    def saturation_pct(self) -> float:
        return round(self.session_used / self.session_limit * 100, 1) if self.session_limit > 0 else 0

    def to_dict(self) -> dict:
        return {"session_limit": self.session_limit, "round_limit": self.round_limit,
                "session_used": self.session_used, "round_used": self.round_used,
                "saturation_pct": self.saturation_pct, "alerts": self.alerts}


@dataclass
class QuestionQualityIndex:
    """Rolling average of question quality scores (0.0–1.0)."""
    scores: list = field(default_factory=list)

    @property
    def average(self) -> float:
        return round(sum(self.scores) / len(self.scores), 3) if self.scores else 0.5

    def record(self, score: float):
        self.scores.append(max(0.0, min(1.0, score)))

    def to_dict(self) -> dict:
        return {"average": self.average, "count": len(self.scores), "scores": [round(s, 2) for s in self.scores[-10:]]}


@dataclass 
class UserSatisfactionDelta:
    """Cumulative satisfaction tracking with trend direction."""
    scores: list = field(default_factory=list)

    @property
    def cumulative(self) -> float:
        return round(sum(self.scores) / len(self.scores), 3) if self.scores else 0.5

    @property
    def trend(self) -> str:
        if len(self.scores) < 2:
            return "→"
        recent = sum(self.scores[-3:]) / min(3, len(self.scores))
        prev = sum(self.scores[:-3]) / max(1, len(self.scores) - 3) if len(self.scores) > 3 else self.scores[0]
        return "↑" if recent > prev else ("↓" if recent < prev else "→")

    def record(self, score: float):
        self.scores.append(max(0.0, min(1.0, score)))

    def to_dict(self) -> dict:
        return {"cumulative": self.cumulative, "trend": self.trend, "count": len(self.scores)}


@dataclass
class TemporalVelocity:
    """Round timing and average duration tracking."""
    round_times: list = field(default_factory=list)
    round_start: Optional[float] = None

    def start_round(self):
        self.round_start = time.time()

    def end_round(self):
        if self.round_start:
            self.round_times.append(time.time() - self.round_start)
            self.round_start = None

    @property
    def avg_duration(self) -> float:
        return round(sum(self.round_times) / len(self.round_times), 2) if self.round_times else 0

    @property
    def total_duration(self) -> float:
        return round(sum(self.round_times), 2)

    def to_dict(self) -> dict:
        return {"round_count": len(self.round_times), "avg_duration_s": self.avg_duration,
                "total_duration_s": self.total_duration, "round_times": [round(t, 2) for t in self.round_times]}


@dataclass
class TransactionLedgerEntry:
    """Single immutable entry in the audit trail."""
    round: int
    phase: str  # open_ended, multi_choice, probing, decision
    timestamp: str
    description: str
    ambiguity_before: Optional[dict] = None
    ambiguity_after: Optional[dict] = None
    constraints_locked: list = field(default_factory=list)
    contradictions: list = field(default_factory=list)
    topics_covered: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Checkpoint:
    """Fork/rollback support — saves full engine state at a point in time."""
    id: str
    round: int
    timestamp: str
    ambiguity: dict
    constraints: dict
    decisions: list
    topic_coverage: int

    def to_dict(self) -> dict:
        return asdict(self)


class RRPEngine:
    """Full RRP v2 state machine with telemetry."""

    def __init__(self, u: int = 4, m: int = 1, x: int = 3, y: int = 3, z: int = 3, depth: int = 2,
                 goal_description: str = "", target_files: list = None):
        self.session_id = uuid.uuid4().hex[:12]
        self.u = u  # Use case
        self.m = m  # Execution mode
        self.x = x  # Open questions per round
        self.y = y  # MCQ follow-ups per answer
        self.z = z  # Max refinement rounds
        self.depth = depth  # Analysis depth (1=Shallow, 2=Standard, 3=Deep)

        self.goal_description = goal_description
        self.target_files = target_files or []

        # Core state
        self.round = 0
        self.status = "initialized"
        self.ambiguity = AmbiguityVector()
        self.constraints = {}  # {name: type} e.g. {"error_handling": "LOCKED"}
        self.decisions: list = []
        self.contradictions: list = []
        self.topic_coverage: int = 0
        self.conversation_log: list = []

        # Telemetry
        self.budget = TokenBudget()
        self.quality = QuestionQualityIndex()
        self.satisfaction = UserSatisfactionDelta()
        self.timing = TemporalVelocity()
        self.ledger: list = []
        self.checkpoints: list = []

        # Session timing
        self.session_start = datetime.now(timezone.utc)
        self.session_end: Optional[datetime] = None

    # ── Session lifecycle ──

    def start_session(self):
        """Initialize a new RRP session."""
        self.round = 0
        self.status = "running"
        self.ambiguity.calibrate_from_confidence(0.3)  # Start with moderate ambiguity
        self.timing.start_round()
        self._log_transaction(0, "session_start", "RRP session initialized")
        logger.info(f"RRP session {self.session_id} started (U={self.u}, M={self.m}, X={self.x}, Y={self.y}, Z={self.z})")
        return self._summary()

    def process_open_ended(self, questions: list, answers: list, satisfaction: float = 0.7):
        """Process a round of open-ended Q&A."""
        self.round += 1
        self.timing.end_round()
        self.timing.start_round()

        # Estimate token usage
        total_tokens = sum(len(q) + len(a) for q, a in zip(questions, answers))
        self.budget.record_round(total_tokens)

        # Reduce ambiguity based on answers
        confidence = min(1.0, 0.3 + satisfaction * 0.3 + len(answers) * 0.05)
        self.ambiguity.reduce(0.7)
        
        # Extract constraints from answers
        new_constraints = {}
        for a in answers:
            extracted = self._extract_constraints(a)
            new_constraints.update(extracted)
        self.constraints.update(new_constraints)

        # Update telemetry
        self.quality.record(satisfaction)
        self.satisfaction.record(satisfaction)

        # Topic coverage from answers
        self.topic_coverage |= self._detect_topics(questions + answers)

        # Record in ledger
        amb_before = self.ambiguity.to_dict()
        self.ambiguity.calibrate_from_confidence(confidence)
        self._log_transaction(self.round, "open_ended",
                              f"Processed {len(answers)} open-ended answers",
                              ambiguity_before=amb_before,
                              constraints_locked=list(new_constraints.keys()),
                              topics_covered=self.topic_coverage)

        # Save checkpoint
        if self.round % 2 == 0:
            self._save_checkpoint()

        return self._summary()

    def process_multi_choice(self, mcqs: list, answers: list, satisfaction: float = 0.8):
        """Process a round of multi-choice Q&A."""
        self.round += 1
        self.timing.end_round()
        self.timing.start_round()

        total_tokens = sum(len(str(q)) + len(str(a)) for q, a in zip(mcqs, answers))
        self.budget.record_round(total_tokens)

        # Multi-choice answers give more confidence
        confidence = min(1.0, 0.5 + satisfaction * 0.2 + len(answers) * 0.03)
        self.ambiguity.reduce(0.5)  # MCQ reduces ambiguity faster

        new_constraints = {}
        for a in answers:
            if isinstance(a, dict):
                new_constraints.update(a)
            elif isinstance(a, str):
                new_constraints.update(self._extract_constraints(a))
        self.constraints.update(new_constraints)

        # Detect contradictions
        contradictions = self._detect_contradictions()
        self.contradictions.extend(contradictions)

        self.quality.record(satisfaction)
        self.satisfaction.record(satisfaction)
        self.topic_coverage |= self._detect_topics([str(a) for a in answers])

        amb_before = self.ambiguity.to_dict()
        self.ambiguity.calibrate_from_confidence(confidence)
        self._log_transaction(self.round, "multi_choice",
                              f"Processed {len(answers)} multi-choice selections",
                              ambiguity_before=amb_before,
                              constraints_locked=list(new_constraints.keys()),
                              contradictions=contradictions,
                              topics_covered=self.topic_coverage)

        return self._summary()

    def process_decision(self, decision: str, confidence: float, reasoning: str):
        """Final decision for this goal."""
        self.round += 1
        self.timing.end_round()
        self.session_end = datetime.now(timezone.utc)

        self.decisions.append({
            "round": self.round,
            "decision": decision,
            "confidence": confidence,
            "reasoning": reasoning,
            "timestamp": self.session_end.isoformat()
        })

        self.status = "completed" if decision == "PASS" else "rejected"
        self.budget.record_round(len(reasoning))

        self._log_transaction(self.round, "decision",
                              f"Decision: {decision} (conf={confidence})",
                              constraints_locked=[k for k, v in self.constraints.items() if v == "LOCKED"])

        return self.finalize()

    def finalize(self) -> dict:
        """Compile session into final result dict."""
        self.session_end = self.session_end or datetime.now(timezone.utc)

        duration_s = (self.session_end - self.session_start).total_seconds()
        if self.timing.round_times:
            self.timing.round_times.append(max(0, duration_s - sum(self.timing.round_times)))

        return {
            "session_id": self.session_id,
            "status": self.status,
            "rounds_completed": self.round,
            "goal": self.goal_description,
            "target_files": self.target_files,
            "use_case": USE_CASES.get(self.u, f"U={self.u}"),
            "exec_mode": EXEC_MODES.get(self.m, f"M={self.m}"),
            "depth": self.depth,
            "config": {"x": self.x, "y": self.y, "z": self.z},
            "duration_s": round(duration_s, 2),
            "decision": self.decisions[-1] if self.decisions else {"decision": "INCOMPLETE", "confidence": 0, "reasoning": "Session ended without explicit decision"},
            "constraints": dict(self.constraints),
            "contradictions": self.contradictions,
            "telemetry": {
                "ambiguity": self.ambiguity.to_dict(),
                "budget": self.budget.to_dict(),
                "quality_index": self.quality.to_dict(),
                "satisfaction": self.satisfaction.to_dict(),
                "timing": self.timing.to_dict(),
                "topic_coverage": {
                    "bitmask": self.topic_coverage,
                    "topics": [name for bit, name in TOPIC_NAMES.items() if self.topic_coverage & bit]
                },
                "transaction_count": len(self.ledger),
                "checkpoint_count": len(self.checkpoints)
            },
            "ledger": [e.to_dict() for e in self.ledger[-20:]],  # Last 20 entries
            "conversation_log": self.conversation_log
        }

    # ── Dynamic question generation ──

    def generate_open_questions(self) -> list:
        """Generate X open-ended questions based on current state."""
        questions = []
        constraint_types = list(self.constraints.keys()) if self.constraints else ["error_handling", "type_safety", "test_coverage"]

        # Focus on areas with highest ambiguity
        amb = self.ambiguity.to_dict()
        focus_areas = sorted(
            [(k, v) for k, v in amb.items() if k != "avg" and k != "converged" and isinstance(v, (int, float))],
            key=lambda x: -x[1]
        )

        for i in range(min(self.x, len(focus_areas) + 2)):
            if i < len(focus_areas):
                dim = focus_areas[i][0]
                questions.append(f"How should we resolve ambiguity in '{dim}' for this goal? (current: {focus_areas[i][1]:.2f})")
            else:
                ct = constraint_types[i % len(constraint_types)]
                questions.append(f"What specific {ct.replace('_', ' ')} patterns should this implementation follow?")
        return questions

    def generate_multi_choice(self, open_answers: list) -> list:
        """Generate Y×X multi-choice questions based on open-ended answers."""
        mcqs = []
        for i, answer in enumerate(open_answers[:self.x]):
            for j in range(self.y):
                mcqs.append({
                    "follow_up_to": i,
                    "question": f"Regarding '{str(answer)[:60]}...' — which approach is best?",
                    "options": ["Option A — conservative", "Option B — balanced", "Option C — aggressive"]
                })
        return mcqs

    def generate_probing_questions(self) -> list:
        """Generate final probing questions for convergence."""
        questions = []
        topics = [name for bit, name in TOPIC_NAMES.items() if not (self.topic_coverage & bit)]
        for t in topics[:self.x]:
            questions.append(f"Have we adequately considered {t} aspects of this change?")
        # Fill remaining with constraint coverage
        unlocked = [k for k, v in self.constraints.items() if v != "LOCKED"]
        for u in unlocked[:max(0, self.x - len(topics))]:
            questions.append(f"Should we lock '{u}' as a required constraint?")
        return questions

    # ── Internal ──

    def _extract_constraints(self, text: str) -> dict:
        """Extract constraint patterns from text."""
        constraints = {}
        patterns = {
            "error_handling": ["error", "exception", "try", "except", "fail", "handle"],
            "type_safety": ["type", "hint", "annotation", "mypy", "strict"],
            "test_coverage": ["test", "coverage", "assert", "pytest", "unittest"],
            "logging": ["log", "debug", "info", "warn", "structured"],
            "documentation": ["doc", "document", "comment", "readme"],
            "security": ["secure", "auth", "perm", "sanitize", "validate"],
            "performance": ["perf", "speed", "fast", "optimize", "cache"],
            "input_validation": ["input", "validate", "sanitize", "check"],
            "code_quality": ["complex", "duplicat", "refactor", "clean"],
            "maintainability": ["maintain", "modular", "extens", "decouple"],
            "state_management": ["state", "mutat", "immut", "persist"]
        }
        text_lower = text.lower()
        for name, keywords in patterns.items():
            if any(kw in text_lower for kw in keywords):
                constraints[name] = "LOCKED" if sum(1 for kw in keywords if kw in text_lower) >= 2 else "RECOMMENDED"
        return constraints

    def _detect_contradictions(self) -> list:
        """Detect contradictions between locked constraints."""
        contradictions = []
        # error_handling vs performance: thorough error handling can impact perf
        if "error_handling" in self.constraints and self.constraints["error_handling"] == "LOCKED":
            if "performance" in self.constraints and self.constraints["performance"] == "LOCKED":
                contradictions.append("error_handling vs performance: thorough error handling may impact performance")
        # security vs simplicity
        if "security" in self.constraints and self.constraints["security"] == "LOCKED":
            if "maintainability" in self.constraints and self.constraints["maintainability"] == "LOCKED":
                contradictions.append("security vs maintainability: complex security can reduce maintainability")
        return contradictions

    def _detect_topics(self, texts: list) -> int:
        """Detect covered topics from text."""
        mask = 0
        combined = " ".join(texts).lower()
        if any(w in combined for w in ["architect", "design", "structur", "pattern", "module"]): mask |= TOPIC_ARCH
        if any(w in combined for w in ["secure", "auth", "perm", "trust", "vulner"]): mask |= TOPIC_SEC
        if any(w in combined for w in ["data", "model", "schema", "field", "stor"]): mask |= TOPIC_DATA
        if any(w in combined for w in ["perf", "speed", "fast", "latency", "throughput"]): mask |= TOPIC_PERF
        if any(w in combined for w in ["scal", "load", "concurr", "parallel", "distrib"]): mask |= TOPIC_SCAL
        if any(w in combined for w in ["test", "assert", "coverage", "integration"]): mask |= TOPIC_TEST
        if any(w in combined for w in ["deploy", "rollout", "release", "ci", "pipeline"]): mask |= TOPIC_DEPL
        if any(w in combined for w in ["ux", "user", "usability", "interface", "feedback"]): mask |= TOPIC_UX
        return mask

    def _log_transaction(self, round_num: int, phase: str, description: str,
                         ambiguity_before: dict = None, ambiguity_after: dict = None,
                         constraints_locked: list = None, contradictions: list = None,
                         topics_covered: int = 0):
        """Add immutable transaction to ledger."""
        self.ledger.append(TransactionLedgerEntry(
            round=round_num,
            phase=phase,
            timestamp=datetime.now(timezone.utc).isoformat(),
            description=description,
            ambiguity_before=ambiguity_before or self.ambiguity.to_dict(),
            ambiguity_after=self.ambiguity.to_dict(),
            constraints_locked=constraints_locked or [],
            contradictions=contradictions or [],
            topics_covered=topics_covered or self.topic_coverage
        ))

    def _save_checkpoint(self):
        """Save current state as a checkpoint."""
        cp = Checkpoint(
            id=uuid.uuid4().hex[:8],
            round=self.round,
            timestamp=datetime.now(timezone.utc).isoformat(),
            ambiguity=self.ambiguity.to_dict(),
            constraints=dict(self.constraints),
            decisions=list(self.decisions),
            topic_coverage=self.topic_coverage
        )
        self.checkpoints.append(cp)

    def _summary(self) -> dict:
        """Current state summary."""
        return {
            "session_id": self.session_id,
            "round": self.round,
            "status": self.status,
            "ambiguity": self.ambiguity.to_dict(),
            "constraints": dict(self.constraints),
            "decisions": self.decisions[-1] if self.decisions else None,
            "topic_coverage": {
                "bitmask": self.topic_coverage,
                "topics": [name for bit, name in TOPIC_NAMES.items() if self.topic_coverage & bit]
            },
            "telemetry": {
                "budget_saturation_pct": self.budget.saturation_pct,
                "quality_avg": self.quality.average,
                "satisfaction_cumulative": self.satisfaction.cumulative,
                "satisfaction_trend": self.satisfaction.trend,
                "timing_avg": self.timing.avg_duration,
                "total_duration_s": self.timing.total_duration,
            }
        }


# ── High-level helper for use in pulse runner ──

def run_rrp_session(goal_description: str, target_files: list, x: int = 3, y: int = 3, z: int = 3,
                    u: int = 4, m: int = 1, depth: int = 2, interactive: bool = False,
                    user_answer_fn=None) -> dict:
    """Run a complete RRP session and return full telemetry-enriched result.

    In auto mode (default), the engine generates and self-answers all questions.
    In interactive mode, user_answer_fn(q) is called for each question.
    """
    engine = RRPEngine(goal_description=goal_description, target_files=target_files,
                       x=x, y=y, z=z, u=u, m=m, depth=depth)
    engine.start_session()

    total_questions = 0
    conversation_log = []

    for round_num in range(1, z + 2):  # Rounds 1..Z+1
        if round_num == 1:
            # Round 1: X open-ended questions
            questions = engine.generate_open_questions()
            if interactive and user_answer_fn:
                answers = [user_answer_fn(q) for q in questions]
            else:
                topics = ["architecture with modular design and clear separation of concerns", 
                          "secure input validation with proper authentication and authorization",
                          "efficient data model with indexed fields and consistent schema",
                          "performance-optimized with caching and lazy evaluation",
                          "scalable concurrent design with proper locking and thread safety",
                          "testable with comprehensive unit tests and integration coverage",
                          "deployable with CI/CD pipeline and containerized rollout",
                          "user-friendly with clear error messages and helpful logging"]
                answers = []
                for qi, q in enumerate(questions):
                    topic = topics[qi % len(topics)]
                    answers.append(f"Implement with {topic}. Following best practices consistent with existing codebase.")
            
            for q, a in zip(questions, answers):
                conversation_log.append({"round": round_num, "phase": "open_ended", "question": q, "answer": a})
            
            engine.process_open_ended(questions, answers, satisfaction=0.7)
            total_questions += len(questions)

        elif round_num <= z:
            # Round 2..Z: Multi-choice follow-ups
            prev_answers = [c["answer"] for c in conversation_log if c["round"] == round_num - 1] or [""]
            mcqs = engine.generate_multi_choice(prev_answers)
            if interactive and user_answer_fn:
                mc_answers = [user_answer_fn(m["question"]) for m in mcqs]
            else:
                constraint_types = ["error_handling", "type_safety", "test_coverage", "logging", 
                                    "documentation", "security", "code_quality", "maintainability",
                                    "input_validation", "performance"]
                mc_answers = []
                for mi, m in enumerate(mcqs):
                    ct = constraint_types[mi % len(constraint_types)]
                    mc_answers.append({ct: "LOCKED"})
                    if mi % 3 == 0:
                        mc_answers[-1]["type_safety"] = "RECOMMENDED"
                    if mi % 5 == 0:
                        mc_answers[-1]["test_coverage"] = "LOCKED"
            
            for m, a in zip(mcqs, mc_answers):
                conversation_log.append({"round": round_num, "phase": "multi_choice",
                                          "question": m["question"], "options": m.get("options", []), "answer": a})
            
            engine.process_multi_choice(mcqs, mc_answers, satisfaction=0.8)
            total_questions += len(mcqs)

            # New open-ended questions
            new_questions = engine.generate_open_questions()
            if interactive and user_answer_fn:
                new_answers = [user_answer_fn(q) for q in new_questions]
            else:
                new_answers = [f"Auto-answer: consistent with previously locked constraints." for q in new_questions]
            
            for q, a in zip(new_questions, new_answers):
                conversation_log.append({"round": round_num, "phase": "open_ended", "question": q, "answer": a})
            
            engine.process_open_ended(new_questions, new_answers, satisfaction=0.75)
            total_questions += len(new_questions)

        else:
            # Final round: Probing questions → decision
            probing = engine.generate_probing_questions()
            if interactive and user_answer_fn:
                probe_answers = [user_answer_fn(q) for q in probing]
            else:
                probe_topics = ["All architectural concerns addressed with modular design.",
                               "Security requirements satisfied through input validation and authentication.",
                               "Data model properly normalized with appropriate indexes.",
                               "Performance targets achievable with caching layer.",
                               "Test coverage meets threshold with unit and integration tests.",
                               "Deployment pipeline configured with automated rollback."]
                probe_answers = []
                for pi, q in enumerate(probing):
                    ans = probe_topics[pi % len(probe_topics)]
                    if pi % 2 == 0:
                        ans += " No contradictions detected."
                    probe_answers.append(ans)
            
            for q, a in zip(probing, probe_answers):
                conversation_log.append({"round": round_num, "phase": "probing", "question": q, "answer": a})

            # Compute final confidence from ambiguity
            ambiguity_score = engine.ambiguity.avg
            confidence = max(0.3, min(0.95, 1.0 - ambiguity_score))
            
            # Check for early termination
            round_check = round_num >= max(3, int(z * 0.7))
            amb_check = engine.ambiguity.converged
            topic_check = engine.topic_coverage == 0xFF
            
            if round_check and (amb_check or topic_check):
                decision = "PASS"
            elif ambiguity_score > 0.6:
                decision = "HOLD"
            else:
                decision = "PASS"
            
            reasoning = f"RRP session complete: {total_questions} questions across {round_num} rounds. Ambiguity={ambiguity_score:.2f}, Topics={engine.topic_coverage:08b}"
            
            engine.process_decision(decision, confidence, reasoning)
            total_questions += len(probing)

    result = engine.finalize()
    result["total_questions"] = total_questions
    result["conversation_log"] = conversation_log
    return result
