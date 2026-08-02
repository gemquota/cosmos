---
type: "concept"
title: "Factory Pattern"
description: "Creating objects through a function or method instead of direct constructors"
tags: ["factory", "creation", "patterns", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Factory Pattern

## Summary
The factory pattern centralizes object creation in a method or function, so callers depend on an interface rather than a concrete class. Factories pay off when construction is complex, conditional, or likely to change.

## Details
- Simple factory centralizes creation; factory method defers to subclasses; abstract factory creates families.
- Use when construction requires config, validation, or pool/reuse decisions.
- Avoid factories for trivial construction — indirection without payoff is ceremony.
- mykb relevance: a slug factory could normalize any input into a valid kebab-case article path.

## Related
- [[wiki/software-engineering/builder-pattern|Builder Pattern]]
- [[wiki/software-engineering/prototype-pattern|Prototype Pattern]]
- [[wiki/software-engineering/dependency-injection|Dependency Injection]]
- [[wiki/software-engineering/singleton-pitfalls|Singleton Pitfalls]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
