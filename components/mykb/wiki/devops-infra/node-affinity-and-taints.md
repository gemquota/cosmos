---
type: "concept"
title: "Node Affinity & Taints"
description: "Scheduling constraints that attract or repel pods"
tags: ["node-affinity", "taints", "scheduling", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Node Affinity & Taints

## Summary
Node affinity and taints/tolerations control where pods land: affinity expresses preference or requirement (this pod should/can run on nodes with these labels), and taints repel pods unless they tolerate the taint. They are the two mechanisms Kubernetes gives for node-level placement policy.

## Details
- Affinity mechanics: nodeSelector is the simple label match; nodeAffinity adds requiredDuringScheduling (hard constraint) and preferredDuringScheduling (soft preference with weights); podAffinity/antiAffinity express relationships between pods (co-locate or spread). Hard rules constrain the scheduler; soft rules shape it.
- Taint mechanics: a node taint is key=value:effect (NoSchedule, PreferNoSchedule, NoExecute); a pod tolerates a taint to be allowed; NoExecute also evicts pods already running without toleration; taints typically mark dedicated nodes (GPU, spot, control-plane).
- Concrete example: GPU nodes tainted so only GPU workloads tolerate them; a stateful app with required nodeAffinity for SSDs and preferred anti-affinity to spread replicas across zones; spot nodes tainted with a short NoExecute window so batch jobs tolerate them but long-running services do not.
- Failure modes: hard affinity over-constraining — if no node matches, pods stay Pending forever (check with kubectl describe); taint storms evicting everything when a taint is applied by mistake; NoExecute taints draining nodes faster than the app can drain; affinity rules that only consider topology at schedule time, ignoring runtime changes.
- Tradeoffs: affinity and taints give precise placement control but shift failure handling to the scheduler and the operator — every constraint reduces scheduling flexibility; overusing hard constraints causes cluster fragmentation (nodes running below capacity); soft preferences and taints with tolerations are the flexible middle ground.
- Operational notes: audit taints before node maintenance, test eviction behavior, and monitor unschedulable pods.
- RSIS3 relevance: if cosmos nodes differ (GPU for embeddings, fast disk for the store), affinity and taints keep workloads on the right hardware — and RSIS3's monitoring should flag pending pods caused by placement rules.

## Related
- [[wiki/devops-infra/node-storage-architecture|Node Storage Architecture]]
- [[wiki/infrastructure/node-pools|Node Pools]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
