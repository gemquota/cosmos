---
type: "concept"
title: "Overfitting in LLMs"
description: "Memorization at the expense of generalization in language models"
tags: ["overfitting", "llm", "generalization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Overfitting in LLMs

## Summary
Overfitting in LLMs is the model fitting training specifics — exact text, formatting quirks, benchmark answers — instead of general rules. The signature is high training performance with brittle deployment behavior: the model succeeds because it memorized the training material, not because it understood the underlying pattern, and any input that departs from the memorized forms exposes the gap.

## Details
- The mechanism is the same as classical overfitting but amplified by scale: language models have enough capacity to memorize enormous amounts of training data, and when capacity exceeds the genuine regularity in the data, the model stores surface forms as a fallback. The tell is sensitivity — an overfit model answers correctly on exact training phrasings and fails on paraphrases, whereas a generalizing model is robust to rephrasing because it learned the concept, not the string. This is why paraphrase-based evaluation is a standard overfitting test.
- It surfaces as benchmark contamination and memorization of private data. Benchmark contamination is overfitting to the eval itself: the model scores high because benchmark items (or near-duplicates) appeared in training, so the benchmark measures retrieval rather than capability. Memorization of private data is the security face: models can emit verbatim training text — personal information, copyrighted passages — which is both an overfitting symptom and a privacy failure. Both are detected by audits: exact and fuzzy matching against training corpora, membership inference, and probing for verbatim recall.
- Detection: held-out paraphrase sets and contamination audits. A held-out paraphrase set tests whether the model generalizes the concept (correct on new phrasings) or memorized the string (correct only on seen forms). Contamination audits check whether eval items leaked into training by exact match, near-duplicate detection, and unusual per-item performance patterns. Neither test is perfect — paraphrase sets need to be genuinely novel, and contamination detection misses paraphrased leakage — but together they bound the overfitting problem.
- The mitigation is the same toolkit as classical ML — regularization, data hygiene, and eval discipline — with LLM-specific additions: deduplicating training data, filtering eval-like content, and monitoring verbatim-recall rates. The deeper point: overfitting in LLMs is not a bug of a specific run but a standing tension between memorization and generalization that every model resolves differently.
- RSIS3 relevance: template memorization in the graph is its overfitting analogue — a wiki that repeats the same phrasing for every concept may be "performing well" on its own corpus while failing on genuinely new queries, the retrieval-side version of the same failure.

## Related
- [[wiki/concepts/underfitting-llm|Underfitting in LLMs]] — the opposite failure
- [[wiki/concepts/memorization-vs-generalization|Memorization vs Generalization]] — the spectrum
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the benchmark symptom
- [[wiki/concepts/regularization-practice|Regularization in Practice]] — the mitigation
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
- [[wiki/ai-ml/data-contamination|Data Contamination]] — existing graph context
