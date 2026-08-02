---
type: "concept"
title: "Kubernetes Scheduling"
description: "Matching pods to nodes under constraints and resources"
tags: ["kubernetes", "scheduling", "pods", "nodes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/",
  "https://kubernetes.io/docs/concepts/scheduling-eviction/",
]
---

# Kubernetes Scheduling

## Summary
Kubernetes scheduling matches pending pods to nodes, respecting resource requests, constraints, and priorities. The scheduler's decisions shape utilization and resilience. Scheduling concepts generalize the whole class of placement problems in distributed systems.

## Details
- The kube-scheduler filters nodes by feasibility (resources, affinity, taints) then scores them by preference.
- Resource requests reserve capacity; limits cap actual usage, and the scheduler uses requests, not limits, for placement decisions.
- Node affinity, taints and tolerations, and topology spread constraints encode placement policy for the scheduler.
- Priority classes let critical workloads preempt lower-priority pods when the cluster is under resource pressure.
- The scheduler runs as a control loop that watches the API for unscheduled pods and continuously reconciles placement.
- In mykb, scheduling connects to autoscaling, priority classes, node affinity, and control-plane articles.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/network-policies-kubernetes|Kubernetes Network Policies]]
- [[wiki/devops-infra/kubernetes-operators-revisited|Kubernetes Operators]]
- [[wiki/devops-infra/kubernetes|Kubernetes]]
- [[wiki/infrastructure/container-scheduling|Container Scheduling]]
