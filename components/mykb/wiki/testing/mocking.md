---
type: "concept"
title: "Mocking"
description: "Replacing collaborators with scripted behavior and verifying call interactions"
tags: ["mocking", "testing", "test-doubles", "interactions"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://jestjs.io/docs/mock-functions", "https://docs.python.org/3/library/unittest.mock.html"]
---

# Mocking

## Summary
Mocking replaces a real collaborator with an object whose behavior is scripted, then verifies that the expected interactions happened with the right arguments. It isolates the system under test and is the most widely used, and most often misused, kind of test double.

## Details
- Standard tools: Jest mock functions, Mockito, unittest.mock, and Moq.
- Two roles: arrange scripted behavior, then assert expected calls; a mock is a stub plus verification.
- Use mocks at boundaries you own, such as network, clock, and filesystem, not at internal classes.
- Danger: over-specifying calls makes refactors painful and breaks tests on innocent renames.
- Prefer asserting observable behavior; use call assertions only when interaction is the contract.
- Mocking third-party SDKs hides real wire behavior, so cover that with contract or integration tests.
- Dependency injection makes collaborators swappable for mocks without global patches.

## Related
- [[wiki/testing/test-doubles|Test Doubles]] — the taxonomy mocking belongs to
- [[wiki/testing/stubbing|Stubbing]] — the canned-response half of a mock
- [[wiki/testing/spies|Spies]] — recording alternatives that keep real behavior
- [[wiki/testing/mocking-frameworks|Mocking Frameworks]] — libraries that automate mocks
- [[wiki/software-engineering/dependency-injection|Dependency Injection]] — the seam that makes mocking easy
- [[wiki/testing/integration-testing|Integration Testing]] — real collaborators where mocks mislead
