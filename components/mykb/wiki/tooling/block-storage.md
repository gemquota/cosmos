---
type: "concept"
title: "Block Storage"
description: "Raw disk volumes attached to machines, formatted by the OS"
tags: ["block-storage", "storage", "volumes", "infrastructure"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Block Storage

## Summary
Block storage presents raw disk blocks over a network or bus — EBS volumes, local NVMe, SAN LUNs — that an OS formats and mounts. It is low-latency, machine-attached storage for databases and filesystems.

## Details
- Snapshots at the volume level capture whole filesystems consistently with coordination.
- Performance classes (SSD vs HDD, IOPS tiers) are the main cost dials.
- Attach/detach and multi-attach semantics vary; know your provider's limits.
- mykb relevance: the wiki DB volume snapshots weekly for point-in-time recovery.

## Related
- [[wiki/cloud-infra/amazon-ebs-provisioning|Amazon EBS Provisioning]]
- [[wiki/cloud-infra/instance-store-vs-ebs|Instance Store vs EBS]]
- [[wiki/tooling/file-storage|File Storage]]
- [[wiki/tooling/network-storage|Network Storage]]
- [[wiki/tooling/storage-tiers|Storage Tiers]]
