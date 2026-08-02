---
type: "concept"
title: "Fake Data Generators"
description: "Generating realistic fake data with libraries like Faker"
tags: ["faker", "testing", "data-generation", "seeding"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://faker.readthedocs.io/en/master/", "https://fakerjs.dev/"]
---

# Fake Data Generators

## Summary
Fake data generators produce realistic-looking names, addresses, emails, and domain values for tests, demos, and seeding. Realism matters because tests behave differently on representative data than on hand-typed lorem ipsum.

## Details
- Libraries: Faker for Python, Faker.js and faker for JavaScript, and JavaFaker.
- Locales: generate per-language and region datasets, including RTL text and local formats.
- Use in factories, seeders, property tests, and performance datasets.
- Determinism: seed the generator for reproducible runs.
- Beware unrealistic collisions: enforce uniqueness for IDs and emails.
- Generated data should validate against the model schema.
- Fine for lower environments, but tag fake personal data clearly.

## Related
- [[wiki/testing/factories-and-fixtures|Factories and Fixtures]] — generators feed factories
- [[wiki/testing/database-seeding|Database Seeding]] — generated rows for databases
- [[wiki/testing/test-data-management|Test Data Management]] — synthetic data strategy
- [[wiki/testing/property-based-testing|Property-Based Testing]] — generated inputs with invariants
- [[wiki/testing/parametrized-tests|Parametrized Tests]] — varied generated cases
- [[wiki/testing/database-testing|Database Testing]] — realistic data for queries
