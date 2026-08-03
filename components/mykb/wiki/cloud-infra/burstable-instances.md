---
type: "concept"
title: "Burstable Instances"
description: "CPU credits that allow short bursts above baseline"
tags: ["burstable", "cpu", "credits", "aws"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Burstable Instances

## Summary

Burstable instances (AWS t-family, Azure B-series) accumulate CPU credits during idle and spend them on bursts above baseline. They are the right choice for spiky, mostly-idle workloads — and the wrong one for sustained load, where credits run out and performance collapses.

## Details
- Mechanism: credits accrue at the baseline rate (e.g. t3.medium baseline 20%) and are consumed when utilization exceeds baseline; unlimited mode borrows credits at a per-hour surcharge; exhausted credits pin CPU to baseline. Credit balances are per-instance and appear in CloudWatch/B-series metrics.
- Concrete example: a CI runner that idles between jobs bursts to 100% during builds — ideal for t-family; a web server that peaks at 60% for hours during business hours burns through credits and throttles; monitoring CreditBalance trending to zero is the early warning before slowdowns.
- Failure modes: deploying sustained-load services on burstables (database, search) and seeing latency cliffs at credit exhaustion; enabling unlimited without cost alerts (surge pricing surprises); assuming credits survive stop/start (balances persist but can be lost on some lifecycle operations in Azure); and mixing workloads so one noisy neighbor drains shared burst capacity.
- Operational tradeoffs: burstables cut cost dramatically for dev/test and spiky batch; the trade is unpredictable ceilings — pair with autoscaling that replaces the instance class or adds capacity when credit balance drops. Watch the metrics, not intuition.
- RSIS3/mykb relevance: experiment VMs use burstables with credit-balance telemetry, and the loop's planner flags workloads whose CPU utilization pattern disqualifies burstable sizing.
- Baseline planning: model the sustained average, not the peak, when choosing burstable; a workload at 50% average burns credits even if the peak is short, and the ceiling arrives exactly when load rises.
- Autoscaling link: drive scale-out from credit balance, not just CPU; a falling balance is the leading indicator of the throttle that follows.

## Related
- [[wiki/cloud-infra/dedicated-hosts-and-instances|Dedicated Hosts & Instances]]
- [[wiki/cloud-infra/reserved-instances-vs-on-demand|Reserved vs On-Demand Instances]]
- [[wiki/cloud-infra/spot-instances|Spot Instances]]
