"""Unit tests for the sync-first EventBus (Agent OS D2 port)."""

import threading
import time

from rsis.event_bus import EventBus


def test_publish_delivers_to_exact_subscriber():
    bus = EventBus()
    sub = bus.subscribe("worker.task.started")
    bus.publish("worker.task.started", {"task_id": "a"})
    events = bus.drain(sub)
    assert len(events) == 1
    assert events[0]["task_id"] == "a"
    assert events[0]["topic"] == "worker.task.started"
    assert "ts" in events[0]


def test_wildcard_subscription():
    bus = EventBus()
    sub = bus.subscribe("worker.*")
    bus.publish("worker.task.started", {})
    bus.publish("worker.priority_tick", {"items": []})
    bus.publish("unrelated", {})
    topics = {e["topic"] for e in bus.drain(sub)}
    assert topics == {"worker.task.started", "worker.priority_tick"}


def test_history_replay_for_late_subscriber():
    bus = EventBus()
    bus.publish("worker.task.completed", {"task_id": "a"})
    # Late subscriber replays from bounded history even without receiving live.
    hist = bus.history("worker.task.completed")
    assert len(hist) == 1
    assert hist[0]["task_id"] == "a"
    assert bus.history("never.published") == []


def test_history_is_bounded():
    bus = EventBus(max_history=5)
    for i in range(10):
        bus.publish("tick", {"i": i})
    hist = bus.history("tick")
    assert len(hist) == 5
    assert hist[0]["i"] == 5
    assert hist[-1]["i"] == 9


def test_unsubscribe_stops_delivery():
    bus = EventBus()
    sub = bus.subscribe("topic")
    bus.unsubscribe("topic", sub)
    bus.publish("topic", {})
    assert bus.drain(sub) == []
    assert bus.subscriber_count == 0


def test_thread_safe_publish():
    bus = EventBus()
    sub = bus.subscribe("load")
    errors = []

    def publisher(start):
        start.wait()
        for i in range(200):
            bus.publish("load", {"i": i})

    start = threading.Event()
    threads = [threading.Thread(target=publisher, args=(start,))
               for _ in range(4)]
    for t in threads:
        t.start()
    start.set()
    for t in threads:
        t.join()
    events = bus.drain(sub)
    assert len(events) == 800
    assert bus.subscriber_count == 1
    # History recorded the same stream.
    assert len(bus.history("load")) == 250  # capped


def test_matches_semantics():
    assert EventBus._matches("worker.*", "worker.task.started")
    assert not EventBus._matches("worker.*", "worker")  # fnmatch: dot required
    assert not EventBus._matches("worker.*", "space.task")
    assert EventBus._matches("worker.task.started", "worker.task.started")
    assert not EventBus._matches("worker.task.started", "worker.task.done")
