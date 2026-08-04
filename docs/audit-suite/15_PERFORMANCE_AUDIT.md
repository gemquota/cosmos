# 15 — Performance Audit

**Doc ID:** COSMOS-AUDIT-15 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [13 Algorithms](13_ALGORITHM_ANALYSIS.md) · [16 Memory](16_MEMORY_ANALYSIS.md) · [17 Concurrency](17_CONCURRENCY_ANALYSIS.md)

> All figures are estimates unless marked [O] (observed). No profiler was run in this audit (no tooling
> installed); a profiling plan is in §8.

---

## 1. Hotspots

| Hotspot | Where | Why | Severity |
|---|---|---|---|
| TF-IDF search loop | `mykb/server.py search_query` | O(Q·D) scan + per-doc `open()` title reads | High at scale |
| Semantic index load | `search_fusion.py` | loads npy vectors into RAM at start; large for corpus | Med |
| Graph build | `build_graph.py` / `enrich_links.py` | full-corpus passes; multi-minute regenerations | Med |
| Priority pool aging | `priority_pool.py pop` | O(log N) fine; aging rewrites could thrash | Low |
| Dashboard aggregation | `gen-static-data.py` | reads all pulses + telemetry each run | Med |
| SPACE exports | exporters | pure string transforms; fine | Low |
| RSIS telemetry flush | `telemetry.py` | per-interval write amplification if flush tiny | Low |

## 2. CPU / Allocation

- Python HTTP servers (`http.server`, `ThreadingTCPServer`) are single-threaded default for handler
  bodies except ThreadingTCPServer (thread-per-connection) — CPU bound under concurrent wiki reads. [I, Med]
- `search_query` allocates per query (word counts, score lists) — GC churn at scale. [I, Med]

## 3. Disk I/O

| Path | Pattern | Impact |
|---|---|---|
| MyKB search index | load once at start; big file (search_index.json + npy) | startup latency |
| graph.json build | full-corpus rewrite each run | per-run seconds-to-minutes |
| pulses | append pulse-NNN.json per pulse | small |
| state files | read at start, write per tuning cycle | negligible |
| wiki `files.json`/`ecosystem.json` | full rewrite by gen-static-data.py | per-commit churn |

## 4. Network I/O

- Localhost-only servers: low by design. RRP pulses / SPACE LLM calls are the only external I/O —
  latency governed by provider API. [I, High impact for loop throughput]

## 5. Concurrency & Lock Contention

- GIL serializes Python compute. `ThreadingTCPServer` → thread-per-connection for the rack dashboard.
- `SharedMemoryManager` guards a shared dict with a lock; candidates contend only during gather. [I, Low]
- No async; no multiprocessing in RSIS3 except `subprocess` tool sandboxing. [O]

## 6. Latency / Throughput Estimates

| Operation | Est. latency |
|---|---|
| MyKB search (5.4k docs, single word) | ~10–50 ms (in-memory loop) [I, Med] |
| Wiki graph rebuild | 10–90 s [I, Med] |
| SPACE `space run` single probe | milliseconds (no LLM) / LLM-call-latency with provider |
| RSIS single pulse (CPU-only) | dominated by tool sandbox + evaluator subprocess |

## 7. Big-O Bottleneck Summary

- Search O(Q·D) — the main asymptotic problem.
- Contradiction detection O(A²) — bounded (≤326 answers) and acceptable.
- Everything else is O(N) or better.

## 8. Profiling Recommendations

1. `python -m cProfile -s cumulative components/mykb/.wiki-daemon/search_fusion.py build-index`
   to confirm graph/search costs.
2. Instrument `server.py search_query` with `perf_counter` around the doc loop (log p95).
3. For the rack/dashboard, time `gen-static-data.py` and monitor link/edge counts.
4. Consider `py-spy dump` on a running loop to find CPU stalls.

## 9. Micro/Macro Optimizations

**Micro (this week):** precompute doc lengths + idf at index build; cache `titles[]`; use array of
`paths` without re-reading files per query; vectorize TF scoring with NumPy.

**Macro (this quarter):** inverted index (or SQLite FTS5) for MyKB; incremental graph updates;
move heavy `gen-static-data.py` off the critical dashboard path (cache the JSON, recompute in CI).

---
*End of document 15. Next: [16 Memory Analysis](16_MEMORY_ANALYSIS.md).*
