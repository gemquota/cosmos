---
type: "concept"
title: "Test Oracles"
description: "Sources of expected behavior used to judge pass or fail"
tags: ["test-oracles", "testing", "expected-behavior", "technique"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.istqb.org/glossary", "https://spectrum.ieee.org/metamorphic-testing"]
---

# Test Oracles

## Summary
A test oracle is any source of expected behavior used to judge pass or fail: a specification, reference implementation, invariant, or human judgment. Choosing the right oracle determines what a test can assert at all.

## Details
- Oracle types: exact specification, reference implementation, invariants, metamorphic relations, and statistical checks.
- The no-oracle problem: systems where correct output is hard to define, such as machine learning and search.
- Solutions: metamorphic testing, differential testing, and human-in-the-loop approval.
- Property-based tests use invariant oracles over generated inputs.
- Golden files are a stored-output oracle.
- Oracle quality bounds test value: weak oracles allow false confidence.
- LLM evaluation uses rubrics and judges as oracles for open-ended outputs.

## Related
- [[wiki/testing/metamorphic-testing|Metamorphic Testing]] — relations as oracles
- [[wiki/testing/differential-testing|Differential Testing]] — reference implementations as oracles
- [[wiki/testing/property-based-testing|Property-Based Testing]] — invariant oracles
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — judge oracles for model output
- [[wiki/testing/golden-file-management|Golden File Management]] — stored-output oracles
- [[wiki/testing/characterization-testing|Characterization Testing]] — observed behavior as oracle
