---
type: "concept"
title: "Component Testing"
description: "Testing UI components in isolation with mocked surroundings"
tags: ["component-testing", "testing", "ui", "react-testing-library"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://testing-library.com/docs/react-testing-library/intro/", "https://storybook.js.org/docs/writing-tests"]
---

# Component Testing

## Summary
Component testing mounts a UI component in isolation with mocked props, context, and dependencies, then asserts on rendering and interaction. It combines the speed of unit tests with user-facing assertions, making it the workhorse of modern frontend quality.

## Details
- Tooling: React Testing Library, Vue Test Utils, Angular TestBed, and Web Components test runners.
- Query by role, label, and text, the way users perceive the interface, not by implementation selectors.
- Mock only surroundings: fetch, router, state store, and child components that are not under test.
- Assert rendered output, emitted events, and accessibility roles in the same pass.
- Environments: jsdom or happy-dom for logic-heavy tests, a real browser for layout-sensitive cases.
- Storybook interaction tests execute component scenarios against the real browser.
- Stable props and event contracts keep component tests resilient to refactors.

## Related
- [[wiki/testing/ui-testing|UI Testing]] — broader rendered-interface verification
- [[wiki/testing/end-to-end-testing|End-to-End Testing]] — journeys that use components together
- [[wiki/testing/test-doubles|Test Doubles]] — mocked surroundings for components
- [[wiki/testing/mocking|Mocking]] — scripting component dependencies
- [[wiki/testing/test-frameworks|Test Frameworks]] — the runners component tests build on
- [[wiki/web-platforms/component-architecture|Component Architecture]] — design patterns components are tested against
