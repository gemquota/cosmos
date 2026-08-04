---
type: "entity"
title: "Stress Testing"
description: "Testing a system under extreme load to find its breaking point"
tags: ["entity", "testing", "load", "performance", "reliability"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# Stress Testing

## Summary

Stress testing pushes a system beyond normal operating conditions to discover its breaking point, failure mode, and recovery behavior. It differs from load testing, which validates expected traffic, by probing what happens past the edge. It matters because the first time a system should learn its limits is not during a real outage.

## Details

- **Definition** — Stress tests ramp load beyond capacity — more users, more data, faster rates — and observe degradation, errors, and recovery.
- **Goals** — Find saturation points, confirm graceful degradation, verify timeouts and queues behave, and measure recovery after load drops.
- **Metrics** — Throughput, latency percentiles, error rates, and resource utilization are tracked against the rising load to locate the cliff.
- **Worked example** — A test ramps requests from 100 to 10,000 per second; at 8,000, latency percentiles climb and errors appear, revealing a database connection limit.
- **Common failure modes** — Testing through a single entry point that hides component limits, load generators bottlenecking first, and destroying environments with runaway load.
- **Practical relevance** — Results feed capacity planning, autoscaling thresholds, and chaos practices that harden the system.
- **Variants** — Soak testing holds moderate load over time to find leaks; spike testing jumps load sharply to test elasticity.
- **Telemetry note** — The stub carries a testing tag; this note preserves the stress-testing practice from session telemetry.
- **Environment** — Stress runs belong on dedicated or isolated environments so degradation does not affect production tenants or neighboring workloads.
- **Baselines** — Comparing results against a baseline build isolates regressions from genuine capacity limits, making the test a regression gate as well as a discovery tool.
- **Worked example** — A stress run doubles the baseline request rate until errors exceed one percent; the recorded saturation point updates the autoscaler's ceiling.
- **Recovery** — Measuring how quickly the system drains queues and returns to normal after load stops reveals whether it recovers or lingers degraded.

## Related

- [[wiki/testing/stress-testing|Stress Testing]] — the practice area
- [[wiki/testing/chaos-engineering|Chaos Engineering]] — fault injection sibling
- [[wiki/testing/api-testing|API Testing]] — functional baseline
- [[wiki/api-protocols/timeouts|Timeouts]] — behavior under pressure
- [[wiki/cloud-infra/timeouts-and-deadlines|Timeouts and Deadlines]] — distributed bounds
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/crisismonitor|CrisisMonitor]] — watching the fallout
