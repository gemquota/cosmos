---
type: "concept"
title: "Persistent Volume Claims"
description: "Requesting storage abstractly so clusters bind volumes on demand"
tags: ["pvc", "storage", "kubernetes", "volumes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Persistent Volume Claims

## Summary
PersistentVolumeClaims (PVCs) are the user-facing request for storage in Kubernetes: a claim asks for capacity, access mode, and storage class, and the cluster binds it to a PersistentVolume (PV) — provisioned dynamically or matched from static volumes. PVCs decouple workloads from the underlying storage implementation.

## Details
- Mechanism: a PVC declares requests (storage size, accessModes like ReadWriteOnce/ReadWriteMany, storageClassName); dynamic provisioning creates a PV via the CSI driver; static provisioning matches an existing PV; pods reference the PVC by name in volume mounts; the reclaim policy decides what happens when the claim is deleted (Delete, Retain, Recycle).
- Concrete example: a database Deployment mounts a PVC requesting 100Gi on the fast storage class; the CSI driver provisions an EBS volume; the pod survives restarts because the volume persists; scaling to two replicas fails on ReadWriteOnce, forcing a shared storage class or a different architecture.
- Failure modes: pending claims when the storage class is missing, quota is exhausted, or the driver cannot provision — pods stay unscheduled; capacity over-requesting that wastes resources; access-mode mistakes that block scaling or multi-pod access; orphaned PVs leaking cost when claims are deleted with Retain; reclaim-policy surprises where Delete destroys data with the claim.
- Tradeoffs: PVCs give portable, declarative storage requests with lifecycle managed by the cluster, but the binding model adds indirection and the real behavior depends on the storage class and driver; static PVs give control but need manual management; the pattern is dynamic provisioning with explicit storage classes and deliberate reclaim policies.
- Operational notes: monitor PVC utilization and pending claims, set quotas, document the storage-class catalog, and test the failure path (node loss, claim deletion).
- RSIS3 relevance: the wiki store and checkpoints running on PVCs need the reclaim policy and backup plan set deliberately — a claim deletion is a data-deletion decision.

## Related
- [[wiki/os-shell/logical-volume-management|Logical Volume Management]]
- [[wiki/devops-infra/local-persistent-volumes|Local Persistent Volumes]]
- [[wiki/infrastructure/persistent-volumes|Persistent Volumes]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
