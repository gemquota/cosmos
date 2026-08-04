---
type: "decision"
title: "Eval Splits"
description: "Partitioning data into train, validation, and test sets"
tags: ["eval-splits", "data", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Eval Splits

## Summary
Eval splits partition data so training, tuning, and final evaluation use disjoint examples.

## Details
- Eval splits partition data so training, tuning, and final evaluation use disjoint examples.
- Leakage between splits inflates scores and hides overfitting.
- Discipline includes never touching test data during development.
- RSIS3 relevance: passes keep new-slug files separate from verification, mirroring eval splits.

## Related
- [[wiki/decisions/test-set-discipline|Test Set Discipline]] — the discipline
- [[wiki/concepts/train-test-contamination|Train-Test Contamination]] — the failure
- [[wiki/concepts/eval-contamination|Eval Contamination]] — the eval variant
- [[wiki/decisions/model-selection-practice|model-selection-practice]] — note
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
- [[wiki/ai-ml/model-selection-strategies|Model Selection Strategies]] — existing graph context
