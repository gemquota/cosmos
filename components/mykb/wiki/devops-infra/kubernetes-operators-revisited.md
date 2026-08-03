---
type: "concept"
title: "Kubernetes Operators"
description: "Controllers that encode application operational knowledge"
tags: ["operators", "kubernetes", "controllers", "crd"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Kubernetes Operators

## Summary
Operators extend Kubernetes with domain knowledge: a controller plus CRDs that encode how to run a specific application — provisioning, scaling, upgrades, backups, and recovery — as declarative reconciliation loops. "Revisited" reflects the mature pattern: operator frameworks (operator-sdk, kubebuilder, Kopf), Helm-driven operator distribution, and a clear line between operator-appropriate and script-appropriate workloads.

## Details
- Mechanism: a CRD defines the desired state; the operator's controller watches instances, compares spec to the live resources, and reconciles — creating, updating, or deleting owned resources and writing status; reconciliation is continuous and event-driven, so the operator heals drift without human action.
- Concrete example: a Postgres operator watches a `Cluster` CR, provisions StatefulSets and PVCs, configures replication, takes backups, and reports Ready conditions; an upgrade is a spec change the operator orchestrates; the operator also handles node failover, which a plain Deployment cannot.
- Failure modes: operators that fight the user or other controllers (dual reconciliation of the same resource); status writes that conflict or never converge, leaving stuck conditions; version upgrades that break existing CR instances (schema conversion issues); operator bugs having the blast radius of the whole application, not one pod; ownership chains that cause mass deletion when a parent is removed.
- Tradeoffs: operators give the highest level of automation but are the most expensive to build and maintain — schema design, reconciliation semantics, and upgrade paths all become yours; the alternative (Helm charts plus scripts) is cheaper but leaves operational gaps; use operators for stateful, long-lived workloads with rich lifecycles, not for stateless ones a Deployment already handles.
- Operational notes: design CRD schemas with defaults, test upgrade paths across versions, and follow the operator pattern of small reconcile loops with requeue.
- RSIS3 relevance: RSIS3's persistent components (MyKB store, checkpoint service) are exactly the stateful workloads where operator-style reconciliation — declare the desired state, heal drift — matches the L1 loop philosophy.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/kubernetes-scheduling|Kubernetes Scheduling]]
- [[wiki/devops-infra/network-policies-kubernetes|Kubernetes Network Policies]]
- [[wiki/infrastructure/kubernetes-operators|Kubernetes Operators]]
