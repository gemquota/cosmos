---
type: "concept"
title: "Aggregates"
description: "DDD clusters of entities and values treated as one consistency unit"
tags: ["ddd", "aggregates", "consistency", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Aggregates

## Summary
An aggregate is a DDD cluster of entities and value objects with one root, guarding the invariants of the whole cluster. All writes go through the root, making the aggregate the transaction and consistency boundary.

## Details
- The aggregate root is the only object external code may hold a reference to.
- Load and save the whole aggregate as a unit — split aggregates to avoid oversized transactions.
- Design around business invariants: what must stay consistent together becomes one aggregate.
- mykb relevance: an Article aggregate (content, sources, links) enforces link-integrity invariants.

## Related
- [[wiki/software-engineering/entities-vs-value-objects|Entities vs Value Objects]]
- [[wiki/software-engineering/repositories-pattern|Repositories Pattern]]
- [[wiki/software-engineering/unit-of-work|Unit of Work]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
