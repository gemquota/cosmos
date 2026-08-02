---
type: "concept"
title: "Mocking Frameworks"
description: "Survey of mocking libraries, their idioms, and common pitfalls"
tags: ["mocking-frameworks", "testing", "mocks", "libraries"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.pytest.org/en/stable/how-to/monkeypatch.html", "https://site.mockito.org/"]
---

# Mocking Frameworks

## Summary
Mocking frameworks automate the creation of doubles, generating objects on the fly, scripting behavior, and verifying calls. Each language ecosystem has idiomatic tools and recurring pitfalls around partial mocks, matchers, and over-mocking.

## Details
- JavaScript: Jest mocks and Vitest vi; Python: unittest.mock and pytest-mock; Java: Mockito and MockK; .NET: Moq and NSubstitute; Go: testify and mockery.
- Core features: auto-generated doubles, argument matchers, call verification, and stubbing helpers.
- Pitfalls: verifying implementation details, brittle argument matchers, and mock-heavy tests that pass while code is broken.
- Modern guidance: prefer real implementations or fakes; use mocks only at slow or irrelevant boundaries.
- Auto-mocking conveniences such as annotations trade setup speed for test opacity.
- Keep mocking at component boundaries; dependency injection makes swapping trivial.
- Frameworks differ in strictness: strict vs lenient verification changes suite noise.

## Related
- [[wiki/testing/mocking|Mocking]] — the practice frameworks automate
- [[wiki/testing/test-doubles|Test Doubles]] — the taxonomy frameworks implement
- [[wiki/testing/stubbing|Stubbing]] — canned responses in framework idioms
- [[wiki/testing/spies|Spies]] — recording wrappers framework APIs expose
- [[wiki/testing/fakes|Fakes]] — the preferred alternative to generated mocks
- [[wiki/testing/test-frameworks|Test Frameworks]] — runners mocking libraries integrate with
