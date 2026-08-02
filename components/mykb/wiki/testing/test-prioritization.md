---
type: "concept"
title: "Test Prioritization"
description: "Ordering tests by failure likelihood and risk for fast feedback"
tags: ["test-prioritization", "testing", "risk", "feedback"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/test-prioritization", "https://martinfowler.com/bliki/TestPyramid.html"]
---

# Test Prioritization

## Summary
Test prioritization orders tests by failure likelihood and risk so the most valuable tests run first. It shrinks feedback time and maximizes the defects found early in a run when budgets are tight.

## Details
- Signals: recent changes, failure history, coverage of changed lines, and test age.
- Prioritize tests on recently modified code, high-risk modules, and slow important ones.
- Combine with time-boxed runs: execute the top-N in limited CI slots.
- Regression test selection is a related, more precise form of the idea.
- Order for failure localization: fast, focused tests before broad ones.
- Measure and tune: track the detection effectiveness of the prioritized order.
- Most valuable when full suites exceed CI budgets.

## Related
- [[wiki/testing/regression-test-selection|Regression Test Selection]] — a precise form of prioritization
- [[wiki/testing/test-ordering|Test Ordering]] — the mechanics of execution order
- [[wiki/testing/risk-based-testing|Risk-Based Testing]] — risk-driven test choices
- [[wiki/testing/test-parallelism|Test Parallelism]] — scheduling alongside priority
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — time-boxed gate runs
- [[wiki/testing/measuring-test-roi|Measuring Test ROI]] — valuing prioritized suites
