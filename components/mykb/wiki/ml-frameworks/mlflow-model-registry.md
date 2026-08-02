---
type: "concept"
title: "MLflow Model Registry"
description: "Central catalog for versioned models with stage transitions from staging to production"
tags: ["registry", "mlops", "model-management"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# MLflow Model Registry

## Summary
Central catalog for versioned models with stage transitions from staging to production

## Details
- Stores model artifacts, metadata, and lineage alongside training runs.
- Stage transitions (staging, production, archived) gate deployments.
- Integrates with CI/CD so only validated models move forward.
- Complements experiment tracking with a governance layer.

## Related
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — concept it implements
- [[wiki/ml-frameworks/runs|Experiment Runs]] — source of registered models
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — pipeline that promotes models
- [[wiki/testing/drift-detection-for-models|Drift Detection for Models]] — monitoring after promotion
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — validation before promotion
