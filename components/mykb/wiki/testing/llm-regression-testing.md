---
type: "concept"
title: "LLM Regression Testing"
description: "Automated testing that detects when model or pipeline changes degrade quality"
tags: ["regression", "testing", "evaluation", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/openai/evals", "https://www.promptfoo.dev/docs/"]
---

# LLM Regression Testing

## Summary
LLM regression testing re-runs fixed evaluation suites whenever a model, prompt, or pipeline changes. It matters because prompt tweaks and model swaps cause subtle quality shifts. Regression gates make those shifts visible before production impact.

## Details
- **Triggers** — new model versions, prompt edits, retrieval changes, and infrastructure updates.
- **Suite** — golden-test-sets, adversarial cases, safety checks, and task-specific metrics.
- **Worked example** — a CI job runs 200 golden prompts against the candidate model; a judge score drop below threshold blocks the merge.
- **Best practice** — keep suites fast enough for every change, and deep enough to catch real regressions.
- **mykb relevance** — every RSIS3 iteration should pass a personal regression suite before adoption.
- **Worked example** — a CI job runs 200 golden prompts against the candidate model; a judge score drop below threshold blocks the merge.
- **Frequency** — run fast smoke suites on every change and deeper suites on release candidates.
- **Suite design** — mix golden-test-sets, adversarial cases, safety checks, and task-specific metrics so regressions surface by type.

## Related
- [[wiki/testing/evals-harness|Evals Harness]] — runner
- [[wiki/testing/drift-detection-for-models|Drift Detection for Models]] — production drift
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — CI integration
- [[wiki/prompt-engineering/prompt-testing|Prompt Testing]] — prompt-level checks
- [[wiki/agent-systems/agent-testing-strategies|Agent Testing Strategies]] — agent-level checks
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/testing/agent-evaluations|Agent Evaluations]] — related concept in this cluster
