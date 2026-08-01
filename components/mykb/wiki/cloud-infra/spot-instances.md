---
type: "concept"
title: "Spot Instances"
description: "Interruptible, discounted cloud compute that trades reliability for cost on fault-tolerant workloads"
tags: ["spot", "compute", "cost", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Spot Instances

## Summary
Spot instances offer spare cloud capacity at steep discounts in exchange for reclaimability — the provider can terminate them with short notice.

## Details
- Discounts typically run 60–90% off on-demand; pricing fluctuates with supply and demand.
- Design for interruption: checkpoint work, use queues, and spread spot across instance types and zones.
- Mixed fleets (on-demand base + spot burst) balance cost and availability.
- Open question: how to price the risk of interruption into a workload's SLO.

## Related
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — the compute unit spot provides
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]] — the cost lever spot pulls
- [[wiki/cloud-infra/reserved-capacity|Reserved Capacity]] — the predictable alternative
- [[wiki/devops-infra/kubernetes|Kubernetes]] — spot node pools for burst work
