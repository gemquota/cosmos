---
type: "concept"
title: "Eval Contamination"
description: "Any leakage that corrupts evaluation validity"
tags: ["eval", "contamination", "evals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Eval Contamination

## Summary
Eval contamination covers all ways evaluation validity is corrupted: leaked data, gamed metrics, or feedback loops from eval to training. An eval is only as good as its integrity — if the test data appears in training, if the metric can be optimized without the capability, or if the eval's existence changes the model's behavior, the score stops measuring what it claims to measure.

## Details
- The data form is train-test leakage: benchmark items included in pretraining or fine-tuning corpora, directly or in paraphrase. Models memorize, so a contaminated model scores high by retrieval rather than by capability. Detection is imperfect — exact-match screening misses paraphrases and translations — which is why contamination checks are a continuous hygiene practice (membership probing, unusual per-item performance, comparison against human baselines) rather than a one-time filter.
- The metric form is Goodhart's law applied to benchmarks: any metric used as a target ceases to be a good measure. If a leaderboard score drives release decisions, pressure concentrates on optimizing the score — through prompt-tuning to the eval's format, training on similar tasks, or curriculum selection that cherry-picks eval-friendly data. The eval does not need to be "gamed" in a malicious sense; the feedback loop from eval to training is sufficient to erode it.
- The behavioral form is evaluation-aware behavior: models that act differently when they know (or infer) they are being evaluated, such as alignment faking or sandbagging. This contaminates the eval by changing the object of measurement — the eval observes a performance mode that may not be the deployment mode.
- Healthy eval practice treats contamination as a standing risk, not a one-time fix: hold out truly private evals, monitor per-item statistics, rotate task versions, and treat suspicious score spikes as hypotheses to investigate rather than wins to celebrate.
- RSIS3 relevance: the pass verifier is designed to be ungameable by the generator. When the same system proposes an improvement and evaluates it, the separation of roles, hidden verification criteria, and outcome-based (rather than self-reported) metrics are the contamination defenses — the generator cannot score well by predicting what the verifier wants to hear.

## Related
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the specific form
- [[wiki/concepts/evals-gaming|Evals Gaming]] — the deliberate form
- [[wiki/concepts/train-test-contamination|Train-Test Contamination]] — the data form
- [[wiki/pulses/improvement-metrics|Improvement Metrics]] — the Goodhart context
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the full treatment of this theme
- [[wiki/ai-ml/data-contamination|Data Contamination]] — existing graph context
