---
type: "concept"
title: "Eval Sets"
description: "Curated collections of test prompts and expected outcomes used to measure an LLM or prompt system's performance"
tags: ["eval-sets", "testing", "benchmarks", "datasets"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2009.03300", "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"]
---

# Eval Sets

## Summary
An eval set is a fixed, versioned collection of prompts (plus expected outputs or scoring rubrics) that a team runs repeatedly to track quality. MMLU is the canonical academic example; production teams build smaller, domain-specific sets that reflect their real traffic.

## Details
- MMLU (Measuring Massive Multitask Language Understanding, 2009.03300) covers 57 subjects and is a standard capability benchmark.
- The Open LLM Leaderboard standardizes eval-set execution across open models with a reproducible harness.
- Good eval sets are: representative of real usage, versioned, balanced across failure modes, and protected from contamination.
- Split roles: smoke sets (fast, always run), regression sets (medium, per change), and deep sets (slow, per release).
- Eval-set maintenance is a first-class engineering task: drift in the product requires new cases, old cases must be audited for staleness.
- RSIS3 relevance: mykb stores eval sets as wiki artifacts, so each prompt or model change is scored against the same versioned cases.

## Related
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The practice eval sets serve
- [[wiki/testing/golden-tests|Golden Tests]] — The smallest, most stable eval-set tier
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — Eval sets power continuous regression gates
- [[wiki/ai-ml/benchmark-gaming|Benchmark Gaming]] — Why benchmark scores must be treated with suspicion
- [[wiki/ai-ml/data-contamination|Data Contamination]] — The contamination risk in public eval sets
- [[wiki/ai-ml/gpt-4|GPT-4]] — Reference model frequently scored on public eval sets
- [[wiki/concepts/mykb-research-report|mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint]] — Benchmark methodology research in the report
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Eval-set telemetry feeds wiki enrichment
