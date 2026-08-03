---
type: "concept"
title: "Reserved vs On-Demand Instances"
description: "Trading flexibility for price with commitment-based pricing"
tags: ["ri", "on-demand", "pricing", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Reserved vs On-Demand Instances

## Summary

Reserved instances and savings plans commit to capacity or spend in exchange for discounts (up to 70%+); on-demand pays list price for flexibility. The choice is a financial hedge: commitment discounts for steady baselines, on-demand for elasticity and uncertainty.

## Details
- Mechanism: AWS RIs come in standard (deep discount, inflexible) and convertible (moderate discount, changeable) forms; savings plans commit to $/hour of compute (EC2 Instance, Compute, SageMaker) and automatically cover matching usage; Azure reserved instances and GCP committed use discounts (CUDs) work similarly. All are per-region and (for RIs) per-family unless converted.
- Concrete example: a stable fleet of 40 web servers buys 3-year Compute savings plans covering ~80% of expected spend and lets instance types vary; a spike-driven batch workload stays on-demand/spot because its baseline is near zero; a mis-bought RI (wrong family/region) becomes stranded capacity unless convertible.
- Failure modes: over-committing on uncertain workloads (savings plans auto-cover, but underutilization still wastes the commitment); buying RIs without analyzing reservation utilization; regional moves stranding reservations; and ignoring that discounts apply to usage, so spot and savings-plan interplay needs explicit modeling.
- Operational tradeoffs: commitment trades flexibility for price; the pattern is reserve the floor (steady baseline) and leave the ceiling on-demand/spot. Review coverage monthly (utilization and coverage reports), and prefer savings plans for their flexibility over classic RIs where licensing allows.
- RSIS3/mykb relevance: the wiki's cost model would track baseline coverage and commitment utilization, so the loop's capacity reviews would adjust commitments instead of letting them drift.
- Coverage review: check reservation utilization quarterly and convert idle reserved instances rather than letting them expire unused; an unused reservation is a sunk cost with a schedule.
- Flexibility premium: when workloads shift families often, pay the premium for savings plans over RIs; the discount difference is smaller than the stranding risk.

## Related
- [[wiki/cloud-infra/dedicated-hosts-and-instances|Dedicated Hosts & Instances]]
- [[wiki/cloud-infra/burstable-instances|Burstable Instances]]
- [[wiki/infrastructure/on-demand-vs-reserved-compute|On Demand Vs Reserved Compute]]
- [[wiki/cloud-infra/demand-forecasting|Demand Forecasting]]
