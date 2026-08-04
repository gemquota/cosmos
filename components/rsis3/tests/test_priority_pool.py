"""Unit tests for the sync-first priority pool stack (Agent OS D2 port)."""

import concurrent.futures
import threading
import time

from rsis.event_bus import EventBus
from rsis.pipeline import TaskStatus
from rsis.priority_pool import (
    AdvancedPriorityWorkerPool,
    CheckpointRunner,
    CheckpointWorkerPool,
    PriorityWorkerPool,
    TaskPreemptedError,
)


def _starts(pool, tasks):
    """Run a single-worker pool and return observed start order."""
    order = []
    lock = threading.Lock()

    def run(task):
        with lock:
            order.append(task.task_id)
        time.sleep(0.01)
        return task.task_id

    for tid, prio in tasks:
        pool.add_task(tid, "worker", {}, priority=prio)
    pool.run(run)
    return order


def test_priority_dispatch_order():
    order = _starts(PriorityWorkerPool(num_workers=1),
                    [("a", 1.0), ("b", 10.0), ("c", 1.0)])
    assert order == ["b", "a", "c"]


def test_aging_reorders_long_waited_task():
    pool = AdvancedPriorityWorkerPool(num_workers=1, aging_rate=200.0)
    pool.add_task("a", "worker", {}, priority=1.0)
    time.sleep(0.05)
    pool.add_task("b", "worker", {}, priority=10.0)
    time.sleep(0.05)
    pool.add_task("c", "worker", {}, priority=1.0)
    order = _starts(pool, [])
    assert order == ["a", "b", "c"]


def test_transient_retries_then_completes():
    state = {"n": 0}
    bus = EventBus()
    pool = PriorityWorkerPool(num_workers=2, event_bus=bus,
                              base_backoff_sec=0.0, max_backoff_sec=0.01)
    pool.add_task("a", "worker", {}, max_retries=3)

    def worker(task):
        state["n"] += 1
        if state["n"] < 3:
            raise ConnectionError("connection reset")
        return "done"

    tasks = pool.run(worker)
    assert tasks["a"].status == TaskStatus.COMPLETED
    assert tasks["a"].result == "done"
    assert tasks["a"].attempts == 2
    retrying = [e for e in bus.history("worker.task.retrying")]
    assert len(retrying) == 2
    assert retrying[0]["error_category"] == "TRANSIENT"
    assert retrying[0]["attempts"] == 1
    complete = bus.history("worker.pool.complete")[-1]
    assert complete["retries"] == 2


def test_fatal_fails_fast():
    bus = EventBus()
    pool = PriorityWorkerPool(num_workers=2, event_bus=bus,
                              base_backoff_sec=0.0)
    pool.add_task("a", "worker", {}, max_retries=3)

    def worker(task):
        raise ValueError("invalid_api_key")

    tasks = pool.run(worker)
    assert tasks["a"].status == TaskStatus.FAILED
    assert tasks["a"].attempts == 0
    assert not bus.history("worker.task.retrying")
    failed = bus.history("worker.task.failed")[-1]
    assert failed["reason"] == "FATAL_ERROR"


def test_budget_exhausted():
    bus = EventBus()
    pool = PriorityWorkerPool(num_workers=2, event_bus=bus,
                              base_backoff_sec=0.0, max_backoff_sec=0.01)
    pool.add_task("a", "worker", {}, max_retries=2)

    def worker(task):
        raise ConnectionError("connection timed out")

    tasks = pool.run(worker)
    assert tasks["a"].status == TaskStatus.FAILED
    assert tasks["a"].attempts == 2
    assert len(bus.history("worker.task.retrying")) == 2
    failed = bus.history("worker.task.failed")[-1]
    assert failed["reason"] == "BUDGET_EXHAUSTED"


def test_rate_limit_retry_category():
    bus = EventBus()
    pool = PriorityWorkerPool(num_workers=2, event_bus=bus,
                              base_backoff_sec=0.0, max_backoff_sec=0.01)
    pool.add_task("a", "worker", {}, max_retries=1)

    state = {"n": 0}

    def worker(task):
        state["n"] += 1
        if state["n"] < 2:
            raise RuntimeError("429 rate limit exceeded")
        return "ok"

    tasks = pool.run(worker)
    assert tasks["a"].status == TaskStatus.COMPLETED
    retrying = bus.history("worker.task.retrying")[0]
    assert retrying["error_category"] == "RATE_LIMIT"


def test_failed_dependency_propagates():
    pool = PriorityWorkerPool(num_workers=2, base_backoff_sec=0.0)
    pool.add_task("a", "worker", {}, max_retries=0)
    pool.add_task("b", "worker", {}, depends_on=["a"], max_retries=0)

    def worker(task):
        if task.task_id == "a":
            raise ValueError("fatal")
        return "b"

    tasks = pool.run(worker)
    assert tasks["a"].status == TaskStatus.FAILED
    assert tasks["b"].status == TaskStatus.FAILED
    assert tasks["b"].error == "dependency failed: a"


def test_deadlock_guard():
    pool = PriorityWorkerPool(num_workers=2)
    pool.add_task("a", "worker", {}, depends_on=["b"])
    pool.add_task("b", "worker", {}, depends_on=["a"])

    def worker(task):
        return task.task_id

    try:
        pool.run(worker)
    except RuntimeError as exc:
        assert "deadlock" in str(exc)
        assert "a" in str(exc) and "b" in str(exc)
    else:
        raise AssertionError("expected RuntimeError for cyclic deps")


