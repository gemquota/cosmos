---
type: "concept"
title: "Filesystem Design"
description: "Data structures and algorithms behind filesystem implementations"
tags: ["filesystem", "design", "inodes", "kernel"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.kernel.org/filesystems/",
  "https://en.wikipedia.org/wiki/File_system",
]
---

# Filesystem Design

## Summary
Filesystem design is about how bytes become files: allocation structures, metadata, and crash safety. The kernel's filesystem layer abstracts many implementations behind one VFS interface. This node is the root of the filesystem tree in mykb.

## Details
- Filesystems organize storage into blocks, inodes (metadata), and directory entries mapping names to inodes.
- The Linux kernel documentation catalogs supported filesystems and their design tradeoffs.
- Allocation strategies (extents, B-trees, copy-on-write) determine fragmentation, scalability, snapshot behavior, and the performance envelope of the filesystem.
- Crash consistency is the hard part, leading to journals, checksums, and write-ahead logs.
- Design choices optimize for different workloads: small files, large files, many directories, or long uptime.
- In mykb, filesystem design links to journaling, copy-on-write, ext4/XFS, tmpfs, and immutable filesystem articles across the OS and storage clusters.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/cloud-infra/aws-vpc-design|AWS VPC Design]]
- [[wiki/infrastructure/network-topology-design|Network Topology Design]]
- [[wiki/cloud-infra/subnet-design|Subnet Design]]
- [[wiki/infrastructure/probe-design|Probe Design]]
