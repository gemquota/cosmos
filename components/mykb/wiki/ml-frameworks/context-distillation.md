---
type: "concept"
title: "Context Distillation"
description: "Compressing a long context or retrieved knowledge into a model via fine-tuning"
tags: ["context-distillation", "distillation", "context", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Context Distillation

## Summary

Context distillation compresses the knowledge contained in a long context or a retrieved document set into a model's weights through fine-tuning. Instead of shipping the full context with every request, the model internalizes the relevant information once. The technique matters because it can reduce token costs, latency, and prompt complexity while retaining task performance.

## Details

- **Definition** — context distillation trains a model on input-output pairs where the inputs are distilled representations of what a longer context would provide.
- **Mechanism** — a teacher (often the same model) answers questions given a long context; the student is fine-tuned to answer from a compressed summary or no context.
- **Motivation** — long contexts cost tokens and slow inference; distillation moves that cost to a one-time training run.
- **Relationship to knowledge distillation** — it is a specialization of knowledge distillation where the knowledge is the content of a context rather than a general capability.
- **Use cases** — document question answering, codebase assistants, and persona systems can internalize a corpus once and serve without retrieval.
- **Tradeoffs** — distilled models may lose detail and freshness; retrieval can still be needed for volatile or very large knowledge.
- **Worked example** — an assistant is fine-tuned on a company's manual so live queries no longer need the manual appended to every prompt.
- **Failure modes** — hallucinating internalized facts, degrading general ability, and staleness are the main risks.
- **Practical relevance** — context distillation complements retrieval and long-context techniques, offering a cost-latency lever.
- **Relation to compression** — prompt compression targets the same goal at inference time; distillation achieves it at training time.

## Related

- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — the general method
- [[wiki/prompt-engineering/context-compression|Context Compression]] — the inference-time alternative
- [[wiki/ai-ml/synthetic-data-generation|Synthetic Data Generation]] — generating training pairs
- [[wiki/ai-ml/catastrophic-forgetting-mitigation|Catastrophic Forgetting Mitigation]] — preserving abilities
- [[wiki/ml-frameworks/long-context-techniques|Long-Context Techniques]] — the competing approach
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — the training base

