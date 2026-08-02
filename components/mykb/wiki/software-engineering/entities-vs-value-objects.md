---
type: "concept"
title: "Entities vs Value Objects"
description: "The DDD distinction between identity-tracked objects and value-defined ones"
tags: ["ddd", "entities", "value-objects", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Entities vs Value Objects

## Summary
Domain-Driven Design splits objects into entities, which have a stable identity and change over time, and value objects, which are interchangeable and immutable. Getting the split right shapes how you model identity, equality, and persistence.

## Details
- Entities: id-based equality, mutable, tracked across time — an Order, a User, an Article.
- Value objects: field-based equality, immutable, replaceable — Money, Address, Slug.
- Common mistake: modeling values as entities, then needing artificial IDs for them.
- mykb relevance: an Article is an entity; its Title and Status are value objects.

## Related
- [[wiki/software-engineering/value-objects|Value Objects]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
- [[wiki/software-engineering/aggregates|Aggregates]]
- [[wiki/software-engineering/object-oriented-principles|Object-Oriented Principles]]
- [[wiki/software-engineering/immutability-practice|Immutability Practice]]
