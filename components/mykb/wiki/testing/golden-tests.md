---
type: "concept"
title: "Golden Tests"
description: "Small, fixed, deterministic test cases with expected outputs used as fast regression checks for LLM systems"
tags: ["golden-tests", "testing", "regression", "quality"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://docs.smith.langchain.com/evaluation"]
---

# Golden Tests

## Summary
Golden tests are a hand-curated set of inputs with known-good expected outputs, re-run after every prompt or model change. They are the cheapest reliable safety net in LLM testing: slow enough to be few, fast enough to run in CI, and stable enough to catch regressions.

## Details
- LangSmith's evaluation docs show golden ('exact match') datasets running against every trace or version change.
- Golden tests excel at catching brittle regressions: output-format drift, lost instructions, broken tool calls, refusal regressions.
- Because LLM outputs are stochastic, golden tests pair with looser scoring (contains, semantic-similarity, LLM-judge) to stay non-flaky.
- Maintenance: goldens rot as the product evolves; each test needs an owner and a review cadence.
- Hierarchy: golden tests sit below eval sets (broad, slow) and above unit tests of pure code.
- RSIS3 relevance: each RRP session can auto-generate goldens from verified outcomes, growing a regression net over time.

## Related
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — The broader discipline golden tests anchor
- [[wiki/testing/eval-sets|Eval Sets]] — Goldens are the stable core of larger eval sets
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The overall quality-measurement practice
- [[wiki/prompt-engineering/message-format|Message Format]] — Message-format stability is a golden-test target
- [[wiki/syntheses/weekly-review|Weekly Review]] — Golden-test drift surfaces in weekly reviews
- [[wiki/prompt-engineering/json-mode|JSON Mode]] — JSON-mode outputs are stable golden subjects
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — Schema-validated tool outputs as goldens
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Auto-generated goldens enrich the wiki
