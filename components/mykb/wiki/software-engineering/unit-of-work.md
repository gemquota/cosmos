---
type: "concept"
title: "Unit of Work"
description: "Tracking changes during a business operation and committing them together"
tags: ["unit-of-work", "ddd", "transactions", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Unit of Work

## Summary
The unit of work pattern tracks objects modified during an operation and flushes all changes in one transaction at the end. It makes atomicity the default — either the whole operation persists or none of it does.

## Details
- ORM session patterns (Hibernate Session, EF DbContext) implement units of work.
- Track add, change, and delete; commit flushes in dependency order.
- Long-lived units of work accumulate stale state and big transactions — keep them short.
- mykb relevance: a batch of article writes commits as one unit, so partial syncs never corrupt the graph.

## Related
- [[wiki/software-engineering/repositories-pattern|Repositories Pattern]]
- [[wiki/software-engineering/aggregates|Aggregates]]
- [[wiki/compositions/database-migrations|Database Migrations]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
