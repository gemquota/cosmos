---
type: "concept"
title: "ROUGE, BLEU, and BERTScore"
description: "Classic n-gram and embedding-based metrics for evaluating generated text"
tags: ["metrics", "evaluation", "nlp"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# ROUGE, BLEU, and BERTScore

## Summary
ROUGE, BLEU, and BERTScore are classic metrics for evaluating generated text, measuring n-gram overlap and semantic similarity against references. They matter because they are cheap, reproducible baselines for summarization and translation, still used across the industry. Their weakness on semantic equivalence is why judge-based evaluation increasingly supplements them. Reference-based metrics reward agreement with a gold answer, not quality per se.

## Details
- **Definition** — ROUGE measures recall-oriented overlap of n-grams for summarization, BLEU measures precision-oriented overlap for translation, and BERTScore compares embeddings for semantic similarity.
- **Strengths** — they are fast, deterministic, and comparable across runs, making them ideal for regression baselines.
- **Weaknesses** — they miss paraphrases and semantic equivalence, rewarding surface similarity over meaning.
- **Use cases** — ROUGE anchors summarization evaluation, BLEU anchors translation evaluation, and BERTScore adds a semantic check where references exist.
- **Worked example** — a translation team tracks BLEU on a held-out set for regressions while routing samples to human review for adequacy.
- **Failure modes** — relying on these metrics alone rewards fluent-but-wrong text and punishes valid rephrasing.
- **Modern context** — llm-as-judge and rubric-based-evaluation are increasingly used for open-ended quality, with classic metrics kept as baselines.
- **Practical relevance** — these metrics remain the standard first pass for text generation evaluation in production pipelines.
- **Reference quality** — metrics inherit the quality of the reference set.
- **Length effects** — BLEU punishes short translations and ROUGE rewards overlap; both are sensitive to style.
- **Worked example** — a summarization team uses ROUGE for regression and judge scores for launch decisions.
- **Failure example** — optimizing BLEU alone encourages rigid, literal translations that read poorly.
- **Usage note** — scores should be reported alongside sample outputs, since numbers alone cannot show what quality looks like.

## Related
- [[wiki/ai-ml/model-evaluation-metrics|Model Evaluation Metrics]] — the metric family
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — the semantic alternative
- [[wiki/agent-systems/translation-agents|Translation Agents]] — a typical user
- [[wiki/agent-systems/summarization-agents|Summarization Agents]] — a typical user
- [[wiki/ai-ml/rubric-based-evaluation|Rubric-Based Evaluation]] — structured judging
