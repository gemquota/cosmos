---
type: "concept"
title: "Reward Model"
description: "A model trained to score the quality of LLM outputs, typically from human preference comparisons, used in RLHF"
tags: ["reward-model", "rlhf", "alignment", "preferences"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Reward Model

## Summary
A reward model learns to predict which of two outputs humans prefer, turning messy preference data into a scalar score. RLHF uses it as the optimization target for policy training.

## Details
- Typically initialized from the SFT model with a classification head over pairwise comparisons.
- Reward models inherit and amplify label noise, bias, and overconfidence.
- Reward hacking — the policy exploiting reward-model blind spots — is the central RLHF failure mode.
- RSIS3 relevance: preference data from pulse outcomes could train a mykb-local reward model for L3 alignment.

## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The training loop reward models enable
- [[wiki/ai-ml/ppo|PPO]] — The optimizer that uses the reward signal
- [[wiki/ai-ml/dpo|DPO]] — An alternative that skips the reward model
- [[wiki/ai-ml/sycophancy|Sycophancy]] — A bias reward models can encode
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — The umbrella family
