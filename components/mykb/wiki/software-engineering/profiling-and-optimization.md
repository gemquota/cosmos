---
type: "concept"
title: "Profiling and Optimization"
description: "Measuring where resources go before and after changing code"
tags: ["profiling", "optimization", "performance", "measurement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Profiling_(computer_programming)", "https://en.wikipedia.org/wiki/Performance_engineering"]
---

# Profiling and Optimization

## Summary
Profiling measures where a program spends CPU, memory, and I/O; optimization then targets the measured hotspots. The discipline is measure-first: profiles replace intuition, and each change is validated against the baseline.

## Details
- Sampling profilers give low-overhead CPU pictures; allocation profiles show memory growth; flame graphs make hotspots obvious.
- Profile in representative environments — production-like data and load, not toy inputs.
- Optimize the top of the profile: a 10% win on a 1% path is noise; a 50% win on a 50% path changes the system.
- Beware premature optimization: correctness and clarity first, then evidence, then speed.
- Optimization is a loop: baseline, change, re-profile, and keep the measurement honest.
- For the mykb bundle, profiling applies to the build and link-check passes that run on every commit.

Worked example — the wiki build takes 3 minutes; a flame graph shows 60% in link resolution, which does regex scanning per file. Caching the slug map cuts build time to 40 seconds, verified by re-profiling.

## Related
- [[wiki/dev-tools/profiling-tools|Profiling Tools]]
- [[wiki/dev-tools/flame-graphs|Flame Graphs]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/dev-tools/benchmark-frameworks|Benchmark Frameworks]]
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/tooling/local-cache|Local Cache]]
- [[wiki/dev-tools/profilers|Profilers]]
- [[wiki/testing/performance-testing|Performance Testing]]
