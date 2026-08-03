---
type: "concept"
title: "Local Persistent Volumes"
description: "Node-local storage with static binding for low-latency workloads"
tags: ["local-pv", "storage", "kubernetes", "node"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Local Persistent Volumes

## Summary
Local persistent volumes bind storage to a specific node: a Local PersistentVolume (local PV) or hostPath-like volume pins data to a node's disk, giving low latency and high throughput at the cost of node-coupling. Kubernetes schedules pods to the node owning their local volume, and data survives pod restarts but not node loss.

## Details
- Mechanism: a StorageClass with `volumeBindingMode: WaitForFirstConsumer` plus a local-path provisioner creates PVs on the node where the pod lands; the scheduler places the pod on a node with the volume; the kubelet mounts the directory; reclaim policy (Delete vs Retain) decides what happens when the PVC goes away.
- Concrete example: a database pod using a local SSD via the local-static-provisioner; node-local caching tier; a benchmark workload needing disk throughput unavailable on network volumes; the scheduler constraint is visible as nodeAffinity on the PV.
- Failure modes: data stranded on a dead node — local volumes do not follow the pod, so a node failure means manual recovery or data loss (replicate at the app level); the scheduler running out of nodes that hold the volume (capacity planning must account for node affinity); provisioning races where a node fills and the PV is unusable; pod evictions that cannot reschedule because the volume is node-pinned.
- Tradeoffs: local volumes give the best I/O (no network hop, consistent latency) but give up the durability and mobility of network storage; the operational contract is explicit — the application must handle node loss via replication, backups, or quorum; network volumes (EBS, Cinder) are slower but survive node loss.
- Operational notes: monitor disk space per node, set reclaim policies deliberately, and pair local volumes with app-level replication.
- RSIS3 relevance: if the wiki store or checkpoints use local volumes, RSIS3's backup strategy must cover node loss — local disks are fast memory, not durable memory.

## Related
- [[wiki/cloud-infra/ipv6-link-local-addresses|IPv6 Link-Local Addresses]]
- [[wiki/devops-infra/persistent-volume-claims|Persistent Volume Claims]]
- [[wiki/infrastructure/persistent-volumes|Persistent Volumes]]
- [[wiki/devops-infra/volumes-emptydir-and-configmaps|emptyDir & ConfigMap Volumes]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
