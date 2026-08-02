---
type: "concept"
title: "Error Guessing"
description: "Anticipating likely defects from experience and heuristics"
tags: ["error-guessing", "testing", "heuristics", "technique"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.istqb.org/glossary", "https://www.ibm.com/topics/error-guessing"]
---

# Error Guessing

## Summary
Error guessing is a technique where testers anticipate likely defects from experience and heuristics, common mistakes, edge conditions, and past bug patterns. It adds high-value cases that intuition alone finds.

## Details
- Heuristics: empty inputs, zero, null, first and last items, duplicates, division by zero, and timeouts.
- Mine history: past bugs and customer reports seed future error guesses.
- Combine with specification-based techniques for systematic coverage.
- Sessions and checklists make guesses repeatable and reviewable.
- Record why each guess matters so tests stay maintainable.
- Pair with risk-based testing to focus guesses where impact is high.
- Use structured heuristics such as Whittaker tours and ISTQB checklists.

## Related
- [[wiki/testing/exploratory-testing|Exploratory Testing]] — heuristic-driven discovery
- [[wiki/testing/negative-testing|Negative Testing]] — the guesses often target invalid inputs
- [[wiki/testing/risk-based-testing|Risk-Based Testing]] — prioritizing high-impact guesses
- [[wiki/testing/boundary-value-analysis|Boundary Value Analysis]] — systematic boundary heuristics
- [[wiki/testing/session-based-testing|Session-Based Testing]] — structured time-boxed guessing
- [[wiki/testing/equivalence-partitioning|Equivalence Partitioning]] — filling gaps heuristics find
