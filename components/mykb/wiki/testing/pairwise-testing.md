---
type: "concept"
title: "Pairwise Testing"
description: "Combinatorial selection of parameter pairs to shrink test matrices"
tags: ["pairwise-testing", "testing", "combinatorial", "technique"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.pairwise.org/", "https://www.ibm.com/topics/pairwise-testing"]
---

# Pairwise Testing

## Summary
Pairwise testing selects test combinations so every pair of parameter values appears at least once, shrinking combinatorial matrices exponentially while covering interaction bugs. Most defects involve one or two interacting parameters.

## Details
- Basis: most bugs are triggered by one or two parameter interactions.
- Matrix: n parameters with v values each shrinks to a few pairwise cases with tools like PICT, AllPairs, or Jenny.
- Example: four parameters with three values is 81 combinations, reduced to about twelve pairwise cases.
- Extend to three-way coverage when interaction depth is known to matter.
- Combine with equivalence partitioning to reduce value sets first.
- Best for configuration matrices: browsers, OS, locale, and feature flags.
- Record constraints so impossible combinations are excluded by the tool.

## Related
- [[wiki/testing/equivalence-partitioning|Equivalence Partitioning]] — reducing values before pairing
- [[wiki/testing/parametrized-tests|Parametrized Tests]] — executing pairwise cases
- [[wiki/testing/decision-table-testing|Decision Table Testing]] — full combinations versus pairs
- [[wiki/testing/compatibility-testing|Compatibility Testing]] — configuration matrices to trim
- [[wiki/testing/test-configuration-management|Test Configuration Management]] — config dimensions to cover
- [[wiki/testing/test-data-management|Test Data Management]] — data dimensions in matrices
