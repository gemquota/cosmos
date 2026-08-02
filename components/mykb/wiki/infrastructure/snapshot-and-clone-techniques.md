---
type: "concept"
title: "Snapshot & Clone Techniques"
description: "Point-in-time copies and space-efficient clones"
tags: ["snapshot", "clone", "storage", "backup"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://en.wikipedia.org/wiki/Snapshot_(computer_storage)",
  "https://en.wikipedia.org/wiki/Snapshot_(computer_storage)",
]
---

# Snapshot & Clone Techniques

## Summary
Snapshots capture a point-in-time state of a volume or filesystem, and clones create writable copies cheaply. They are the basis of backup, testing, and development workflows. Understanding their semantics prevents data-loss surprises.

## Details
- Snapshots are typically incremental: they record changes since creation, so the original data stays referenced until every dependent snapshot is deleted.
- OpenZFS snapshots are instantaneous and nearly free until blocks change.
- Clones diverge from a snapshot and can be promoted or destroyed independently.
- Retention policies chain snapshots; deleting an intermediate snapshot merges its changes into the next one.
- Cloud volume snapshots (EBS, GCE disks) are stored in object storage and can be copied across regions.
- In mykb, snapshots connect to backup strategies, lifecycle policies, and copy-on-write filesystems.
- Physical and virtual layers interact here; the cabling, power, and rack articles document the physical side of these decisions.
- Capacity and redundancy tradeoffs for this topic are covered in the datacenter redundancy and power articles.

## Related
- [[wiki/cloud-infra/snapshot-lifecycle-policies|Snapshot Lifecycle Policies]]
- [[wiki/devops-infra/dark-launch-techniques|Dark Launch Techniques]]
- [[wiki/cloud-infra/snapshot-strategies|Snapshot Strategies]]
- [[wiki/infrastructure/data-anonymization-techniques|Data Anonymization Techniques]]
