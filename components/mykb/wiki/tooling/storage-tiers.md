---
type: "concept"
title: "Storage Tiers"
description: "Classes of storage with different cost, latency, and durability"
tags: ["storage", "tiers", "cost", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Storage Tiers

## Summary
Storage tiers range from hot (fast, expensive) through warm and cold to archive (cheap, slow). Choosing the right tier per workload — hot DB, warm logs, cold backups — is how storage cost stays sane.

## Details
- Tier by access pattern and RPO/RTO: active data hot, recoverable data cold.
- Lifecycle rules move objects between tiers automatically as they age.
- Accessing cold data costs time and sometimes retrieval fees — document the expectations.
- mykb relevance: the wiki index is hot; raw captures move to warm; archives go cold.

## Related
- [[wiki/tooling/archive-policies|Archive Policies]]
- [[wiki/cloud-infra/storage-tiering|Storage Tiering]]
- [[wiki/cloud-infra/cold-storage|Cold Storage]]
- [[wiki/tooling/object-storage-practice|Object Storage Practice]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
