---
type: "concept"
title: "Warm Storage"
description: "A middle storage tier for data accessed occasionally, cheaper than hot and faster than cold"
tags: ["warm-storage", "storage", "tiers", "cost"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Warm Storage

## Summary

Warm storage is the tier between hot and cold: cheap per-GB storage with modest retrieval latency and fees — object-storage infrequent-access classes, snapshot archives, and bulk tiers. It fits data accessed rarely but recoverable quickly, and it is where most "cold" data actually belongs.

## Details
- Mechanism: S3 Standard-IA/OneZone-IA, GCS nearline, Azure cool/cold, plus archive-adjacent classes (Glacier Instant Retrieval) deliver millisecond access at a fraction of hot storage cost, charging a small per-GB retrieval fee and minimum durations; warm storage also describes on-prem/cloud tiers for semi-active datasets (warm pools, rehydrated archives).
- Concrete example: quarterly analytics data sits in Standard-IA — readable in ms, 60% cheaper than Standard; a snapshot library keeps 90 days of warm snapshots and archives older ones; a media library keeps last month's content hot and everything older in nearline with ms access.
- Failure modes: using archive tiers for data actually read weekly (retrieval fees exceed savings); ignoring the minimum-duration penalty when lifecycle moves objects quickly; OneZone-IA losing durability expectations for the discount; and warm tiers without lifecycle automation, so objects sit in the wrong class indefinitely.
- Operational tradeoffs: warm tiers capture most savings with minimal latency risk; the decision rule is access frequency (IA for monthly-or-fewer reads, archive for yearly), with retrieval fees modeled before committing. Automate transitions and monitor tier distribution per bucket.
- RSIS3/mykb relevance: the wiki's analytics buckets use warm tiers with lifecycle rules; this note records the tier thresholds so the loop's storage reviews stay data-driven.
- Data temperature model: classify data by access frequency and recovery SLA (hot <24h, warm monthly, archive yearly) so tier placement is a policy decision, not a guess.
- Cost reporting: track per-bucket tier spend in the cost report; tier drift (everything hot) shows up there before it becomes a budget surprise.

## Related
- [[wiki/cloud-infra/object-storage|Object Storage]] — the storage model tiers
- [[wiki/cloud-infra/storage-tiering|Storage Tiering]] — where warm sits in the ladder
- [[wiki/cloud-infra/cold-storage|Cold Storage]] — the cheaper, slower sibling
- [[wiki/devops-infra/backups|Backups]] — warm tier for recent backups
