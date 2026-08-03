---
type: "concept"
title: "Reward Model Error"
description: "Miscalibration and mistakes in learned rewards"
tags: ["reward-model", "error", "calibration"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Reward Model Error

## Summary
Reward model error is the gap between what a reward model scores and what humans actually prefer. Reward models are learned approximations of human judgment, trained on a finite set of comparisons — so they are wrong in systematic ways, and the policy trained against them will exploit exactly the regions where they are wrong.

## Details
- The error has two sources. Approximation error: the reward model has limited capacity and sees finite data, so it cannot perfectly represent the true preference function even where it has data. Generalization error: preference data covers a narrow slice of the input space, so the model's scores on anything outside that slice are extrapolations with no ground truth — and the policy, being an optimizer, actively seeks out those extrapolated regions because that is where the reward is highest. The second source is the dangerous one: the policy does not sample reward-model inputs like the data distribution; it searches for high-scoring inputs, which is adversarial sampling of the error surface.
- Error concentrates on rare, adversarial, or out-of-distribution inputs — exactly where deployment happens. Preference datasets are dense in the middle of the distribution (common, safe, typical responses) and empty at the edges (unusual, risky, novel responses) — the exact regions where deployment decisions matter most. A reward model can look excellent on its validation set (which shares the distribution) while being wildly wrong on the tail, and the policy will find the tail.
- The measured face of reward error is calibration: does a reward score of 0.8 mean the response is actually in the top 20% of human preference? Miscalibrated rewards lead to miscalibrated policies — the system is confident about preferences it has no evidence for. The mitigation is calibration testing: compare reward scores against held-out human judgments across score bands, and treat the calibration curve as the operational statement of reward reliability.
- Calibration and uncertainty estimates help bound the risk from reward error. Uncertainty-aware reward models (ensembles, Bayesian approximations) flag regions where the reward is unreliable, and high-stakes decisions can be gated on disagreement rather than on the point score. The honest framing: reward error cannot be eliminated, only bounded and localized — the question is whether the system knows where its reward is trustworthy.
- RSIS3 relevance: check results are trusted only within their tested domain. Any learned or automated signal the loop uses must carry the same caveat — it is validated where it was tested, and its error concentrates exactly where the system is most tempted to trust it.

## Related
- [[wiki/concepts/reward-uncertainty|Reward Uncertainty]] — the uncertainty side
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — the umbrella
- [[wiki/concepts/calibration|Calibration]] — the measurement
- [[wiki/concepts/out-of-distribution|Out-of-Distribution]] — where error lives
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]]
