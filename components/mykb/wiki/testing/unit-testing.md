---
type: "concept"
title: "Unit Testing"
description: "Verifying individual functions and classes in isolation for fast, deterministic feedback"
tags: ["unit-testing", "testing", "isolation", "fast-feedback"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://jestjs.io/docs/getting-started", "https://docs.pytest.org/en/stable/"]
---

# Unit Testing

## Summary
Unit tests verify a single unit, typically a function, class, or module, in isolation with collaborators replaced by doubles. They run in milliseconds, localize failures to one assertion, and form the base layer of the test pyramid.

## Details
- Frameworks: Jest and Vitest for JavaScript, pytest for Python, JUnit 5 for Java, and the Go testing package.
- Isolation: replace filesystem, network, and clock access with fakes or stubs so the unit is the only thing under test.
- Fast feedback: a unit suite for a medium service finishes in seconds, enabling per-commit verification.
- Failure locality: a failing unit test names the exact function and assertion, sharply cutting debugging time.
- Contract encoding: unit tests document inputs, outputs, and invariants, so refactors stay safe.
- Behavior focus: assert observable outcomes rather than internal call sequences.
- Edge cases: empty inputs, nulls, overflow, and boundary values belong at this layer.
- Keep tests independent so any subset can run in any order.

## Related
- [[wiki/testing/integration-testing|Integration Testing]] — the next layer up in the pyramid
- [[wiki/testing/test-doubles|Test Doubles]] — the isolation mechanism unit tests rely on
- [[wiki/testing/test-pyramid|Test Pyramid]] — unit tests are the wide base
- [[wiki/testing/test-frameworks|Test Frameworks]] — runners and assertions used here
- [[wiki/testing/coverage-metrics|Coverage Metrics]] — measures how much of the unit is exercised
- [[wiki/software-engineering/refactoring|Refactoring]] — unit tests make refactors safe
