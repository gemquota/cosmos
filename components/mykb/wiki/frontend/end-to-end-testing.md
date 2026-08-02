---
type: "concept"
title: "End-to-End Testing"
description: "Browser-level full-flow automation"
tags: [testing", "e2e", "playwright", "cypress", "automation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://playwright.dev/docs/intro", "https://docs.cypress.io/guides/overview/why-cypress"]
---

# End-to-End Testing

## Summary
End-to-end testing drives a real browser through complete user journeys — login, search, checkout — asserting on the visible UI and network behavior. Playwright and Cypress are the dominant tools, with auto-waiting, screenshots, and trace recording. E2E tests validate integration across components, APIs, and third-party services at the cost of speed and flakiness risk.

## Details
- User perspective: tests find elements by role and text, click, type, and assert on outcomes rather than internals.
- Auto-waiting: Playwright and Cypress retry assertions and waits, replacing brittle sleep-based tests.
- Network control: request interception and route mocking simulate slow networks, errors, and API responses.
- Parallelism: browsers and workers shard suites across machines, keeping full-suite time acceptable.
- Flake control: stable selectors, no shared state, and retry policies keep flaky tests from eroding trust.
- CI integration: tests run against a preview or staging deploy; traces and video aid failure diagnosis.

## Related
- [[wiki/frontend/frontend-testing|Frontend Testing]] — the layers beneath E2E
- [[wiki/frontend/visual-regression-testing|Visual Regression Testing]] — screenshot checks alongside
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — browser-level a11y assertions
- [[wiki/testing/entities/test-patterns|Test Patterns]] — E2E design patterns
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — E2E in pipelines
- [[wiki/frontend/dev-server|Dev Server]] — the local target E2E runs against
