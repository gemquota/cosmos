---
type: "concept"
title: "Boundary Value Analysis"
description: "Testing the edges of equivalence classes"
tags: ["boundary-value", "testing", "edge-cases", "technique"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.istqb.org/glossary", "https://www.ibm.com/topics/boundary-value-analysis"]
---

# Boundary Value Analysis

## Summary
Boundary value analysis tests the edges of equivalence classes, minimum, maximum, just inside, and just outside, where off-by-one and comparison bugs concentrate. Boundaries are where most validation defects live.

## Details
- Test at, just below, and just above each boundary, for example one, zero, and two for a minimum of one.
- Applies to numeric ranges, string lengths, dates, pagination, and array indices.
- Incorporate open and closed interval semantics from the specification.
- Pair with equivalence partitioning: partitions pick cases, boundaries pick edges.
- Watch floating-point boundaries and inclusive versus exclusive endpoint bugs.
- Automate boundaries with parametrized tables for readability.
- Boundary bugs are classic in age checks, coupon codes, and paging.

## Related
- [[wiki/testing/equivalence-partitioning|Equivalence Partitioning]] — classes whose edges to test
- [[wiki/testing/parametrized-tests|Parametrized Tests]] — boundary tables as cases
- [[wiki/testing/negative-testing|Negative Testing]] — just-outside values
- [[wiki/testing/decision-table-testing|Decision Table Testing]] — boundary conditions in rules
- [[wiki/testing/test-oracles|Test Oracles]] — expected boundary results
- [[wiki/testing/unit-testing|Unit Testing]] — boundary cases in unit suites
