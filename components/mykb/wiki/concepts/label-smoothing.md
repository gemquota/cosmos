---
type: "concept"
title: "Label Smoothing"
description: "Softening targets to improve calibration and robustness"
tags: ["label-smoothing", "calibration", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Label Smoothing

## Summary
Label smoothing replaces one-hot targets with slightly distributed ones, discouraging overconfidence.

## Details
- Label smoothing replaces one-hot targets with slightly distributed ones, discouraging overconfidence.
- It improves calibration and sometimes robustness, at slight accuracy cost.
- Over-smoothing can hide genuine certainty.
- RSIS3 relevance: graded practice checks are label-smoothed audits of the workspace.

## Related
- [[wiki/concepts/temperature-scaling|Temperature Scaling]] — the inference-side fix
- [[wiki/concepts/calibration|Calibration]] — the goal
- [[wiki/concepts/overfitting-llm|Overfitting in LLMs]] — what it mitigates
- [[wiki/concepts/regularization-practice|Regularization in Practice]] — the family
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
