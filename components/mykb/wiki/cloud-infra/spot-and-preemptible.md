---
type: "concept"
title: "Spot & Preemptible Instances"
description: "Interruptible capacity at a discount and how to use it"
tags: ["spot", "preemptible", "cost", "compute"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html",
  "https://cloud.google.com/compute/docs/instances/preemptible",
]
---

# Spot & Preemptible Instances

## Summary
Spot and preemptible instances offer large discounts on idle cloud capacity in exchange for interruption. Stateless, checkpointed workloads can run on them safely and cheaply. They are a major lever for compute cost reduction in batch and elastic workloads.

## Details
- AWS spot instances fluctuate in price with supply and can be reclaimed with a two-minute warning.
- GCP preemptible instances run up to 24 hours and can be reclaimed when demand returns.
- Interruption handling requires graceful shutdown: draining work, checkpointing, and restarting elsewhere.
- Batch jobs, CI workers, and stateless services fit; databases and stateful nodes do not.
- Fleet diversification across instance types improves spot availability.
- In mykb, spot connects to autoscaling, savings plans, and burstable instance articles.
- Combining spot capacity with on-demand fallback keeps critical services available when spot is reclaimed.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.
- Cost and latency tradeoffs for this choice are quantified in the capacity planning and cost-of-bandwidth articles.

## Related
- [[wiki/cloud-infra/spot-market-behavior|Spot Market Behavior]]
- [[wiki/cloud-infra/preemptible-vm-workloads|Preemptible VM Workloads]]
- [[wiki/cloud-infra/spot-instances|Spot Instances]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
