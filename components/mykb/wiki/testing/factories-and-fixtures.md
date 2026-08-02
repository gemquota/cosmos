---
type: "concept"
title: "Factories and Fixtures"
description: "Building test objects via factories and loading fixture datasets"
tags: ["factories", "fixtures", "testing", "setup"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://github.com/thoughtbot/factory_bot", "https://docs.pytest.org/en/stable/how-to/fixtures.html"]
---

# Factories and Fixtures

## Summary
Factories build test objects with sensible defaults and overridable attributes; fixtures load static datasets. Together they make test setup compact, readable, and maintainable instead of a wall of boilerplate.

## Details
- Factories: FactoryBot for Rails, Factory Boy for Python, with Faker integration.
- Fixtures: pytest fixtures, JUnit setup methods, and static JSON or SQL datasets.
- Factory pattern: define once, override per test, such as user, admin user, or expired token.
- Fixtures suit read-only reference data; factories suit per-test variations.
- Avoid implicitly building deep object graphs; make dependencies explicit.
- Deterministic attributes, fixed IDs and dates, stabilize assertions.
- Balance: over-using factories hides required fields; validate in tests.

## Related
- [[wiki/testing/database-seeding|Database Seeding]] — loading factories into databases
- [[wiki/testing/fake-data-generators|Fake Data Generators]] — realistic attribute values
- [[wiki/testing/test-data-management|Test Data Management]] — the broader data strategy
- [[wiki/testing/parametrized-tests|Parametrized Tests]] — variations across factories
- [[wiki/testing/test-isolation|Test Isolation]] — fresh fixtures per test
- [[wiki/testing/test-frameworks|Test Frameworks]] — fixture lifecycle support
