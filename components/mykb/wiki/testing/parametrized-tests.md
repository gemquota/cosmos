---
type: "concept"
title: "Parametrized Tests"
description: "Running the same test body across many input cases"
tags: ["parametrized-tests", "testing", "table-driven", "coverage"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.pytest.org/en/stable/how-to/parametrize.html", "https://junit.org/junit5/docs/current/user-guide/#writing-tests-parameterized-tests"]
---

# Parametrized Tests

## Summary
Parametrized tests run the same test body across many input cases, turning a loop of examples into structured, individually reported tests. They compress coverage and make each failure specific.

## Details
- Tools: pytest.mark.parametrize, JUnit ParameterizedTest, Jest test.each, and Go table tests.
- Each case gets its own name and failure report, no loop-failed-at-index guessing.
- Combine with property-based testing for generated cases.
- Table-driven data: inputs, expected outputs, and labels live next to the test.
- Name cases by intent with pytest ids or Jest test.each titles.
- Edge cases: empty, null, boundaries, duplicates, and unicode belong in tables.
- Beware combinatorial explosion; choose representative cases or pairwise selection.

## Related
- [[wiki/testing/property-based-testing|Property-Based Testing]] — generated cases beyond tables
- [[wiki/testing/equivalence-partitioning|Equivalence Partitioning]] — choosing representative cases
- [[wiki/testing/boundary-value-analysis|Boundary Value Analysis]] — edge cases for tables
- [[wiki/testing/test-frameworks|Test Frameworks]] — framework support for parametrization
- [[wiki/testing/pairwise-testing|Pairwise Testing]] — trimming combinations
- [[wiki/testing/code-review-for-tests|Code Review for Tests]] — reviewing case tables
