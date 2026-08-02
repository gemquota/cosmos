---
type: "concept"
title: "Prompt Versioning"
description: "Tracking prompt revisions with metadata so changes are auditable and reversible"
tags: ["prompt-versioning", "prompts", "governance", "llmops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://langchain-ai.github.io/langgraph/", "https://www.promptfoo.dev/docs/"]
---

# Prompt Versioning

## Summary
Prompt versioning stores prompts as versioned artifacts with owners, change history, and linked eval results. It matters because prompts change behavior and must be managed like code. Versioning enables rollback, comparison, and audit trails.

## Details
- **Artifact** — prompt text, model target, parameters, eval scores, and changelog per version.
- **Workflow** — edit in a repo, run prompt-testing, review, then promote with a version tag.
- **Worked example** — a support bot prompt v42 is rolled back when its regression suite flags a refusal-rate increase.
- **Best practice** — hash prompt versions into trace logs so every response maps to its prompt.
- **mykb relevance** — RSIS3 prompt evolution should be replayable and reversible.
- **Worked example** — a support bot prompt v42 is rolled back when its regression suite flags a refusal-rate increase.
- **Traceability** — hash prompt versions into logs so every response maps to its exact prompt.
- **Workflow** — edit in a repository, run prompt-testing, review, then promote with a version tag and linked eval results.

## Related
- [[wiki/prompt-engineering/prompt-repositories|Prompt Repositories]] — storage layer
- [[wiki/prompt-engineering/prompt-testing|Prompt Testing]] — eval gate
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — regression checks
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — pipeline integration
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — model analog
- [[wiki/prompt-engineering/prompt-debugging|Prompt Debugging]] — debugging
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — context budgeting
