---
type: "entity"
title: "EvaluationResult"
description: "Evaluation"
tags: ["entity", "ajax", "android", "api", "ast", "auth"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
status: "growing"
---

## Evaluationresult

Evaluation — the assessment of LLM output quality. Sessions show manual review, automated scoring, and benchmarking patterns.

**Related topics:** ajax, android, api, auth

**Domain:** Web Platforms › [[wiki/web-platforms/supercategories/frontend/index|Frontend]] › [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/index|Frontend Frameworks]] › Evaluationresult

## Overview

An evaluation result is the outcome of assessing how well an LLM output satisfies a goal. Sessions show three patterns: manual review, where a human judges correctness and tone; automated scoring, where code applies rubrics or checks; and benchmarking, where many outputs are compared against a reference set. A useful result is more than a score: it carries the input, the output, the rubric, and enough context to reproduce the judgment.

## Evaluation Dimensions

Results are typically judged on factual accuracy, instruction following, format compliance, and safety. Factual checks may compare against retrieved evidence; format checks may parse JSON, code, or markdown; safety checks screen for harmful content. Each dimension should be scored independently so a failure in one does not mask success in another. Criteria should be written before the run and kept stable, otherwise results drift between sessions and cannot be compared.

## Scoring and Benchmarking

Automated scoring can be rule-based, model-based, or human-rated, and each approach has its own bias. Benchmarking generalizes beyond single samples: fixed datasets, reference answers, and aggregated metrics such as pass rate give a stable signal. Results should be stored with versioned prompts and model identifiers so regressions are attributable. Self-consistency checks and reflection loops can turn one run into several independent signals.

## Related Concepts

- [[wiki/llm-agents/success-criteria|Success Criteria]] — defining what good output means
- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]] — recording results alongside runs
- [[wiki/llm-agents/self-consistency|Self-Consistency]] — sampling multiple outputs for agreement
- [[wiki/llm-agents/traceability|Traceability]] — linking a result to its inputs
- [[wiki/dev-tools/benchmark-testing|Benchmark Testing]] — systematic comparisons

## Related Entities

- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ace-10|Ace 10]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrains-10|Jetbrains 10]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/csv-10|Csv 10]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
