---
type: "concept"
title: "Context Distillation"
description: "Compressing a long context or retrieved knowledge into a model via fine-tuning"
tags: ["context-distillation", "distillation", "context", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Context Distillation

## Summary
Compressing a long context or retrieved knowledge into a model via fine-tuning

## Details
- Distills the reasoning and facts of long contexts into weights.
- Reduces inference-time context cost for repeated patterns.
- Distillation losses include faithfulness checks.
- Connects knowledge-distillation and context-compression.

## Related
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — teacher-student family
- [[wiki/prompt-engineering/context-compression|Context Compression]] — inference-time analog
- [[wiki/ai-ml/synthetic-data-generation|Synthetic Data Generation]] — data source
- [[wiki/ai-ml/catastrophic-forgetting-mitigation|Catastrophic Forgetting Mitigation]] — risk management
- [[wiki/ml-frameworks/long-context-techniques|Long-Context Techniques]] — alternative to length
