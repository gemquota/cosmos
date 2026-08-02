---
type: "concept"
title: "Preference Elicitation"
description: "Inferring what people want from their choices and feedback"
tags: ["preferences", "elicitation", "rlhf", "alignment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Preference_elicitation", "https://arxiv.org/abs/1706.03741"]
---

# Preference Elicitation

## Summary
Preference elicitation is the process of learning human preferences from comparisons, ratings, or behavior. In RLHF, human preference pairs train a reward model that then steers the policy — making elicitation quality the ceiling on alignment quality.

## Details
- **Methods** — pairwise comparisons, rankings, Likert ratings, and behavioral observation (imitation, choice data).
- **RLHF pipeline** — preference data → reward model → policy optimization; noise in the first step propagates.
- **Bias sources** — annotator disagreement, framing effects, and preference falsification distort the signal.
- **RLAIF extension** — AI-generated comparisons scale elicitation but inherit model biases.
- **RSIS3 parallel** — preference elicitation is how the workspace's practices evolved: check failures and review feedback update the rules.

## Related
- [[wiki/concepts/preference-uncertainty|Preference Uncertainty]] — noise in what was learned
- [[wiki/concepts/preference-learning-issues|Preference Learning Issues]] — bias taxonomy
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]] — AI-assisted elicitation
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — downstream of elicitation
- [[wiki/concepts/preference-falsification|Preference Falsification]] — lying about preferences
- [[wiki/concepts/calibration|Calibration]] — elicitor reliability
- [[wiki/concepts/utility-functions|Utility Functions]] — objective structure in the existing graph
