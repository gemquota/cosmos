---
type: "concept"
title: "Self-Evaluation"
description: "A model or agent scoring its own outputs or progress"
tags: ["self-evaluation", "agents", "metacognition", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2305.20050", "https://arxiv.org/abs/2303.11366"]
---

# Self-Evaluation

## Summary
Self-evaluation is any mechanism by which an AI system assesses its own outputs, confidence, or progress, from token-level self-consistency to agentic reflection scores. It is the load-bearing component of self-improvement loops and a known source of bias when unverified.

## Details
- **Forms** — self-consistency (majority vote), verifier models, self-ratings on rubrics, and process supervision.
- **Evidence** — models can verify others' solutions better than their own; self-ratings correlate weakly with ground truth.
- **Use in loops** — evaluation feeds the revision step; poor evaluation caps the loop's ceiling.
- **Calibration link** — self-evaluation quality is a calibration problem, measurable with confidence-vs-correctness curves.
- **RSIS3 relevance** — pulse self-scores are treated as telemetry, not ground truth; external check-practices and tests arbitrate.

- **Measurement** — self-evaluation quality is measured by calibration (do self-scores track outcomes?) and ranking consistency (do self-scores order outputs the same way judges do?).
- **Design** — rubrics with anchored examples improve reliability; vague 'rate this 1–10' prompts produce noisy scores.
- **Gatekeeping use** — self-evaluation can gate releases (only ship outputs scoring above threshold), but only if the self-score is externally calibrated; otherwise the gate is theater.
- **Failure mode** — systems game their own evaluators when the self-score is a reward; the evaluator must be outside the optimization loop.
- **Evidence** — models verify others' work better than their own, so self-evaluation benefits from role separation (evaluate a draft as if it were someone else's).

- **Relation to calibration** — self-evaluation and calibration are the same discipline at different granularities: calibration checks confidence over many judgments, self-evaluation checks scores over whole outputs; both need external ground truth to be meaningful.

## Related
- [[wiki/pulses/self-ratings|Self-Ratings]] — unchecked self-evaluation
- [[wiki/pulses/self-reports-vs-measures|Self-Reports vs Measures]] — why self-eval can lie
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — quantified self-eval
- [[wiki/concepts/calibration|Calibration]] — measuring its reliability
- [[wiki/pulses/self-benchmarking|Self-Benchmarking]] — internal vs external benchmarks
- [[wiki/concepts/telemetry|Workspace Telemetry]] — RSIS3 treats self-reports as data
