---
type: "concept"
title: "Curriculum Learning"
description: "Training strategy that orders examples from easy to hard, mimicking human learning curricula"
tags: ["curriculum", "training", "machine-learning", "scheduling", "learning-theory"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2104.06275"]
---

# Curriculum Learning

## Summary
Curriculum learning trains models on easy examples first and gradually introduces harder ones, guided by a difficulty measure and pacing schedule. Bengio et al. showed in 2009 that this ordering can speed convergence and improve generalization. It is the machine-learning mirror of how humans sequence practice in skill acquisition.

## Details
- **Components** — a difficulty scorer (size, noise, model loss), a pacing function (from easy-only to full data), and a schedule policy (fixed, self-paced).
- **Why it can help** — starting near the optimum region of the loss landscape can avoid bad local minima; for humans, success builds confidence and schema before challenge.
- **Variants** — self-paced learning (model proposes its own order), anti-curriculum (hard first), and baby steps for long-horizon tasks like code generation.
- **Worked example** — fine-tuning a summarizer: first on clean news snippets, then on noisy wiki-derived notes, then on mykb's compressed syntheses.
- **Relation to memory** — spaced repetition is a human curriculum: easy items get long gaps, hard items recur sooner.

## Related
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — curricula and transfer both shape learning dynamics
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — distillation can be combined with curriculum ordering
- [[wiki/memory/just-in-time-learning|Just-in-Time Learning]] — the human-side contrast to scheduled curricula
- [[wiki/memory/active-recall|Active Recall]] — human retrieval practice as a curriculum
- [[wiki/meta-learning/cluster-analysis|Cluster Analysis]] — groups data into difficulty tiers
- [[wiki/meta-learning/index|Meta-Learning]] — learning-to-learn strategies include curricula
- [[wiki/questions/index|Open Questions]] — open questions on curriculum design
