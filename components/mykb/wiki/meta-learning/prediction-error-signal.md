---
type: "concept"
title: "Prediction Error Signal"
description: "Neural and computational signal encoding the gap between expected and actual outcomes"
tags: ["prediction-error", "dopamine", "learning", "neuroscience"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Prediction Error Signal

## Summary
Prediction error is the difference between expected and received reward, and the brain broadcasts it via dopamine to drive learning. Positive errors reinforce; negative errors update expectations downward. It is the computational core of reinforcement learning and of curiosity-driven exploration.

## Details
- **Rescorla-Wagner legacy** — errors gate associative learning.
- **Dopamine** — phasic firing encodes reward prediction error.
- **Modern RL** — TD-learning algorithms use the same signal.
- **In mykb** — treat outcome surprises as update triggers, not noise.

## Related
- [[wiki/meta-learning/error-driven-learning|Error-Driven Learning]] — the learning rule
- [[wiki/meta-learning/reward-prediction-error|Reward Prediction Error]] — the reward version
- [[wiki/questions/surprise-and-learning|Surprise and Learning]] — the experience
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — the algorithm
