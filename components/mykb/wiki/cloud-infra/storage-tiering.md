---
type: "concept"
title: "Storage Tiering"
description: "Moving data between hot, warm, and cold storage classes as access frequency changes"
tags: ["storage", "tiering", "cost", "lifecycle"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Storage Tiering

## Summary
Storage tiering places data in the cheapest class that meets its access needs: hot storage for active data, warm for occasional reads, cold for archives. Lifecycle policies automate the transitions.

## Details
- Access pattern decides the tier: frequent = hot, monthly = warm, yearly-or-never = cold/archive.
- Retrieval costs and minimum durations make cold tiers a trade-off, not free storage.
- Lifecycle rules (age-based transitions, expiration) do the bookkeeping automatically.
- Open question: where the sweet spot is between one simple tier and many optimized ones.

## Related
- [[wiki/cloud-infra/object-storage|Object Storage]] — the platform tiers apply to
- [[wiki/cloud-infra/cold-storage|Cold Storage]] — the cheapest, slowest tier
- [[wiki/cloud-infra/warm-storage|Warm Storage]] — the middle tier
- [[wiki/devops-infra/backups|Backups]] — tiered backup retention
