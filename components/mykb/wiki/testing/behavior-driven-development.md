---
type: "concept"
title: "Behavior-Driven Development"
description: "Given/When/Then specifications shared across business and technical roles"
tags: ["bdd", "testing", "gherkin", "specification"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cucumber.io/docs/bdd/", "https://specflow.org/learn/"]
---

# Behavior-Driven Development

## Summary
Behavior-driven development frames specification as concrete examples: given a context, when an action happens, then an outcome. These scenarios are written in shared language, automated as tests, and serve as living documentation for both business and technical roles.

## Details
- Gherkin syntax: Feature, Scenario, Given, When, and Then parsed by Cucumber, SpecFlow, behave, or JBehave.
- The three amigos, product, development, and testing, author scenarios collaboratively.
- Scenarios double as acceptance criteria and regression tests; automate at the layer matching the behavior.
- Avoid scenario bloat: keep each scenario to one behavior with readable intent.
- Anti-patterns: testing implementation details or building a parallel UI-test layer in Gherkin.
- Example mapping sessions turn vague requirements into concrete, testable examples.
- Treat the feature files as documentation and review them with stakeholders.

## Related
- [[wiki/testing/acceptance-testing|Acceptance Testing]] — BDD scenarios operationalize acceptance criteria
- [[wiki/testing/test-driven-development|Test-Driven Development]] — the development rhythm BDD specifications feed
- [[wiki/testing/test-frameworks|Test Frameworks]] — runners that execute Gherkin scenarios
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — ubiquitous language shared by BDD roles
- [[wiki/testing/code-review-for-tests|Code Review for Tests]] — scenario quality deserves review
