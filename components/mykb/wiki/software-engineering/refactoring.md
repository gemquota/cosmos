---
type: "concept"
title: "Refactoring"
description: "Restructuring code to improve its internal structure without changing observable behavior"
tags: ["refactoring", "quality", "clean-code", "maintenance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://refactoring.com/"]
---

# Refactoring

## Summary
Refactoring, as defined by Martin Fowler, is changing the internal structure of software to make it easier to understand and cheaper to modify, without altering its observable behavior. It is a disciplined, test-backed activity, not an excuse for big-bang rewrites.

## Details
- The core discipline: behavior-preserving transformations, each small enough to verify immediately, strung together into a larger improvement.
- The catalog is the vocabulary: Extract Function, Rename Variable, Replace Conditional with Polymorphism, and dozens more are named recipes with mechanics.
- Refactoring only feels safe with a test suite; tests are the safety net that catches accidental behavior changes between steps.
- It attacks the root cause of many ills: code smells such as long functions, feature envy, and duplicated logic are the signals that a refactor is needed.
- Refactoring is distinct from rewriting: continuous small steps preserve value, while rewrites discard working history and risk regressions.
- RSIS3 relevance: the wiki itself refactors — stubs grow into full articles, categories get reorganized — with the link graph as the test suite.
- Worked example: a 200-line function with three responsibilities becomes three extracted functions, with the test suite rerun after each step.

## Related
- [[wiki/software-engineering/technical-debt|Technical Debt]] — refactoring is the principal repayment mechanism
- [[wiki/software-engineering/code-review|Code Review]] — reviewers propose refactors that keep code healthy
- [[wiki/software-engineering/clean-architecture|Clean Architecture]] — the target structure that refactors aim toward
- [[wiki/testing/entities/test-patterns|Testing Patterns]] — tests make behavior-preserving change verifiable
- [[wiki/dev-tools/code-coverage|Code Coverage]] — coverage maps which code the refactoring net protects
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — curation is to the wiki what refactoring is to code
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — refactors often converge on named patterns
- [[wiki/software-engineering/type-systems|Type Systems]] — strong types make behavior-preserving change safer
