---
type: "concept"
title: "Container Scheduling"
description: "How orchestrators place containers onto nodes based on resources, constraints, and topology"
tags: ["kubernetes", "scheduling", "containers", "orchestration"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Container Scheduling

## Summary
Container scheduling decides which node runs which container, honoring resource requests, affinity rules, and failure domains. The scheduler is the brain that turns a declarative workload spec into physical placement — and placement quality determines utilization, latency, and resilience, so scheduling is where cluster economics and reliability meet.

## Details
- The Kubernetes scheduler filters nodes (resources, taints, node selectors) then scores them (spread, affinity). Scheduling runs in two phases: filtering (feasibility) removes nodes that cannot run the pod — insufficient allocatable resources, a taint the pod does not tolerate, a node selector mismatch, or anti-affinity conflicts; scoring (preference) then ranks the feasible nodes by weighted criteria — how balanced the cluster is, how well the pod's affinity requirements are satisfied, and (in newer versions) the pod's own scoring hints. The highest-scoring node wins. The scheduler is a control loop: it watches the API for unscheduled pods, runs filter+score, and binds.
- Requests vs limits: requests drive placement, limits drive enforcement — mis-set requests wreck scheduling. A pod's `requests` are the reservation the scheduler honors (a node is feasible only if the sum of requests fits), while `limits` are the ceiling the runtime enforces. The classic failure: requests set far above real usage (the scheduler reserves capacity that never gets used — utilization plummets and pods go unschedulable) or far below real usage (nodes get oversubscribed and the runtime kills or throttles pods under pressure). The operational discipline is to set requests from measured usage, not from guesses — requests are the language the scheduler speaks.
- Topology spread and pod anti-affinity keep workloads across zones and nodes. By default the scheduler will happily pack pods onto one node; topology spread constraints force distribution across zones/regions/nodes (for resilience: one zone failure cannot take down the whole service), and pod anti-affinity keeps replicas of the same service apart (hard anti-affinity: never co-locate; soft: prefer to spread). The tradeoff with bin-packing: spread preferences sacrifice packing density for resilience, and the scheduler cannot do both — so the cluster's spread-vs-packing policy is a deliberate choice.
- Open question: how bin-packing and spread preferences should trade off — the scheduler's default leans to balance, but a cluster running homogeneous batch workloads gets better utilization from packing, and the right blend depends on workload mix.
- For mykb: container scheduling connects containerization, pod lifecycle, and node pools — the orchestration cluster's core.

## Related
- [[wiki/infrastructure/containerization|Containerization]] — the unit being scheduled
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — what happens after placement
- [[wiki/infrastructure/node-pools|Node Pools]] — the candidate node groups
- [[wiki/devops-infra/kubernetes|Kubernetes]] — the orchestrator that schedules
