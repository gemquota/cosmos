---
type: "concept"
title: "Logical Volume Management"
description: "Pooling and resizing block storage with LVM"
tags: ["lvm", "volumes", "storage", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.sourceware.org/lvm2/",
  "https://man7.org/linux/man-pages/man8/lvm.8.html",
]
---

# Logical Volume Management

## Summary
LVM abstracts physical disks into logical volumes that can be resized, snapshotted, and pooled without downtime. It is the standard volume layer on Linux servers. LVM separates storage capacity from the filesystems using it.

## Details
- LVM combines physical disks into volume groups, then carves logical volumes from that pooled capacity for filesystems.
- Resizing is online and non-destructive: grow the logical volume and the filesystem while the data is in active use.
- Snapshots at the LVM layer are space-efficient and feed backup workflows without interrupting running services.
- The LVM2 project site and man pages document commands such as vgcreate, lvcreate, and lvextend.
- Thin provisioning allows overcommitment with pool-based allocation, trading capacity guarantees for utilization.
- In mykb, LVM connects to RAID, filesystem mounting, and snapshot/clone techniques.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]]
- [[wiki/infrastructure/security-information-and-event-management|SIEM]]
- [[wiki/cloud-infra/dns-management|DNS Management]]
- [[wiki/cloud-infra/quota-management|Quota Management]]
