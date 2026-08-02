---
type: "concept"
title: "Preference Learning Issues"
description: "Why learning preferences from data is hard"
tags: ["preference-learning", "issues", "rlhf"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Preference Learning Issues

## Summary
Preference learning issues include noisy labels, annotator disagreement, framing sensitivity, and unrepresentative annotator pools.

## Details
- Preference learning issues include noisy labels, annotator disagreement, framing sensitivity, and unrepresentative annotator pools.
- Each issue biases the learned preference model in ways policy optimization amplifies.
- Robust elicitation designs and uncertainty modeling mitigate but don't solve them.
- RSIS3 relevance: feedback loops in the workspace face the same data-quality questions.

## Related
- [[wiki/concepts/preference-elicitation|Preference Elicitation]] — the method
- [[wiki/concepts/preference-falsification|Preference Falsification]] — the data corruption
- [[wiki/concepts/preference-uncertainty|Preference Uncertainty]] — the epistemic residue
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — the downstream
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — existing graph context
