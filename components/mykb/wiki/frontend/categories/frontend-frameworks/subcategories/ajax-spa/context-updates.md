---
status: "growing"
type: "entity"
title: "Context Updates"
description: "Context"
tags: ["entity", "api", "ast", "auth", "cdn", "cli"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

## Context Updates

Context — the information provided to an LLM alongside a query. Sessions show context window management, summarization, and pruning strategies.

**Related topics:** api, auth, cdn, cli

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Frontend]] › [[wiki/web-platforms/00-index|Frontend Frameworks]] › Context Updates

## Overview

In LLM applications, context is everything the model can see when it generates a response: system instructions, conversation history, retrieved documents, and tool results. Context updates are the decisions about what enters that window and what is removed as the session grows. Since the window is finite and tokens cost money and latency, updates must balance completeness against budget.

## Update Strategies

- **Summarization**: compress older turns into a short digest that preserves key facts and decisions.
- **Pruning**: drop turns below a relevance threshold, keeping recent or high-signal exchanges.
- **Retrieval injection**: pull in fresh documents or results at query time so the window reflects current state.
- **Pinning**: keep critical instructions or invariants in a protected region that summarization cannot evict.

## Trade-offs

- Larger context improves recall but raises cost, latency, and the chance of distraction.
- Aggressive pruning risks losing constraints stated early in the conversation.
- Updates should be traceable so a later audit can reconstruct what the model saw.
## Operational Concerns

Updates should be deterministic and observable. Log which turns were summarized or pruned and why, so a bad update can be replayed and reversed. Version the context snapshot alongside each response: any tool that generates output from a window should record the window identity in its telemetry. Prompt caching works best when stable prefixes stay untouched, so updates that append rather than rewrite preserve cache hits. When retrieval is involved, document chunk boundaries determine what can be summarized cleanly, so summarization should align with chunk structure.

- [[wiki/llm-agents/prompt-caching|Prompt Caching]] — stable prefixes make updates cheaper
- [[wiki/llm-agents/traceability|Traceability]] — reconstructing what the model saw
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — where updates are orchestrated
- [[wiki/data-storage/chunking-strategies|Chunking Strategies]] — how documents are segmented for retrieval

## Related Concepts

- [[wiki/llm-agents/context-management|Context Management]] — agent patterns for window limits
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — external memory that survives updates

## Related Entities

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ace|Ace 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrains|Jetbrains 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/csv|Csv 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
