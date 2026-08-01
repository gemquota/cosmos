---
type: "concept"
title: "Transfer Learning"
description: "Reusing knowledge from one task or domain to improve learning on a different but related one"
tags: ["transfer-learning", "pretraining", "fine-tuning", "machine-learning", "generalization"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Transfer_learning"]
---

# Transfer Learning

## Summary
Transfer learning reuses representations or weights learned on one task as a starting point for another, dramatically cutting the data and compute needed for the new task. Pretrained language and vision models are the canonical example: one pretrained model adapts to dozens of downstream tasks. It is the practical backbone of modern NLP and embedding systems.

## Details
- **Forms** — inductive (same domain, different task), transductive (different domain, same task), and self-taught learning; plus fine-tuning, feature extraction, and domain adaptation.
- **Why it works** — early layers learn general features (edges, syntax, semantics) that transfer; only task-specific layers need task data.
- **Worked example** — a sentence-transformer pretrained on web text is fine-tuned on a few thousand labeled pairs of wiki-query relevance judgments to become a strong mykb retriever.
- **Risks** — negative transfer (source task hurts the target), catastrophic forgetting during fine-tuning, and distribution shift.
- **Relation to memory** — embeddings and retrieval models are transfer-learning artifacts: they carry corpus-general knowledge into a specific knowledge base.

## Related
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — transfers knowledge between model sizes
- [[wiki/meta-learning/curriculum-learning|Curriculum Learning]] — orders training to ease transfer
- [[wiki/data-storage/embeddings|Embeddings]] — transfer-learned representations power search
- [[wiki/meta-learning/word2vec|Word2Vec]] — early transfer of word representations
- [[wiki/meta-learning/graph-embeddings|Graph Embeddings]] — transferring structural knowledge from graphs
- [[wiki/meta-learning/node2vec|Node2Vec]] — graph representation learning for transfer
- [[wiki/meta-learning/index|Meta-Learning]] — the field that studies learning to transfer
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — survey of transfer-based retrieval models
