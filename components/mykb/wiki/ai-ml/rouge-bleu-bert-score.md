---
type: "concept"
title: "ROUGE, BLEU, and BERTScore"
description: "Classic n-gram and embedding-based metrics for evaluating generated text"
tags: ["metrics", "evaluation", "nlp"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# ROUGE, BLEU, and BERTScore

## Summary
Classic n-gram and embedding-based metrics for evaluating generated text

## Details
- ROUGE and BLEU measure n-gram overlap; BERTScore uses embeddings.
- Cheap and reproducible but weak on semantic equivalence.
- LLM-as-judge increasingly supplements or replaces them.
- Still standard for summarization and translation baselines.

## Related
- [[wiki/ai-ml/model-evaluation-metrics|Model Evaluation Metrics]] — metric family
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — semantic alternative
- [[wiki/agent-systems/translation-agents|Translation Agents]] — typical user
- [[wiki/agent-systems/summarization-agents|Summarization Agents]] — typical user
- [[wiki/ai-ml/rubric-based-evaluation|Rubric-Based Evaluation]] — structured judging
