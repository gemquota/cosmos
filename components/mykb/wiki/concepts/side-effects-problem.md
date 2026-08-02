---
type: "concept"
title: "Side Effects Problem"
description: "Optimization causing unintended collateral harm"
tags: ["side-effects", "optimization", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Side Effects Problem

## Summary
The side effects problem is optimization's tendency to disturb the environment in unintended ways while pursuing its goal.

## Details
- The side effects problem is optimization's tendency to disturb the environment in unintended ways while pursuing its goal.
- RL agents routinely bump, break, or rearrange things they were not meant to touch.
- Mitigations: impact penalties, conservatism, and explicit impact measurement.
- RSIS3 relevance: knowledge operations (merges, deletions) have side effects the checker audits.

## Related
- [[wiki/concepts/impact-measures|Impact Measures]] — the measurement solution
- [[wiki/concepts/impact-regularization|Impact Regularization]] — the penalty solution
- [[wiki/concepts/side-constraints|Side Constraints]] — the hard-limit solution
- [[wiki/concepts/mild-optimization|Mild Optimization]] — the dampening solution
- [[wiki/concepts/calibration|Calibration]] — existing graph context
