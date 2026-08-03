---
type: "concept"
title: "Topology Spread Constraints"
description: "Spreading pods across zones, nodes, or racks"
tags: ["topology-spread", "scheduling", "kubernetes", "availability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Topology Spread Constraints

## Summary
Topology spread constraints distribute pods across failure domains — zones, regions, nodes — so that losing one domain does not take down the whole workload. They extend node affinity: instead of just placing pods, they enforce an even spread across labeled topologies with configurable skew.

## Details
- Mechanism: a pod spec declares topologySpreadConstraints with a topology key (topology.kubernetes.io/zone), maxSkew (the allowed imbalance), whenUnsatisfiable (DoNotSchedule or ScheduleAnyway), and labelSelector; the scheduler counts matching pods per domain and prefers or requires balanced placement.
- Concrete example: a 6-replica Deployment spreads maxSkew=1 across 3 zones, so each zone holds 2 replicas; a node loss in one zone leaves 4 replicas running; a workload spread across nodes with anti-affinity avoids co-location; batch workloads use ScheduleAnyway so they still schedule when balance is impossible.
- Failure modes: constraints that cannot be satisfied, leaving pods Pending (check with events); skew creeping when scaling up without rebalancing (the scheduler balances at placement, not retroactively); counting only scheduled pods, ignoring crash-looping ones; constraints conflicting with other scheduling rules (affinity, taints), making scheduling impossible; spreading that ignores real fault domains because labels are wrong.
- Tradeoffs: spread constraints buy blast-radius isolation at the cost of scheduling flexibility and cluster fragmentation; the alternative — no constraints — lets the scheduler pack efficiently and fail whole regions together; the mature pattern is spread across zones for critical workloads, node spread for the rest, with maxSkew tuned to real failure domains.
- Operational notes: verify topology labels, monitor pod distribution per domain, and test zone-loss behavior in drills.
- RSIS3 relevance: if cosmos runs replicated services, spread constraints keep the wiki available when a zone fails — a small spec change with large availability impact.

## Related
- [[wiki/os-shell/numa-and-cpu-topology|NUMA & CPU Topology]] — related coverage in the same cluster
- [[wiki/infrastructure/network-topology-design|Network Topology Design]] — related coverage in the same cluster
- [[wiki/os-shell/pci-e-topology|PCIe Topology]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
