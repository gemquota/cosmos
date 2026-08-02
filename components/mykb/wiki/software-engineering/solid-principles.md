---
type: "concept"
title: "SOLID Principles"
description: "The five object-oriented design principles for maintainable class hierarchies"
tags: ["solid", "design", "oop", "principles"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/SOLID", "https://en.wikipedia.org/wiki/Object-oriented_programming"]
---

# SOLID Principles

## Summary
SOLID is the acronym for five object-oriented design principles: single responsibility, open-closed, Liskov substitution, interface segregation, and dependency inversion. Together they guide class design toward changeability and testability, especially in larger systems.

## Details
- Single responsibility: a class should have one reason to change, keeping each unit small and focused.
- Open-closed: extend behavior without modifying existing code, typically via polymorphism and composition.
- Liskov substitution: subtypes must be usable wherever their base type is expected, preserving invariants and expectations.
- Interface segregation: prefer many small, specific interfaces over one fat interface that forces implementers to stub methods.
- Dependency inversion: depend on abstractions, not concretions, so implementations can be swapped.
- SOLID is a diagnostic toolkit: when a change hurts, one of these principles usually names the pain and the remedy.

Worked example — an ArticlePublisher class that formats, saves, and emails violates single responsibility. Split into an ArticleFormatter, an ArticleRepository, and an ArticleNotifier, each behind an interface, and every change localizes to one class.

## Related
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/software-engineering/object-oriented-principles|Object-Oriented Principles]]
- [[wiki/software-engineering/composition-over-inheritance|Composition Over Inheritance]]
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]]
- [[wiki/software-engineering/code-smells|Code Smells]]
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/software-engineering/template-method|Template Method]]
- [[wiki/software-engineering/strategy-pattern|Strategy Pattern]]
- [[wiki/software-engineering/object-oriented-programming|Object-Oriented Programming]]