def test_cancel_pending_task():
    ran = []
    pool = PriorityWorkerPool(num_workers=1)
    pool.add_task("a", "worker", {})
    assert pool.cancel_task("a") is True
    pool.run(lambda task: ran.append(task.task_id) or "x")
    assert ran == []


def test_events_published_to_bus():
    bus = EventBus()
    sub = bus.subscribe("worker.*")
    pool = PriorityWorkerPool(num_workers=2, event_bus=bus,
                              base_backoff_sec=0.0)
    pool.add_task("a", "worker", {})
    pool.run(lambda task: "ok")
    topics = {e["topic"] for e in bus.drain(sub)}
    assert topics >= {
        "worker.task.created", "worker.task.started",
        "worker.task.completed", "worker.pool.complete",
    }


def test_update_task_priority_requeues_order():
    pool = AdvancedPriorityWorkerPool(num_workers=1, aging_rate=0.0)
    pool.add_task("a", "worker", {}, priority=1.0)
    pool.add_task("b", "worker", {}, priority=10.0)
    assert pool.update_task_priority("a", 20.0) is True
    # a was PENDING, so the boost takes effect before dispatch.
    order = _starts(pool, [])
    assert order == ["a", "b"]
    assert pool.update_task_priority("a", 1.0) is False  # already running


def test_checkpoint_runner_skips_completed_steps():
    task = pool_add("work")
    executed = []
    runner = CheckpointRunner(task)
    state = {"v": 0}

    def step(v):
        executed.append(v["v"])
        return {"v": v["v"] + 1}

    s = runner.run_step(0, "s0", step, state)
    s = runner.run_step(1, "s1", step, s)
    # Simulated preemption after step 1: checkpoint step_index == 1.
    s = runner.run_step(2, "s2", step, s)
    assert executed == [0, 1, 2]
    assert task.checkpoint.step_index == 2
    # A fresh runner on the same task resumes from the checkpoint.
    runner2 = CheckpointRunner(task)
    s2 = runner2.run_step(0, "s0", step, {})
    assert s2["v"] == 3 and executed == [0, 1, 2]


def test_preempted_task_resumes_from_checkpoint():
    bus = EventBus()
    pool = AdvancedPriorityWorkerPool(num_workers=1, event_bus=bus,
                                      preemption_threshold=0.0)
    task = pool.add_task("work", "worker", {}, priority=5.0)
    executed = []

    def make_step(idx):
        def step(state):
            time.sleep(0.05)
            executed.append(idx)
            return dict(state, last=idx)
        return step

    def run(task):
        runner = CheckpointRunner(task, event_bus=bus)
        state = {"last": -1}
        for idx, name in enumerate(["step0", "step1", "step2", "step3"]):
            state = runner.run_step(idx, name, make_step(idx), state)
        return state

    # Run in a worker thread; preempt mid-flight, then join.
    result = {}
    thread = threading.Thread(target=lambda: result.update(pool.run(run)))
    thread.start()
    time.sleep(0.10)   # mid-step-1
    assert pool.request_preemption("work") is True
    thread.join(timeout=10)

    tasks = pool.tasks
    assert tasks["work"].status == TaskStatus.COMPLETED
    assert tasks["work"].completed_steps == ["step0", "step1", "step2", "step3"]
    assert executed == [0, 1, 2, 3]      # no step re-ran after resume
    assert tasks["work"].priority >= 6.0  # +1.0 compensation boost
    assert len(bus.history("worker.task.preempted")) == 1
    assert bus.history("worker.task.requeued")[-1]["reason"] == \
        "preempted_by_higher_priority"


def test_preempt_lowest_for_threshold():
    pool = AdvancedPriorityWorkerPool(preemption_threshold=5.0)
    low = pool.add_task("low", "worker", {}, priority=1.0)
    high = pool.add_task("high", "worker", {}, priority=10.0)
    pool._running_futures["low"] = concurrent.futures.Future()  # RUNNING stub
    pool._preempt_lowest_for(high)
    assert low.preempt_requested is True
    assert high.preempt_requested is False
    low.preempt_requested = False
    close = pool.add_task("close", "worker", {}, priority=5.0)
    pool._preempt_lowest_for(close)   # 5 < 1 + 5 -> no preemption
    assert low.preempt_requested is False


def test_priority_tick_emitted():
    bus = EventBus()
    pool = CheckpointWorkerPool(num_workers=1, event_bus=bus,
                                aging_rate=5.0, aging_interval_s=0.1)
    pool.add_task("a", "worker", {}, priority=10.0)
    pool.add_task("b", "worker", {}, priority=1.0, depends_on=["a"])

    def run(task):
        time.sleep(0.3)
        return "ok"

    pool.run(run)
    ticks = bus.history("worker.priority_tick")
    assert ticks
    items = ticks[0]["items"]
    b_item = next(i for i in items if i["task_id"] == "b")
    assert b_item["aged_delta"] >= 0.0
    assert b_item["effective_prio"] >= b_item["base_prio"]


def pool_add(task_id="work"):
    pool = PriorityWorkerPool(num_workers=1)
    return pool.add_task(task_id, "worker", {}, priority=5.0)


def test_checkpoint_runner_preempt_requested_raises():
    task = pool_add()
    task.preempt_requested = True
    runner = CheckpointRunner(task)
    try:
        runner.run_step(0, "s0", lambda s: s, {})
    except TaskPreemptedError:
        pass
    else:
        raise AssertionError("expected TaskPreemptedError")
