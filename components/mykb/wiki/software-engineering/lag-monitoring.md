---
type: "concept"
title: "Lag Monitoring"
description: "Tracking how far consumers are behind the latest message"
tags: ["lag", "monitoring", "consumer-groups", "kafka"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Lag Monitoring

## Summary
Lag is the distance between the last produced message and where a consumer group has read. Lag monitoring turns that distance into an alertable metric — sustained growth means consumers cannot keep up.

## Details
- Lag per group and partition: a single stuck partition skews the whole story — watch per-partition max.
- Lag is a symptom: growth signals slow consumers, backpressure, or a producer flood.
- Alert on lag trends and age of oldest unread message, not just raw counts.
- mykb relevance: lag on the ingestion queue shows whether curation keeps up with captures.

## Related
- [[wiki/software-engineering/consumer-groups|Consumer Groups]]
- [[wiki/software-engineering/offset-management|Offset Management]]
- [[wiki/software-engineering/rebalancing|Rebalancing]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
- [[wiki/dev-tools/alerting-rules|Alerting Rules]]
