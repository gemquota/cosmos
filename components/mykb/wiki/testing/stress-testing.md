---
type: "concept"
title: "Stress Testing"
description: "Pushing systems beyond expected capacity to find breaking points"
tags: ["stress-testing", "testing", "capacity", "resilience"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grafana.com/docs/k6/latest/testing-guides/stress-testing/", "https://www.ibm.com/topics/stress-testing"]
---

# Stress Testing

## Summary
Stress testing pushes the system beyond expected capacity to find its breaking point and observe how it fails. It reveals whether overload leads to graceful degradation, circuit breaking, or a cascading outage.

## Details
- Load beyond peak, commonly two to ten times expected traffic, until errors or saturation.
- Identify the ceiling: max throughput, memory exhaustion, connection limits, queue backlogs.
- Observe the failure mode: timeouts, 503s, retries, circuit breakers, crash-restart loops.
- Results feed capacity planning, autoscaling configuration, and chaos experiments.
- Check recovery: does the system drain queues and stabilize after load drops?
- Distinguish from spike testing: stress is sustained overload, spike is a burst.
- The k6 stress-testing guide documents the standard approach.

## Related
- [[wiki/testing/load-testing|Load Testing]] — within-capacity baseline before stress
- [[wiki/testing/spike-testing|Spike Testing]] — sudden bursts versus sustained overload
- [[wiki/testing/recovery-testing|Recovery Testing]] — behavior after the breaking point
- [[wiki/cloud-infra/autoscaling|Autoscaling]] — elastic response under stress
- [[wiki/testing/chaos-engineering|Chaos Engineering]] — failure injection beyond load
- [[wiki/cloud-infra/capacity-planning|Capacity Planning]] — stress results set sizing
