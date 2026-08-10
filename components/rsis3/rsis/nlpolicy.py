"""Natural-language policy — plain-language rules compiled to checks.

Phase 37 (Sequel VIII): humans amend rules in plain language; the system
compiles them to executable policy with a deterministic, reviewable
mapping. Compiled policy renders back to natural language for round-trip
confirmation; rules that contradict existing policy are flagged at
authoring time.
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, load_json, now_ts, save_json

logger = logging.getLogger(__name__)

#: deterministic, reviewable sentence patterns -> policy path
PATTERNS = [
    (r"never spend more than \$?([0-9.]+) per (day|cycle) on (\w+)",
     "budget", lambda m: ("per_loop", {m.group(3): {"daily_usd": float(m.group(1))}})),
    (r"spend at most \$?([0-9.]+) per (day|cycle)",
     "budget", lambda m: ("default_daily_usd", float(m.group(1)))),
    (r"always ask (?:before|for approval) (?:before )?touching (\S+)",
     "approval", lambda m: ("approval_required.paths", m.group(1))),
    (r"never (touch|modify|write) (\S+)",
     "approval", lambda m: ("approval_required.paths", m.group(2))),
]


def compile_rule(sentence: str) -> Optional[dict]:
    """Compile one plain-language sentence to a policy delta + mapping."""
    s = " ".join(sentence.lower().split())
    for pattern, kind, fn in PATTERNS:
        m = re.search(pattern, s)
        if m:
            key, value = fn(m)
            return {"sentence": sentence, "kind": kind, "policy_key": key,
                    "value": value, "compiled": True}
    return {"sentence": sentence, "compiled": False}


def compile_rules(workspace: Path, sentences: list[str]) -> dict:
    """Compile several sentences; flag conflicts with the live policy."""
    ws = Path(workspace)
    from rsis.policy import load_policy
    policy = load_policy(ws)
    compiled, conflicts, rejected = [], [], []
    for s in sentences:
        c = compile_rule(s)
        if not c.get("compiled"):
            rejected.append(s)
            continue
        compiled.append(c)
        # conflict detection: same key, different value in live policy
        key, value = c["policy_key"], c["value"]
        if key == "per_loop":
            existing = ((policy.get("per_loop") or {}).get(
                list(value.keys())[0]) or {}).get("daily_usd")
            if existing is not None and existing != list(value.values())[0].get("daily_usd"):
                conflicts.append({**c, "existing": existing})
        elif key in ("default_daily_usd",):
            if policy.get(key) is not None and policy.get(key) != value:
                conflicts.append({**c, "existing": policy.get(key)})
    result = {"compiled": compiled, "conflicts": conflicts,
              "rejected": rejected, "ts": now_ts()}
    save_json(Path(ws) / "rack" / "policy_nl.json", result)
    emit(ws, "policy_compiled", rules=len(compiled), conflicts=len(conflicts),
         rejected=len(rejected))
    return result


def roundtrip(compiled: list[dict]) -> list[str]:
    """Render compiled rules back to natural language for confirmation."""
    out = []
    for c in compiled:
        key, value = c["policy_key"], c["value"]
        if key == "per_loop":
            for agent, cfg in value.items():
                out.append(f"Limit {agent} to ${cfg['daily_usd']} per day.")
        elif key == "default_daily_usd":
            out.append(f"Spend at most ${value} per day.")
        elif key == "approval_required.paths":
            out.append(f"Always ask before touching {value}.")
        else:
            out.append(c["sentence"])
    return out


def apply(workspace: Path, compiled: list[dict],
          actor: str = "approver") -> int:
    """Apply compiled rules to rack/policy.json (after round-trip gate)."""
    ws = Path(workspace)
    from rsis.policy import load_policy, save_policy
    policy = load_policy(ws)
    for c in compiled:
        key, value = c["policy_key"], c["value"]
        if key == "per_loop":
            policy.setdefault("per_loop", {}).update(value)
        elif key == "approval_required.paths":
            paths = policy.setdefault("approval_required", {}).setdefault(
                "paths", [])
            if value not in paths:
                paths.append(value)
        else:
            policy[key] = value
    save_policy(ws, policy)
    emit(ws, "policy_roundtrip", rules=len(compiled), actor=actor)
    return len(compiled)


def status(workspace: Path) -> dict:
    data = load_json(Path(workspace) / "rack" / "policy_nl.json")
    return {"rules": len(data.get("compiled", [])),
            "conflicts": len(data.get("conflicts", [])),
            "rejected": len(data.get("rejected", []))}
