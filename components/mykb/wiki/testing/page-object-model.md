---
type: "concept"
title: "Page Object Model"
description: "Encapsulating selectors and interactions in reusable page objects"
tags: ["page-object-model", "testing", "ui-testing", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/", "https://playwright.dev/docs/test-pom"]
---

# Page Object Model

## Summary
The Page Object Model encapsulates page structure and interactions in reusable objects so UI tests read like user actions instead of brittle selector soup. It decouples tests from DOM changes and is the standard UI test pattern.

## Details
- Each page or screen gets a class exposing actions and assertions, such as login or add to cart.
- Tests call page objects; selectors live in one place for maintainability.
- Selenium's documentation recommends POM as an encouraged test practice.
- Page fragments compose for repeated sections like headers and dialogs.
- Modern frameworks offer equivalents: Playwright fixtures and Cypress custom commands.
- Pitfall: over-abstracting into generic helpers that hide intent.
- Reduces duplication and diff churn when markup changes.

## Related
- [[wiki/testing/ui-testing|UI Testing]] — the practice POM structures
- [[wiki/testing/end-to-end-testing|End-to-End Testing]] — journeys benefit from page objects
- [[wiki/testing/component-testing|Component Testing]] — component-level alternatives
- [[wiki/software-engineering/refactoring|Refactoring]] — maintainable test code
- [[wiki/testing/testability|Testability]] — design for testable UI layers
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — the surface selectors target
