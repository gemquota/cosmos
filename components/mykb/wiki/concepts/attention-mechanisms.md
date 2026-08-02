---
type: "concept"
title: "Attention Mechanisms"
description: "Selection processes that decide what information an agent focuses on"
tags: ["attention", "selection", "cognition", "context"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Attention_(machine_learning)", "https://arxiv.org/abs/1706.03762"]
---

# Attention Mechanisms

## Summary
Attention mechanisms allocate processing and context to the most relevant information, whether in the model's internal computation or the agent's retrieval choices. They matter because selection determines what the agent actually considers. Attention is what keeps context manageable.

## Details
- Internal: transformer attention weights select relevant tokens.
- External: agent-level attention chooses which files, memories, and tools to consult.
- RSIS3 relevance: retrieval selection and prompt construction are attention policies.
- Open questions: aligning agent-level attention with task relevance.
- Attention mechanisms in machine learning let a model selectively focus on relevant parts of its input by computing weighted combinations of features.
- They solved the bottleneck of fixed-length context vectors in sequence models and became the core operation of the transformer.
- Attention is differentiable and trainable: the weights are learned from data, so the model discovers which inputs matter for each output.
- The family includes self-attention, cross-attention, multi-head attention, and the many sparse and linear approximations for long contexts.
- **Worked example / comparison** — Worked example — in translation, the output word 'bank' attends strongly to the source word 'river' or 'money', letting the model choose the right sense.
- For mykb, attention-mechanisms is the umbrella article in the AI/ML cluster, linking down to the specific attention variants.

## Related
- [[wiki/llm-agents/context-management|Context Management]]
- [[wiki/concepts/working-memory|Working Memory]]
- [[wiki/concepts/perception-loop|Perception Loop]]
- [[wiki/concepts/cognitive-load|Cognitive Load]]
- [[wiki/concepts/metacognition|Metacognition]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
