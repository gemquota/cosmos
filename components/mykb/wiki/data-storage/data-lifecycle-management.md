---
type: "concept"
title: "Data Lifecycle Management"
description: "Retention, archival, and deletion policies"
tags: ["data-lifecycle", "retention", "archival", "data-governance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html", "https://www.postgresql.org/docs/current/storage-file-layout.html"]
---

# Data Lifecycle Management

## Summary
Data lifecycle management (DLM) defines how data moves from creation through active use, archival, and deletion. Policies set retention periods, transition rules, and deletion schedules so storage costs stay bounded, compliance obligations are met, and stale data stops confusing analytics.

## Details
- **Stages** — data typically passes through hot (frequently accessed), warm (occasionally accessed), and cold (rarely accessed) tiers before archival or deletion; each stage has different storage media, cost, and access guarantees.
- **Retention policies** — rules stating how long data must be kept: event logs, telemetry, and transaction records each have business, legal, or regulatory retention windows (e.g., financial records for 7 years).
- **Lifecycle transitions** — object storage automates movement: S3 lifecycle rules can expire objects, transition them to cheaper storage classes (Standard-IA, Glacier), and apply filters by prefix, tag, or age.
- **Tiered databases** — databases use partition-based lifecycle: drop or archive old partitions, move them to slower tablespaces, or use time-based automatic partitioning (TimescaleDB chunks, ClickHouse TTL) so deletes become cheap metadata operations.
- **Compliance and deletion** — deletion must be provable: legal holds pause deletion, and audit trails record what was removed and when; GDPR and similar regimes add a right-to-erasure dimension.
- **Anti-patterns** — hoarding "just in case" data inflates cost and degrades query quality; deleting without a retention policy risks non-compliance; snapshot systems must retain versioned copies per the same policy.

## Related
- [[wiki/data-storage/storage-tiering|Storage Tiering]] — the hot/warm/cold infrastructure
- [[wiki/data-storage/object-storage|Object Storage]] — where lifecycle rules are native
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — retention for copies
- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — partition-based expiry
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — cheap archival by partition
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — reclaiming deleted data
