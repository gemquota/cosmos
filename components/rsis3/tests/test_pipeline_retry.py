"""Unit tests for DAGWorkerPool retry budgets (Agent OS wave 2)."""

from rsis.pipeline import DAGWorkerPool, TaskStatus


def _events(pool):
    out = []
    pool.on_event = out.append
    return out


def test_transient_retries_then_completes():
    state = {"n": 0}
    events = []
    pool = DAGWorkerPool(num_workers=2, max_retries=3,
                         retry_base_delay_s=0.0, on_event=events.append)
    pool.add_task("a", "worker", {})

    def worker(task):
        state["n"] += 1
        if state["n"] < 3:
            raise ConnectionError("connection reset")
        return "done"

    tasks = pool.run_pipeline(worker)
    assert tasks["a"].status == TaskStatus.COMPLETED
    assert tasks["a"].result == "done"
    assert tasks["a"].attempts == 2
    retry_events = [e for e in events if e.get("kind") == "dag_task_retrying"]
    assert len(retry_events) == 2
    assert retry_events[0]["attempt"] == 1
    assert retry_events[1]["attempt"] == 2
    complete = [e for e in events if e.get("kind") == "dag_complete"][-1]
    assert complete["retries"] == 2


def test_fatal_fails_fast():
    events = []
    pool = DAGWorkerPool(num_workers=2, max_retries=3,
                         retry_base_delay_s=0.0, on_event=events.append)
    pool.add_task("a", "worker", {})

    def worker(task):
        raise ValueError("syntax error")

    tasks = pool.run_pipeline(worker)
    assert tasks["a"].status == TaskStatus.FAILED
    assert tasks["a"].attempts == 0
    assert not [e for e in events if e.get("kind") == "dag_task_retrying"]


def test_budget_exhausted_fails():
    attempts = {"n": 0}
    pool = DAGWorkerPool(num_workers=2, max_retries=1,
                         retry_base_delay_s=0.0)
    pool.add_task("a", "worker", {})

    def worker(task):
        attempts["n"] += 1
        raise RuntimeError("503 service unavailable")

    tasks = pool.run_pipeline(worker)
    assert tasks["a"].status == TaskStatus.FAILED
    assert tasks["a"].attempts == 1
    assert attempts["n"] == 2          # initial run + one retry


def test_dependents_fail_when_dependency_fails():
    pool = DAGWorkerPool(num_workers=2, max_retries=0)
    pool.add_task("a", "fatal", {})
    pool.add_task("b", "never", {}, depends_on=["a"])

    def fatal(task):
        raise ValueError("boom")

    tasks = pool.run_pipeline(fatal)
    assert tasks["a"].status == TaskStatus.FAILED
    assert tasks["b"].status == TaskStatus.FAILED
    assert "dependency failed" in tasks["b"].error


def test_backoff_does_not_trip_deadlock_guard():
    # Even with a non-zero backoff window, the pool must settle rather than
    # raising the deadlock guard while waiting on retry_at.
    pool = DAGWorkerPool(num_workers=1, max_retries=2,
                         retry_base_delay_s=0.05, retry_max_delay_s=0.05)
    pool.add_task("a", "worker", {})
    attempts = {"n": 0}

    def worker(task):
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise TimeoutError("timed out")
        return "ok"

    tasks = pool.run_pipeline(worker)
    assert tasks["a"].status == TaskStatus.COMPLETED
    assert attempts["n"] == 3
