"""Event bus / pub-sub — in-process telemetry backbone (ported from Agent OS).

A thread-safe broker with per-topic subscriber queues and a bounded history
ring so late subscribers can replay.  Topics may contain ``*`` wildcards
(fnmatch semantics): ``subscribe("worker.*")`` receives every event whose
topic matches, e.g. ``worker.task.started`` and ``worker.priority_tick``.
Exact-topic subscriptions are unchanged.

The AO original exposes an async ``stream()``; RSIS3 is sync-first, so
subscriptions here are plain :class:`queue.Queue` objects — ``publish`` is
thread-safe from any worker thread, which is what the thread-pool
dispatchers need.  For distributed setups, swap this class for a Redis or
WebSocket broker with the same ``publish / subscribe / history`` API.
"""

from __future__ import annotations

import fnmatch
import queue
import threading
import time

__all__ = ["EventBus"]


class EventBus:
    """Topic-based publish/subscribe with replayable history."""

    def __init__(self, max_history: int = 250):
        self._subs: dict[str, set[queue.Queue]] = {}
        self._history: dict[str, list[dict]] = {}
        self._max_history = max_history
        self._lock = threading.Lock()

    @staticmethod
    def _matches(pattern: str, topic: str) -> bool:
        """True when `topic` matches the subscription key (exact or wildcard)."""
        if "*" in pattern:
            return fnmatch.fnmatchcase(topic, pattern)
        return topic == pattern

    def publish(self, topic: str, event: dict) -> dict:
        """Fan out one event to all subscribers matching `topic` + history."""
        event = dict(event)
        event.setdefault("ts", time.time())
        event.setdefault("topic", topic)
        with self._lock:
            history = self._history.setdefault(topic, [])
            history.append(event)
            if len(history) > self._max_history:
                del history[:-self._max_history]
            for pattern, queues in list(self._subs.items()):
                if not self._matches(pattern, topic):
                    continue
                for sub_queue in list(queues):
                    sub_queue.put_nowait(event)
        return event

    def subscribe(self, topic: str) -> queue.Queue:
        """Open a subscriber queue for `topic` (exact or ``*`` wildcard)."""
        sub_queue: queue.Queue = queue.Queue()
        with self._lock:
            self._subs.setdefault(topic, set()).add(sub_queue)
        return sub_queue

    def unsubscribe(self, topic: str, sub_queue: queue.Queue) -> None:
        """Close a subscriber queue; it stops receiving new events."""
        with self._lock:
            self._subs.get(topic, set()).discard(sub_queue)

    def drain(self, sub_queue: queue.Queue) -> list[dict]:
        """Pull every currently-queued event from a subscription."""
        events: list[dict] = []
        while True:
            try:
                events.append(sub_queue.get_nowait())
            except queue.Empty:
                return events

    def history(self, topic: str) -> list[dict]:
        """Bounded replayable history for late subscribers / dashboards."""
        with self._lock:
            return list(self._history.get(topic, []))

    @property
    def subscriber_count(self) -> int:
        """Total active subscriber queues (exact + wildcard patterns)."""
        with self._lock:
            return sum(len(queues) for queues in self._subs.values())
