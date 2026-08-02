---
type: "concept"
title: "Reward Prediction Error"
description: "Difference between expected and received reward, the signal driving reinforcement learning"
tags: ["reward", "prediction", "reinforcement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Reinforcement_learning", "https://dictionary.apa.org/reward-prediction-error"]
---

# Reward Prediction Error

## Summary

Reward Prediction Error — Difference between expected and received reward, the signal driving reinforcement learning.

## Details

- Reward prediction error (RPE) is the difference between received and expected reward. Schultz's recordings of midbrain dopamine neurons showed phasic firing for unexpected rewards, suppression when expected rewards are omitted, and transfer to reward-predicting cues — the signature of a temporal-difference learning signal.
- RPEs drive learning in model-free reinforcement learning: values update toward observed outcomes, so behavior adapts to changing contingencies. Positive RPEs reinforce, negative RPEs punish and promote behavioral change.
- Worked example: a slot machine pays unexpectedly → large positive RPE, dopamine burst, approach reinforced; the same win after many consistent wins produces little RPE — the brain learns expectations, not raw payoffs.
- Clinical relevance: blunted or aberrant RPE signaling appears in depression, addiction, and schizophrenia; computational psychiatry models use RPE parameters as biomarkers.
- mykb relevance: reward prediction error is the neural counterpart of the wiki's prediction-error-signal and error-driven-learning entries.

## Related

- [[wiki/concepts/prediction-error-signal|Prediction Error Signal]] — formal abstraction
- [[wiki/meta-learning/model-free-learning|Model-Free Learning]] — algorithmic home
- [[wiki/meta-learning/novelty-seeking|Novelty Seeking]] — related dopaminergic drive
- [[wiki/ai-ml/reward-model|Reward Model]] — existing wiki article
- [[wiki/concepts/temporal-difference-learning|Temporal Difference Learning]] — existing wiki article
