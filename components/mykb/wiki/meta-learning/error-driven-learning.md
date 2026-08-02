---
type: "concept"
title: "Error-Driven Learning"
description: "Learning by adjusting predictions or behavior in proportion to errors"
tags: ["learning", "errors", "prediction"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Error-driven_learning", "https://dictionary.apa.org/error-driven-learning"]
---

# Error-Driven Learning

## Summary

Error-Driven Learning — Learning by adjusting predictions or behavior in proportion to errors.

## Details

- Error-driven learning is the family of mechanisms that change a system based on the difference between predicted and actual outcomes. It covers delta-rule and backpropagation learning in connectionist networks, temporal-difference learning in reinforcement learning, and the brain's use of prediction errors (e.g., dopamine signals).
- The core insight: learning rate scales with surprise, and errors are information, not just failures. When predictions match outcomes, nothing changes; when they differ, representations and policies update in the direction of reducing future error.
- Worked example: a model predicts a 10-minute commute; the drive takes 25 minutes. The prediction error (15 minutes) updates the estimate; repeated errors calibrate the model to reality, and calibrated predictions stop generating large errors.
- Design consequences: feedback must be timely and informative for error-driven learning to work; rewards and punishments are error signals in behavior. Error-driven accounts complement deliberate, rule-based learning.
- mykb relevance: belief-updating and calibration practice are error-driven learning at the knowledge level — predictions logged, errors fed back.

## Related

- [[wiki/meta-learning/reward-prediction-error|Reward Prediction Error]] — the neural signal
- [[wiki/concepts/prediction-error-signal|Prediction Error Signal]] — formal signal
- [[wiki/memory/belief-updating|Belief Updating]] — belief-level analogue
- [[wiki/concepts/predictive-coding|Predictive Coding]] — perceptual analogue
- [[wiki/ai-ml/continual-learning|Continual Learning]] — existing wiki article
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — existing wiki article
