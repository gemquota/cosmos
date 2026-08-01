---
type: "concept"
title: "Persistent Volumes"
description: "Cluster storage resources that outlive pods and provide durable state to containers"
tags: ["kubernetes", "storage", "volumes", "state"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Persistent Volumes

## Summary
Persistent volumes decouple storage from pod lifetime: a volume is provisioned once and claimed by pods as needed. They are how stateful applications survive restarts and rescheduling.

## Details
- PVs are cluster resources; PVCs are requests; binding pairs them, often via dynamic provisioning.
- Access modes (ReadWriteOnce, ReadOnlyMany, ReadWriteMany) constrain multi-pod use.
- Snapshots and CSI drivers connect volumes to backup and tiering tooling.
- Open question: how volume backups should integrate with application-level backup strategies.

## Related
- [[wiki/infrastructure/storage-classes|Storage Classes]] — defines the volume types
- [[wiki/infrastructure/containerization|Containerization]] — the workload model volumes serve
- [[wiki/infrastructure/stateful-workloads|Stateful Workloads]] — primary consumers of volumes
- [[wiki/cloud-infra/snapshot-strategies|Snapshot Strategies]] — volume-level recovery
- [[wiki/devops-infra/kubernetes|Kubernetes]] — storage in the cluster
