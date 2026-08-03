---
type: "concept"
title: "Code Coverage"
description: "The percentage of code exercised by tests, used as a signal for test sufficiency"
tags: ["testing", "metrics", "quality", "coverage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Code_coverage", "https://martinfowler.com/bliki/TestCoverage.html"]
---

# Code Coverage

## Summary
Code coverage measures which lines, branches, or paths tests execute. It is a useful signal for finding untested code, but it measures exercise, not correctness — 100% coverage can still miss bugs.

## Details
- Line vs branch coverage: branch coverage catches untested decision paths.
- Use as a floor and a diff gate (new code must be covered), not a target to game.
- RSIS3 relevance: wiki link validation covers the graph; missing links are uncovered edges.
- Code coverage measures what fraction of code is executed by tests — line, branch, function, and statement coverage being the common metrics.
- Coverage is a floor, not a quality metric: 100% coverage of weak assertions still proves little.
- The useful practice is coverage-guided test design: find uncovered branches that correspond to real risk and add tests there.
- Coverage trends matter more than absolute numbers; drops in coverage should fail CI only when policy says so.
- **Worked example / comparison** — Worked example — the wiki's link-checker would reach 90% branch coverage; the uncovered branches would be the timeout and parse-error paths, which then get targeted tests.
- Branch coverage is the useful signal for decision logic: it catches untested if/else and switch paths that line coverage misses, which is where most regressions hide.
- Mutation testing complements coverage: it changes the code and checks whether tests catch the change, exposing assertions that pass for the wrong reasons.
- Coverage gates should be policy-driven: enforce a floor on new code and review drops, but treat the number as a tripwire for inspection rather than a score to maximize.
- Coverage trends matter more than snapshots: a slowly falling number is how tests rot, and CI should make that trend visible even when no single commit crosses a threshold.
- For mykb, code-coverage is documented as the test-adequacy signal in the dev-tools testing cluster.

## Related
- [[wiki/testing/entities/test-patterns|Testing Patterns]]
- [[wiki/dev-tools/mutation-testing|Mutation Testing]]
- [[wiki/testing/eval-sets|Eval Sets]]
- [[wiki/software-engineering/refactoring|Refactoring]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
