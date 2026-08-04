---
type: "entity"
title: "QuestionQualityIndex"
description: "QuestionQualityIndex is an entity from the wiki's session index whose name describes a metric for scoring how good a question is. Question quality matters becau"
tags: ["entity", "api", "ast", "auth", "aws", "bash"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# QuestionQualityIndex

## Summary
QuestionQualityIndex is an entity from the wiki's session index whose name describes a metric for scoring how good a question is. Question quality matters because retrieval, evaluation, and training data all inherit the quality of the questions they start from. This page documents the concept behind the entity. Question quality is a gate that protects both users and evaluation integrity.

## Details
- **Definition** — a question quality index scores questions on properties such as clarity, specificity, answerability, and ambiguity.
- **Why it matters** — in evaluation pipelines, low-quality questions produce noisy scores; in retrieval, ambiguous queries return poor results.
- **Scoring dimensions** — common dimensions are grammatical clarity, sufficient context, unambiguity, and whether the question has a verifiable answer.
- **Applications** — quality indexes filter benchmark items, prioritize support-ticket questions, and curate training data.
- **Scoring methods** — quality can be scored by heuristics, rubric-based evaluation, or llm-as-judge ratings.
- **Worked example** — an evaluation pipeline computes a quality index for each benchmark question and excludes items below a threshold from scoring.
- **Failure modes** — subjective criteria, scorer inconsistency, and over-filtering that removes useful hard questions are the risks.
- **Practical relevance** — question quality is a quiet multiplier on everything downstream, from eval reliability to user experience.
- **Automation** — scoring can be automated and then spot-audited by humans.
- **Feedback** — quality scores can guide users to reformulate poor questions.
- **Failure example** — a quality gate that is never audited rejects good questions on bad rules.
- **Dimensions** — combining clarity, specificity, and answerability scores yields a richer index.
- **Calibration** — thresholds should be validated against human judgments of quality.

## Related
- [[wiki/ai-ml/rubric-based-evaluation|Rubric-Based Evaluation]] — structured scoring of quality
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — automated quality ratings
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — curated question sets
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/00-index|API REST HTTP Index]] — the cluster this entity belongs to
- [[wiki/data-storage/full-text-search-and-tokenization|Full-Text Search and Tokenization]] — query quality in search
