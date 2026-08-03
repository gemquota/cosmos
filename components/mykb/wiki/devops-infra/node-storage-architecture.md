---
type: "concept"
title: "Node Storage Architecture"
description: "How node-local storage, CSI, and cloud disks compose in Kubernetes"
tags: ["node", "storage", "kubernetes", "csi"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Node Storage Architecture

## Summary
Node storage architecture describes how a Kubernetes node provides disk to containers: the container runtime's storage drivers, image layers, the kubelet's volume management, and the underlying filesystems (overlayfs, ext4, xfs). Understanding it explains disk usage, I/O behavior, and the failure modes of container persistence.

## Details
- Mechanism: container images are layer trees stored under the runtime's storage root (containerd/overlayfs, Docker/overlay2); each container's writable layer sits on top; volumes (emptyDir, hostPath, PVs) mount at paths into the container; the kubelet manages volume lifecycle and garbage collection of unused images and dead containers.
- Concrete example: a pod with an emptyDir backed by the node's local disk (tmpfs if medium: Memory); a PVC mounted from a network volume; image pulls expanding the node's storage root; disk pressure thresholds (eviction at 85-90%) triggering pod evictions.
- Failure modes: node disk full — the most common silent killer: image GC cannot keep up, evictions begin, and the kubelet marks the node NotReady; I/O contention from many pods sharing one disk; layer corruption from unclean shutdowns, breaking container starts; storage-root exhaustion from log files and dead containers; orphaned volumes leaking space after pod deletion.
- Tradeoffs: local storage is fast and cheap but node-bound; network storage is durable but slower; the architecture choice (overlayfs vs device-mapper, dedicated data disks vs shared root) determines performance isolation and blast radius; monitoring must watch disk usage per node, per volume, and per layer store.
- Operational notes: set eviction thresholds deliberately, reserve disk for the kubelet, and monitor inode usage as well as bytes.
- RSIS3 relevance: the wiki daemon's disk usage and the node's storage architecture explain sudden evictions or slow writes — RSIS3's operational notes should track disk pressure as a first-class signal.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
