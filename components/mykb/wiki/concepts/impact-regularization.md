---
type: "concept"
title: "Impact Regularization"
description: "Penalizing agents for large or irreversible impact"
tags: ["impact", "regularization", "rl"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Impact Regularization

## Summary
Impact regularization adds a penalty term discouraging large or irreversible changes to the environment.

## Details
- Impact regularization adds a penalty term discouraging large or irreversible changes to the environment.
- It implements conservatism inside the reward function.
- Calibration is delicate: too weak, side effects persist; too strong, the agent becomes passive.
- RSIS3 relevance: staged passes with bounded file scopes are an impact-regularized process.

## Related
- [[wiki/concepts/impact-measures|Impact Measures]] — the metric behind the penalty
- [[wiki/concepts/side-effects-problem|Side Effects Problem]] — the target
- [[wiki/concepts/restraint-training|Restraint Training]] — the training-time cousin
- [[wiki/concepts/conservatism-ai|Conservatism in AI Design]] — the stance
- [[wiki/concepts/mild-optimization|Mild Optimization]] — the full treatment of this theme
- [[wiki/concepts/calibration|Calibration]] — existing graph context
