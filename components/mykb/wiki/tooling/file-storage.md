---
type: "concept"
title: "File Storage"
description: "Network filesystems that present shared directories to many clients"
tags: ["file-storage", "nfs", "storage", "infrastructure"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# File Storage

## Summary
File storage exposes shared hierarchical filesystems — NFS, SMB, EFS — that many machines mount simultaneously. It suits shared content and legacy apps; consistency and locking semantics are its classic pain points.

## Details
- File locking across clients is weak or advisory in most implementations — design around it.
- Performance varies wildly with workload (small files vs large sequential I/O).
- Shared file storage pairs with cluster filesystems (GPFS, Lustre) for HPC-scale needs.
- mykb relevance: a shared wiki workspace mounts EFS so all workers see the same tree.

## Related
- [[wiki/tooling/block-storage|Block Storage]]
- [[wiki/tooling/network-storage|Network Storage]]
- [[wiki/tooling/object-storage-practice|Object Storage Practice]]
- [[wiki/cloud-infra/azure-managed-disks|Azure Managed Disks]]
- [[wiki/tooling/storage-tiers|Storage Tiers]]
