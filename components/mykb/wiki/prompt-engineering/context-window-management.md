---
type: "concept"
title: "Context Window Management"
description: "Strategies for fitting the most useful information into a model context window"
tags: ["context", "llm", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Context Window Management

## Summary
Strategies for fitting the most useful information into a model context window

## Details
- Budget attention across system prompts, retrieved evidence, tools, and history.
- Management includes truncation, summarization, and selective retrieval.
- Token budgets make context allocation explicit and auditable.
- Good management directly improves answer quality and cost.

## Related
- [[wiki/prompt-engineering/token-budget-planning|Token Budget Planning]] — budgeting mechanism
- [[wiki/prompt-engineering/context-compression|Context Compression]] — shrinking existing content
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — the discipline it serves
- [[wiki/llm-agents/conversation-history-management|Conversation History Management]] — history curation
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — external context source
