---
type: "concept"
title: "Composition Over Inheritance"
description: "Building behavior by combining objects and functions instead of subclassing"
tags: ["oop", "composition", "inheritance", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Composition Over Inheritance

## Summary

Composition over inheritance builds behavior by combining small objects rather than extending base classes. Composition yields flexible, testable code; inheritance couples subclasses to parent internals and makes change ripple. The heuristic: favor has-a over is-a unless the hierarchy is genuinely stable.

## Details
- Mechanism: inheritance shares implementation via subclassing (tight coupling: a base-class change affects all subclasses; fragile base class problem); composition holds collaborating objects and delegates behavior, choosing implementations at runtime; interfaces/roles (protocols, traits) preserve polymorphism without implementation inheritance.
- Concrete example: a Logger with a Formatter and a Writer composed in beats a LoggerBase with overriding methods; an event handler composed of filters and strategies adapts without subclass explosion; frameworks like React and Go (embedding + interfaces) push composition structurally. The smell: deep hierarchies with overridden methods and "protected" internals leaking.
- Failure modes: composition without interfaces (concrete dependencies, harder testing); over-composition creating indirection and object soup; and misreading the rule — stable, domain-model inheritance (Shape → Circle) is fine; the problem is implementation inheritance for reuse.
- Operational tradeoffs: composition adds a bit of boilerplate (wiring) and indirection for dramatically better change isolation and testability; the standard is interface-based composition, with inheritance reserved for true is-a domain modeling.
- RSIS3/mykb relevance: the wiki's agent capabilities are composed (tools + policies + memory) rather than subclassed, so the loop adds behaviors without rewriting base agents.
- Interface discipline: compose through small role interfaces so dependencies stay swappable; concrete-composition defeats the testability benefit.
- Hierarchy audit: when a class extends another solely to reuse methods, that is the smell — extract and compose instead of deepening the tree.
- Testing payoff: composed behavior is unit-testable in isolation — each collaborator mocked at its interface — while deep hierarchies force constructing the whole ancestor chain to test a leaf.
- Change economics: adding a capability via composition is a new collaborator and wiring; via inheritance it is a new level or override, rippling through every subclass — which is why composition keeps change local.

## Related
- [[wiki/software-engineering/object-oriented-programming|Object-Oriented Programming]]
- [[wiki/software-engineering/object-oriented-principles|Object-Oriented Principles]]
- [[wiki/software-engineering/decorator-pattern|Decorator Pattern]]
- [[wiki/software-engineering/strategy-pattern|Strategy Pattern]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
