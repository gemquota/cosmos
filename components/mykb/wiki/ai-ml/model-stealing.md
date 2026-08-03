---
type: "concept"
title: "Model Stealing"
description: "Extracting a proprietary model's capabilities, weights, or training data through API probing or side channels"
tags: ["model-stealing", "security", "apis"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Model Stealing

## Summary
Model stealing attacks reconstruct a model's behaviour (distillation) or expose its private data (extraction) through carefully chosen queries. They threaten the economics and confidentiality of hosted models.

## Details
- **Attack families** — three distinct goals: (1) *functional stealing* copies behaviour by training an imitation model on queried outputs; (2) *weight extraction* recovers exact parameters via equations over confidence scores; (3) *data extraction* pulls memorized verbatim text or private attributes out of the model.
- **Distillation stealing** — the most practical attack: query the API heavily and train a local imitation, often matching the original within a few percent on public benchmarks at a fraction of the serving cost. Query budgets in the tens of thousands to millions suffice depending on task difficulty.
- **Mitigations** — rate limits and output watermarking slow the attack but do not stop it; differential privacy on training data limits extraction; rounding logits or adding calibrated noise degrades weight-extraction equations; monitoring for high-volume, coverage-seeking query patterns flags active stealing campaigns.
- **Training-data extraction** — prompt models to regurgitate memorized verbatim text; success correlates with model capacity, duplication in pretraining data, and absence of deduplication, so extraction risk is highest for rare but repeated strings such as contact details or code identifiers.
- **Membership inference** — determine whether a sample was in training data by comparing confidence on that sample against the calibration of held-out items; it is the weakest but cheapest attack and is used to audit data leakage.
- **Side channels** — latency, token-level logits, and cache behaviour leak information; even black-box APIs expose enough signal for functional cloning.
- **RSIS3 relevance** — any hosted model RSIS3 relies on should be chosen with extraction risk and data sensitivity in mind; mykb should keep a model-selection checklist that weighs closed-model convenience against the exposure of internal prompts and wiki content passed to third-party endpoints.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — A related API-facing attack family
- [[wiki/ai-ml/data-poisoning|Data Poisoning]] — The training-side counterpart
- [[wiki/ai-ml/gpt-4|GPT-4]] — A frequent target of extraction research
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — The exposed surface
