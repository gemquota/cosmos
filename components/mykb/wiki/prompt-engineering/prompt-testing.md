---
type: "concept"
title: "Prompt Testing"
description: "Automated evaluation of prompt variants against expected outputs"
tags: ["prompt-testing", "prompts", "testing", "evaluation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Prompt Testing

## Summary

Prompt testing is the automated evaluation of prompt variants against expected outputs, turning prompt improvement from anecdote into engineering. It uses test sets, metrics, and regression tracking to catch degradations before they reach users. Testing matters because prompt behavior is probabilistic and changes with model versions, so quality cannot be assumed — it must be measured. Prompt testing pays off continuously because prompts drift as underlying models change, even when nothing else is edited.

## Details

- **Definition** — prompt testing runs prompts against a set of inputs with expected outputs and scores the results.
- **Test sets** — golden test sets capture representative cases, edge cases, and adversarial inputs that the prompt must handle.
- **Metrics** — exact match, rubric-based scoring, semantic similarity, and task-specific metrics measure different quality dimensions.
- **A/B comparisons** — testing variants side by side on the same inputs reveals which wording actually improves outcomes.
- **Regression protection** — automated suites catch regressions when prompts, templates, or underlying models change.
- **Iteration loop** — testing feeds debugging: failures in tests generate hypotheses for prompt edits, which are then re-tested.
- **Worked example** — a summarization prompt is tested on 200 articles with rubric scores; a wording change raises average score and is rolled out.
- **Failure modes** — overfitting the test set, weak metrics that miss real defects, and untested edge cases undermine confidence.
- **Practical relevance** — prompt testing is the quality gate for prompt libraries, agent pipelines, and production LLM features.
- **Relation to evals** — prompt testing is a form of evaluation focused on the prompt artifact, complementing model and system evals.
- **Model-version gates** — re-running the test suite whenever the deployed model changes detects degradation before users do.


## Related

- [[wiki/prompt-engineering/prompt-debugging|Prompt Debugging]] — the diagnostic loop
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — the test foundation
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — change protection
- [[wiki/prompt-engineering/prompt-versioning|Prompt Versioning]] — tracking tested versions
- [[wiki/testing/evals-harness|Evals Harness]] — the evaluation infrastructure
- [[wiki/prompt-engineering/prompt-libraries|Prompt Libraries]] — curated tested prompts

