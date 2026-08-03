---
type: "entity"
title: "MagicMock"
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---
description: "Python's flexible mock object that auto-creates attributes and records interactions"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "testing", "python"]

# MagicMock

## Summary
MagicMock is Python's flexible test double from the unittest.mock module: any attribute access or method call succeeds and returns another mock, while every interaction is recorded. It matters because it lets tests isolate code from dependencies quickly. That flexibility must be used deliberately, or tests silently pass against behavior that never actually happens.

## Details
- **Definition** — a MagicMock is a mock object whose attributes and methods are created on demand, returning child mocks, so unconfigured code paths still run.
- **Magic methods** — unlike plain Mock, MagicMock supports Python protocol methods such as iteration, containment, and arithmetic, matching real objects more closely.
- **Recording** — every call's arguments are stored, enabling assertions like assert_called_once_with and inspection of call counts and order.
- **Configuration** — return values, side effects, and raised exceptions are set per call, so a fake can simulate success, failure, and sequencing.
- **Isolation** — patching dependencies such as network clients, databases, or time functions makes tests fast and deterministic.
- **Over-mocking hazard** — asserting on mocks that were never wired into the code under test gives false confidence; integration coverage is still required.
- **Common failure modes** — unconfigured mocks returning mocks that flow into real logic, and assertions that drift from the actual call signatures.
- **Worked example** — a login handler is tested by patching the auth service client; the mock returns a token for valid credentials and raises for invalid ones, and the handler's branches are asserted.
- **Practical relevance** — MagicMock is the standard tool for unit-level isolation in Python, but it is a scalpel, not a substitute for integration tests.

## Related
- [[wiki/testing/mocking|Mocking]] — when and how to mock
- [[wiki/testing/mocking-frameworks|Mocking Frameworks]] — tooling landscape
- [[wiki/testing/unit-testing|Unit Testing]] — the context for mocks
- [[wiki/testing/property-based-testing|Property-Based Testing]] — beyond hand-written cases
- [[wiki/testing/test-timeouts|Test Timeouts]] — bounding slow fakes
- [[wiki/software-engineering/object-oriented-programming|Object-Oriented Programming]] — mockable seams
