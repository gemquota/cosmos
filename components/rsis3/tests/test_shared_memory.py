"""Unit tests for sync-first SharedMemoryManager (Agent OS D2 port)."""

import threading

from rsis.shared_memory import MemoryConflictError, SharedMemoryManager


def test_write_and_read_versioning():
    mem = SharedMemoryManager()
    assert mem.read("k") is None
    r1 = mem.write("k", {"v": 1}, "agent-a")
    r2 = mem.write("k", {"v": 2}, "agent-b")
    assert r1.version == 1 and r1.updated_by == "agent-a"
    assert r2.version == 2 and r2.updated_by == "agent-b"
    assert mem.read("k").value == {"v": 2}


def test_snapshot_reads_are_immutable_copies():
    mem = SharedMemoryManager()
    mem.write("k", {"v": 1}, "a")
    snap = mem.read("k")
    snap.value = {"v": 999}   # replace the caller's copy
    snap.updated_by = "hacker"
    assert mem.read("k").value == {"v": 1}
    assert mem.read("k").updated_by == "a"
    assert mem.snapshot()["k"].value == {"v": 1}


def test_compare_and_swap_success_and_conflict():
    mem = SharedMemoryManager()
    mem.write("k", "old", "a")
    reg = mem.compare_and_swap("k", 1, "new", "b")
    assert reg.value == "new" and reg.version == 2
    try:
        mem.compare_and_swap("k", 1, "stale", "c")
    except MemoryConflictError as exc:
        assert "expected version 1" in str(exc)
        assert "found 2" in str(exc)
    else:
        raise AssertionError("expected MemoryConflictError")


def test_cas_on_missing_key_requires_version_zero():
    mem = SharedMemoryManager()
    reg = mem.compare_and_swap("new", 0, "seed", "a")
    assert reg.value == "seed" and reg.version == 1
    try:
        mem.compare_and_swap("new", 0, "again", "b")
    except MemoryConflictError:
        pass
    else:
        raise AssertionError("expected MemoryConflictError")


def test_atomic_mutate_initial_and_update():
    mem = SharedMemoryManager()
    reg = mem.atomic_mutate("counter", lambda v: (v or 0) + 1, "a")
    assert reg.value == 1 and reg.version == 1
    reg = mem.atomic_mutate("counter", lambda v: (v or 0) + 1, "b")
    assert reg.value == 2 and reg.version == 2


def test_atomic_mutate_is_lost_update_free_under_threads():
    mem = SharedMemoryManager()
    errors = []

    def worker():
        try:
            for _ in range(100):
                mem.atomic_mutate("counter", lambda v: (v or 0) + 1, "t")
        except Exception as exc:  # pragma: no cover
            errors.append(exc)

    threads = [threading.Thread(target=worker) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert not errors
    reg = mem.read("counter")
    assert reg.value == 800
    assert reg.version == 800


def test_clear_and_snapshot():
    mem = SharedMemoryManager()
    mem.write("a", 1, "x")
    mem.write("b", 2, "y")
    assert set(mem.snapshot().keys()) == {"a", "b"}
    mem.clear()
    assert mem.snapshot() == {}
