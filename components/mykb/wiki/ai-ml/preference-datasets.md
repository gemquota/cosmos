---
type: "concept"
title: "Preference Datasets"
description: "Paired or ranked examples that teach models which outputs humans prefer"
tags: ["datasets", "preferences", "alignment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Preference Datasets

## Summary
Preference datasets are paired or ranked examples that teach models which outputs humans prefer, forming the substrate of alignment methods. They matter because alignment is fundamentally about learning taste, and taste must be captured in data first. Quality issues in preference data transfer directly into reward hacking and misaligned behavior. Preference data is the taste the model will optimize, so curate it like code.

## Details
- **Definition** — a preference dataset records, for each prompt, which of two or more responses a judge preferred, with optional rationale.
- **Structure** — examples are typically chosen-versus-rejected pairs or full rankings across several responses.
- **Sources** — data comes from human-feedback-collection, AI feedback, and arena vote streams, each with different quality characteristics.
- **Uses** — preference data powers rlhf-stages, reward-model-training, and direct-preference-optimization.
- **Quality matters** — noisy or biased preferences teach reward models the wrong signal and increase reward-hacking risk downstream.
- **Worked example** — a team collects ten thousand pairwise votes on assistant answers, filters low-confidence votes, and trains a reward model on the cleaned set.
- **Failure modes** — annotator disagreement, reward hacking from easy-to-game examples, and distribution skew are the main risks.
- **Practical relevance** — preference datasets are the highest-leverage data asset in alignment, determining what models are trained to prefer.
- **Disagreement** — high-disagreement pairs are either noise or valuable signal; triage them explicitly.
- **Bias** — data collected from one user segment produces a model tuned to that segment.
- **Worked example** — a team filters low-confidence votes and keeps only pairs with strong annotator agreement.
- **Failure example** — a preference set with trivially distinguishable pairs teaches the model little about real choices.

## Related
- [[wiki/ai-ml/human-feedback-collection|Human Feedback Collection]] — collection methods
- [[wiki/ai-ml/reward-model-training|Reward Model Training]] — the reward supervision consumer
- [[wiki/ai-ml/direct-preference-optimization|Direct Preference Optimization]] — the reward-free consumer
- [[wiki/ai-ml/rlhf-stages|RLHF Stages]] — pipeline placement
- [[wiki/ai-ml/arena-ranking|Arena Ranking]] — a ranking source
