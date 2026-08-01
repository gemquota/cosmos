---
type: "concept"
title: "Container Scheduling"
description: "How orchestrators place containers onto nodes based on resources, constraints, and topology"
tags: ["kubernetes", "scheduling", "containers", "orchestration"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Container Scheduling

## Summary
Container scheduling decides which node runs which container, honoring resource requests, affinity rules, and failure domains. The scheduler is the brain that turns a declarative workload spec into physical placement.

## Details
- The Kubernetes scheduler filters nodes (resources, taints, node selectors) then scores them (spread, affinity).
- Requests vs limits: requests drive placement, limits drive enforcement — mis-set requests wreck scheduling.
- Topology spread and pod anti-affinity keep workloads across zones and nodes.
- Open question: how bin-packing and spread preferences should trade off.

## Related
- [[wiki/infrastructure/containerization|Containerization]] — the unit being scheduled
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — what happens after placement
- [[wiki/infrastructure/node-pools|Node Pools]] — the candidate node groups
- [[wiki/devops-infra/kubernetes|Kubernetes]] — the orchestrator that schedules
