---
type: "concept"
title: "Reward Model Issues"
description: "Failure modes of learned reward models"
tags: ["reward-model", "issues", "rlhf"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reward Model Issues

## Summary
Reward models learn to approximate human judgment from comparison data, and they inherit every bias and blind spot in that data.

## Details
- Reward models learn to approximate human judgment from comparison data, and they inherit every bias and blind spot in that data.
- Known issues include overfitting to annotator quirks, reward hacking by the policy, and miscalibration on edge cases.
- Reward model quality is the ceiling on RLHF alignment quality.
- RSIS3 relevance: any learned signal in the loop (self-scores, feedback) needs the same scrutiny.

## Related
- [[wiki/concepts/reward-model-error|Reward Model Error]] — the accuracy side
- [[wiki/concepts/reward-model-gaming|Reward Model Gaming]] — the adversarial side
- [[wiki/concepts/preference-learning-issues|Preference Learning Issues]] — the data side
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]] — the AI-feedback variant
- [[wiki/ai-ml/reward-model|Reward Model]] — existing graph context
