---
type: "concept"
title: "Model Cards"
description: "Structured documentation of a model's training data, intended use, limitations, and evaluation results"
tags: ["model-cards", "documentation", "governance"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Model Cards

## Summary
Model cards are the standard format for documenting machine-learning models: what they are for, how they were trained, what they fail at, and how they were evaluated. They are the trust contract between model publishers and users, and they make model selection a documented decision rather than a guess.

## Details
The format originated with the paper Model Cards for Model Reporting (2019) and is now common practice for frontier labs. A well-formed card contains sections on intended use, training data, evaluation methodology, limitations, and ethical considerations, and it states metrics in a way that lets a reader reproduce or at least interpret them. The point of the structure is to force disclosure: a card that omits eval details or failure modes is a warning sign, not a neutral absence.

The operational value shows up in model selection. When RSIS3 or a mykb pipeline must choose between models, the card is the first document to read: it says what the model was optimized for, what data it saw, and where its reported scores are trustworthy. Cards also pin down versioning — model families evolve, and the card ties a specific checkpoint to specific behaviour, so a score without a card reference is not comparable to anything else.

The failure modes are real. Cards can become marketing documents that emphasize headline scores and bury limitations; eval sections can hide methodology choices such as prompt templates, few-shot counts, or contamination checks; and cards can go stale as the underlying model is fine-tuned. The reader-side discipline is to treat a card as a claim, then verify the claims that matter against the actual model on one's own eval set.

Good cards disclose eval scores, biases, and failure modes — they are not marketing. RSIS3 relevance: mykb should attach a model card to every model it benchmarks or serves locally, effectively creating cards inside the wiki so that every model decision recorded there carries its own documented contract.

## Related
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The results model cards report
- [[wiki/ai-ml/data-contamination|Data Contamination]] — A disclosure model cards should make
- [[wiki/ai-ml/benchmark-gaming|Benchmark Gaming]] — Why cards must report eval methodology
- [[wiki/ai-ml/llama|Llama]] — A family published with model cards
- [[wiki/ai-ml/claude|Claude]] — Frontier family with extensive cards
