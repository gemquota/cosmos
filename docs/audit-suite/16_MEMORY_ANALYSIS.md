# 16 — Memory Analysis

**Doc ID:** COSMOS-AUDIT-16 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [15 Performance](15_PERFORMANCE_AUDIT.md) · [17 Concurrency](17_CONCURRENCY_ANALYSIS.md) · [29 Risks](29_RISK_REGISTER.md)

---

## 1. Memory Domains

| Domain | In memory | Persisted |
|---|---|---|
| MyKB search index | `SEARCH_INDEX` (docs, idf, paths) + npy vectors | search_index.json + *.npy |
| RSIS telemetry/ledger | in-process accumulators | .jsonl / rack/pulses |
| SPACE sessions | `Map<session_id, SessionState>` | ~/.space/** or sql.js |
| MyKB graph | loaded by tools at build time | graph.json |

## 2. Allocation Profile

- MyKB search: per-query allocations for scores + token counters (GC churn). [I, Med]
- semantic vectors: NumPy arrays, one contiguous block per model — good locality. [O]
- SPACE artifact tracker: holds extracted artifacts for the process lifetime. [I, Low]

## 3. Growth / Eviction

- RSIS `MemoryManager` accumulates outcomes with no eviction/TTL — unbounded growth for long-lived
  workspaces. [I, Med]
- SPACE sessions Map cleared on process exit; persisted sessions reloaded on demand. [O]
- No explicit memory limits at app layer; OS/kernel rlimits only in the sandbox Tier-1. [O]

## 4. Peak Memory Estimates

| Config | Estimate |
|---|---|
| MyKB server (5.4k docs) | search JSON ~ tens of MB + npy vectors (variable) [I, Med] |
| SPACE session (326 Q) | tens of KB per session [I, Low] |
| RSIS memory store | grows with workshop history [I, Med] |

## 5. Findings

- **M1** — No eviction policy for the RSIS outcome store or telemetry aggregator. [I, Med]
- **M2** — `SEARCH_INDEX` may ghost against on-disk changes until rebuild (index vs source skew). [I, Low]
- **M3** — No memory-usage telemetry in the runtime dashboard; only `ResourceEnforcer` on the engine side
  tracks RSS. [O, Med]
- **M4** — npy vectors loaded eagerly at server start; consider lazy load to cut cold-start. [I, Low]

## 6. Recommendations

1. Add rolling window/TTL on `MemoryManager` (keep last N outcomes or by date).
2. Add a `memory: {rss, index_size, doc_count}` status endpoint to MyKB server.
3. Lazy-load npy vectors; flush search index rebuilds. [Low]

---
*End of document 16. Next: [17 Concurrency Analysis](17_CONCURRENCY_ANALYSIS.md).*
