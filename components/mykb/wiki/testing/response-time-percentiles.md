---
type: "concept"
title: "Response Time Percentiles"
description: "Evaluating latency via p50, p95, and p99 distributions"
tags: ["latency", "testing", "percentiles", "slo"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grafana.com/docs/k6/latest/using-k6/metrics/", "https://prometheus.io/docs/practices/histograms/"]
---

# Response Time Percentiles

## Summary
Response time percentiles, p50, p95, and p99, describe the latency distribution better than averages, because a few slow requests skew the mean. Tail latency determines perceived quality and SLO compliance.

## Details
- Percentiles: p50 is the typical user, p95 and p99 the slowest users, and max is mostly noise.
- Averages hide the tail: a 200 millisecond mean can coexist with a five second p99.
- Measure per endpoint and dependency; waterfall analysis finds the tail source.
- High p99 causes: GC pauses, cold caches, contention, retries, and oversized payloads.
- Set SLOs on percentiles, for example p99 under 300 milliseconds, and alert on error budgets.
- k6, Prometheus, and tracing systems all report percentile views.
- Streaming and batch pipelines track per-stage latency percentiles too.

## Related
- [[wiki/testing/performance-testing|Performance Testing]] — latency measurement context
- [[wiki/testing/performance-budgets|Performance Budgets]] — percentile thresholds as budgets
- [[wiki/devops-infra/error-budgets|Error Budgets]] — SLOs expressed on percentiles
- [[wiki/devops-infra/golden-signals|Golden Signals]] — latency as an operational signal
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]] — locating tail latency sources
- [[wiki/testing/load-testing|Load Testing]] — collecting percentile distributions
