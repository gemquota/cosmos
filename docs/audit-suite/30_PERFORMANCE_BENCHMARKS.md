# 30 — Performance Benchmarks

**Doc ID:** COSMOS-AUDIT-30 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [13 Algorithm Analysis](13_ALGORITHM_ANALYSIS.md) · [15 Performance Audit](15_PERFORMANCE_AUDIT.md) · [17 Concurrency](17_CONCURRENCY_ANALYSIS.md)

---

## 1. Observed Data Points (2026-08-04)

| Metric | Value | Source |
|---|---|---|
| Wiki documents | 6,855 | `files.json` |
| `files.json` size | 407 KB | static snapshot |
| Knowledge-graph edges | 35,514 | `graph.json` |
| Python census | 90 files / 21,659 LOC | `data/audit_py.json` |
| TS census | 77 entries | `data/audit_ts.json` |
| Test suite | 49 cases / ~2.2 s | `pytest tests/` |
| Priority-pool suite | 16 cases / ~2.0 s (timing-sensitive) | `test_priority_pool.py` |
| Sidebar render cap | 300 entries (MAX_RENDER) | `index.html` |

## 2. Scaling Behavior (Observed / Inferred)

- **Sidebar:** capped at 300 rendered entries with a count indicator — bounds DOM cost at
  6,855 docs. [O]
- **Search:** TF-IDF over the file list is client-side; `api/v2/search` (daemon) delegates to
  an external search build. Index builds are explicit (rebuild button). [O]
- **Graph:** topology queries accept root + depth (1–5) — bounded subgraph, not full-graph
  render by default. [O]
- **DAG/priority pools:** `num_workers` caps concurrency; retries add latency bounded by
  budget. [O]
- **Wiki daemon:** thread-per-connection; a slow search spawns a subprocess per request
  (expensive at load). [I, Med]

## 3. Benchmark Gaps

- No formal benchmark runner or baseline suite for dashboard load, search latency, or graph
  render time. [O]
- No memory profiling of the viewer at 6,855 docs (list + search index in JS). [O]
- No load test for the wiki daemon / SPACE server. [O]

## 4. Findings

| # | Finding | Severity |
|---|---|---|
| P-1 | Client keeps the full file list + search index in memory; fine at 6.8k, unproven at 50k+ | Low |
| P-2 | Per-request subprocess spawns in the daemon search path are the likely first bottleneck | Med |
| P-3 | Timing-based tests (aging/preemption) add flake risk to CI signal | Low |
| P-4 | `files.json` re-fetches on each load; no cache-control strategy | Low |

## 5. Recommendations

1. Add `bench/` scripts: time `files.json` parse + sidebar render in a headless browser, and
   daemon `/api/stats` + search latency.
2. Cache the parsed file index in `localStorage` with a content-hash guard (files.json ships
   with a hash in `ecosystem.json`).
3. Cache daemon subprocess results (temp index) to avoid per-request spawns.
4. De-flake timing tests with injected clocks.
