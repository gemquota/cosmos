---
type: "concept"
title: "Attention Patterns"
description: "Observed attention distributions that reveal what inputs a model focuses on and how information flows"
tags: ["attention-patterns", "interpretability", "attention"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Attention Patterns

## Summary
Attention patterns are the learned weight distributions of individual attention heads, often visualized as matrices or graphs. They show *where* a model looks — which tokens, positions, or references receive weight — and they are a gateway to interpreting transformer behavior, from syntax to induction to retrieval in RAG systems.

## Details
- Mechanism: at each layer, an attention head computes a probability distribution over key positions for every query position; that distribution is the head's attention pattern. Over training, heads specialize into recognizable types: induction heads (copy a previous occurrence of the current token and advance one), copy heads, positional heads (attend to fixed offsets), and function-word or separator heads that route information around the sentence structure. Patterns are cheap to extract (a forward pass records them) and are among the most studied artifacts in interpretability.
- Concrete examples: induction heads explain how models continue sequences like "a b ... a" by finding the earlier instance and attending to the token after it; in a retrieval-augmented system, examining which tokens of the retrieved passage receive attention when the model answers can reveal whether the answer is grounded or hallucinated — low attention on the relevant passage is a red flag; pruning research removes redundant heads whose patterns are duplicates, shrinking models with minimal loss; RAG failure analysis uses attention on injected or retrieved text to flag adversarial content that the model "paid attention to" in the wrong way.
- Failure modes: the classic failure is over-reading patterns: attention shows *focus*, not *meaning* — a head can attend heavily to a token and the computation can still ignore it (or vice versa), so attention weights alone underdetermine the model's behavior. Patterns are also layer- and context-dependent: the same head shows different patterns across inputs, and aggregating patterns across contexts hides the variance. Claims like "the model looked here, therefore it reasoned here" are the interpretability equivalent of correlation-versus-causation.
- Operational tradeoffs: pattern analysis is a fast, low-cost lens into model internals — no training required, works on any transformer — and its tradeoff is that it is suggestive rather than conclusive; causal methods (activation patching, ablation) are needed to confirm what a pattern does. The practice rules: use patterns for hypothesis generation and triage, confirm with interventions, and treat pattern-based claims as requiring causal verification. RSIS3 relevance: anomalous attention on injected or retrieved text can flag adversarial content — a runtime signal for the harness's RAG layer, but one that must be validated causally before it becomes a control.

## Related
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]] — The operation behind the patterns
- [[wiki/ai-ml/multi-head-attention|Multi-Head Attention]] — Where distinct patterns arise
- [[wiki/ai-ml/interpretability|Interpretability]] — The field that studies patterns
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — Patterns as circuit evidence
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — Attention on retrieved passages
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Pattern analysis supports output diagnostics
