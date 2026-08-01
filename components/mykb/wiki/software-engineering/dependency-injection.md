---
type: "concept"
title: "Dependency Injection"
description: "Technique for supplying an object with its dependencies from outside rather than constructing them internally"
tags: ["design", "testing", "ioc", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Dependency Injection

## Summary
Dependency injection (DI) passes dependencies into a component through its constructor or setters, so the component does not create its own collaborators. This makes behavior explicit and swappable.

## Details
- DI is a specific form of inversion of control; containers automate the wiring at composition time.
- Biggest payoff is testability: fakes and mocks replace real collaborators without touching production code.
- Overuse creates invisible wiring graphs; constructor injection with few parameters keeps it readable.

## Related
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]] — the principle DI implements
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]] — DI wires adapters into the core's ports
- [[wiki/testing/entities/test-patterns|Testing Patterns]] — injected fakes make tests fast
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — DI relates to factory and service locator patterns
