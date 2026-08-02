---
type: "concept"
title: "Spies"
description: "Wrapping real objects to record calls for later assertions"
tags: ["spies", "testing", "test-doubles", "interactions"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://sinonjs.org/releases/latest/spies/", "https://jestjs.io/docs/mock-functions"]
---

# Spies

## Summary
Spies wrap real objects to record calls, arguments, return values, and call counts without changing behavior. Tests run the real implementation and afterwards assert how it was used, giving observation without substitution.

## Details
- Tooling: jest.spyOn, Sinon spies, Mockito spy, and pytest monkeypatch wrappers.
- Spy at the seam, run real code, then assert what was called, how often, and with which payload.
- Use spies when the real object is cheap but interactions matter, such as logging or event emission.
- Less intrusive than mocks: real behavior stays, so internal refactors do not break assertions.
- Partial mocks, spying plus stubbing selected methods, mix responsibilities and deserve caution.
- Assert the calls that matter, not every incidental interaction, to avoid brittle tests.
- Spies are also a debugging aid for inspecting what a collaborator actually received.

## Related
- [[wiki/testing/test-doubles|Test Doubles]] — the family spies belong to
- [[wiki/testing/mocking|Mocking]] — scripted behavior versus recorded observation
- [[wiki/testing/mocking-frameworks|Mocking Frameworks]] — libraries that create spies
- [[wiki/testing/integration-testing|Integration Testing]] — spies observe real collaborators
- [[wiki/testing/code-review-for-tests|Code Review for Tests]] — call assertions need review discipline
