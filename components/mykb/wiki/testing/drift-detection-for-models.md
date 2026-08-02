---
type: "concept"
title: "Drift Detection for Models"
description: "Detecting when model behavior or the data distribution shifts away from what was validated"
tags: ["drift", "monitoring", "mlops", "detection"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.evidentlyai.com/", "https://arxiv.org/abs/2210.01779"]
---

# Drift Detection for Models

## Summary
Drift detection watches model inputs, outputs, and performance metrics for statistically significant change. It matters because deployed models degrade as users and data evolve. Early detection triggers retraining, rerouting, or rollback before quality visibly collapses.

## Details
- **Drift types** — data drift (input distribution), concept drift (input-output relationship), and model drift (behavior change).
- **Methods** — PSI/KS tests on features, embedding-distance monitoring, and live eval on golden-test-sets.
- **Worked example** — an embedding-based search logs query embeddings; when their distribution shifts, an alert triggers index re-embedding review.
- **Response** — thresholds route traffic to a fallback model while retraining happens.
- **mykb relevance** — knowledge drift (topics changing over time) is a first-class signal for a personal KB.
- **Alerting** — thresholds with severity tiers route to retraining, fallback routing, or manual review.
- **Worked example** — an embedding search logs query embeddings; a distribution shift triggers index re-embedding review before quality visibly drops.
- **Methods** — PSI and KS tests on features, embedding-distance monitoring, and live eval on golden-test-sets catch shifts early.

## Related
- [[wiki/ai-ml/embedding-regression|Embedding Regression]] — embedding drift
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — regression detection
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — pipeline response
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — retraining flow
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — live eval data
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
- [[wiki/testing/traces-spans|Traces and Spans]] — related concept in this cluster
