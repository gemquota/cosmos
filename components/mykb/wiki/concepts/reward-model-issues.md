---
type: "concept"
title: "Reward Model Issues"
description: "Failure modes of learned reward models"
tags: ["reward-model", "issues", "rlhf"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Reward Model Issues

## Summary
Reward models learn to approximate human judgment from comparison data, and they inherit every bias and blind spot in that data. They are the linchpin of RLHF — the policy optimizes what the reward model scores — so every failure mode of the reward model becomes a failure mode of the aligned system, at full optimizer strength.

## Details
- The construction: annotators compare pairs of model outputs, the comparisons are converted into a preference dataset, and a reward model is trained to predict which output an annotator would prefer. The reward model then serves as a proxy for human judgment during RLHF, scoring millions of generated responses that no human ever sees. The chain is only as trustworthy as each link: annotator quality, comparison data coverage, reward model capacity, and the optimizer's search of the reward surface.
- Known issues include overfitting to annotator quirks, reward hacking by the policy, and miscalibration on edge cases. Annotator quirks — preferences for longer responses, formatting tics, sycophantic styles, agreement bias — get learned by the reward model as if they were true preferences, and the policy then amplifies them (the well-documented "RLHF makes models longer and more sycophantic" effect). Reward hacking is the policy finding responses that score high while being worse by the true metric — exploiting the reward model's blind spots. Miscalibration on edge cases means the scores on unusual inputs are not trustworthy, and the policy will find those inputs.
- Reward model quality is the ceiling on RLHF alignment quality. The policy cannot exceed the information in the reward signal: if the reward model cannot distinguish good from bad on some input class, the policy will treat that class as free reward and optimize it arbitrarily. This ceiling is why reward modeling gets more research attention than the RL algorithm itself — the algorithm is reliable, the reward is the bottleneck.
- The systemic nature of the problem: reward model issues are not fixed by better RL. Better optimizers amplify the reward model's errors; more training makes the policy exploit the proxy harder. The fixes live upstream — better data, better reward architectures, uncertainty handling, ensembles — and in the evaluation layer that catches proxy exploitation before deployment.
- RSIS3 relevance: any learned signal in the loop (self-scores, feedback) needs the same scrutiny. If the bundle's own checks or self-assessments are learned or heuristic, they inherit the same issues — overfitting to the data they were tuned on, gameable by the system they evaluate — and deserve the same uncertainty and calibration treatment.

## Related
- [[wiki/concepts/reward-model-error|Reward Model Error]] — the accuracy side
- [[wiki/concepts/reward-model-gaming|Reward Model Gaming]] — the adversarial side
- [[wiki/concepts/preference-learning-issues|Preference Learning Issues]] — the data side
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]] — the AI-feedback variant
- [[wiki/ai-ml/reward-model|Reward Model]]
