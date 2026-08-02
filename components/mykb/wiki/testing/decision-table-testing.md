---
type: "concept"
title: "Decision Table Testing"
description: "Modeling condition combinations and their expected actions"
tags: ["decision-tables", "testing", "business-rules", "technique"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.istqb.org/glossary", "https://www.ibm.com/topics/decision-table-testing"]
---

# Decision Table Testing

## Summary
Decision table testing models combinations of conditions and their expected actions, covering every meaningful rule in a system. It finds missing and conflicting logic that case-by-case testing misses.

## Details
- Structure: condition rows, action rows, and rule columns where each column is a test case.
- Useful for business rules: pricing, eligibility, routing, and validation matrices.
- Impossible or dead combinations are marked and excluded from execution.
- Tables expose all combinations; pairwise testing can trim huge ones.
- Implement tables as parametrized tests with one case per rule column.
- Keep tables small, up to about ten conditions; split complex rules.
- Review tables with stakeholders as executable specifications.

## Related
- [[wiki/testing/equivalence-partitioning|Equivalence Partitioning]] — input classes feed decision tables
- [[wiki/testing/state-transition-testing|State Transition Testing]] — states versus rule conditions
- [[wiki/testing/pairwise-testing|Pairwise Testing]] — trimming condition combinations
- [[wiki/testing/parametrized-tests|Parametrized Tests]] — encoding rule columns
- [[wiki/testing/black-box-testing|Black-Box Testing]] — the family this belongs to
- [[wiki/testing/behavior-driven-development|Behavior-Driven Development]] — rules as shared examples
