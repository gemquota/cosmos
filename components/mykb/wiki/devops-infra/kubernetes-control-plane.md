---
type: "concept"
hub: true
title: "Kubernetes Control Plane"
description: "The API, scheduler, and controllers that drive cluster state"
tags: ["kubernetes", "control-plane", "api", "etcd"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://kubernetes.io/docs/concepts/overview/components/",
  "https://etcd.io/docs/",
]
---

# Kubernetes Control Plane

## Summary
The Kubernetes control plane is the API server, scheduler, and controller managers that hold and reconcile desired state. Everything a user does goes through the API server, with etcd as the backing store. Its availability determines cluster availability.

## Details
- kube-apiserver exposes the REST API, authenticates and authorizes requests, and validates mutations.
- The kube-scheduler assigns pods to nodes based on resources, constraints, and topology.
- Controller managers run loops that converge the cluster toward desired state (deployments, endpoints, nodes).
- etcd stores all state and is the source of truth; losing quorum freezes the control plane.
- High availability requires replicated API servers and etcd across nodes or zones.
- In mykb, the control plane connects to scheduling, operators, admission controllers, and cluster management.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/infrastructure/data-plane-versus-control-plane|Data Plane vs Control Plane]]
- [[wiki/cloud-infra/congestion-control-algorithms|Congestion Control Algorithms]]
- [[wiki/devops-infra/kubernetes|Kubernetes]]
- [[wiki/infrastructure/kubernetes-operators|Kubernetes Operators]]
