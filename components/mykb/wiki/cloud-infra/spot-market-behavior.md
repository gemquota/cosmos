---
type: "concept"
title: "Spot Market Behavior"
description: "How spot prices fluctuate with supply, demand, and interruption"
tags: ["spot", "pricing", "market", "aws"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Spot Market Behavior

## Summary

The spot market clears supply and demand for spare capacity: prices move with utilization, and interruptions cluster when capacity tightens. Understanding the market's behavior — not just its discounts — is what separates reliable spot usage from weekend incidents.

## Details
- Mechanism: AWS prices spot by instance type/AZ over time (historically a price curve, now more stable with capacity-based allocation); interruptions happen when AWS needs capacity back or, less commonly, price exceeds your bid; GCP preemptibles are fixed-price with arbitrary reclaim; Azure spot is market-priced with eviction policies. Diversification (multiple types/AZs) is the main lever against interruption.
- Concrete example: a spot fleet that spans 3 instance types across 3 AZs survives a capacity crunch that would take out a single-type single-AZ fleet; batch jobs monitor interruption rates and shift hours when the market is tight (e.g. price spikes during a regional launch); a workload with per-instance 30-minute tasks tolerates 10% interruption with trivial cost.
- Failure modes: bidding strategies that chase price (interruptions are about capacity, not price); assuming the market is stable — regional events, launches, and holidays shift it; no interruption-rate monitoring, so the fleet quietly degrades; and fallback designs that cannot execute (on-demand capacity also constrained during crunches).
- Operational tradeoffs: market awareness buys most of the savings with bounded risk; the discipline is diversification, interruption telemetry, and rehearsed fallbacks. Treat spot as capacity with a probabilistic availability profile, and size the on-demand floor accordingly.
- RSIS3/mykb relevance: the wiki's spot telemetry (interruption rates by type/AZ) feeds the loop's fleet mix decisions and is recorded in this node for capacity planning.
- Capacity floor: size the on-demand floor to the workload's critical portion and treat spot as opportunistic; a fleet that depends on spot for its core is a market bet.

## Related
- [[wiki/cloud-infra/spot-and-preemptible|Spot & Preemptible Instances]]
- [[wiki/cloud-infra/spot-instances|Spot Instances]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
