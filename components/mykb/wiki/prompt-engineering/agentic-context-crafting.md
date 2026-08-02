---
type: "concept"
title: "Agentic Context Crafting"
description: "Building and maintaining the context an agent sees each step from memory, retrieval, and tool results"
tags: ["agents", "context", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Agentic Context Crafting

## Summary
Building and maintaining the context an agent sees each step from memory, retrieval, and tool results

## Details
- Each step assembles a minimal, relevant context slice rather than appending everything.
- Combines system instructions, working memory, evidence, and action history.
- Prevents context bloat that degrades long-running agents.
- Ties together memory systems and retrieval.

## Related
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — underlying discipline
- [[wiki/llm-agents/memory-hierarchy-agentic|Agentic Memory Hierarchy]] — what feeds context
- [[wiki/llm-agents/conversation-history-management|Conversation History Management]] — history curation
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — retrieval into context
- [[wiki/prompt-engineering/token-budget-planning|Token Budget Planning]] — budget enforcement
