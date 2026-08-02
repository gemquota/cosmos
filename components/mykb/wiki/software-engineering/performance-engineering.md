---
type: "concept"
title: "Performance Engineering"
description: "Designing and maintaining systems that meet latency and throughput targets"
tags: ["performance", "latency", "capacity", "engineering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Performance_engineering", "https://en.wikipedia.org/wiki/Profiling_(computer_programming)"]
---

# Performance Engineering

## Summary
Performance engineering treats speed as a designed property: budgets, load testing, profiling, and capacity planning from the start, not firefighting at the end. It spans the whole stack — code, databases, caches, networks — and sets explicit targets.

## Details
- Set performance budgets early: latency per request path, throughput per node, and error budgets for slowness.
- Measure with load tests at realistic scale and percentiles, then profile to find the bottleneck.
- Architecture moves performance: caching layers, indexes, batching, and async paths beat micro-optimizations.
- Performance is a system property: one slow dependency can dominate an otherwise fast path.
- Keep regression testing for speed — CI performance gates catch slowdowns before they ship.
- For the mykb bundle, performance engineering keeps the wiki responsive: index lookups fast, builds quick, sync bounded.

Worked example — the wiki API budget: p95 under 200ms. Load testing shows the tag query at 1.8s; an index and a cache-aside layer bring it to 90ms, and a CI gate fails future regressions.

## Related
- [[wiki/software-engineering/profiling-and-optimization|Profiling and Optimization]]
- [[wiki/dev-tools/benchmark-frameworks|Benchmark Frameworks]]
- [[wiki/tooling/caching-layers|Caching Layers]]
- [[wiki/dev-tools/tail-latency|Tail Latency]]
- [[wiki/testing/load-testing|Load Testing]]
- [[wiki/dev-tools/latency-percentiles|Latency Percentiles]]
- [[wiki/testing/response-time-percentiles|Response Time Percentiles]]
