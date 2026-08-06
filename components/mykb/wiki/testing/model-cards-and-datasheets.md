---
type: "concept"
title: "Model Cards and Datasheets"
description: "Structured documentation of model behavior, training data, and limitations"
tags: ["model-cards", "documentation", "governance", "transparency"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Model Cards and Datasheets

## Summary
Model cards and datasheets are structured documentation that accompanies machine-learning artifacts: a model card describes a model's intended use, evaluation results, and known limits; a datasheet describes a dataset's provenance, composition, and collection process. Together they make deployment decisions auditable and informed.

## Details
- **Model card contents** — intended and out-of-scope uses, training and evaluation data, performance by subgroup, fairness metrics, and known limitations; the card makes claims falsifiable by tying them to specific evaluations.
- **Datasheet contents** — how and why the data was collected, who the subjects are, what preprocessing was applied, known gaps, and intended uses; provenance enables reproduction and catches hidden biases.
- **Auditability** — documentation turns a model release into a decision record: regulators, downstream users, and reviewers can check what was measured and what was not.
- **Living documents** — cards and datasheets should be updated when the model or dataset changes; a stale card is worse than none because it certifies outdated claims.
- **For mykb** — documentation practice sits alongside provenance-and-disclosure and model versioning so every model entry carries its measured behavior with it.
- **Worked example** — a speech model ships with a card reporting accuracy overall and by accent; the datasheet records that training audio came from volunteer recordings under a known license; both files travel with the model in the registry.
- **Relationship to governance** — responsible-ai frameworks recommend cards and datasheets as a minimum transparency bar, and bias-and-fairness evaluations are the substance the card reports.

- **Template discipline** — use a fixed section template so cards are comparable across releases; free-form documentation drifts and makes the promised metrics impossible to check, which is why templates are part of the registry contract.
## Related
- [[wiki/testing/responsible-ai-principles|Responsible AI Principles]] — value base
- [[wiki/testing/ai-governance-frameworks|AI Governance Frameworks]] — policy context
- [[wiki/ai-ml/provenance-and-disclosure|Provenance and Disclosure]] — disclosure practice
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — versioned docs
- [[wiki/testing/bias-and-fairness-eval|Bias and Fairness Evaluation]] — documented metrics
- [[wiki/data-storage/data-lineage-and-provenance|Data Lineage and Provenance]] — dataset-side record
