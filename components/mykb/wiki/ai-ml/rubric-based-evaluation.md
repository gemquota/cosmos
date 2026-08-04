---
type: "concept"
title: "Rubric-Based Evaluation"
description: "Scoring model outputs against explicit criteria and quality bands"
tags: ["evaluation", "rubrics", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Rubric-Based Evaluation

## Summary
Rubric-based evaluation scores model outputs against explicit criteria and quality bands, making judgment consistent and auditable. It matters because vague evaluation produces arbitrary scores, while a rubric turns taste into a shared standard. Rubrics are the bridge between human expectations and automated judging. Rubrics turn evaluation from an opinion into a documented standard.

## Details
- **Definition** — a rubric defines criteria, quality levels, and score anchors that an evaluator applies to each output.
- **Structure** — good rubrics name the dimensions being scored, describe what each band looks like, and give examples of anchor responses.
- **Consistency** — because the standard is written down, different evaluators and judges produce comparable scores over time.
- **Automation** — rubrics combine with llm-as-judge to grade large output volumes at scale while keeping the standard explicit.
- **Worked example** — a rubric scores support answers on accuracy, completeness, and tone across four bands; the judge assigns a band and cites the criterion violated.
- **Failure modes** — vague bands invite inconsistent scoring, rubric drift weakens comparability, and evaluators anchoring on one dimension distort results.
- **Integration** — rubrics support golden-test-sets and regression gates by making pass-or-fail thresholds defensible.
- **Practical relevance** — rubrics are the quality standard of modern evaluation pipelines, from content generation to agent behavior.
- **Anchor examples** — concrete exemplars for each band reduce disagreement between judges.
- **Review** — rubric definitions should be reviewed as they age with the product.
- **Worked example** — a rubric with four bands for accuracy lets two judges produce matching scores on most samples.
- **Failure example** — a rubric with overlapping band descriptions makes judge scores inconsistent.

## Related
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — the scoring engine that applies rubrics
- [[wiki/ai-ml/model-evaluation-metrics|Model Evaluation Metrics]] — quantitative scoring alongside rubrics
- [[wiki/ai-ml/data-labeling-workflows|Data Labeling Workflows]] — producing rubric judgments
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — regression evaluation with rubrics
- [[wiki/ai-ml/quality-filtering|Quality Filtering]] — rubric scores as selection signals
