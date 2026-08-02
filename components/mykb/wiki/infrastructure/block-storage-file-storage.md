---
type: "concept"
title: "Block vs File Storage"
description: "Low-level volumes versus network filesystems and their tradeoffs"
tags: ["block-storage", "file-storage", "nfs", "san"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html",
  "https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html",
]
---

# Block vs File Storage

## Summary
Block storage exposes raw volumes to a single host, while file storage presents shared, network-accessible filesystems. The two models optimize different workloads: databases versus collaboration and shared state. Cloud platforms offer both as managed services.

## Details
- Block storage attaches as a device with no filesystem structure of its own; the OS formats and mounts it.
- File storage provides POSIX-like semantics over the network (NFS/SMB) for concurrent access from many clients.
- AWS EBS is block storage with per-volume IOPS and durability, while EFS is elastic file storage.
- Latency and locking differ: block devices have low latency but single-attach, file systems add metadata overhead but multi-attach.
- Backup mechanics differ too: block snapshots are volume-level, file backups operate on paths.
- In mykb, this article links to NFS/SMB, iSCSI, and object storage to complete the storage model map.
- Physical and virtual layers interact here; the cabling, power, and rack articles document the physical side of these decisions.

## Related
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]]
- [[wiki/cloud-infra/cold-storage|Cold Storage]]
- [[wiki/cloud-infra/object-storage|Object Storage]]
