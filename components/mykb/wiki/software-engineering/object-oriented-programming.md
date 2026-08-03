---
type: "concept"
title: "Object-Oriented Programming"
description: "Programming paradigm organizing code around objects that bundle state and behavior"
tags: ["programming", "paradigm", "oop", "encapsulation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Object-Oriented Programming

## Summary

Object-oriented programming models a system as objects bundling state and behavior, communicating through messages. Its value is encapsulation and polymorphism; its failure mode is inheritance-heavy designs that couple everything. Modern practice favors composition and interfaces over deep hierarchies.

## Details
- Mechanism: objects encapsulate state behind methods (invariants stay local); polymorphism lets callers depend on interfaces, not classes; inheritance reuses implementation but couples subclasses to parent internals (fragile base class); message passing (method calls) is the interaction model — which maps naturally to the actor model and to domain-driven design's aggregates.
- Concrete example: a Payment object with pay() encapsulates its state transitions; a Shape interface with area() lets drawing code handle any shape; domain entities enforce invariants (an Order rejects negative quantities). The anti-pattern: a 10-level class hierarchy where behavior changes are scattered as overrides.
- Failure modes: deep inheritance and god classes; mutable shared state escaping encapsulation (getters exposing internals); object graphs that are hard to test without mocks; and classes that are really just namespaces with state, losing the modeling value.
- Operational tradeoffs: OOP buys encapsulation and polymorphism at the cost of indirection and state management; the pragmatic blend is OOP structure with functional cores (pure methods where possible), interface-based polymorphism, and composition instead of inheritance.
- RSIS3/mykb relevance: the wiki's domain model uses encapsulated aggregates with interfaces, so loop tooling can extend behavior without breaking core invariants.
- Encapsulation discipline: hide mutable state behind behavior; getters that expose internals are the first step toward the god-class spiral.
- Testing: prefer testing through public behavior (contracts) over white-box internal access, which couples tests to implementation details.

## Related
- [[wiki/software-engineering/functional-programming|Functional Programming]] — the paradigm that favors data transformation over state mutation
- [[wiki/software-engineering/type-systems|Type Systems]] — static typing sharpens OOP interfaces
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — design patterns grew up in OOP
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Ecosystem]] — a mainstream OOP-flavored language
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — tactical DDD patterns are OOP-shaped
