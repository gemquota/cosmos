---
type: "concept"
title: "Composite Pattern"
description: "Treating individual objects and groups of objects uniformly"
tags: ["composite", "patterns", "design", "hierarchy"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Composite Pattern

## Summary
The composite pattern builds tree structures where leaves and branches share an interface, so clients treat a single item and a whole subtree identically. File systems, UI trees, and org charts are composites.

## Details
- The uniform interface is the key: children(), add(), remove() on both leaves and composites.
- Recursion is built in: an operation on a composite recursively hits every leaf.
- Guard against cycles and unbounded depth in shared or graph-like structures.
- mykb relevance: wiki sections compose — a section contains paragraphs or nested sections alike.

## Related
- [[wiki/software-engineering/iterator-pattern|Iterator Pattern]]
- [[wiki/software-engineering/visitor-pattern|Visitor Pattern]]
- [[wiki/software-engineering/flyweight-pattern|Flyweight Pattern]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
