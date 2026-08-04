---
type: "concept"
title: "LLM-as-Judge"
description: "Using a language model to score or compare outputs instead of human annotation"
tags: ["evaluation", "judging", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# LLM-as-Judge

## Summary
LLM-as-judge uses a language model to score or compare outputs instead of human annotation, making evaluation fast and scalable. It matters because human evaluation does not scale to the volume of modern model development, and judge models approximate human judgment well enough for most decisions. The catch is that judges inherit preferences and biases that must be audited. Judge models are tools whose biases must be measured, not assumed away.

## Details
- **Definition** — a judge model evaluates outputs either pointwise on a rubric or pairwise by choosing the better response.
- **Modes** — pointwise scoring rates quality against criteria; pairwise comparison picks winners, which can feed preference data and rankings.
- **Speed and scale** — judge evaluation runs automatically across thousands of examples, enabling continuous regression testing.
- **Bias** — judges favor their own style, length, and format patterns; position bias and self-preference are documented effects.
- **Calibration** — calibration checks against human ratings and periodic audits keep judge scores trustworthy.
- **Worked example** — a team scores a candidate model against a golden set with a judge rubric, then spot-checks one hundred samples with human raters.
- **Failure modes** — judge drift across model updates, sycophantic scoring, and rubric ambiguity produce unreliable ratings.
- **Tooling** — judge evaluation is core to evals-harness workflows and arena-ranking alternatives.
- **Practical relevance** — LLM-as-judge is the workhorse of modern evaluation pipelines, bridging human taste and automated testing.
- **Position bias** — swapping answer order and averaging responses reduces systematic preference effects.
- **Judge choice** — a strong judge model generally agrees more with humans than a weak one.
- **Worked example** — a team validates judge scores against a human-labeled subset each quarter.
- **Failure example** — a judge that rewards longer answers inflates verbose models that users dislike.

## Related
- [[wiki/ai-ml/rubric-based-evaluation|Rubric-Based Evaluation]] — structured judging
- [[wiki/ai-ml/pairwise-comparisons|Pairwise Comparisons]] — the comparison mode
- [[wiki/ai-ml/arena-ranking|Arena Ranking]] — crowd-based ranking
- [[wiki/ai-ml/calibration-and-confidence|Calibration and Confidence]] — judge reliability
- [[wiki/testing/evals-harness|Evals Harness]] — evaluation integration
