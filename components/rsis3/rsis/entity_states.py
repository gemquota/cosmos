"""Entity lifecycle & constraint registry — SPACE series 2 (Ontological Characteristics).

Executable form of the series-2 spec artifacts ``entity_lifecycles`` and
``entity_constraints``: runtime entities are stateful objects with defined
states, allowed transitions, and required-field validity rules.

- ``entity_lifecycles`` — stateful lifecycle: entities pass through defined
  states with transition rules.
- ``entity_constraints`` — moderate constraints: several required fields and
  validity rules.

Every transition and record is validated; violations raise
``EntityStateError`` instead of silently corrupting workspace state.
"""

from __future__ import annotations

from typing import Any, Callable, Optional

# Lifecycle registry: state set + allowed transitions + required fields per
# runtime entity. Mirrors the actual record shapes written by the loops
# (sessions/telemetry, convergence proposals, L2 candidates, git
# checkpoints, strategy populations).
LIFECYCLES: dict[str, dict[str, Any]] = {
    "session": {
        "states": ("active", "completed", "abandoned"),
        "transitions": (
            ("active", "completed"),
            ("active", "abandoned"),
        ),
        "required": ("session_id", "status"),
    },
    "proposal": {
        "states": ("proposed", "applied", "rejected"),
        "transitions": (
            ("proposed", "applied"),
            ("proposed", "rejected"),
        ),
        "required": ("ts", "generation"),
    },
    "candidate": {
        "states": ("generated", "evaluated", "applied", "rejected"),
        "transitions": (
            ("generated", "evaluated"),
            ("evaluated", "applied"),
            ("evaluated", "rejected"),
        ),
        "required": ("description", "target_files"),
    },
    "checkpoint": {
        "states": ("created", "restored", "superseded"),
        "transitions": (
            ("created", "restored"),
            ("created", "superseded"),
        ),
        "required": ("message",),
    },
    "strategy": {
        "states": ("evolved", "active", "retired"),
        "transitions": (
            ("evolved", "active"),
            ("evolved", "retired"),
            ("active", "retired"),
        ),
        "required": ("generation", "population"),
    },
}

# Extra per-entity validity rules beyond required fields.
_EXTRA_RULES: dict[str, Callable[[dict], Optional[str]]] = {
    "proposal": lambda r: (
        None if ("loop" in r or "proposed_loop" in r)
        else "must carry one of 'loop' / 'proposed_loop'"),
    "candidate": lambda r: (
        None if isinstance(r.get("target_files"), list)
        else "'target_files' must be a list"),
    "strategy": lambda r: (
        None if isinstance(r.get("population"), list)
        else "'population' must be a list"),
}


class EntityStateError(ValueError):
    """Raised for unknown entities, invalid transitions, or invalid records."""


def states(entity_type: str) -> tuple[str, ...]:
    """Return the defined states for an entity type."""
    spec = LIFECYCLES.get(entity_type)
    if spec is None:
        raise EntityStateError(f"unknown entity type: {entity_type!r}")
    return spec["states"]


def can_transition(entity_type: str, current: str, next_: str) -> bool:
    """Whether ``current -> next_`` is an allowed transition."""
    spec = LIFECYCLES.get(entity_type)
    if spec is None:
        raise EntityStateError(f"unknown entity type: {entity_type!r}")
    return (current, next_) in spec["transitions"]


def transition(entity_type: str, current: str, next_: str) -> str:
    """Validate and return the next state; raises ``EntityStateError``."""
    spec = LIFECYCLES.get(entity_type)
    if spec is None:
        raise EntityStateError(f"unknown entity type: {entity_type!r}")
    if current not in spec["states"]:
        raise EntityStateError(
            f"{entity_type}: {current!r} is not a defined state "
            f"(expected one of {spec['states']})")
    if next_ not in spec["states"]:
        raise EntityStateError(
            f"{entity_type}: {next_!r} is not a defined state "
            f"(expected one of {spec['states']})")
    if (current, next_) not in spec["transitions"]:
        raise EntityStateError(
            f"{entity_type}: invalid transition {current!r} -> {next_!r} "
            f"(allowed: {spec['transitions']})")
    return next_


def validate_record(entity_type: str, record: dict) -> None:
    """Validate a record against the entity's required fields and rules."""
    spec = LIFECYCLES.get(entity_type)
    if spec is None:
        raise EntityStateError(f"unknown entity type: {entity_type!r}")
    if not isinstance(record, dict):
        raise EntityStateError(f"{entity_type}: record must be a dict")
    missing = [f for f in spec["required"]
               if f not in record or record[f] is None]
    if missing:
        raise EntityStateError(
            f"{entity_type}: missing required field(s): {', '.join(missing)}")
    rule = _EXTRA_RULES.get(entity_type)
    if rule is not None:
        problem = rule(record)
        if problem:
            raise EntityStateError(f"{entity_type}: {problem}")
