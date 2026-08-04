---
type: "entity"
title: "PerformanceMetric"
resource: ""
---
description: "Quantifying system performance through latency, throughput, and error signals"
tags: ["entity", "android", "api", "ast", "auth", "authorization", "performance", "metrics"]
timestamp: "2026-07-19T22:41:43Z"

# PerformanceMetric

## Summary
A performance metric quantifies how well a system meets its timing and capacity goals, typically through latency, throughput, and error measurements. It matters because teams cannot improve what they cannot measure, and vague impressions of "slowness" hide where the problem actually is. Well-chosen metrics convert performance debates into data. The hard part is choosing and instrumenting the right ones consistently.

## Details
- **Definition** — performance metrics describe response times, request rates, concurrency, and error counts over a defined window.
- **Latency distributions** — percentiles such as p50, p95, and p99 expose the tail, which averages hide; tail latency drives user-perceived quality.
- **Throughput** — requests per second and the saturation point show how much work a system sustains before degrading.
- **Error rate** — the share of failed requests is a performance signal in its own right, since errors are the worst response time.
- **Measurement integrity** — metrics are only meaningful with consistent sampling, defined start and end points, and correct clock handling.
- **Budgeting** — explicit budgets, such as "p95 under 200 ms", turn metrics into contracts that regressions can be measured against.
- **Correlation** — joining performance metrics with deployment and traffic events explains why a number moved.
- **Common failure modes** — averaging away the tail, measuring client and server times inconsistently, and alerting on noisy raw values.
- **Worked example** — an API team tracks p50 and p99 latency per endpoint; after a schema change, p99 climbs, the diff is caught by the budget, and the team reverts.
- **Practical relevance** — disciplined performance metrics make capacity planning and regression detection routine rather than reactive.

## Related
- [[wiki/software-engineering/metrics-and-monitoring|Metrics and Monitoring]] — collecting signals
- [[wiki/software-engineering/performance-engineering|Performance Engineering]] — acting on metrics
- [[wiki/testing/performance-testing|Performance Testing]] — measuring under load
- [[wiki/testing/response-time-percentiles|Response Time Percentiles]] — tail analysis
- [[wiki/testing/load-testing|Load Testing]] — driving workload
- [[wiki/data-storage/anomaly-detection-in-metrics|Anomaly Detection in Metrics]] — spotting regressions
