---
type: "concept"
title: "Explanation-Based Learning"
description: "Learning from a single example by explaining why it satisfies a general rule"
tags: ["explanation", "learning", "generalization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Explanation-based_learning", "https://dictionary.apa.org/explanation-based-learning"]
---

# Explanation-Based Learning

## Summary

Explanation-Based Learning — Learning from a single example by explaining why it satisfies a general rule.

## Details

- Explanation-based learning (EBL) derives a general rule from a single example plus domain knowledge, by explaining why the example is an instance of a concept. In AI, EBL compiles search experience into general macro-operators; in psychology it parallels the finding that explanatory understanding supports transfer beyond statistical similarity.
- EBL trades sample size for prior knowledge: with a good domain theory, one example suffices; without one, it overgeneralizes. Modern deep learning inverts the trade-off, needing many examples but little structure.
- Worked example: shown one instance of a pawn fork in chess, a learner who understands the underlying threat pattern can recognize and exploit forks in novel positions — the explanation, not the surface position, transfers.
- Current relevance: hybrid systems combine explanation and statistics; LLMs produce explanations whose value depends on whether they actually constrain future predictions.
- mykb relevance: self-explanation and knowledge-articulation entries are EBL in human form — turning one episode into a reusable principle.

## Related

- [[wiki/memory/self-explanation|Self-Explanation]] — the human mechanism
- [[wiki/memory/transfer-of-learning|Transfer of Learning]] — the payoff
- [[wiki/concepts/exemplar-theory|Exemplar Theory]] — contrast — many examples
- [[wiki/memory/knowledge-integration|Knowledge Integration]] — combining explanations
- [[wiki/meta-learning/model-based-learning|Model-Based Learning]] — adjacent stub in this cluster
- [[wiki/ai-ml/continual-learning|Continual Learning]] — existing wiki article
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — existing wiki article
