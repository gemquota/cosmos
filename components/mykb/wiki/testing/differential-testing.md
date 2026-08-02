---
type: "concept"
title: "Differential Testing"
description: "Comparing outputs of two implementations on the same inputs"
tags: ["differential-testing", "testing", "oracles", "reference-implementation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/differential-testing", "https://llvm.org/docs/TestingGuide.html"]
---

# Differential Testing

## Summary
Differential testing runs the same inputs against two implementations, a reference and a candidate, and compares outputs. Any divergence signals a bug when the implementations are supposed to be equivalent, providing an oracle where none else exists.

## Details
- Classic uses: optimized versus old implementation, reimplementation versus spec reference.
- Also compares across versions, platforms, or language runtimes for consistency.
- Requires an oracle: the reference implementation defines expected behavior.
- Generate inputs with property-based testing and compare outputs automatically.
- Handle nondeterminism by pinning seeds and isolating time and randomness.
- Widely used in compilers, for example Csmith against C compilers, browsers, and databases.
- Pair with fuzzing: differential fuzzing turns any divergence into a finding.

## Related
- [[wiki/testing/property-based-testing|Property-Based Testing]] — generates the shared input space
- [[wiki/testing/test-oracles|Test Oracles]] — reference implementations as oracles
- [[wiki/testing/metamorphic-testing|Metamorphic Testing]] — relations when no reference exists
- [[wiki/testing/fuzzing|Fuzz Testing]] — differential fuzzing combines both
- [[wiki/testing/regression-testing|Regression Testing]] — catches divergence after changes
- [[wiki/testing/regression-test-selection|Regression Test Selection]] — rerunning differential suites efficiently
