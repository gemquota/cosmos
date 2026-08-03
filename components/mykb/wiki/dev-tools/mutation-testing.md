---
type: "concept"
title: "Mutation Testing"
description: "Injecting small faults into code to check whether the test suite detects them"
tags: ["testing", "quality", "mutants", "verification"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Mutation Testing

## Summary
Mutation testing mutates the program — flipping < to >, deleting a line, changing a constant — and reruns the suite: if tests pass, the mutant survived, revealing a weakness in the tests. It measures test quality, not coverage quantity: the question is whether the tests would notice a real bug.

## Details
- Mechanism: the tool generates mutants (small semantic changes), runs the suite against each, and reports the mutation score — killed mutants are caught by tests, surviving mutants are not; surviving mutants are either untested behavior or redundant assertions; each survivor is a concrete, human-readable gap.
- Concrete example: a validation function where mutating a boundary condition (>= to >) survives the suite means the boundary is untested; flipping a boolean that controls error handling surviving means the error path is dead weight; Stryker or PIT report survivors per line, guiding where tests are weak.
- Failure modes: the computational cost — a large suite times every mutant, so runs are slow (run on subsets or nightly); equivalent mutants (mutations that do not change behavior) inflating the score artificially; the mutation score gamed by over-specifying tests; survivors that represent intentional behavior, requiring human triage.
- Tradeoffs: mutation testing is coverage's stronger cousin — it proves the tests assert real behavior rather than merely executing lines — at a steep computational price; the alternative, line/branch coverage, is cheap and easily gamed; the mature pattern is mutation testing on critical modules in CI or nightly, with survivors triaged into real tests.
- Operational notes: run it where correctness matters most, review survivors, and track the score over time.
- RSIS3 relevance: an LLM eval set is mutation-tested when perturbations flip outputs and evals catch them — the same quality-check applied to evaluation rather than code.

## Related
- [[wiki/dev-tools/code-coverage|Code Coverage]] — mutation testing is coverage's stronger cousin
- [[wiki/testing/eval-sets|Eval Sets]] — perturbed inputs reveal eval blind spots
- [[wiki/software-engineering/technical-debt|Technical Debt]] — surviving mutants are hidden debt
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — mutation thinking applies to model outputs
