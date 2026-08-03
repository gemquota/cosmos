---
type: "concept"
title: "Test Set Discipline"
description: "The practice of keeping test data untouched until final evaluation"
tags: ["test-set", "discipline", "evals"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Test Set Discipline

## Summary
Test set discipline means the final test data is never used for training, tuning, or decisions until the end. It protects the credibility of reported numbers — a violated test set (even by accidental peeking) invalidates results and poisons every downstream decision built on them.

## Details
- Mechanism: split data into training, validation, and test sets at the start; iterate on training and validation only; touch the test set exactly once, at final evaluation; the discipline includes keeping test data out of logs, retrieval corpora, and human review loops where it could leak into the model's environment.
- Concrete example: an eval harness reserves a held-out set of article-summary pairs; the team tunes prompts on the validation split for weeks; the final model runs once on the test set and the number is recorded; a later analysis discovers the test set appeared in a retrieval corpus — the results are discarded and the corpus is cleaned.
- Failure modes: test leakage through shared corpora (retrieval databases, few-shot examples scraped from test data); peeking during iterative evaluation and then reporting as final; test sets reused across model versions, gradually memorized; data leakage through the human loop (reviewers see test examples); splitting errors where test rows also appear in training.
- Tradeoffs: strict holdout costs a chunk of scarce data and delays final feedback; the alternative, iterating on everything, produces better-looking numbers that mean nothing; the mature pattern is a locked test set, a documented evaluation protocol, and contamination checks.
- Operational notes: store the test set separately, log every evaluation run, and audit for contamination before reporting.
- RSIS3 relevance: the pass verifier runs on files the generator never tuned against — the same holdout discipline applied to the wiki's eval artifacts.

## Related
- [[wiki/decisions/eval-splits|Eval Splits]] — the structure
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the violation
- [[wiki/concepts/test-set-leakage|Test Set Leakage]] — the leak
- [[wiki/concepts/evals-practice-ai|Evals Practice]] — the norms
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]]
- [[wiki/ai-ml/model-selection-strategies|Model Selection Strategies]]
