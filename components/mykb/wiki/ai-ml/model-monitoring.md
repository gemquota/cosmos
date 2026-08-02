---
type: "concept"
title: "Model Monitoring"
description: "Continuous observation of model quality, latency, cost, and safety in production"
tags: ["monitoring", "mlops", "observability", "production"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.evidentlyai.com/", "https://github.com/whylabs/whylogs"]
---

# Model Monitoring

## Summary
Model monitoring tracks production metrics so quality problems surface early. It matters because models degrade silently through drift, data changes, and misuse. Dashboards, alerts, and live evals turn raw traffic into actionable signals.

## Details
- **Metrics** — latency, cost, error rates, feedback signals, safety flags, and live eval scores.
- **Signals** — user feedback, golden-set runs, embedding drift, and refusal-rate changes.
- **Worked example** — a chatbot dashboard shows p95 latency, token spend, judge score trend, and moderation flag rate per day.
- **Response** — alerts trigger fallback routing, retraining, or prompt rollback via drift-detection-for-models.
- **mykb relevance** — personal systems benefit from lightweight monitoring of retrieval quality and response cost.
- **Worked example** — a chatbot dashboard shows p95 latency, token spend, judge score trend, and moderation flag rate per day.
- **Actionability** — every alert should name the decision (reroute, retrain, rollback) and the owner.
- **Signals** — user feedback, golden-set runs, embedding drift, and refusal-rate changes complement raw usage telemetry.

## Related
- [[wiki/testing/drift-detection-for-models|Drift Detection for Models]] — drift alerts
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — pipeline response
- [[wiki/ml-frameworks/token-accounting-and-cost|Token Accounting and Cost]] — cost metrics
- [[wiki/testing/runtime-observability-agent|Runtime Observability for Agents]] — agent telemetry
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — live regression checks
- [[wiki/ai-ml/embedding-regression|Embedding Regression]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
