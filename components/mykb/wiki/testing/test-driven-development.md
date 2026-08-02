---
type: "concept"
title: "Test-Driven Development"
description: "Red-green-refactor cycles and how tests drive design"
tags: ["tdd", "testing", "red-green-refactor", "design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.agilealliance.org/glossary/tdd/", "https://www.ibm.com/topics/test-driven-development"]
---

# Test-Driven Development

## Summary
Test-driven development is a practice where tests are written before code in tight red-green-refactor cycles. The failing test defines expected behavior, the minimal implementation makes it pass, and the refactor keeps the design clean.

## Details
- Cycle: write a failing test (red), make it pass with the minimal code (green), then refactor.
- The discipline guarantees tests exist, focuses design on interfaces, and gives constant feedback.
- Schools: outside-in stubs collaborators from behavior at boundaries; classicist tests through real collaborators.
- Write the next test only when the current one passes; the suite becomes the specification.
- Best for pure logic and well-seamed code; UI, legacy, and exploratory areas need adaptations.
- Not a complete testing strategy: it pairs with integration, E2E, and property-based layers.
- Common failure: writing tests after the fact and calling it TDD; the design benefit comes from test-first.

## Related
- [[wiki/testing/behavior-driven-development|Behavior-Driven Development]] — example-driven specification sharing the cycle's spirit
- [[wiki/testing/testability|Testability]] — design properties TDD depends on
- [[wiki/testing/legacy-code-testing|Legacy Code Testing]] — applying TDD where no tests exist
- [[wiki/testing/characterization-testing|Characterization Testing]] — locking behavior before refactoring
- [[wiki/software-engineering/refactoring|Refactoring]] — the third step of the cycle
- [[wiki/testing/unit-testing|Unit Testing]] — the primary artifact TDD produces
