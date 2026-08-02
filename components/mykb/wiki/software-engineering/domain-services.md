---
type: "concept"
title: "Domain Services"
description: "Stateless operations that coordinate multiple aggregates or encode domain rules"
tags: ["ddd", "domain-services", "design", "services"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Domain Services

## Summary
Domain services hold domain logic that does not naturally belong to one aggregate — transfers between accounts, pricing across a cart. They are stateless, operate on aggregates, and express the language of the domain.

## Details
- Put logic in the aggregate when it fits; use domain services for cross-aggregate operations.
- Domain services are distinct from application services: no transactions, no I/O, pure domain.
- Their methods read like domain language: transferMoney(from, to, amount).
- mykb relevance: a LinkIntegrityService checks cross-article invariants no single article owns.

## Related
- [[wiki/software-engineering/application-services|Application Services]]
- [[wiki/software-engineering/aggregates|Aggregates]]
- [[wiki/software-engineering/use-case-layer|Use Case Layer]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
- [[wiki/software-engineering/clean-architecture|Clean Architecture]]
