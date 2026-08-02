---
type: "concept"
title: "Equivalence Partitioning"
description: "Dividing inputs into classes expected to behave identically"
tags: ["equivalence-partitioning", "testing", "black-box", "technique"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.istqb.org/glossary", "https://www.ibm.com/topics/equivalence-partitioning"]
---

# Equivalence Partitioning

## Summary
Equivalence partitioning divides inputs into classes expected to behave identically, so one representative per class suffices for testing. It collapses an infinite input space into a few meaningful cases.

## Details
- Classes follow behavior: valid and invalid, ranges, formats, and states such as age bands.
- One representative per partition is enough; more cases add little value.
- Combine with boundary value analysis for the edges of each class.
- Derive classes from requirements and code conditions such as if and switch boundaries.
- Pair with decision tables for condition combinations.
- Prevents redundant tests on equivalent inputs and gaps on untested classes.
- Document the partition logic so future tests stay aligned.

## Related
- [[wiki/testing/boundary-value-analysis|Boundary Value Analysis]] — edges of each partition
- [[wiki/testing/decision-table-testing|Decision Table Testing]] — condition combinations
- [[wiki/testing/parametrized-tests|Parametrized Tests]] — representatives as cases
- [[wiki/testing/black-box-testing|Black-Box Testing]] — the family this belongs to
- [[wiki/testing/negative-testing|Negative Testing]] — invalid partitions
- [[wiki/testing/test-oracles|Test Oracles]] — expected results per partition
