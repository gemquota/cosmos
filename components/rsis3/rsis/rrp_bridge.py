"""RRP bridge — goal refinement service for the rack RRP tools.

A thin, dependency-free refinement layer used by
``rack/rrp_conversation.py`` (and the pulse runner) to turn a raw goal
string into typed constraints. Production deployments can swap this for
an LLM-backed refinement; the interface is the contract:

    result = RRPBridge().refine_goal(goal)
    result.constraints            # {"error_handling": "LOCKED", ...}
    result.contradiction_detected # bool
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

CONSTRAINT_TYPES = (
    "security",
    "error_handling",
    "test_coverage",
    "logging",
    "documentation",
    "maintainability",
    "input_validation",
    "type_safety",
    "performance",
)

# keyword → constraint type, with the emphasis direction: presence of the
# keyword suggests the constraint should be LOCKED (hard) for this goal.
_KEYWORD_MAP = {
    "security": "security",
    "injection": "security",
    "auth": "security",
    "privilege": "security",
    "sanitize": "input_validation",
    "validation": "input_validation",
    "input": "input_validation",
    "error": "error_handling",
    "exception": "error_handling",
    "timeout": "error_handling",
    "recovery": "error_handling",
    "retry": "error_handling",
    "test": "test_coverage",
    "coverage": "test_coverage",
    "regression": "test_coverage",
    "log": "logging",
    "monitor": "logging",
    "observ": "logging",
    "doc": "documentation",
    "readme": "documentation",
    "refactor": "maintainability",
    "maintain": "maintainability",
    "complex": "maintainability",
    "readab": "maintainability",
    "type": "type_safety",
    "annotation": "type_safety",
    "mypy": "type_safety",
    "perf": "performance",
    "cache": "performance",
    "latency": "performance",
}


@dataclass
class RRPRefinement:
    """Result of ``RRPBridge.refine_goal``."""

    goal: str
    constraints: dict = field(default_factory=dict)
    contradiction_detected: bool = False
    locked: list = field(default_factory=list)

    @property
    def total_questions(self) -> int:
        return 0


class RRPBridge:
    """Keyword-driven goal refiner with an LLM-swappable interface."""

    def refine_goal(self, goal: str) -> RRPRefinement:
        """Map a goal string to typed constraints.

        Keyword hits lock the matching constraint type; the rest default
        to RECOMMENDED so every goal carries a full constraint profile.
        """
        text = (goal or "").lower()
        locked: set[str] = set()
        for keyword, constraint in _KEYWORD_MAP.items():
            if keyword in text:
                locked.add(constraint)

        constraints = {
            ctype: ("LOCKED" if ctype in locked else "RECOMMENDED")
            for ctype in CONSTRAINT_TYPES
        }

        # Contradiction heuristic: goals that demand both strict typing and
        # fast hot paths without further qualification are ambiguous.
        contradiction = (
            "type_safety" in locked and "performance" in locked
            and not any(w in text for w in ("profile", "measure"))
        )

        return RRPRefinement(
            goal=goal,
            constraints=constraints,
            contradiction_detected=contradiction,
            locked=sorted(locked),
        )
