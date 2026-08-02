---
type: "concept"
title: "Composition Over Inheritance"
description: "Building behavior by combining objects and functions instead of subclassing"
tags: ["oop", "composition", "inheritance", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Composition Over Inheritance

## Summary
Composition over inheritance favors assembling small, focused units — objects that hold other objects, functions that wrap functions — over deep subclass hierarchies. It avoids fragile base classes and makes behavior explicit and testable.

## Details
- Composition: a class holds collaborators and delegates to them; inheritance: a subclass inherits behavior implicitly.
- The fragile base class problem — changes to a base break many subclasses — mostly disappears with composition.
- Interfaces plus delegation preserve polymorphism without the hierarchy tax.
- mykb relevance: wiki content types compose (article wraps frontmatter, body, sources) rather than subclassing.

## Related
- [[wiki/software-engineering/object-oriented-programming|Object-Oriented Programming]]
- [[wiki/software-engineering/object-oriented-principles|Object-Oriented Principles]]
- [[wiki/software-engineering/decorator-pattern|Decorator Pattern]]
- [[wiki/software-engineering/strategy-pattern|Strategy Pattern]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
