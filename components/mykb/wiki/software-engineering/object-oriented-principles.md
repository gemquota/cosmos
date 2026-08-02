---
type: "concept"
title: "Object-Oriented Principles"
description: "Modeling systems as objects with state, behavior, and polymorphism"
tags: ["oop", "objects", "principles", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Object-oriented_programming", "https://en.wikipedia.org/wiki/SOLID"]
---

# Object-Oriented Principles

## Summary
Object-oriented programming models a system as objects that bundle state and behavior, communicating through messages. Its principles — encapsulation, abstraction, inheritance, and polymorphism — organize code around the data it manipulates and the contracts between objects.

## Details
- Encapsulation hides internal state behind behavior, so invariants stay enforceable.
- Abstraction names concepts as interfaces; polymorphism lets one interface serve many implementations.
- Inheritance reuses and specializes behavior but couples types; composition over inheritance keeps hierarchies shallow.
- Design principles like SOLID guide object design: responsibilities, open-closed extension, and dependency inversion.
- OOP and FP are not enemies: most systems blend objects at the boundary with pure logic inside.
- For the mykb bundle, objects model the article and pipeline stages, with pure functions for the transformations.
- Worked example — an Article object encapsulates its frontmatter and body, exposing publish() and validate() rather than raw fields, so its invariants cannot be broken from outside.

Worked example — an Article object encapsulates its frontmatter and body, exposing publish() and validate() rather than raw fields, so its invariants cannot be broken from outside.

## Related
- [[wiki/software-engineering/solid-principles|SOLID Principles]]
- [[wiki/software-engineering/composition-over-inheritance|Composition Over Inheritance]]
- [[wiki/software-engineering/object-oriented-programming|Object-Oriented Programming]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/software-engineering/entities-vs-value-objects|Entities vs Value Objects]]
- [[wiki/software-engineering/strategy-pattern|Strategy Pattern]]
- [[wiki/software-engineering/observer-pattern|Observer Pattern]]
- [[wiki/software-engineering/dependency-injection|Dependency Injection]]
