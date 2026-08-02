---
type: "concept"
title: "Reward Modeling"
description: "Learning a scalar reward from human preferences to guide model optimization"
tags: ["reward-model", "preferences", "rlhf", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2212.03551", "https://arxiv.org/abs/2305.18290"]
---

# Reward Modeling

## Summary
Reward modeling learns a function that scores outputs the way humans would, from preference data. The reward model is the teacher signal for RLHF and a standalone ranking tool for filtering and evaluation. Reward models concentrate the alignment burden: if the reward is wrong, optimization amplifies the error.

## Details
- **Training** — pairwise comparisons are converted into a Bradley-Terry-style loss; the model learns to rank outputs, not just score them.
- **Uses** — RLHF reward, best-of-N selection, data filtering, and automated evaluation of candidate outputs.
- **Failure modes** — reward hacking, overfitting to annotator quirks, and Goodhart pressure as optimization intensifies.
- **Worked example** — a team trains a reward model on 50k human comparisons of support responses, then uses it to select the best of 8 sampled drafts.
- **Quality signals** — agreement with held-out human judgments measures reward-model reliability.
- **mykb relevance** — reward-model training and reward models are existing mykb topics; RSIS3's self-evaluation uses similar scoring.

## Related
- [[wiki/ai-ml/reward-model|Reward Model]] — existing reward model concept
- [[wiki/ai-ml/rlhf-stages|RLHF Stages]] — where the reward model fits
- [[wiki/ai-ml/preference-datasets|Preference Datasets]] — the training data
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — optimization failure
- [[wiki/ai-ml/human-feedback-collection|Human Feedback Collection]] — collecting preferences
- [[wiki/ai-ml/best-of-n-sampling|Best-of-N Sampling]] — using the reward to select
- [[wiki/ai-ml/rlhf|RLHF]] — RLHF context
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — judges vs reward models
