---
type: "concept"
title: "Acceptance Criteria"
description: "The concrete conditions that make a story done and testable"
tags: ["acceptance-criteria", "testing", "requirements", "definition-of-done"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Acceptance_testing", "https://en.wikipedia.org/wiki/User_story"]
---

# Acceptance Criteria

## Summary
Acceptance criteria are the testable conditions a story must meet to be accepted: specific, observable outcomes written before the work starts. They turn vague stories into contracts and give testers and developers the same target.

## Details
- Write criteria as behaviors: given a state, when an action, then an observable outcome (Gherkin style).
- Good criteria are testable, unambiguous, and cover the happy path plus key edge cases.
- They become acceptance tests: automated where cheap, manual where the interaction is visual.
- Involve the product owner in writing them — acceptance is their decision, not the developer's guess.
- Criteria are the definition of done for the story; without them, done is an opinion.
- For the mykb bundle, acceptance criteria define what makes an article publishable: frontmatter valid, links resolve, sources verified.
- Worked example — acceptance criteria for link-check: 'Given an article with a broken wikilink, when the build runs, then the build fails and the report names the link'.

Worked example — acceptance criteria for link-check: 'Given an article with a broken wikilink, when the build runs, then the build fails and the report names the link'.

## Related
- [[wiki/software-engineering/user-stories|User Stories]]
- [[wiki/software-engineering/specification-by-example|Specification by Example]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
- [[wiki/software-engineering/requirements-engineering|Requirements Engineering]]
- [[wiki/testing/acceptance-testing|Acceptance Testing]]
- [[wiki/software-engineering/coding-standards|Coding Standards]]
- [[wiki/testing/behavior-driven-development|Behavior-Driven Development]]
- [[wiki/tooling/smoke-tests|Smoke Tests]]
- [[wiki/dev-tools/coverage-gauges|Coverage Gauges]]
