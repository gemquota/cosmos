---
type: "concept"
title: "Agent Versioning"
description: "Tracking versions of agent code, prompts, policies, and identity"
tags: ["agent-versioning", "versioning", "config", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://langchain-ai.github.io/langgraph/", "https://github.com/mlflow/mlflow"]
---

# Agent Versioning

## Summary
Agent versioning treats the whole agent — code, prompts, tool configs, policies, persona — as a versioned artifact. It matters because agents drift silently, and reproducibility requires knowing exactly what ran. Versioning is the precondition for rollback and comparison.

## Details
- **What to version** — system prompts, tool schemas, model IDs and parameters, policy files, and the runtime code.
- **Immutability** — every run records the exact version IDs of all components; traces and logs reference them.
- **Rollback** — when a behavior regression appears, comparing versions identifies the changed component, and rollback restores the prior set.
- **Worked example** — a support bot's prompt v7 with a stricter refusal policy changes behavior; traces show v7 introduced it, and the team rolls back to v6 while editing.
- **Tooling** — prompt versioning in the app, config in git, and model registries for model versions.
- **mykb relevance** — agent versioning is an existing mykb topic; RSIS3 commits prompts and policies with checkpoints, making recursion auditable.

## Related
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — replay requires versions
- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]] — telemetry tagged with versions
- [[wiki/agent-systems/canary-deployments-agents|Canary Deployments for Agents]] — versioned canaries
- [[wiki/agent-systems/feature-flags-for-agents|Feature Flags for Agents]] — switching versions safely
- [[wiki/testing/drift-detection-for-models|Drift Detection for Models]] — detecting version drift
- [[wiki/prompt-engineering/prompt-repositories|Prompt Repositories]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/ml-frameworks/mlflow-model-registry|MLflow Model Registry]] — model registry tooling
