---
type: "concept"
title: "Offset Management"
description: "Tracking and committing where a consumer has read in a log"
tags: ["offsets", "kafka", "consumers", "messaging"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Offset Management

## Summary
Offsets record a consumer's position in a log so it resumes where it left off after a restart. Offset management — when and how to commit — decides how many messages are reprocessed after a failure.

## Details
- Auto-commit risks skipping messages on crash; commit after processing for at-least-once.
- Store offsets with the processing effect (transactional outbox style) for safer semantics.
- Seek tools (reset to earliest/latest) are the operational escape hatches.
- mykb relevance: the ingestion consumer commits offsets only after an article is durably written.

## Related
- [[wiki/software-engineering/consumer-groups|Consumer Groups]]
- [[wiki/software-engineering/lag-monitoring|Lag Monitoring]]
- [[wiki/software-engineering/at-least-once|At-Least-Once]]
- [[wiki/api-protocols/kafka|Kafka]]
- [[wiki/software-engineering/rebalancing|Rebalancing]]
