---
type: "concept"
title: "Profiling Tools"
description: "Tools that measure where CPU time, memory, and I/O are spent in a running program"
tags: ["profiling", "performance", "tooling", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Profiling Tools

## Summary
Profiling tools attach to a process and report where time or memory goes: sampling profilers (perf, py-spy) periodically snapshot the call stack, while tracing profilers instrument every call. Both convert guesses about slowness into evidence — measure first, then change.

## Details
- Mechanism: sampling profilers interrupt the process at intervals and record the stack, building a statistical picture with low overhead — safe for production; tracing profilers instrument every function entry and exit for exact counts, at the cost of slowing execution; heap and allocation profiles track memory growth; off-CPU analysis (waits, locks, I/O) finds stalls that CPU profiles miss.
- Concrete example: py-spy attach to a slow agent process shows 60% of time in tokenization; a Go pprof heap profile shows an unbounded cache; perf on a build machine shows link-time contention; each profile localizes the fix before any optimization is attempted.
- Failure modes: profiling the wrong workload (a benchmark instead of production traffic) leading to irrelevant optimizations; sampling too briefly, missing the hot path; optimized builds with inlined frames obscuring the stack; profile overhead itself distorting results on hot paths; profiling only CPU while the bottleneck is I/O or locking.
- Tradeoffs: sampling is cheap and approximate, tracing is exact and slow — the choice is precision versus overhead; profiling before optimization prevents optimizing the wrong thing, at the cost of tooling time; the mature pattern is sample in production, trace in staging, and re-profile after every change.
- Operational notes: collect profiles under representative load, keep symbols in sync, and automate profile capture during incidents.
- RSIS3 relevance: profile the agent loop to find where token and latency budgets are actually spent — the same measure-before-change discipline for loop efficiency.

- Profile both hot spots and cold waits: a service can be slow because it is busy or because it is blocked.
## Related
- [[wiki/dev-tools/profilers|Profilers]]
- [[wiki/software-engineering/profiling-and-optimization|Profiling and Optimization]]
- [[wiki/dev-tools/flame-graphs|Flame Graphs]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/testing/performance-testing|Performance Testing]]
