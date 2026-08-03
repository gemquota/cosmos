---
type: "concept"
title: "Preemptible VM Workloads"
description: "Designing stateless, checkpointed work for interruptible VMs"
tags: ["preemptible", "gcp", "spot", "workloads"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Preemptible VM Workloads

## Summary

Preemptible/spot VM workloads are interruptible by design — preemptible instances (GCP), spot instances (AWS/Azure) can be reclaimed with ~30 seconds notice. They offer 60-90% savings for workloads that tolerate interruption: batch, stateless workers, CI, and checkpointed jobs.

## Details
- Mechanism: providers reclaim capacity at will (pricing pressure or capacity need); GCP preemptibles run max 24h and stop with a 30s warning (A3-style preemptibles differ); AWS spot uses a market with interruption reasons (price, capacity) and 2-minute notices on newer instances; Azure spot is similar. Workloads must handle SIGTERM/stop gracefully — checkpoint, drain, and restart elsewhere.
- Concrete example: a rendering farm splits frames into independent tasks; when nodes are preempted, finished frames persist and the scheduler redistributes the rest; CI runners are idempotent (builds can restart); batch ML training checkpoints every few minutes so a preemption loses little work.
- Failure modes: stateful services (databases, queues) on preemptible capacity losing data; single-point workloads (a lone long job) losing hours on one preemption; no re-queueing mechanism, so preempted work is simply lost; and forgetting the 24h cap on GCP preemptibles, breaking jobs assumed to run for days.
- Operational tradeoffs: savings vs reliability — the standard pattern is preemptible for elastic stateless layers with a small on-demand core for coordination; implement interruption handling as a first-class design constraint and measure the effective loss rate (typically 5-15%) against the savings.
- RSIS3/mykb relevance: the wiki's batch experiments would run on preemptible capacity with checkpointing, and the loop records preemption rates to keep the savings-vs-risk decision data-driven.
- Scheduling: run preemptible work during off-peak capacity windows where interruption rates are lowest, and treat interruption metrics as a scheduling input rather than an afterthought.
- Cost accounting: compare effective cost after accounting for restarted work; the discount is real only if the interruption overhead does not eat it.

## Related
- [[wiki/cloud-infra/spot-and-preemptible|Spot & Preemptible Instances]]
- [[wiki/infrastructure/stateful-workloads|Stateful Workloads]]
