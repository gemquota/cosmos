---
type: "concept"
title: "Unit Testing Practice"
description: "Testing individual units of code in isolation, fast and often"
tags: ["unit-testing", "testing", "quality", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Unit_testing", "https://en.wikipedia.org/wiki/Test-driven_development"]
---

# Unit Testing Practice

## Summary
Unit testing verifies a single unit — a function, class, or module — in isolation, with dependencies faked and inputs chosen deliberately. Practice means fast, deterministic tests that run constantly, name behavior, and fail with clear messages.

## Details
- A unit test isolates: fakes replace collaborators so failures localize to the unit.
- Tests should be fast, deterministic, and independent — shared mutable state is a test smell.
- Name tests by behavior ('rejects empty slug'), not by implementation ('test_slug_function').
- The test pyramid puts unit tests at the base: thousands of them, milliseconds each.
- TDD writes the test first: red, green, refactor — the test is a design conversation.
- Coverage is a floor, not a goal: assertion quality matters more than line counts.
- For the mykb bundle, unit tests cover slug normalization, frontmatter validation, and link resolution.

Worked example — the wiki's slug utility has unit tests: kebab-case conversion, unicode handling, and duplicate detection; a mutation-testing pass confirms the assertions actually fail when the code breaks.

## Related
- [[wiki/dev-tools/code-coverage-tools|Code Coverage Tools]]
- [[wiki/dev-tools/mutation-testing-tools|Mutation Testing Tools]]
- [[wiki/testing/unit-testing|Unit Testing]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/dev-tools/property-testing-libraries|Property Testing Libraries]]
- [[wiki/software-engineering/refactoring-techniques|Refactoring Techniques]]
- [[wiki/dev-tools/fuzzing-tools|Fuzzing Tools]]
- [[wiki/testing/test-frameworks|Test Frameworks]]
