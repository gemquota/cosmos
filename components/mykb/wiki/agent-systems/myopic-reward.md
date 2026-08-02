---
type: "concept"
title: "Myopic Reward"
description: "Rewards that depend only on current-step outcomes"
tags: ["myopic", "reward", "rl"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Myopic Reward

## Summary
Myopic reward shapes agents to value only immediate outcomes, e.g., current-timestep return without discounting far futures.

## Details
- Myopic reward shapes agents to value only immediate outcomes, e.g., current-timestep return without discounting far futures.
- It can prevent long-horizon goal pursuit — both the intended benefit and the failure mode.
- Trade-offs with task competence are poorly understood.
- RSIS3 relevance: step-wise check outcomes are a myopic reward for workers.

## Related
- [[wiki/agent-systems/discount-factor-ai|Discount Factor in AI]] — the tuning knob
- [[wiki/agent-systems/myopia-ai|Myopia in AI]] — the property
- [[wiki/agent-systems/horizon-length|Horizon Length]] — the window
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — the side effects
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — the full treatment of this theme
- [[wiki/ai-ml/reward-model|Reward Model]] — existing graph context
