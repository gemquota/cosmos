---
type: "concept"
title: "Data Archiving"
description: "Retaining data long-term for compliance, audit, or historical value with retrieval-friendly organization"
tags: ["archiving", "data", "retention", "compliance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-classes.html", "https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview"]
---

# Data Archiving

## Summary
Data archiving moves data that is no longer active but must be kept — records, logs, old versions — into cheap, durable storage with a clear retention and retrieval plan.

## Details
- Define retention by regulation and value, then automate deletion or transition at expiry.
- Archives need indexes and manifests; an unsearchable archive is a liability, not an asset.
- Encryption and access control still apply — archived data is a juicy target.
- Open question: how to keep decade-scale archives readable as formats and tools change.
- Data archiving moves data that is no longer actively used into long-term storage, preserving it for compliance, history, or recovery while cutting cost.
- The archive tier decision depends on retention requirements, retrieval frequency, and access latency tolerance.
- An archive is only as good as its index and restore process — data that cannot be found or restored might as well not exist.
- Archiving is a lifecycle practice: classify data, set retention, automate transitions, and test restores on a schedule.
- **Worked example / comparison** — Worked example — completed wiki sessions are archived after 6 months with a manifest index; a quarterly restore drill proves the archive actually works.
- For mykb, data-archiving is documented alongside the wiki's own archival-criteria lifecycle for articles and raw captures.

## Related
- [[wiki/cloud-infra/cold-storage|Cold Storage]]
- [[wiki/cloud-infra/storage-tiering|Storage Tiering]]
- [[wiki/cloud-infra/object-storage|Object Storage]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
- [[wiki/concepts/maintenance-tasks|Maintenance Tasks]]
