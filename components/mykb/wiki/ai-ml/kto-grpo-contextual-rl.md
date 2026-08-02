---
type: "concept"
title: "KTO, GRPO, and Contextual RL"
description: "Alternative alignment objectives: KTO uses binary feedback, GRPO drops the critic network"
tags: ["alignment", "training", "preferences"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# KTO, GRPO, and Contextual RL

## Summary
Alternative alignment objectives: KTO uses binary feedback, GRPO drops the critic network

## Details
- KTO optimizes from desirable/undesirable signals without pairs.
- GRPO uses group-relative advantage, removing the value model.
- These methods simplify and stabilize RLHF pipelines.
- Dominated by direct-preference-optimization in adoption debates.

## Related
- [[wiki/ai-ml/direct-preference-optimization|Direct Preference Optimization]] — primary alternative
- [[wiki/ai-ml/reinforcement-learning-from-human-feedback|Reinforcement Learning from Human Feedback]] — family
- [[wiki/ai-ml/preference-optimization|Preference Optimization]] — objective family
- [[wiki/ai-ml/rlhf-stages|RLHF Stages]] — pipeline context
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — shared risk
