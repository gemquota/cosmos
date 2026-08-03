---
type: "concept"
title: "Latency Percentiles"
description: "Reporting latency by percentile so outliers and tail behavior are visible"
tags: ["latency", "percentiles", "metrics", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Latency Percentiles

## Summary
Latency percentiles (p50, p90, p99) describe the distribution of request times instead of just the average. Averages hide the slow requests that frustrate users, so percentiles are the standard way to talk about performance — the tail, not the mean, is what users feel.

## Details
- Mechanism: latency samples are aggregated into time-bucketed histograms; percentiles are read from the histogram (p50 is the median, p99 the worst typical case); per-endpoint and per-service percentiles separate the slow paths; percentiles over short windows capture current behavior rather than lifetime history.
- Concrete example: a service reports p50 40ms, p95 120ms, p99 800ms — the p99 reveals a slow path the average of 55ms hides; a dashboard tracks how p99 diverges from p50 as load grows, showing saturation onset before errors appear; SLOs are defined on percentiles (p99 under 500ms), tying performance to a number.
- Failure modes: reporting only averages, hiding the tail; percentiles computed over too-long windows, masking spikes; bucket boundaries too coarse, distorting the p99; comparing percentiles across different measurement points (server time versus user-perceived time); ignoring the error path — slow errors counted as fast or excluded entirely.
- Tradeoffs: percentiles give an honest view of the distribution at the cost of histogram storage and careful bucketing; the alternative, averages, is cheap and misleading; the mature pattern is a few percentiles (p50/p95/p99) per endpoint, time-bucketed, feeding SLOs and burn alerts.
- Operational notes: align bucket boundaries with targets, monitor percentile divergence, and always include the error path in latency measurement.
- RSIS3 relevance: article-generation latency should be reported at p95 so slow agent turns are visible — the same tail-awareness RSIS3 wants in its telemetry.

- Report percentiles with the sample count and window so a thin sample is not mistaken for a stable p99.
## Related
- [[wiki/dev-tools/four-golden-signals|Four Golden Signals]]
- [[wiki/dev-tools/tail-latency|Tail Latency]]
- [[wiki/testing/response-time-percentiles|Response Time Percentiles]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/dev-tools/metric-backends|Metric Backends]]
