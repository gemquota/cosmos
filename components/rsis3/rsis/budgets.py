"""Cost budgets — per-loop and per-day LLM spend governance (Phase 8).

Extends the Phase 5 cost ledger (``.rsis/costs.jsonl``) into a budget
ledger: per-loop daily allocations plus a global ceiling. Crossing a budget
emits a ``cost.budget_hit`` event and fail-closes LLM enrichment for that
loop until reviewed.

Budget file: ``.rsis/budgets.json`` (env-templated ``$VAR`` values).

    {
      "version": 1,
      "per_loop": {"evaluator": {"daily_usd": 0.05}},
      "default_daily_usd": 0.02,
      "ceiling_usd": 0.50
    }
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT = {
    "version": 1,
    "per_loop": {},
    "default_daily_usd": 0.02,
    "ceiling_usd": 0.50,
}


def _expand(value):
    """Expand ``$VAR`` / ``${VAR}`` references from the environment."""
    if isinstance(value, str) and value.startswith("$"):
        return os.environ.get(value[1:].strip("{}"), value)
    return value


def budgets_path(workspace: Path) -> Path:
    return Path(workspace) / ".rsis" / "budgets.json"


def load_budgets(workspace: Path) -> dict:
    path = budgets_path(workspace)
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            data.setdefault("per_loop", {})
            data.setdefault("default_daily_usd", DEFAULT["default_daily_usd"])
            data.setdefault("ceiling_usd", DEFAULT["ceiling_usd"])
            return data
        except (OSError, json.JSONDecodeError) as e:
            logger.warning("budgets.json unreadable (%s); using defaults", e)
    return dict(DEFAULT)


def save_budgets(workspace: Path, data: dict) -> None:
    path = budgets_path(workspace)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def ensure_budgets(workspace: Path) -> dict:
    data = load_budgets(workspace)
    if not budgets_path(workspace).is_file():
        save_budgets(workspace, data)
    return data


def _day_of(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def spend_by_agent(workspace: Path, day: Optional[str] = None) -> dict:
    """USD spend per agent for a UTC day (default: today)."""
    day = day or _day_of(datetime.now(timezone.utc).timestamp())
    ledger = Path(workspace) / ".rsis" / "costs.jsonl"
    out: dict[str, float] = {}
    if not ledger.is_file():
        return out
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if _day_of(float(rec.get("ts", 0))) != day:
            continue
        agent = rec.get("agent", "unknown")
        out[agent] = round(out.get(agent, 0.0) + float(rec.get("cost", 0.0)), 6)
    return out


def daily_limit(budgets: dict, agent: str) -> float:
    per = budgets.get("per_loop", {}).get(agent, {})
    if isinstance(per, dict) and "daily_usd" in per:
        return float(_expand(per["daily_usd"]))
    return float(_expand(budgets.get("default_daily_usd",
                                     DEFAULT["default_daily_usd"])))


def emit_budget_hit(workspace: Path, agent: str, spend: float,
                    limit: float) -> dict:
    """Record a ``cost.budget_hit`` event in ``.rsis/budget_hits.jsonl``."""
    event = {
        "kind": "cost.budget_hit",
        "agent": agent,
        "spend_usd": round(spend, 6),
        "limit_usd": round(limit, 6),
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    path = Path(workspace) / ".rsis" / "budget_hits.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event) + "\n")
    logger.warning("cost.budget_hit — %s spent $%.4f of $%.4f daily limit",
                   agent, spend, limit)
    return event


def check_budget(workspace: Path, agent: str) -> dict:
    """Fail-close check for one agent's LLM spend.

    Returns {allowed, agent, spend, limit, ceiling, ceiling_remaining}.
    """
    budgets = load_budgets(workspace)
    spend = spend_by_agent(workspace).get(agent, 0.0)
    limit = daily_limit(budgets, agent)
    ceiling = float(_expand(budgets.get("ceiling_usd", 0.0)))
    total_today = sum(spend_by_agent(workspace).values())
    ceiling_remaining = (float("inf") if ceiling <= 0
                         else round(ceiling - total_today, 6))
    allowed = spend < limit and ceiling_remaining > 0
    result = {
        "allowed": allowed,
        "agent": agent,
        "spend": round(spend, 6),
        "limit": round(limit, 6),
        "ceiling": ceiling,
        "ceiling_remaining": ceiling_remaining,
    }
    if not allowed:
        emit_budget_hit(workspace, agent, spend, limit)
    return result


def budget_status(workspace: Path) -> dict:
    """Aggregate budget status for /api/cosmos and dashboards."""
    budgets = load_budgets(workspace)
    today = _day_of(datetime.now(timezone.utc).timestamp())
    spend = spend_by_agent(workspace, today)
    per_loop = {}
    for agent, spent in sorted(spend.items()):
        limit = daily_limit(budgets, agent)
        per_loop[agent] = {"spend": spent, "limit": limit,
                           "remaining": round(limit - spent, 6),
                           "hit": spent >= limit}
    ceiling = float(_expand(budgets.get("ceiling_usd", 0.0)))
    total = sum(spend.values())
    return {
        "day": today,
        "per_loop": per_loop,
        "total": round(total, 6),
        "ceiling": ceiling,
        "remaining": (float("inf") if ceiling <= 0
                      else round(ceiling - total, 6)),
    }
