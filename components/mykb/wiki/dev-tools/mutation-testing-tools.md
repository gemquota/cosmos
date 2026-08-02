---
type: "concept"
title: "Mutation Testing Tools"
description: "Tools that mutate source code to check whether tests actually detect faults"
tags: ["mutation-testing", "testing", "tooling", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Mutation Testing Tools

## Summary
Mutation testing tools inject small faults — flipping operators, deleting statements — and run the suite to see whether any test fails. Surviving mutants reveal assertions that are too weak.

## Details
- Stryker (JS/.NET/Java) and PIT (Java) are the mainstream tools; cosmic-ray covers Python.
- Run on changed code or a module subset: full-suite mutation is expensive, often 10-50x slower.
- The mutation score (killed mutants over total) is a stronger quality signal than line coverage.
- RSIS3 relevance: mutate mykb links and summaries to see if curation checks would catch drift.

## Related
- [[wiki/dev-tools/mutation-testing|Mutation Testing]]
- [[wiki/testing/mutation-testing|Mutation Testing]]
- [[wiki/dev-tools/code-coverage-tools|Code Coverage Tools]]
- [[wiki/testing/ci-quality-gates|CI Quality Gates]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
