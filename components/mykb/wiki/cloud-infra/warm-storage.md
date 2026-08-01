---
type: "concept"
title: "Warm Storage"
description: "A middle storage tier for data accessed occasionally, cheaper than hot and faster than cold"
tags: ["warm-storage", "storage", "tiers", "cost"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Warm Storage

## Summary
Warm storage is the middle tier between hot and cold: lower per-GB cost than hot storage, faster retrieval than cold, with per-access charges.

## Details
- Good for: monthly reports, older logs kept for audit, training data re-used in batches.
- Retrieval pricing makes frequent reads expensive — measure access before choosing warm.
- Lifecycle rules can tier data into warm automatically after a hot-period TTL.
- Open question: when warm's retrieval fees make keeping data hot cheaper overall.

## Related
- [[wiki/cloud-infra/object-storage|Object Storage]] — the storage model tiers
- [[wiki/cloud-infra/storage-tiering|Storage Tiering]] — where warm sits in the ladder
- [[wiki/cloud-infra/cold-storage|Cold Storage]] — the cheaper, slower sibling
- [[wiki/devops-infra/backups|Backups]] — warm tier for recent backups
