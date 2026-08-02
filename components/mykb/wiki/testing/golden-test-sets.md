---
type: "concept"
title: "Golden Test Sets"
description: "Frozen sets of inputs with expected outputs used to catch model regressions"
tags: ["golden", "testing", "regression", "evaluation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/openai/evals", "https://www.promptfoo.dev/docs/"]
---

# Golden Test Sets

## Summary
Golden test sets lock in a fixed batch of prompts and expected outputs that every model version must pass. They matter because they turn vague quality concerns into a numeric gate. Any change — prompt, model, or pipeline — can be checked against the same yardstick.

## Details
- **Construction** — collect real production inputs, hand-write expected outputs or rubrics, and review them as a team.
- **Usage** — run before deploys, after prompt edits, and periodically to detect drift.
- **Worked example** — a summarization service keeps 50 gold documents with 3 reference summaries each; a regression check computes ROUGE and judge scores per version.
- **Maintenance** — goldens age; add new cases as product scope grows, and keep old cases for history.
- **mykb relevance** — a personal golden set of RSIS3 queries would make every system iteration measurable.
- **Review** — golden outputs must be team-reviewed; one wrong expected output poisons the gate.
- **Coverage** — sample across intents, formats, and edge cases so the set represents real traffic.

## Related
- [[wiki/testing/evals-harness|Evals Harness]] — running goldens
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — regression gate
- [[wiki/prompt-engineering/prompt-testing|Prompt Testing]] — prompt changes
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — scoring method
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — version gates
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
