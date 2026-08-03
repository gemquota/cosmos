---
type: "concept"
title: "Container Storage Interfaces"
description: "The CSI plugin standard for attaching storage to containers"
tags: ["csi", "storage", "containers", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Container Storage Interfaces

## Summary
The Container Storage Interface (CSI) standardizes how Kubernetes provides storage to containers: storage vendors implement a driver that provisions volumes, attaches them to nodes, and mounts filesystems, orchestrated by the controller-manager and kubelet through a common API. It replaces in-tree cloud volume code with out-of-tree drivers.

## Details
- Mechanism: CSI has a controller plugin (CreateVolume, DeleteVolume), a node plugin (NodeStage, NodePublish), and sidecars that watch PersistentVolumeClaims and call the driver; the flow is PVC to provision, attach, mount, pod; deletion reverses it. Volume modes (filesystem versus block) and expansion are part of the spec.
- Concrete example: an EBS or GCE PD driver provisions a volume from a StorageClass, attaches it to the node, and mounts ext4 or xfs into the pod; a local-path CSI provides fast node-local storage without network round trips.
- Failure modes: attach/detach timeouts when the driver or cloud API hangs — pods can get stuck Terminating; multi-attach errors when a ReadWriteOnce volume is scheduled on two nodes; resize failures when the filesystem is not expanded after the PV grows; driver upgrades that restart while volumes are mounted, causing I/O errors; orphaned volumes after PVC deletion when the driver fails to delete, leaking cost.
- Tradeoffs: CSI standardizes the interface but shifts complexity into drivers with uneven vendor maturity, so test attach, detach, and resize paths; network volumes are safe across node failure but slow; local volumes are fast but pinned to a node and need application-level replication.
- Operational notes: monitor PV/PVC state, set reclaim policies deliberately (Retain versus Delete), and test volume expansion and snapshot/restore in staging.
- Expansion detail: online resize needs both the driver and the mounted filesystem to support it — expanding the PV alone leaves the pod's usable space unchanged.
- RSIS3 relevance: RSIS3's persistent state (the mykb store, checkpoints) on Kubernetes relies on CSI volumes — driver behavior explains backup, capacity, and attach failure modes.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]]
- [[wiki/devops-infra/container-network-interfaces|Container Network Interfaces]]
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]]
