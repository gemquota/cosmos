---
type: "concept"
title: "Cold Storage"
description: "The cheapest storage tier for rarely accessed data, with slower retrieval and retrieval fees"
tags: ["cold-storage", "archive", "storage", "cost"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Cold Storage

## Summary
Cold storage holds data that is rarely or never read — archives, compliance records, old backups — at the lowest price per GB.

## Details
- Glacier-style tiers price for long-term retention, not fast access; retrieval can take minutes to hours.
- Minimum storage durations mean short-lived data should never go cold.
- Integrity risk grows with time: checksums and periodic spot-checks matter for decade-scale archives.
- Open question: how to balance cold-tier savings against the risk of provider lock-in for archives.

## Related
- [[wiki/cloud-infra/object-storage|Object Storage]] — the home of cold tiers
- [[wiki/cloud-infra/storage-tiering|Storage Tiering]] — how data lands there
- [[wiki/cloud-infra/data-archiving|Data Archiving]] — the business need cold storage
- [[wiki/devops-infra/backups|Backups]] — cold tier for old backups
