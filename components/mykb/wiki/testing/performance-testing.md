---
type: "concept"
title: "Performance Testing"
description: "Measuring response times, throughput, and resource usage under conditions"
tags: ["performance-testing", "testing", "latency", "throughput"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grafana.com/docs/k6/latest/", "https://jmeter.apache.org/"]
---

# Performance Testing

## Summary
Performance testing measures response times, throughput, and resource usage under defined conditions to validate speed, stability, and capacity. It turns performance from opinion into data collected before release, not after an incident.

## Details
- Types: load, stress, soak, spike, volume, and endurance testing.
- Tools: k6, JMeter, Gatling, Locust, and Vegeta; browser-level checks via Playwright and Lighthouse.
- Metrics: latency distribution, throughput, error rate, CPU, memory, and saturation points.
- Establish baselines in controlled environments and compare against budgets.
- Environment realism matters: hardware, network, and data volume change results.
- Run reduced-scale performance tests in CI and full-scale pre-release.
- Investigate regressions with profilers and fix the measured bottleneck.

## Related
- [[wiki/testing/load-testing|Load Testing]] — realistic demand within performance work
- [[wiki/testing/response-time-percentiles|Response Time Percentiles]] — how latency is reported
- [[wiki/testing/performance-budgets|Performance Budgets]] — thresholds performance tests verify
- [[wiki/dev-tools/profilers|Profilers]] — finding the bottleneck behind regressions
- [[wiki/dev-tools/benchmark-testing|Benchmark Testing]] — micro-level speed measurement
- [[wiki/testing/test-environments|Test Environments]] — realistic infrastructure for valid results
