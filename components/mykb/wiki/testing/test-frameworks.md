---
type: "concept"
title: "Test Frameworks"
description: "Comparing xUnit-style frameworks, conventions, and features"
tags: ["test-frameworks", "testing", "xunit", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://junit.org/junit5/docs/current/user-guide/", "https://docs.pytest.org/en/stable/"]
---

# Test Frameworks

## Summary
Test frameworks provide runners, assertions, fixtures, mocking, and reporting, the substrate every test suite builds on. Choosing and using them well shapes the ergonomics of the whole quality process.

## Details
- xUnit family: JUnit, pytest, Jest and Vitest, Go testing, xUnit.net, PHPUnit, and RSpec.
- Features: discovery, parametrization, fixtures and setup, assertions, mocking, coverage, and parallel runs.
- Ecosystem matters: plugins such as pytest-xdist and jest-extended, plus CI integrations.
- Pick a framework per layer: unit framework, E2E framework, and contract tool.
- Consistency beats features: standardize patterns within a team.
- Framework upgrades are risky: pin versions and test migrations.
- Read the documentation on fixtures and lifecycle to avoid common misuse.

## Related
- [[wiki/testing/parametrized-tests|Parametrized Tests]] — a framework feature that scales cases
- [[wiki/testing/async-testing|Asynchronous Testing]] — framework support for async code
- [[wiki/testing/mocking-frameworks|Mocking Frameworks]] — doubles integrated with runners
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — frameworks feeding pipelines
- [[wiki/testing/unit-testing|Unit Testing]] — the primary framework use
- [[wiki/testing/code-review-for-tests|Code Review for Tests]] — framework idiom review
