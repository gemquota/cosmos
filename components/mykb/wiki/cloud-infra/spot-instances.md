---
type: "concept"
title: "Spot Instances"
description: "Interruptible, discounted cloud compute that trades reliability for cost on fault-tolerant workloads"
tags: ["spot", "compute", "cost", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Spot Instances

## Summary

Spot instances sell spare cloud capacity at 60-90% discounts with the risk of interruption. They are the economic engine of elastic, stateless, and checkpointed workloads — and a reliability trap when used for stateful or latency-critical services.

## Details
- Mechanism: providers price spare capacity dynamically (AWS spot market, GCP preemptible fixed 24h/80% discount, Azure spot); AWS gives 2-minute interruption notices via instance metadata and integrates with EC2 Fleet/ASGs for diversification; workloads must handle termination gracefully — drain, checkpoint, and reschedule. GCP preemptibles stop after 24h or on demand.
- Concrete example: a rendering farm spreads independent jobs across spot fleets with interruption-aware scheduling; a CI runner pool uses spot with on-demand fallback when interruption rates spike; a batch ML training job checkpoints every 5 minutes so a preemption costs minutes, not hours.
- Failure modes: stateful services (queues, databases) on spot losing data on interruption; single long jobs with no checkpointing losing all progress; no capacity diversification (all spot in one AZ/type, so a price spike interrupts everything); and cost models that ignore the retry/restart overhead of interrupted work.
- Operational tradeoffs: spot savings are real but come with availability variance; the pattern is spot for elastic stateless layers + a small on-demand core, with interruption rates monitored and fallback strategies rehearsed. Measure effective savings after accounting for restarts.
- RSIS3/mykb relevance: the wiki's batch layer runs spot-first with checkpointing; this note records interruption-rate telemetry so the loop tunes the spot/on-demand mix empirically.
- Graceful handling: register the interruption-notice handler (metadata polling or instance lifecycle hooks) to run drain logic, and make every job idempotent so a restart anywhere converges.
- Fleet design: use capacity-optimized allocation and mixed instance types so the fleet rides market shifts; monitor the interruption rate per fleet as a first-class metric.

## Related
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — the compute unit spot provides
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]] — the cost lever spot pulls
- [[wiki/cloud-infra/reserved-capacity|Reserved Capacity]] — the predictable alternative
- [[wiki/devops-infra/kubernetes|Kubernetes]] — spot node pools for burst work
