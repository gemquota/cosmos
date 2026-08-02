---
type: "concept"
title: "Load Testing"
description: "Applying realistic concurrent load to validate capacity and stability"
tags: ["load-testing", "testing", "k6", "capacity"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grafana.com/docs/k6/latest/testing-guides/", "https://jmeter.apache.org/usermanual/test_plan.html"]
---

# Load Testing

## Summary
Load testing applies realistic concurrent traffic to validate that the system stays within targets, latency, throughput, and error rate, under expected demand. It answers whether the system can handle normal and peak load before users arrive.

## Details
- Model real users: think time, navigation paths, payload mixes, and growth projections.
- k6 scripts, JMeter thread groups, and Locust tasks simulate virtual users.
- Ramp up gradually to observe latency degradation and saturation points.
- Key outputs: throughput ceiling, p95 and p99 latency at target load, and error rate.
- Combine with monitoring: server metrics explain the latency story.
- Load test on realistic hardware and data; scale results with caution.
- Run per release to catch performance regressions early.

## Related
- [[wiki/testing/performance-testing|Performance Testing]] — the umbrella load testing sits under
- [[wiki/testing/stress-testing|Stress Testing]] — beyond-capacity extremes
- [[wiki/testing/response-time-percentiles|Response Time Percentiles]] — target latency metrics
- [[wiki/testing/test-environments|Test Environments]] — realistic infrastructure for load runs
- [[wiki/devops-infra/observability|Observability]] — server metrics during load
- [[wiki/cloud-infra/capacity-planning|Capacity Planning]] — load results inform sizing
