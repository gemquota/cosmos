---
type: "concept"
title: "Calibration and Confidence"
description: "Aligning model-reported confidence with actual correctness rates"
tags: ["calibration", "confidence", "uncertainty", "evaluation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2203.02155", "https://arxiv.org/abs/2307.05789"]
---

# Calibration and Confidence

## Summary
Calibration is the alignment between a model's reported confidence and its true accuracy: a well-calibrated model that says 80% is right 80% of the time. LLMs are systematically overconfident, especially on hard or unfamiliar questions. Calibration measurement turns confidence into a usable decision signal.

## Details
- **Measurement** — bin predictions by confidence and compare with accuracy; reliability diagrams and expected calibration error (ECE) quantify gaps.
- **Sources of overconfidence** — softmax temperatures, RLHF-induced sycophancy, and unfamiliarity all inflate confidence.
- **Fixes** — temperature scaling at inference, verbalized-confidence prompts, self-consistency agreement rates, and deferral rules.
- **Worked example** — a triage agent reports confidence per ticket; after calibration analysis, it defers anything below 0.7 to a human instead of guessing.
- **In agents** — confidence gates feed escalation and human-in-the-loop decisions; they are only as good as the calibration behind them.
- **mykb relevance** — calibration is an existing mykb concept; RSIS3 uses confidence signals in its evaluation phases.

## Related
- [[wiki/concepts/calibration|Calibration]] — existing calibration concept
- [[wiki/agent-systems/escalation-handling|Escalation Handling]] — confidence-driven escalation
- [[wiki/llm-agents/self-consistency-voting|Self-Consistency Voting]] — agreement as confidence
- [[wiki/prompt-engineering/temperature-sampling|Temperature Sampling]] — temperature and confidence
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — judge calibration
- [[wiki/ai-ml/model-evaluation-metrics|Model Evaluation Metrics]] — measuring correctness
- [[wiki/agent-systems/human-in-the-loop-approvals|Human-in-the-Loop Approvals]] — deferral on low confidence
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — refusing when unsure
