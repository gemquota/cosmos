---
type: "concept"
title: "Value Objects"
description: "Immutable objects defined by their values, not their identity"
tags: ["value-objects", "ddd", "immutability", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Value Objects

## Summary
Value objects are immutable objects whose equality depends on field values — an Amount, a DateRange, a Slug — not on identity. They encode domain invariants and remove primitive obsession from models.

## Details
- Two value objects with the same fields are equal; they are interchangeable.
- Encode invariants at construction: an Email validates on creation, so invalid emails cannot exist.
- Immutability is required: values that change silently break equality and sharing.
- mykb relevance: Slug, Status, and SourceUrl as value objects keep wiki entities honest.

## Related
- [[wiki/software-engineering/entities-vs-value-objects|Entities vs Value Objects]]
- [[wiki/software-engineering/immutability-practice|Immutability Practice]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
- [[wiki/software-engineering/builder-pattern|Builder Pattern]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
