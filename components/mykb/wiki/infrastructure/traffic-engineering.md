---
type: "concept"
title: "Traffic Engineering"
description: "Routing and shaping to use network capacity efficiently"
tags: ["traffic-engineering", "routing", "capacity", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Traffic Engineering

## Summary
Traffic engineering plans and steers how traffic flows across a network so that capacity is used efficiently, latency is controlled, and failures do not overload remaining paths. It operates above ordinary routing: where IGP metrics pick a shortest path, traffic engineering picks the path that fits the demand pattern, the SLAs, and the failure scenarios.

## Details
- Mechanism: demand is measured or estimated per ingress/egress pair, then paths are computed across the topology — either explicitly (MPLS TE tunnels, segment routing policies) or implicitly (ECMP spreading, equal-cost hashing). The goal is to keep utilization balanced and avoid hot links that queue packets while parallel links sit idle.
- Concrete examples: a backbone with two diverse paths between regions where the shortest path saturates at 90% while the alternate sits at 30% — traffic engineering shifts part of the traffic onto the alternate; an inter-datacenter link whose capacity plan must survive one path failing, so each path is run below 50% utilization.
- Failure modes: static TE configurations that cannot react to traffic shifts; hash polarization on ECMP causing one flow to dominate a member link; loops and black holes when a TE tunnel's underlying path changes without recomputation; and under-provisioned alternate paths that collapse under failover.
- Tradeoffs: central TE gives optimal placement but adds state and complexity; dynamic TE reacts to measurement but can oscillate; segment routing simplifies the signaling compared to RSVP-TE but requires controller intelligence to choose paths well. The cheapest traffic engineering is often better topology design, not more control machinery.
- Operational practice: measure utilization per link and per flow, model demand growth, run failure drills on the alternate paths, and validate that TE changes actually move traffic where intended — use netflow/sflow and per-path counters.
- RSIS3/mykb relevance: capacity planning is a standing concern for loops that grow the knowledge store across machines; this node keeps the demand-versus-topology framing retrievable so scaling decisions consider where traffic can actually flow.

## Related
- [[wiki/devops-infra/chaos-engineering-revisited|Chaos Engineering]]
- [[wiki/devops-infra/site-reliability-engineering-revisited|Site Reliability Engineering]]
- [[wiki/infrastructure/traffic-shaping-and-qos|Traffic Shaping & QoS]]
- [[wiki/devops-infra/release-engineering|Release Engineering]]
