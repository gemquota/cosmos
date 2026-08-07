---
type: "concept"
title: "Hallucination Benchmarks"
description: "Evaluations that measure how often and how badly a model fabricates content"
tags: ["hallucination", "benchmarks", "evaluation", "factuality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Hallucination Benchmarks

## Summary
Hallucination benchmarks measure how often and how badly a model fabricates content — statements that are fluent but not supported by the context or the world. They score factuality, faithfulness to retrieved evidence, and the severity of invented claims, and they are the regression guard for any generation pipeline.

## Details
- **What they measure** — unsupported statements (fabrication), context-mismatched claims (unfaithfulness to a source), and severity grading from harmless confabulation to dangerous misinformation.
- **Scoring styles** — automatic metrics compare against ground truth or check claims against a knowledge source; human rating remains the reference for subtle cases because automatic verdicts can miss plausible-sounding errors.
- **Closed-book versus grounded** — closed-book benchmarks test what the model knows and admits; grounded benchmarks feed a document and check that claims stay within it, which is the relevant axis for retrieval-augmented pipelines.
- **Common patterns** — claim-level decomposition (split answers into atomic claims and verify each), entailment checks against evidence, and error-rate reporting over a fixed prompt set.
- **Uses** — model selection, regression testing across releases, and monitoring after deployment; hallucination rates are reported alongside accuracy because accuracy alone hides fabrication.
- **Caveats** — benchmarks sample a finite prompt set, severity judgments are subjective, and models can overfit to benchmark style; a good suite is refreshed as the production prompt distribution shifts.
- **Relation to other evals** — hallucination benchmarks sit inside the broader factuality and model-evaluation landscape and are a key input to llm-regression-testing.

- **Reporting practice** — publish both the aggregate rate and the severity breakdown; a low aggregate rate with a tail of high-severity errors is worse than a uniform moderate rate, and the breakdown exposes which deployment guardrails are needed.
## Related
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — techniques they evaluate
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — grounding approach
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — continuous checks
- [[wiki/ai-ml/model-evaluation-metrics|Model Evaluation Metrics]] — scoring methods
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — the broader evaluation practice
- [[wiki/ai-ml/rag-benchmarks|RAG Benchmarks]] — pipeline-level evaluation
