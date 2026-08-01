---
type: "concept"
title: "Right-Sizing"
description: "Adjusting instance and resource sizes to match actual workload demand, cutting waste without sacrificing headroom"
tags: ["right-sizing", "cost", "capacity", "finops"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Right-Sizing

## Summary
Right-sizing matches compute, memory, and storage allocations to what workloads actually use. Over-provisioned fleets waste money; under-provisioned ones degrade performance — measurement finds the middle.

## Details
- Use utilization metrics over weeks, not minutes: p50/p95 CPU and memory paint the real picture.
- Cloud tools make size changes cheap, so iterate: shrink, measure, adjust.
- Beware bursty workloads where p95 utilization justifies the larger size.
- Open question: when does vertical resizing stop and horizontal scaling take over?

## Related
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — the instances being resized
- [[wiki/cloud-infra/autoscaling|Autoscaling]] — automates the size decision
- [[wiki/cloud-infra/capacity-planning|Capacity Planning]] — fleet-level context
- [[wiki/cloud-infra/finops-practices|FinOps Practices]] — cost discipline behind sizing
