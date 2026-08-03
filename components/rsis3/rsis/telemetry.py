"""Workspace telemetry collection.

Collects file modification events, command history, resource usage, and
error rates per the RSIS specification.
"""

import json
import logging
import os
import time
import uuid
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock, Thread
from typing import Optional

logger = logging.getLogger(__name__)


class TelemetryEvent:
    """A single telemetry event."""

    def __init__(
        self,
        event_type: str,
        path: Optional[str] = None,
        delta: Optional[str] = None,
        duration_ms: Optional[int] = None,
        metadata: Optional[dict] = None,
    ):
        self.type = event_type
        self.path = path
        self.delta = delta
        self.duration_ms = duration_ms
        self.metadata = metadata or {}
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "path": self.path,
            "delta": self.delta,
            "duration_ms": self.duration_ms,
            "timestamp": self.timestamp,
            **self.metadata,
        }


class TelemetryCollector:
    """Collects and flushes workspace telemetry."""

    def __init__(self, telemetry_dir: str = ".rsis/telemetry", flush_interval_s: int = 5):
        self.telemetry_dir = Path(telemetry_dir)
        self.telemetry_dir.mkdir(parents=True, exist_ok=True)
        self.flush_interval_s = flush_interval_s
        self._buffer: list[dict] = []
        self._lock = Lock()
        self._session_id = str(uuid.uuid4())
        self._running = False
        self._thread: Optional[Thread] = None
        self._last_flush = time.monotonic()

    def start(self) -> None:
        """Start the background flush thread."""
        if self._running:
            return
        self._running = True
        self._thread = Thread(target=self._flush_loop, daemon=True, name="telemetry-flush")
        self._thread.start()
        logger.info("Telemetry collector started (session=%s)", self._session_id[:8])

    def stop(self) -> None:
        """Stop the flush thread and flush remaining events."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=5)
        self.flush()

    def record(self, event: TelemetryEvent) -> None:
        """Record a telemetry event."""
        with self._lock:
            self._buffer.append(event.to_dict())

    def flush(self) -> None:
        """Write buffered events to disk."""
        with self._lock:
            if not self._buffer:
                return
            events = self._buffer
            self._buffer = []

        filename = f"{self._session_id}_{int(time.time())}.jsonl"
        path = self.telemetry_dir / filename
        try:
            with open(path, "a") as f:
                for ev in events:
                    f.write(json.dumps(ev) + "\n")
            self._last_flush = time.monotonic()
        except OSError as e:
            logger.error("Failed to flush telemetry: %s", e)
            # Put events back
            with self._lock:
                self._buffer.extend(events)

    def _flush_loop(self) -> None:
        while self._running:
            time.sleep(self.flush_interval_s)
            try:
                self.flush()
            except Exception:
                logger.exception("Telemetry flush error")

    def session_report(self) -> dict:
        """Generate a summary report for the current session."""
        return {
            "session_id": self._session_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "events_collected": len(self._buffer),
            # In production, this would aggregate from persisted files
        }


class WorkspaceMonitor:
    """Lightweight workspace resource monitor using psutil when available."""

    def __init__(self):
        self._psutil = None
        try:
            import psutil
            self._psutil = psutil
        except ImportError:
            logger.warning("psutil not available — resource monitoring disabled")

    def cpu_usage(self) -> Optional[float]:
        if self._psutil:
            try:
                return self._psutil.cpu_percent(interval=0.1)
            except Exception:
                return None
        return None

    def memory_usage_mb(self) -> Optional[float]:
        if self._psutil:
            try:
                proc = self._psutil.Process()
                return proc.memory_info().rss / (1024 * 1024)
            except Exception:
                return None
        return None

    def disk_usage_pct(self, path: str = ".") -> Optional[float]:
        if self._psutil:
            try:
                return self._psutil.disk_usage(path).percent
            except Exception:
                return None
        return None


# ── LLM Cost Accounting (ported from Agent OS telemetry) ──────────────────
# Costs are estimated from a local price table ($ per 1M tokens) so the
# ledger works offline; wire real per-call costs from the provider when
# available. The ledger persists every call to costs.jsonl and replays it at
# startup, so budget caps hold across separate loop processes.

PRICE_TABLE = [
    ("claude-opus", 15.0, 75.0),
    ("claude-sonnet", 3.0, 15.0),
    ("claude", 3.0, 15.0),
    ("gemini-2.5-pro", 1.25, 10.0),
    ("gemini-2.5-flash", 0.3, 2.5),
    ("gpt-4.1-mini", 0.4, 1.6),
    ("gpt-4o-mini", 0.15, 0.6),
    ("gpt-4o", 2.5, 10.0),
]
DEFAULT_PRICES = (1.0, 2.0)  # fallback $ per 1M tokens


def estimate_cost(model: str, in_tokens: int, out_tokens: int) -> float:
    """Estimate USD cost of one LLM call from the local price table."""
    model = (model or "").lower()
    rate_in, rate_out = DEFAULT_PRICES
    for key, ri, ro in PRICE_TABLE:
        if key in model:
            rate_in, rate_out = ri, ro
            break
    return in_tokens / 1e6 * rate_in + out_tokens / 1e6 * rate_out


class CostLedger:
    """Thread-safe, persistent LLM cost ledger with a hard budget cap.

    Every LLM call is appended to `log_path` as JSONL and replayed at
    startup, so aggregates and the budget latch survive process restarts
    (each RSIS loop runs as its own process).
    """

    def __init__(self, log_path: str = ".rsis/costs.jsonl",
                 budget_cap_usd: float = 0.0):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self.budget_cap_usd = max(0.0, float(budget_cap_usd))  # 0 = unlimited
        self.budget_exceeded = False
        self._lock = Lock()
        self._by_agent: dict[str, dict] = {}
        self._by_model: dict[str, dict] = {}
        self._events: deque = deque(maxlen=500)
        self.started_at = time.time()
        self._replay()

    # ------------------------------------------------------------------ #
    def record_llm(self, agent: str, model: str, latency_s: float = 0.0,
                   usage: Optional[dict] = None, error: bool = False) -> dict:
        """Record one LLM call (tokens, estimated cost, latency)."""
        usage = usage or {}
        in_tokens = int(usage.get("prompt_tokens") or 0)
        out_tokens = int(usage.get("completion_tokens") or 0)
        cost = estimate_cost(model, in_tokens, out_tokens)
        entry = {
            "kind": "llm", "trace_id": uuid.uuid4().hex[:12],
            "agent": agent, "model": model,
            "latency_s": round(latency_s, 3), "tokens_in": in_tokens,
            "tokens_out": out_tokens, "cost": round(cost, 6), "error": error,
        }
        with self._lock:
            agg = self._by_agent.setdefault(agent, {
                "calls": 0, "tokens_in": 0, "tokens_out": 0,
                "cost": 0.0, "latency_s": 0.0, "errors": 0})
            agg["calls"] += 1
            agg["tokens_in"] += in_tokens
            agg["tokens_out"] += out_tokens
            agg["cost"] += cost
            agg["latency_s"] += latency_s
            agg["errors"] += int(error)
            model_agg = self._by_model.setdefault(model, {
                "calls": 0, "tokens": 0, "cost": 0.0})
            model_agg["calls"] += 1
            model_agg["tokens"] += in_tokens + out_tokens
            model_agg["cost"] += cost
            self._check_budget_locked(entry)
            self._push(entry)
        return entry

    # ------------------------------------------------------------------ #
    def guard_budget(self, model: str, in_tokens: int = 0,
                     out_tokens: int = 0) -> bool:
        """Pre-flight check: would this call blow the budget cap?

        Returns False when the caller should refuse the request. Exact
        token counts are unknowable in advance, so callers pass an
        estimate; the running total is the baseline.
        """
        if self.budget_cap_usd <= 0:
            return True
        estimate = estimate_cost(model, in_tokens, out_tokens)
        with self._lock:
            if self.budget_exceeded:
                return False
            total = self.total_cost_locked()
            if estimate and total + estimate > self.budget_cap_usd:
                return False
            return True

    def budget_remaining(self) -> float:
        """USD left before the hard cap (inf when unlimited)."""
        if self.budget_cap_usd <= 0:
            return float("inf")
        with self._lock:
            return round(self.budget_cap_usd - self.total_cost_locked(), 6)

    def total_cost(self) -> float:
        with self._lock:
            return round(self.total_cost_locked(), 6)

    def total_cost_locked(self) -> float:
        return sum(a["cost"] for a in self._by_agent.values())

    # ------------------------------------------------------------------ #
    def snapshot(self) -> dict:
        """Point-in-time state for the dashboard / CLI."""
        with self._lock:
            total = self.total_cost_locked()
            remaining = (float("inf") if self.budget_cap_usd <= 0
                         else round(self.budget_cap_usd - total, 6))
            llm = {"calls": 0, "tokens_in": 0, "tokens_out": 0,
                   "cost": 0.0, "latency_s": 0.0, "errors": 0,
                   "by_agent": {k: dict(v) for k, v in self._by_agent.items()},
                   "by_model": {k: dict(v) for k, v in self._by_model.items()}}
            for agg in llm["by_agent"].values():
                llm["calls"] += agg["calls"]
                llm["tokens_in"] += agg["tokens_in"]
                llm["tokens_out"] += agg["tokens_out"]
                llm["cost"] += agg["cost"]
                llm["latency_s"] += agg["latency_s"]
                llm["errors"] += agg["errors"]
            return {
                "uptime_s": round(time.time() - self.started_at, 1),
                "budget_cap_usd": self.budget_cap_usd,
                "budget_exceeded": self.budget_exceeded,
                "budget_remaining_usd": remaining,
                "llm": llm,
                "recent_events": list(self._events)[-20:],
            }

    def report(self) -> str:
        """Human-readable summary for the CLI."""
        snap = self.snapshot()
        llm = snap["llm"]
        cap = snap["budget_cap_usd"]
        cap_str = ("unlimited" if cap <= 0
                   else f"${cap:.4f}" if cap < 1 else f"${cap:.2f}")
        lines = [
            f"  LLM calls: {llm['calls']}  tokens: "
            f"{llm['tokens_in'] + llm['tokens_out']}  "
            f"spend: ${llm['cost']:.4f}",
            f"  Budget: {cap_str} cap "
            f"({'EXCEEDED' if snap['budget_exceeded'] else 'ok'})",
        ]
        for agent, agg in sorted(llm["by_agent"].items()):
            lines.append(f"    {agent}: {agg['calls']} calls, "
                         f"${agg['cost']:.4f}, {agg['errors']} errors")
        return "\n".join(lines)

    # ------------------------------------------------------------------ #
    def _check_budget_locked(self, entry: dict) -> None:
        """Latch the budget flag when spend crosses the cap."""
        if self.budget_cap_usd <= 0 or self.budget_exceeded:
            return
        total = self.total_cost_locked()
        if total >= self.budget_cap_usd:
            self.budget_exceeded = True
            self._push({"kind": "budget_exceeded",
                        "cap_usd": self.budget_cap_usd,
                        "spend_usd": round(total, 6)})
            logger.error("[cost] budget cap $%.2f exceeded (spend $%.4f) — "
                         "new LLM calls will be refused",
                         self.budget_cap_usd, total)

    def _push(self, entry: dict) -> None:   # caller must hold the lock
        entry["ts"] = time.time()
        self._events.append(entry)
        with self.log_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry) + "\n")

    def _replay(self) -> None:
        """Rebuild aggregates from prior records (cross-process budget)."""
        if not self.log_path.exists():
            return
        for line in self.log_path.read_text(encoding="utf-8").splitlines():
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("kind") != "llm":
                continue
            agent = entry.get("agent", "?")
            model = entry.get("model", "?")
            agg = self._by_agent.setdefault(agent, {
                "calls": 0, "tokens_in": 0, "tokens_out": 0,
                "cost": 0.0, "latency_s": 0.0, "errors": 0})
            agg["calls"] += 1
            agg["tokens_in"] += entry.get("tokens_in", 0)
            agg["tokens_out"] += entry.get("tokens_out", 0)
            agg["cost"] += entry.get("cost", 0.0)
            agg["latency_s"] += entry.get("latency_s", 0.0)
            agg["errors"] += int(entry.get("error", False))
            model_agg = self._by_model.setdefault(model, {
                "calls": 0, "tokens": 0, "cost": 0.0})
            model_agg["calls"] += 1
            model_agg["tokens"] += entry.get("tokens_in", 0) + entry.get("tokens_out", 0)
            model_agg["cost"] += entry.get("cost", 0.0)
            self._events.append(entry)
        if self.budget_cap_usd > 0 and self.total_cost_locked() >= self.budget_cap_usd:
            self.budget_exceeded = True
            logger.warning("[cost] replayed ledger already at/over cap "
                           "(spend $%.4f / cap $%.2f)",
                           self.total_cost_locked(), self.budget_cap_usd)


_DEFAULT_LEDGER: Optional[CostLedger] = None


def default_ledger() -> CostLedger:
    """Module-level ledger bound to CONFIG (lazy; env overrides apply)."""
    global _DEFAULT_LEDGER
    if _DEFAULT_LEDGER is None:
        from rsis.config import CONFIG
        _DEFAULT_LEDGER = CostLedger(CONFIG.cost_log, CONFIG.budget_cap_usd)
    return _DEFAULT_LEDGER
