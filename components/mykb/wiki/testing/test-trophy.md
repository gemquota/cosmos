---
type: "concept"
title: "Test Trophy"
description: "Prioritizing static analysis, unit, integration, and few E2E tests"
tags: ["test-trophy", "testing", "testing-library", "frontend"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications", "https://testing-library.com/docs/"]
---

# Test Trophy

## Summary
The test trophy reweights the pyramid for modern web apps: static analysis and unit tests form the wide base, integration tests with a real DOM are the biggest tier, and E2E tests stay few. It reflects where bugs actually live in componentized UIs.

## Details
- Kent C. Dodds popularized the trophy and the Testing Library philosophy.
- Static tools such as ESLint and TypeScript catch whole classes of errors before runtime.
- Integration tests render whole components with a real DOM, mocking only network boundaries.
- Unit tests cover pure logic; E2E tests cover critical user journeys only.
- Rationale: integration tests give the most confidence per unit of cost in component apps.
- Testing Library encourages testing as users use the app, not implementation details.
- The trophy suits component-heavy frontends more than backend monoliths.

## Related
- [[wiki/testing/test-pyramid|Test Pyramid]] — the classic model the trophy reweights
- [[wiki/testing/component-testing|Component Testing]] — the unit of frontend integration tests
- [[wiki/testing/integration-testing|Integration Testing]] — the largest trophy tier
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]] — the trophy's static base
- [[wiki/software-engineering/type-systems|Type Systems]] — compile-time checks in the base
- [[wiki/testing/end-to-end-testing|End-to-End Testing]] — few journeys at the trophy top
