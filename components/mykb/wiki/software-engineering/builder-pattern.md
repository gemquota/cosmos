---
type: "concept"
title: "Builder Pattern"
description: "Constructing complex objects step by step with fluent, readable calls"
tags: ["builder", "creation", "patterns", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Builder Pattern

## Summary
The builder pattern constructs complex objects incrementally — set fields, then build() — keeping construction readable and separate from the object's structure. It shines for objects with many optional parameters.

## Details
- Fluent builders read like named arguments and can validate before building.
- Immutable builders produce immutable results, unlike long constructor parameter lists.
- Builders also model stepwise processes where order matters (protocol builders).
- mykb relevance: an article builder assembles frontmatter, body sections, and sources with validation at the end.

## Related
- [[wiki/software-engineering/factory-pattern|Factory Pattern]]
- [[wiki/software-engineering/value-objects|Value Objects]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/software-engineering/immutability-practice|Immutability Practice]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
