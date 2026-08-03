---
type: "concept"
title: "Knowledge Distillation"
description: "Training a small student model to imitate a larger teacher model's predictions and knowledge"
tags: ["distillation", "model-compression", "training", "student-teacher", "efficiency"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1503.02531"]
---

# Knowledge Distillation

## Summary
Knowledge distillation transfers a large teacher model's knowledge into a smaller student model by training the student on the teacher's softened output probabilities, not just hard labels. It compresses expensive models for deployment and can even improve small models on target tasks. Hinton, Vinyals and Dean introduced the modern formulation in 2015.

## Details
- **Mechanism** — teacher logits are softened by a temperature parameter; the student minimizes a weighted loss between its distribution and the teacher's, learning dark knowledge such as class similarities.
- **Why it works** — probabilities encode more than labels: a teacher's 'cat vs dog' odds reveal shared features a hard label hides.
- **Variants** — offline (train teacher first), online (joint training), self-distillation (model distills itself), and feature-level distillation (match hidden representations).
- **Worked example** — a 7B generalist model distills into a 1B model on retrieval-ranking data; the student inherits ranking preferences with a fraction of the inference cost.
- **Relation to search** — distilled bi-encoders are common in production semantic search: small student encoders that approximate large teacher rankings.

## Related
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — distillation is a transfer mechanism between models
- [[wiki/meta-learning/curriculum-learning|Curriculum Learning]] — another training strategy that shapes learning
- [[wiki/data-storage/embeddings|Embeddings]] — distilled encoders produce cheaper embeddings
- [[wiki/meta-learning/bi-encoder|Bi-Encoder]] — the student architecture often distilled for search
- [[wiki/meta-learning/cross-encoder|Cross-Encoder]] — the teacher architecture in ranking distillation
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — practical host of distilled encoders
- [[wiki/meta-learning/00-index|Meta-Learning]] — learning-to-learn techniques like distillation
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — surveys distilled retrieval models
