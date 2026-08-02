---
type: "concept"
title: "Risk-Based Testing"
description: "Prioritizing test effort by failure likelihood and impact"
tags: ["risk-based-testing", "testing", "risk", "prioritization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/risk-based-testing", "https://www.istqb.org/glossary"]
---

# Risk-Based Testing

## Summary
Risk-based testing prioritizes test effort by the likelihood and impact of failure, testing what hurts most first. It optimizes limited budgets against business exposure instead of spreading effort evenly.

## Details
- Risk equals likelihood times impact; rank features and modules accordingly.
- Signals: change frequency, complexity, criticality, past defects, and dependencies.
- Allocate effort: deep testing for high risk, smoke-level checks for low risk.
- Communicate risk posture: what was tested, what remains, and residual risk.
- Combine with test prioritization and exploratory charters.
- Revisit the risk matrix as the product evolves.
- Risk registers make testing decisions auditable and defensible.

## Related
- [[wiki/testing/test-prioritization|Test Prioritization]] — ordering by the same risk signals
- [[wiki/testing/exploratory-testing|Exploratory Testing]] — charters aimed at high risk
- [[wiki/testing/error-guessing|Error Guessing]] — focused high-impact guesses
- [[wiki/testing/measuring-test-roi|Measuring Test ROI]] — justifying risk-based allocation
- [[wiki/testing/regression-test-selection|Regression Test Selection]] — risk-driven test choice
- [[wiki/testing/manual-testing|Manual Testing]] — human effort on high-risk areas
