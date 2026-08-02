---
type: "concept"
title: "Specification by Example"
description: "Collaborating on requirements through concrete examples and automated tests"
tags: ["specification-by-example", "bdd", "examples", "requirements"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://gojko.net/books/specification-by-example/", "https://en.wikipedia.org/wiki/Behavior-driven_development"]
---

# Specification by Example

## Summary
Specification by example builds shared understanding through concrete examples of behavior — discussed with stakeholders, written in a readable format, and automated as executable tests. The examples become the living specification.

## Details
- The flow: identify key examples, describe them collaboratively, automate them, then validate continuously.
- Examples surface ambiguity that abstract requirements hide — 'fast' becomes a concrete latency budget.
- The executable specification prevents drift: tests and requirements cannot diverge if they are the same artifact.
- It pairs with BDD: Given/When/Then scenarios are the shared language.
- Investment is upfront (facilitation) and ongoing (example maintenance), paid back in fewer defects.
- For the mykb bundle, curation rules are specified by example: sample articles that define valid frontmatter and linking.
- Worked example — the wiki defines 'valid stub' by examples: a fixture with 3 tags and a related block passes, one with 1 tag fails — those examples are the test suite.

Worked example — the wiki defines 'valid stub' by examples: a fixture with 3 tags and a related block passes, one with 1 tag fails — those examples are the test suite.

## Related
- [[wiki/software-engineering/acceptance-criteria|Acceptance Criteria]]
- [[wiki/software-engineering/requirements-engineering|Requirements Engineering]]
- [[wiki/software-engineering/user-stories|User Stories]]
- [[wiki/testing/behavior-driven-development|Behavior-Driven Development]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
- [[wiki/software-engineering/coding-standards|Coding Standards]]
- [[wiki/testing/golden-tests|Golden Tests]]
- [[wiki/communities/checksums|Checksums]]
- [[wiki/communities/package-pinning|Package Pinning]]
