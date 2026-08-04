---
type: "concept"
title: "Data Science Agents"
description: "Agents that explore data, run analyses, and produce reports or models"
tags: ["ds-agents", "data-science", "agents", "analysis"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data Science Agents

## Summary
Data science agents explore data, run analyses, and produce reports or models, combining code execution with statistical reasoning. They matter because analysis is iterative and tool-heavy, and an agent that can run code closes the loop between hypotheses and evidence. Safe execution and data governance are the enabling constraints. Data science agents earn trust through reproducible steps and honest uncertainty.

## Details
- **Definition** — a data science agent works through an analysis pipeline: load data, clean it, explore, model, and report, executing code as it goes.
- **Tool use** — agents use code-execution-environments to run analyses, produce plots, and generate tables, with results feeding back into the reasoning loop.
- **Messy data** — real data requires iterative cleaning: missing values, outliers, and schema inconsistencies are handled step by step.
- **Outputs** — deliverables include notebooks, charts, summaries, and model evaluations, often as structured tables via table-output-generation.
- **Worked example** — an agent receives a churn dataset, profiles the columns, builds a logistic model, and drafts a summary of the top drivers for review.
- **Failure modes** — silent data-quality errors, p-hacking through excessive exploration, and unreproducible analysis steps are the main risks.
- **Governance** — data provenance and access controls matter because analyses touch sensitive data and feed decisions.
- **Practical relevance** — data science agents generalize the research-agents pattern from text to computation, a core workload for agent platforms.
- **Reproducibility** — pinned data versions, seeds, and environment specs let analyses be re-run.
- **Uncertainty** — outputs should state confidence and limitations rather than presenting single numbers as truth.
- **Worked example** — an agent reports a model's ROC curve and its confidence intervals, not just the headline metric.
- **Failure example** — an agent that silently drops missing rows changes the population without telling anyone.

## Related
- [[wiki/agent-systems/code-execution-environments|Code Execution Environments]] — the runtime for analyses
- [[wiki/agent-systems/research-agents|Research Agents]] — the text-focused sibling
- [[wiki/prompt-engineering/table-output-generation|Table Output Generation]] — producing tabular results
- [[wiki/ai-ml/data-labeling-workflows|Data Labeling Workflows]] — preparing data for analysis
- [[wiki/agent-systems/agent-observability|Agent Observability]] — tracing analysis steps
