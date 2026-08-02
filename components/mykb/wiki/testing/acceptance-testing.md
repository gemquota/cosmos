---
type: "concept"
title: "Acceptance Testing"
description: "Verifying the system meets business acceptance criteria"
tags: ["acceptance-testing", "testing", "business-criteria", "uat"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cucumber.io/docs/bdd/", "https://www.istqb.org/glossary"]
---

# Acceptance Testing

## Summary
Acceptance tests verify that the delivered system satisfies business acceptance criteria, expressed in stakeholder and user language. They answer whether the team built the right thing at the feature level, complementing the technical verification provided by other test layers.

## Details
- Criteria sources: user stories, acceptance criteria, and regulatory requirements.
- BDD tools like Cucumber, SpecFlow, and behave express criteria as executable Given/When/Then scenarios.
- Levels: business-rule acceptance at the API layer, journey acceptance at the UI layer.
- Distinct from regression testing: acceptance is feature-scoped and criteria-driven.
- Run a fast subset per commit and the complete set before release.
- Failures should map to a violated business rule, not a technical detail.
- Treat scenarios as living requirements that stay executable and reviewed.

## Related
- [[wiki/testing/behavior-driven-development|Behavior-Driven Development]] — the Given/When/Then format acceptance tests use
- [[wiki/testing/end-to-end-testing|End-to-End Testing]] — journey-level execution of acceptance criteria
- [[wiki/testing/test-pyramid|Test Pyramid]] — acceptance tests are a thin top layer
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — where acceptance suites gate releases
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — ubiquitous language behind criteria
