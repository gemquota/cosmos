#!/usr/bin/env python3
"""TelemetryWriter — Lightweight subconscious telemetry stream.

Records periodic system observations to ``wiki/telemetry/`` independently
of pulse cycles.  This creates a "subconscious" stream — low-level status
data that the dashboard can display as a raw telemetry feed.

Observations are timestamped JSON lines stored in daily files:
``wiki/telemetry/YYYY-MM-DD.jsonl``.  Each line is a single observation.

The writer debounces high-frequency updates (>100/min) to 2Hz
to prevent file bloat and browser lockup in the dashboard.

Usage::

    from memory_bridge.telemetry_writer import TelemetryWriter

    writer = TelemetryWriter()              # auto-discovers wiki path
    writer.observe("layer_scores", {"L1": 75, "L3": 45})
    writer.observe("active_goals", {"count": 3, "top_priority": 0.85})

    # Or use as a context manager for automatic flushing
    with TelemetryWriter() as tw:
        tw.observe("pulse_start", {"pulse_id": 42})
        # ... system does work ...
        tw.observe("pulse_end", {"decision": "PASS"})
"""

import json
import os
import threading
import time
from collections import deque
from datetime import datetime
from pathlib import Path
from typing import Optional

from memory_bridge.config import resolve_wiki_path


class TelemetryWriter:
    """Records timestamped system observations to ``wiki/telemetry/``.

    Each observation is a JSON line in a daily file.  The writer is
    thread-safe and self-flushing (flushes every 10 observations or
    on context manager exit).

    Observations are debounced: if the same ``channel`` is observed
    more than 100 times in 60 seconds, subsequent observations on that
    channel are skipped until the rate drops.
    """

    def __init__(self, wiki_root: Optional[str | Path] = None,
                 auto_flush: int = 10):
        self._wiki = Path(wiki_root) if wiki_root else resolve_wiki_path()
        self._telemetry_dir = self._wiki / "telemetry"
        self._telemetry_dir.mkdir(parents=True, exist_ok=True)
        self._auto_flush = auto_flush
        self._buffer: list[str] = []
        self._lock = threading.Lock()
        self._channel_timestamps: dict[str, deque] = {}  # channel -> [timestamps]

    # ── public API ──────────────────────────────────────────

    def observe(self, channel: str, data: dict) -> bool:
        """Record one observation on a named channel.

        Args:
            channel: Observation category (e.g. ``"layer_scores"``,
                     ``"active_goals"``, ``"pulse_cycle"``).
            data:    Arbitrary JSON-serialisable dict.

        Returns:
            ``True`` if the observation was recorded, ``False`` if it
            was dropped due to rate limiting.
        """
        if not self._rate_limit(channel):
            return False

        observation = {
            "t": time.time(),
            "ts": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "c": channel,
            "d": data,
        }

        line = json.dumps(observation, default=str)

        with self._lock:
            self._buffer.append(line)
            if len(self._buffer) >= self._auto_flush:
                self._flush_unlocked()

        return True

    def flush(self):
        """Flush buffered observations to disk immediately."""
        with self._lock:
            self._flush_unlocked()

    def recent(self, limit: int = 50, channel: Optional[str] = None) -> list[dict]:
        """Return recent observations from the current daily file.

        Args:
            limit:   Maximum number of observations to return.
            channel: Optional filter — only return observations from
                     this channel.

        Returns:
            List of observation dicts, most recent first.
        """
        today = datetime.utcnow().strftime("%Y-%m-%d")
        path = self._telemetry_dir / f"{today}.jsonl"

        if not path.exists():
            return []

        observations = []
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obs = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if channel and obs.get("c") != channel:
                    continue
                observations.append(obs)

        return observations[-limit:][::-1]

    # ── internal ────────────────────────────────────────────

    def _rate_limit(self, channel: str) -> bool:
        """Return False if the channel is exceeding 100 obs/min."""
        now = time.time()
        window = 60.0
        max_per_window = 100

        if channel not in self._channel_timestamps:
            self._channel_timestamps[channel] = deque()

        ts_deque = self._channel_timestamps[channel]

        # Purge timestamps outside the window
        while ts_deque and ts_deque[0] < now - window:
            ts_deque.popleft()

        ts_deque.append(now)

        return len(ts_deque) <= max_per_window

    def _flush_unlocked(self):
        """Write buffered lines to today's file (caller must hold lock)."""
        if not self._buffer:
            return

        today = datetime.utcnow().strftime("%Y-%m-%d")
        path = self._telemetry_dir / f"{today}.jsonl"

        with open(path, "a") as f:
            for line in self._buffer:
                f.write(line + "\n")

        self._buffer.clear()

    # ── context manager ─────────────────────────────────────

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.flush()
        return False

    # ── count ───────────────────────────────────────────────

    def count(self) -> int:
        """Approximate number of observations stored today."""
        today = datetime.utcnow().strftime("%Y-%m-%d")
        path = self._telemetry_dir / f"{today}.jsonl"
        if not path.exists():
            return 0
        with open(path) as f:
            return sum(1 for line in f if line.strip())
