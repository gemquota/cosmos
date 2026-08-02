---
type: "concept"
title: "Dual Writes"
description: "Writing to two systems in one operation and the consistency traps involved"
tags: ["dual-writes", "consistency", "transactions", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dual Writes

## Summary
Dual writes update two stores — a database and a cache, a database and a search index — in the same logical operation. Without coordination, one write can succeed and the other fail, leaving the systems permanently divergent.

## Details
- The classic failure: write DB ok, write cache fails (or vice versa) — divergence with no retry.
- Fixes: transactional outbox, CDC-driven sync, or making one store authoritative.
- Avoid dual writes where possible; event-sourced or outboxed sync is more reliable.
- mykb relevance: wiki article saves must not dual-write the DB and index without an outbox.

## Related
- [[wiki/software-engineering/outbox-table|Outbox Table]]
- [[wiki/software-engineering/transactional-outbox|Transactional Outbox]]
- [[wiki/software-engineering/projections|Projections]]
- [[wiki/compositions/data-backfills|Data Backfills]]
- [[wiki/software-engineering/cqrs-pattern|CQRS Pattern]]
