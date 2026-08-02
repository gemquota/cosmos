---
type: "concept"
title: "Cold Storage"
description: "The cheapest storage tier for rarely accessed data, with slower retrieval and retrieval fees"
tags: ["cold-storage", "archive", "storage", "cost"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-classes.html", "https://cloud.google.com/storage/docs/storage-classes"]
---

# Cold Storage

## Summary
Cold storage holds data that is rarely or never read — archives, compliance records, old backups — at the lowest price per GB.

## Details
- Glacier-style tiers price for long-term retention, not fast access; retrieval can take minutes to hours.
- Minimum storage durations mean short-lived data should never go cold.
- Integrity risk grows with time: checksums and periodic spot-checks matter for decade-scale archives.
- Open question: how to balance cold-tier savings against the risk of provider lock-in for archives.
- Cold storage classes hold data that is rarely accessed, trading lower storage cost for higher retrieval cost and latency.
- Cloud providers tier this: standard, infrequent access, archive, and deep archive classes with escalating access penalties.
- The economics work when access is genuinely rare — backups, archives, compliance records — and fail when hot data gets archived by accident.
- Lifecycle policies move objects between classes automatically based on age and access patterns, which is where the savings actually come from.
- **Worked example / comparison** — Worked example — a wiki's backup sets are moved to archive class after 90 days and deep archive after a year, cutting storage cost by an order of magnitude while keeping restore options.
- For mykb, cold storage is documented as the cost lever for data that must be kept but rarely read, complementing data-archiving.

## Related
- [[wiki/cloud-infra/object-storage|Object Storage]]
- [[wiki/cloud-infra/storage-tiering|Storage Tiering]]
- [[wiki/cloud-infra/data-archiving|Data Archiving]]
- [[wiki/devops-infra/backups|Backups]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
