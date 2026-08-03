---
type: "concept"
hub: true
title: "Storage Systems"
description: "The spectrum from RAM to tape and the systems that serve data"
tags: ["storage", "systems", "architecture", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://en.wikipedia.org/wiki/Computer_data_storage",
  "https://www.snia.org/",
]
---

# Storage Systems

## Summary
Storage systems span the performance spectrum from RAM and NVMe to tape, each with distinct latency, cost, and durability properties. Choosing and combining them is a core infrastructure skill. This node anchors the storage cluster of the mykb graph.

## Details
- Storage media form a hierarchy: registers, cache, RAM, flash, disk, and tape, with orders of magnitude between their costs and latencies.
- Access models differ: block storage for raw volumes, file storage for shared filesystems, and object storage for immutable blobs.
- Durability comes from replication, erasure coding, and backups rather than from the media itself.
- SNIA publishes educational material describing storage technologies and terminology.
- Capacity planning must account for growth, snapshots, and garbage, not just current usage.
- In mykb, storage systems connect to block/file/object articles, RAID, filesystem design, and backup strategies.
- Physical and virtual layers interact here; the cabling, power, and rack articles document the physical side of these decisions.
- Capacity and redundancy tradeoffs for this topic are covered in the datacenter redundancy and power articles.

## Related
- [[wiki/infrastructure/intrusion-detection-systems|Intrusion Detection Systems]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/cloud-infra/cold-storage|Cold Storage]]
- [[wiki/cloud-infra/object-storage|Object Storage]]
