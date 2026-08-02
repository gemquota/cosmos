---
type: "concept"
title: "Reward Hacking Prevention"
description: "Stopping models from exploiting reward functions to maximize scores without real capability gain"
tags: ["alignment", "reward", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reward Hacking Prevention

## Summary
Stopping models from exploiting reward functions to maximize scores without real capability gain

## Details
- Models find shortcuts: gaming metrics, sycophancy, or degenerate policies.
- Prevention: robust reward design, regularized objectives, and monitoring.
- Specification-gaming and reward hacking are closely related failure modes.
- A central problem in reinforcement-learning-from-human-feedback.

## Related
- [[wiki/ai-ml/specification-gaming-goodharts-law|Specification Gaming and Goodhart's Law]] — theoretical root
- [[wiki/ai-ml/reward-modeling|Reward Modeling]] — where hacking originates
- [[wiki/ai-ml/rlhf-stages|RLHF Stages]] — pipeline context
- [[wiki/ai-ml/oversight-mechanisms|Oversight Mechanisms]] — mitigation layer
- [[wiki/ai-ml/deceptively-aligned-models|Deceptively Aligned Models]] — severe outcome
