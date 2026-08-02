---
type: "concept"
title: "Frontend Testing"
description: "Unit, integration, and end-to-end strategy"
tags: [testing", "frontend", "unit-tests", "integration-tests", "qa"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://vitest.dev/guide/", "https://testing-library.com/docs/"]
---

# Frontend Testing

## Summary
Frontend testing covers unit tests for logic and components, integration tests for component interactions, and end-to-end tests for complete user flows. The testing pyramid keeps most tests fast and small, with fewer slow browser tests at the top. Testing Library's user-centric queries and vitest/Jest runners are the common stack.

## Details
- Unit tests: pure functions, reducers, and utilities with fast runners; components get render tests with assertions on behavior.
- Component tests: render a component, fire user events, and assert on accessible output using role queries.
- Integration tests: exercise feature flows across components with mocked network boundaries.
- Mocking: fetch, timers, and modules get mocked; React Testing Library discourages testing implementation details.
- Coverage: code coverage finds untested lines but not missing scenarios; pair it with behavioral review.
- CI: run fast suites on every commit, E2E on merge, and keep tests deterministic with fixed time and locale.

## Related
- [[wiki/frontend/end-to-end-testing|End-to-End Testing]] — the browser-level layer
- [[wiki/testing/entities/test-patterns|Test Patterns]] — reusable test design
- [[wiki/frontend/visual-regression-testing|Visual Regression Testing]] — UI appearance checks
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — automated a11y assertions
- [[wiki/dev-tools/code-coverage|Code Coverage]] — measuring coverage
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — running tests in pipelines
