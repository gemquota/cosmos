---
type: "concept"
title: "Test Doubles"
description: "Taxonomy of dummies, fakes, stubs, spies, and mocks"
tags: ["test-doubles", "testing", "mocks", "fakes"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/TestDouble.html", "https://www.ibm.com/topics/test-doubles"]
---

# Test Doubles

## Summary
Test doubles are stand-ins for real collaborators that make tests fast, deterministic, and isolated. The taxonomy, dummies, fakes, stubs, spies, and mocks, distinguishes objects by what they fake and what they verify.

## Details
- Dummy: passed around to satisfy signatures but never actually used.
- Fake: a lightweight working implementation such as an in-memory repository with real behavior.
- Stub: returns canned responses; no verification of calls.
- Spy: wraps a real object to record calls for later assertions.
- Mock: scripted expectations verified at the end, combining stubbing with call verification.
- Choose the weakest double that works: prefer fakes for behavior, mocks for collaboration checks.
- Over-mocking couples tests to internals; integration tests should use real collaborators.
- Fowler's TestDouble article defines the vocabulary most frameworks follow.

## Related
- [[wiki/testing/mocking|Mocking]] — scripted expectations and verification
- [[wiki/testing/stubbing|Stubbing]] — canned responses without verification
- [[wiki/testing/fakes|Fakes]] — lightweight working implementations
- [[wiki/testing/spies|Spies]] — recording wrappers around real objects
- [[wiki/testing/mocking-frameworks|Mocking Frameworks]] — libraries that generate doubles
- [[wiki/testing/unit-testing|Unit Testing]] — the layer doubles serve
