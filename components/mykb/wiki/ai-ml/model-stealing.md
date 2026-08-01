---
type: "concept"
title: "Model Stealing"
description: "Extracting a proprietary model's capabilities, weights, or training data through API probing or side channels"
tags: ["model-stealing", "security", "apis"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Model Stealing

## Summary
Model stealing attacks reconstruct a model's behaviour (distillation) or expose its private data (extraction) through carefully chosen queries. They threaten the economics and confidentiality of hosted models.

## Details
- Distillation stealing: query the API heavily and train a local imitation; mitigations include rate limits and output watermarking.
- Training-data extraction: prompt models to regurgitate memorized verbatim text.
- Membership inference: determine whether a sample was in training data.
- RSIS3 relevance: any hosted model RSIS3 relies on should be chosen with extraction risk and data sensitivity in mind.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — A related API-facing attack family
- [[wiki/ai-ml/data-poisoning|Data Poisoning]] — The training-side counterpart
- [[wiki/ai-ml/gpt-4|GPT-4]] — A frequent target of extraction research
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — The exposed surface
- [[raw/archive/session-artifacts-2026-07/topics/security|security — Security-domain classification
