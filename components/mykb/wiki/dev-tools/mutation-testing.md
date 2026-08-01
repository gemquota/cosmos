---
type: "concept"
title: "Mutation Testing"
description: "Injecting small faults into code to check whether the test suite detects them"
tags: ["testing", "quality", "mutants", "verification"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Mutation Testing

## Summary
Mutation testing mutates the program (e.g., flipping `<` to `>`) and reruns the suite: if tests pass, the mutant survived, revealing a weakness in the tests. It measures test quality rather than coverage quantity.

## Details
- Surviving mutants are either untested behavior or redundant assertions.
- Computationally expensive, so it runs on subsets or in CI nightly; tools include Stryker and PIT.
- RSIS3 relevance: an LLM eval set is mutation-tested when perturbations flip outputs and evals catch them.

## Related
- [[wiki/dev-tools/code-coverage|Code Coverage]] — mutation testing is coverage's stronger cousin
- [[wiki/testing/eval-sets|Eval Sets]] — perturbed inputs reveal eval blind spots
- [[wiki/software-engineering/technical-debt|Technical Debt]] — surviving mutants are hidden debt
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — mutation thinking applies to model outputs
