---
type: "concept"
title: "Latency Percentiles"
description: "Reporting latency by percentile so outliers and tail behavior are visible"
tags: ["latency", "percentiles", "metrics", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Latency Percentiles

## Summary
Latency percentiles (p50, p90, p99) describe the distribution of request times instead of just the average. Averages hide the slow requests that frustrate users, so percentiles are the standard way to talk about performance.

## Details
- p50 tells you the typical experience; p99 tells you the worst typical experience; averages are almost useless.
- A single percentile is incomplete — track a few and watch how p99 diverges from p50 as load grows.
- Measuring percentiles requires time-bucketed histograms; naive storage of every latency is too expensive.
- mykb relevance: article-generation latency should be reported at p95 so slow agent turns are visible.

## Related
- [[wiki/dev-tools/four-golden-signals|Four Golden Signals]]
- [[wiki/dev-tools/tail-latency|Tail Latency]]
- [[wiki/testing/response-time-percentiles|Response Time Percentiles]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/dev-tools/metric-backends|Metric Backends]]
