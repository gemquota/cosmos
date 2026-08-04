# 26 — Testing & Verification Audit

**Doc ID:** COSMOS-AUDIT-26 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [07 Function-by-Function](07_FUNCTION_BY_FUNCTION_AUDIT.md) · [22 Build & CI](22_BUILD_CI_ANALYSIS.md) · [27 Code Quality](27_CODE_QUALITY_SCORECARD.md)

---

## 1. Test Inventory (Observed)

`components/rsis3/tests/` — the seed pytest suite (49 cases, ~2s):

| Suite | Focus | Cases |
|---|---|---|
| `test_error_classifier.py` | retry classification | 10 |
| `test_pipeline_retry.py` | DAG retry budgets, fatal fail-fast, deadlock guard | ~8 |
| `test_loop_l1_retry.py` | L1 transient/fatal/rate-limit retry | ~8 |
| `test_event_bus.py` | pub/sub, wildcards, history, thread safety | 7 |
| `test_shared_memory.py` | OCC, atomic mutate, lock behavior | 7 |
| `test_priority_pool.py` | priority ordering, aging, preemption, checkpoints | 16 |
| `test_l2_parallel_d2.py` | L2 parallel session + telemetry bridge | (integration) |

## 2. Other Verification Paths

- `python -m rsis pipeline` — demo asserts retry recovery, fatal fail-fast, deadlock guard. [O]
- `python -m rsis check-practices` — registry invariants, state-file disjointness, telemetry
  coverage, checkpoints (17 checks). [O]
- `gen-static-data.py --check` — snapshot freshness verification. [O]
- Byte-compile + whitespace checks used during development (not scripted). [O]

## 3. Coverage Gaps (High → Low)

| Gap | Severity |
|---|---|
| Loops L3–L9 (evolution, meta-optimizer, strategies, identity, metacog, metameta, MMM) have **no** unit tests | High |
| Wiki markdown parser (`index.html` `parseMarkdown`) is untested | Med |
| Wiki daemon endpoints (search, stats, graph topology) untested | Med |
| Dashboard JS (charts, event rendering) untested | Med |
| `memory.py` vector store (numpy path) untested | Med |
| No mutation/fuzz input for error classifier tokens | Low |
| No E2E browser test (agent-browser unavailable in this env) | Low |

## 4. Findings

| # | Finding | Severity |
|---|---|---|
| T-1 | Test suite exists only for the AO-port surface (D1/D2); core loops untested | High |
| T-2 | No CI runs the suite on push (see [22](22_BUILD_CI_ANALYSIS.md)) | High |
| T-3 | Tests use real timers/sleeps in a few places (priority aging, preemption) → mild flake risk | Low |
| T-4 | `requirements.txt` has pytest, but no `pytest.ini`/`pyproject` config; tests rely on `conftest.py` sys.path bootstrap | Low |

## 5. Recommendations

1. Add smoke tests for each loop command (`python -m rsis optimize/strategies/identity/…`)
   asserting exit code + telemetry write.
2. Extract `parseMarkdown` into a testable module or add a Node test harness for the wiki
   viewer.
3. Add a `pytest.ini` with `testpaths`, and CI wiring from [22](22_BUILD_CI_ANALYSIS.md).
4. Convert the timing-sensitive priority tests to inject clocks where feasible.
