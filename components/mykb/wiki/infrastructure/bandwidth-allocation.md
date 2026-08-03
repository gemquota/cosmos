---
type: "concept"
title: "Bandwidth Allocation"
description: "Dividing limited capacity among tenants and classes"
tags: ["bandwidth", "allocation", "qos", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Bandwidth Allocation

## Summary
Bandwidth allocation is the problem of dividing limited link capacity among competing tenants and traffic classes. Since capacity is finite and demand is bursty, the allocation scheme decides who gets served when the network is congested — and those decisions determine latency, fairness, and whether any tenant's workload succeeds.

## Details
- The core mechanism is scheduling: when multiple flows compete for a link, a scheduler at the queue decides the service order. The simplest allocation is FIFO (first in, first out), which is fair by arrival but lets one aggressive flow starve others. Fair queuing (and variants like DRR, deficit round robin) allocates bandwidth roughly equally per flow, protecting well-behaved flows from noisy neighbors. Strict priority queues serve high-priority classes first, at the cost of starving lower classes — the classic tradeoff between latency guarantees and fairness.
- QoS allocation adds the class dimension: traffic is classified (by DSCP marking, ACL, or application) into classes with different allocations — voice gets strict priority and low latency, bulk transfer gets what remains, and best-effort gets the leftovers. The allocation parameters are per-class bandwidth reservations (min/max rates), priorities, and drop policies, and the system's job is to honor those commitments under congestion. This is where bandwidth allocation meets traffic shaping and priority queuing: the shaper enforces the contract on entry, the scheduler enforces it in the queue.
- Multi-tenant allocation adds the fairness dimension: in a shared fabric, tenants are entitled to their purchased or fair share of capacity, and the network must prevent one tenant's burst from harming others. Mechanisms include per-tenant rate limiting (committed and burst rates), weighted fair sharing proportional to purchased capacity, and congestion isolation via separate queues or virtual channels.
- Failure modes: allocation schemes that are too rigid waste idle capacity (a reserved-but-unused class blocks traffic that could use it), too lax ones let a noisy neighbor degrade everyone (the "noisy neighbor" problem), and misconfiguration — the most common failure — sends critical traffic into a class that gets starved. The operational discipline is to measure actual per-class utilization, because allocation decisions made without traffic data are guesses.
- For mykb: bandwidth allocation is the networking analog of resource budgeting everywhere — the same fairness-vs-efficiency tension appears in memory allocation, storage QoS, and the RSIS3 loop's own compute budgeting.

## Related
- [[wiki/cloud-infra/bandwidth-vs-throughput|Bandwidth vs Throughput]]
- [[wiki/cloud-infra/cost-of-bandwidth|Cost of Bandwidth]]
- [[wiki/os-shell/dhcp-and-ip-allocation|DHCP & IP Allocation]]
- [[wiki/os-shell/memory-allocation|Memory Allocation]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
