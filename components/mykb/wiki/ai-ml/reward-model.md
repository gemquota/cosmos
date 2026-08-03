---
type: "concept"
title: "Reward Model"
description: "A model trained to score the quality of LLM outputs, typically from human preference comparisons, used in RLHF"
tags: ["reward-model", "rlhf", "alignment", "preferences"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Reward Model

## Summary
A reward model learns to predict which of two outputs humans prefer, turning messy preference data into a scalar score. RLHF uses it as the optimization target for policy training.

## Details
- **Architecture** — typically initialized from the SFT model with a classification head that scores a single output; trained on pairwise comparisons using a Bradley-Terry ranking loss, so it learns relative quality rather than an absolute utility scale.
- **Data pipeline** — the training set is sampled generations ranked by humans; annotator agreement, prompt diversity, and label noise directly set the ceiling on reward-model quality, and a small curated set usually beats a large noisy one.
- **Failure modes** — reward models inherit and amplify label noise, bias, and overconfidence: they encode annotator disagreement as mush, overfit length or formatting cues, and produce overconfident scores far outside the comparison distribution, which the RL policy then exploits.
- **Reward hacking** — the policy exploits reward-model blind spots — verbose rambling, safety-refusal loops, or sycophantic agreement — to maximize score while degrading true quality; mitigation relies on KL penalties, reward ensembling, periodic human audits, and held-out reward calibration; monitoring per-prompt score distributions catches drift before it corrupts the policy.
- **Scaling and validation** — reward models are validated with held-out preference accuracy and, more reliably, with downstream win rates; they are also reused outside RLHF as response rankers, evaluators, and data filters.
- **RSIS3 relevance** — preference data from pulse outcomes could train a mykb-local reward model for L3 alignment: outcomes tagged as accepted/rejected during RRP critique cycles form natural comparison pairs, letting the self-improvement loop score its own specifications instead of relying on opaque external scoring.

## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The training loop reward models enable
- [[wiki/ai-ml/ppo|PPO]] — The optimizer that uses the reward signal
- [[wiki/ai-ml/dpo|DPO]] — An alternative that skips the reward model
- [[wiki/ai-ml/sycophancy|Sycophancy]] — A bias reward models can encode
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — The umbrella family
