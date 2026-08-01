---
type: "concept"
title: "Regression Testing for LLMs"
description: "Continuously re-running evaluation cases to detect quality loss when prompts, models, or pipelines change"
tags: ["regression-testing", "testing", "ci", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.promptfoo.dev/docs/intro"]
---

# Regression Testing for LLMs

## Summary
Regression testing for LLMs applies the classic engineering idea of a regression suite to prompt systems: a versioned set of cases re-run on every change so that a new system prompt, model version, or library upgrade cannot silently degrade output quality.

## Details
- promptfoo is a purpose-built open-source tool: declare prompts and test cases, run against multiple models, and diff results with side-by-side views.
- Regression suites catch: format drift, tool-call breakage, refusal regressions, cost regressions, and quality drops after model swaps.
- Determinism trade-off: use temperature 0 plus similarity thresholds so CI runs stay stable without flaking.
- Version everything: prompts, models, eval sets, and harness config are the regression contract; mykb can store each as a wiki artifact.
- Cost control: run a fast subset per commit and the full suite per release.
- RSIS3 relevance: L2 code generation is already test-gated (git-rollback on failure); extending that gate to prompt outputs is the natural next step.

## Related
- [[wiki/testing/golden-tests|Golden Tests]] — The fast, stable core of the regression suite
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — The measurement practice regression relies on
- [[wiki/ai-ml/guardrails|Guardrails]] — Guardrail changes must be regression-tested
- [[wiki/syntheses/weekly-review|Weekly Review]] — Regression trends feed the weekly review
- [[wiki/prompt-engineering/adversarial-prompts|Adversarial Prompts]] — Adversarial cases belong in the regression suite
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — Red-team findings become regression cases
- [[wiki/concepts/mykb-implementation-report|mykb Implementation Report: 6-Phase Buildout — Actual State, Architecture, and Results]] — Test-gated buildout extended to prompts
