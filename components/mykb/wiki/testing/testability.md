---
type: "concept"
title: "Testability"
description: "Designing code with seams and dependency injection for easy testing"
tags: ["testability", "testing", "design", "seams"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/Testability.html", "https://www.ibm.com/topics/testability"]
---

# Testability

## Summary
Testability is the design quality that makes code easy to test: clear seams, dependency injection, deterministic behavior, and observable outputs. Testable design is the root enabler of every other testing practice.

## Details
- Seams: inject collaborators through constructors and parameters instead of global access.
- Determinism: inject clocks, randomness, and I/O; avoid hidden mutable state.
- Observable outputs: prefer return values and events over side-effect soup.
- Small units: focused functions and components with single responsibilities.
- Inversion of control and hexagonal architecture improve testability.
- Testable code also tends to be clearer and more modular.
- Refactor legacy code toward seams incrementally.

## Related
- [[wiki/software-engineering/dependency-injection|Dependency Injection]] — the primary seam mechanism
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]] — framework-level testability
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]] — ports and adapters for testing
- [[wiki/testing/legacy-code-testing|Legacy Code Testing]] — adding seams to old systems
- [[wiki/testing/unit-testing|Unit Testing]] — what testable design enables
- [[wiki/testing/test-doubles|Test Doubles]] — collaborators swapped at seams
