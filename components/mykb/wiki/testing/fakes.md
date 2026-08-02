---
type: "concept"
title: "Fakes"
description: "Lightweight in-memory implementations standing in for real dependencies"
tags: ["fakes", "testing", "test-doubles", "in-memory"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/TestDouble.html", "https://www.ibm.com/topics/test-doubles"]
---

# Fakes

## Summary
Fakes are lightweight in-memory implementations that behave like the real dependency, with the same interface but simplified internals. They provide realistic behavior, including state and edge cases, without I/O cost, and are the strongest double for logic tests.

## Details
- Examples: in-memory repositories, fake clocks, in-memory queues, and email senders that collect messages.
- Unlike stubs, fakes implement real semantics: duplicates, ordering, and errors are handled.
- They run in-process, so they are fast and deterministic, with no network or disk.
- Main risk: fake drift, where the fake diverges from the real dependency; contract tests keep them honest.
- Prefer fakes when behavior matters and the real dependency is slow, flaky, or hard to license.
- Containerized integration tests with the real engine complement fakes where fidelity matters.
- A well-designed fake can be shared across many test files and teams.

## Related
- [[wiki/testing/test-doubles|Test Doubles]] — the category fakes belong to
- [[wiki/testing/stubbing|Stubbing]] — canned responses versus real semantics
- [[wiki/testing/in-memory-databases|In-Memory Databases]] — a common kind of fake persistence
- [[wiki/testing/contract-testing|Contract Testing]] — keeps fakes aligned with real dependencies
- [[wiki/testing/service-virtualization|Service Virtualization]] — network-level stand-ins for services
- [[wiki/testing/integration-testing|Integration Testing]] — real collaborators validate fake behavior
