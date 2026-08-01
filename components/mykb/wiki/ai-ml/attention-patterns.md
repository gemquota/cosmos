---
type: "concept"
title: "Attention Patterns"
description: "Observed attention distributions that reveal what inputs a model focuses on and how information flows"
tags: ["attention-patterns", "interpretability", "attention"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Attention Patterns

## Summary
Attention patterns are the learned weight distributions of attention heads, often visualized as matrices or graphs. They show where the model looks — syntax, references, positions — and are a gateway to interpreting transformer behaviour.

## Details
- Patterns include induction, copy, positional, and function-word heads.
- Patterns alone underdetermine computation: they show focus, not meaning.
- Used in pruning (redundant heads) and in failure analysis for RAG systems.
- RSIS3 relevance: anomalous attention on injected or retrieved text can flag adversarial content.

## Related
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]] — The operation behind the patterns
- [[wiki/ai-ml/multi-head-attention|Multi-Head Attention]] — Where distinct patterns arise
- [[wiki/ai-ml/interpretability|Interpretability]] — The field that studies patterns
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — Patterns as circuit evidence
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — Attention on retrieved passages
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Pattern analysis supports output diagnostics
