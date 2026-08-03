---
type: "concept"
title: "Storage Tiering"
description: "Moving data between hot, warm, and cold storage classes as access frequency changes"
tags: ["storage", "tiering", "cost", "lifecycle"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Storage Tiering

## Summary

Storage tiering matches data classes to storage economics — hot, warm, cold, archive — with automatic movement where possible. It is the single biggest storage cost lever: most teams can cut storage spend 50-80% by tiering what they never read.

## Details
- Mechanism: tiers differ in storage cost, retrieval fee, latency, and minimum duration (S3 Standard → IA → Glacier tiers; GCS standard → nearline → coldline → archive; Azure hot → cool → cold → archive); movement is manual, via lifecycle rules, or automatic (S3 Intelligent-Tiering, GCS autoclass); retrieval economics dominate the decision, not storage price alone.
- Concrete example: a media library keeps 30 days hot, transitions to IA at 90, and archives at 365 via lifecycle; access telemetry shows 5% of the archive is read yearly, so deep archive is right; a "hot" bucket that analytics reads weekly is a tiering miss that costs 5-10x.
- Failure modes: tiering by age instead of access pattern (young-but-dead data stays hot, old-but-read data gets retrieval fees); lifecycle churn (objects oscillating between tiers, accruing operation fees); ignoring minimum-duration penalties; and applications that assume synchronous access to archived data.
- Operational tradeoffs: automatic tiering removes guesswork at a small premium; manual lifecycle rules are cheaper for known patterns. Instrument access per object class, review tier placement quarterly, and always validate restore times for the archive tier in DR plans.
- RSIS3/mykb relevance: the wiki's storage cost model maps every dataset to a tier with telemetry; the loop's cost reviews move tiers based on measured access, not calendar age.
- Retrieval fee awareness: read-heavy but cold data can cost more in retrieval fees than it saves in storage; compute the break-even access rate per class before tiering.
- Testing restores: schedule annual restore drills from the archive tier so RTO claims match reality, and document expected restore times per tier.

## Related
- [[wiki/cloud-infra/object-storage|Object Storage]] — the platform tiers apply to
- [[wiki/cloud-infra/cold-storage|Cold Storage]] — the cheapest, slowest tier
- [[wiki/cloud-infra/warm-storage|Warm Storage]] — the middle tier
- [[wiki/devops-infra/backups|Backups]] — tiered backup retention
