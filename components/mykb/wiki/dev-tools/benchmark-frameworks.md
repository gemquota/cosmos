---
type: "concept"
title: "Benchmark Frameworks"
description: "Frameworks for writing and running reproducible performance comparisons"
tags: ["benchmarking", "performance", "tooling", "metrics"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Benchmark Frameworks

## Summary
Benchmark frameworks (JMH, pytest-benchmark, criterion, hyperfine) standardize how performance experiments are written, executed, and reported. They handle warmup, timing loops, and statistical noise so numbers can be compared across runs.

## Details
- Warmup and iteration control separate JIT warmup effects from steady-state performance.
- Results are reported as distributions (mean, median, percentiles), not single raw timings.
- Guard benchmarks from noise: pin CPU frequency, close background load, and run on dedicated hardware when possible.
- mykb relevance: benchmark article-indexing and wikilink resolution so the knowledge base stays fast at scale.

## Related
- [[wiki/dev-tools/benchmark-testing|Benchmark Testing]]
- [[wiki/testing/performance-testing|Performance Testing]]
- [[wiki/testing/load-testing|Load Testing]]
- [[wiki/dev-tools/profiling-tools|Profiling Tools]]
- [[wiki/testing/response-time-percentiles|Response Time Percentiles]]
