---
type: "concept"
title: "Persistent Volumes"
description: "Cluster storage resources that outlive pods and provide durable state to containers"
tags: ["kubernetes", "storage", "volumes", "state"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Persistent Volumes

## Summary
Persistent volumes (PVs) decouple storage from pod lifetime: a volume is provisioned once and claimed by pods as needed, surviving pod restarts, rescheduling, and node failure. They are how stateful applications work in Kubernetes — the mechanism that turns a stateless-by-default platform into one that can host databases, caches, and file services with durable data.

## Details
- PVs are cluster resources; PVCs are requests; binding pairs them, often via dynamic provisioning. The two-object design is the Kubernetes answer to "who owns storage?": the PV is the cluster-level resource (the actual storage: an EBS/GCE PD volume, an NFS share, a local disk), created by an administrator or by a provisioner; the PVC (persistent volume claim) is a pod's request for storage (size, access mode, storage class). The binding matches claims to volumes — statically (an admin-created PV satisfies the claim) or dynamically (a StorageClass provisioner creates the PV on demand when a claim appears, the standard path on managed Kubernetes). A pod references the PVC, and the volume is mounted into the container; when the pod dies, the PVC and its PV survive — the data persists for the next pod to claim.
- Access modes (ReadWriteOnce, ReadOnlyMany, ReadWriteMany) constrain multi-pod use. The access mode declares how the volume can be mounted: ReadWriteOnce (one node, read-write — the default for databases), ReadOnlyMany (many nodes, read-only — shared config/data), ReadWriteMany (many nodes, read-write — shared file systems like NFS). The failure mode: choosing a claim with an access mode the underlying storage cannot honor (a block volume is RWO-only; requesting RWX against it fails binding), or choosing RWX when the application cannot actually handle concurrent writers (a database on an RWX filesystem is corruption waiting to happen).
- Snapshots and CSI drivers connect volumes to backup and tiering tooling. The CSI (Container Storage Interface) is the plugin boundary: every storage vendor implements CSI, and Kubernetes uses it for provisioning, attachment, snapshots, and resize. Volume snapshots (CSI snapshot support) give point-in-time copies for backup and cloning, and the volume's storage class (fast SSD vs cold tiers) sets the performance/cost profile — so the storage story is: StorageClass defines the type, PVC requests it, CSI implements it, snapshots protect it.
- Open question: how volume backups should integrate with application-level backup strategies — volume snapshots protect bytes but not application consistency (a snapshot of a database mid-transaction is a crash-consistent copy, not a clean one), so the design must combine application-level backup (log shipping, consistent dumps) with volume-level protection.
- For mykb: persistent volumes anchor the Kubernetes storage cluster — storage classes, stateful workloads, and snapshot strategies all connect here.

## Related
- [[wiki/infrastructure/storage-classes|Storage Classes]] — defines the volume types
- [[wiki/infrastructure/containerization|Containerization]] — the workload model volumes serve
- [[wiki/infrastructure/stateful-workloads|Stateful Workloads]] — primary consumers of volumes
- [[wiki/cloud-infra/snapshot-strategies|Snapshot Strategies]] — volume-level recovery
- [[wiki/devops-infra/kubernetes|Kubernetes]] — storage in the cluster
