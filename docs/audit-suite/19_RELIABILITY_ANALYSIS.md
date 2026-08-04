# 19 — Reliability Analysis

**Doc ID:** COSMOS-AUDIT-19 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [09 Control Flow](09_CONTROL_FLOW_ANALYSIS.md) · [17 Concurrency](17_CONCURRENCY_ANALYSIS.md) · [20 Resilience](20_RESILIENCE_ANALYSIS.md)

---

## 1. Failure Taxonomy (Observed)

`rsis/error_classifier.py` (Phase D1 port from AO) distinguishes:

| Category | Examples (token-matched) | Disposition |
|---|---|---|
| `TRANSIENT` | 5xx, timeout, connection reset, refused | retry with backoff |
| `RATE_LIMIT` | 429, rate limit, throttled | retry with 2× backoff growth |
| `FATAL` | 400/401/403/404, invalid_api_key, SyntaxError | fail fast, never retry |
| unknown | default | treated as TRANSIENT (safe-to-retry bias) |

## 2. Retry Policy Inventory

| Site | Budget | Backoff | Notes (observed) |
|---|---|---|---|
| L1 tool calls | `l1.max_retries` (L4-tunable, default 3) | jittered exponential | fatal fail-fast; recovered retry reports success (Phase D1 fix) |
| L2 DAG candidates | `parallel_retries` (default 0 = fail fast) | base 0.5s, cap 30s | `dag_task_retrying` events |
| Priority pool (D2) | per-task `max_retries` | category-scaled (2.0 RATE_LIMIT / 1.5 else) | `worker.task.retrying` events |
| Evaluator calls | none (immutable gate) | — | failure propagates to session |

## 3. Budgets & Timeouts

- `rsis/timeout.py` `Budget` guards iterations + wall-clock per session (`session_timeout_s`). [O]
- Cost ledger caps spend (`budget_cap_usd`); exceeding halts the session. [O]
- L2 parallel path ticks the shared budget from coder tasks, so fan-out cannot outrun the
  session budget. [O]
- Tool step timeout + sandbox timeout bound individual executions. [O]

## 4. Failure Propagation (Observed)

- DAG dependents of a failed task settle as `dependency failed: <task>` instead of
  deadlocking (Phase D1 corrected ordering — failed-dep check now precedes readiness). [O]
- Deadlock guard raises on unresolvable cycles; demo + tests assert both paths. [O]
- Recovery manager (`rsis/recovery.py`) implements checkpoint rollback → HITL notify →
  fallback interpreter on cascading failures. [O]

## 5. Reliability Findings

| # | Finding | Severity |
|---|---|---|
| R-1 | Pulse/state JSON writes non-atomic → torn reads on crash | Med |
| R-2 | Thread-per-connection servers have no connection limits | Med |
| R-3 | No automated reliability soak/chaos tests beyond injected-failure unit tests | Low |
| R-4 | Unknown errors default to retryable → a genuinely fatal bug may burn budget before surfacing | Low |
| R-5 | Evaluator is a hard subprocess dependency; if missing, sessions fail at first evaluation | Med |

## 6. Recommendations

1. Add a `max_attempts` sanity ceiling derived from budget when `parallel_retries > 0` so a
   pathological retry loop cannot outlive the session.
2. Implement atomic JSON writes (shared with [17](17_CONCURRENCY_ANALYSIS.md) / [18](18_SECURITY_AUDIT.md)).
3. Add a soak test: run the DAG + priority pool demos with injected flaky/fatal mix under
   `pytest` (extend [26 Testing Audit](26_TESTING_AUDIT.md)).
4. Consider surfacing `last_error_category` on `L2Result` for dashboard reliability metrics.
