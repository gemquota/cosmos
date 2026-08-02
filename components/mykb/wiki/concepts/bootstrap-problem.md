---
type: "concept"
title: "Bootstrap Problem"
description: "How an agent validates an improvement using only the competence it already has"
tags: ["bootstrap", "RSI", "epistemics", "self-improvement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Bootstrapping", "https://en.wikipedia.org/wiki/Technological_singularity"]
---

# Bootstrap Problem

## Summary
The bootstrap problem is the catch-22 of recursive self-improvement: to verify that a proposed upgrade is better, you need capabilities you may only get after accepting the upgrade. Every self-improving system must find trustworthy static or external anchors to break the circularity.

## Details
- **Form** — proving P(n+1) better than P(n) looks like it requires P(n+1)'s own judgment.
- **Escapes** — hold-out evaluation on frozen benchmarks, external oversight, formal verification of the evaluator, and conservatism about accepting large deltas.
- **Relevant failure** — a system that self-rates as improved without external evidence is just flattering itself (self-report vs measure).
- **Worked example** — RSIS3's immutable evaluator and git-based rollback are bootstrap anchors: the current self is trusted to run tests, not to rewrite the tests.
- **Relation to Gödelian views** — some see self-trust limits as fundamental; others note that external oracles break the circle.

## Related
- [[wiki/concepts/seed-ai|Seed AI]] — the system that faces the bootstrap problem
- [[wiki/pulses/self-benchmarking|Self-Benchmarking]] — internal attempt to solve it
- [[wiki/pulses/self-reports-vs-measures|Self-Reports vs Measures]] — why self-ratings cannot close the loop
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the fix: freeze the judge
- [[wiki/decisions/test-set-discipline|Test Set Discipline]] — holding out evaluation from optimization
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — context
