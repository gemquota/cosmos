---
type: "concept"
title: "Induction Heads"
description: "Attention heads that copy and complete repeated patterns"
tags: ["induction-heads", "circuits", "attention"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Induction Heads

## Summary
Induction heads are attention heads that detect a repeated token and attend to its next occurrence, enabling copying and in-context learning. Concretely: given the sequence "A B ... A", an induction head attends from the second "A" back to the first "A" and copies the token that followed it — producing "B" — which is exactly the mechanism behind "A B A C → predict B" in-context pattern completion.

## Details
- The mechanism is a two-head circuit. A previous-token head in an early layer moves the representation of the current token (say, the second "A") back one position so it attends to the preceding token (the first "A"); then the induction head itself attends to the first "A" position and copies forward the token that followed it ("B"). The copied token is written into the residual stream in a way that biases the next-token prediction, completing the repeated pattern.
- Their discovery in 2021-2022 was a landmark for mechanistic interpretability: it was one of the first cases where a real, important behavior in a trained transformer was fully reverse-engineered into a concrete circuit, verified by causal interventions — ablate the heads and the induction behavior disappears — rather than merely correlated with them. The Anthropic "In-context Learning and Induction Heads" paper established the pattern and the method.
- They appear to be a general circuit for pattern completion in transformers. Induction heads emerge during training, strengthen with scale and data, and correlate strongly with the model's ability to do in-context learning tasks — the behavior that underpins few-shot prompting. Their generality across tasks and architectures suggests that transformers are not memorizing every pattern but implementing a reusable copying mechanism, which is a foundational result for understanding what the models are actually doing.
- The caveat: induction heads are one circuit among many. They explain simple "copy the pattern" behavior, not the full machinery of in-context learning, and later work has found a richer zoo of heads — variable binding, context matching, and copy-suppression variants — that together implement the behavior. The lesson is that even a famous circuit is a component, not the whole story.
- RSIS3 relevance: understanding induction-like circuits informs how in-context knowledge retrieval works — the same copy-and-complete mechanism is what lets a model use retrieved context to answer, and knowing its circuit-level basis clarifies both its power and its failure modes.

## Related
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — the framework
- [[wiki/prompt-engineering/in-context-learning|In-Context Learning]] — the behavior
- [[wiki/concepts/attention-mechanisms|Attention Mechanisms]] — the substrate
- [[wiki/concepts/circuit-tracing|Circuit Tracing]] — how they were found
- [[wiki/concepts/emergence-in-llms|Emergence in LLMs]]
