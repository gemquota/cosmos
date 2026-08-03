---
type: "concept"
title: "Interpretability"
description: "Methods for understanding what models compute and why they produce the outputs they do"
tags: ["interpretability", "llm", "research"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Interpretability

## Summary
Interpretability aims to open the black box: locating concepts in activations, tracing reasoning, and predicting failure modes. It is a research frontier with practical payoffs for debugging, safety, and eval design, and it spans several distinct levels of analysis that answer different questions.

## Details
The field operates at three complementary levels. Behavioural interpretability treats the model as a black box and infers its strategies from input-output pairs: probing classifiers read information from activations, and controlled perturbations reveal which features drive which outputs. Mechanistic interpretability reverse-engineers the internal circuits — the actual weights and attention heads — that implement specific behaviours, such as induction heads that copy patterns or feature detectors for concepts. Architectural analysis studies how design choices, like depth, width, and attention structure, shape what is learnable in the first place.

The practical uses are concrete. Hidden prompt-injection detection becomes more tractable when you can identify internal states that correlate with injected instructions. Knowledge-conflict behaviour — where a model has two incompatible facts and picks one — can be located and audited. Bias auditing moves from aggregate scorecards to specific neurons or attention patterns that mediate a stereotype, which in turn suggests targeted mitigations rather than blanket fine-tuning.

The honest caveats matter for anyone operationalizing the field. Findings transfer unevenly across model families and even across checkpoints: a circuit discovered in one model often does not exist in the next generation. Interpretability tools measure correlation with behaviour, not always causation. And the cost is high — mechanistic analysis is manual, expert-heavy, and slow, which is why it rarely runs continuously in production.

RSIS3 relevance: interpretability of RSIS3's own models could explain why certain prompts fail or drift over time, and mykb should store interpretability findings alongside the eval results they explain, so a circuit analysis is not orphaned from the behaviour it describes.

## Related
- [[wiki/ai-ml/probing|Probing]] — Reading information from activations
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — Reverse-engineering circuits
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — Feature extraction from activations
- [[wiki/ai-ml/logit-lens|Logit Lens]] — Reading predictions from intermediate layers
- [[wiki/ai-ml/attention-patterns|Attention Patterns]] — Interpreting attention weights
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Interpretability informs eval design
