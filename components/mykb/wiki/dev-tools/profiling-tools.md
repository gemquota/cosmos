---
type: "concept"
title: "Profiling Tools"
description: "Tools that measure where CPU time, memory, and I/O are spent in a running program"
tags: ["profiling", "performance", "tooling", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Profiling Tools

## Summary
Profiling tools attach to a process and report where time or memory goes: sampling profilers (perf, py-spy) periodically snapshot the call stack, while tracing profilers instrument every call. Both convert guesses about slowness into evidence.

## Details
- Sampling profilers have low overhead and are safe for production; tracing profilers give exact counts but slow execution.
- CPU profiles find hotspots; heap and allocation profiles find memory growth; off-CPU analysis finds waits.
- Profiling before optimization prevents optimizing the wrong thing — measure first, then change.
- RSIS3 relevance: profile the agent loop to find where token and latency budgets are actually spent.

## Related
- [[wiki/dev-tools/profilers|Profilers]]
- [[wiki/software-engineering/profiling-and-optimization|Profiling and Optimization]]
- [[wiki/dev-tools/flame-graphs|Flame Graphs]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/testing/performance-testing|Performance Testing]]
