---
type: "concept"
title: "Working Memory"
description: "The small, active set of information an agent holds while reasoning"
tags: ["working-memory", "memory", "context", "cognition"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Working Memory

## Summary
Working memory is the limited, immediately accessible information an agent uses during a task — in LLM terms, the current context window. It matters because it bounds how much can be considered at once. Managing it well is the core of context management.

## Details
- Capacity is limited; overflow degrades performance (cognitive load).
- Content is chosen by attention and retrieval, then held until task completion.
- RSIS3 relevance: mykb offloads overflow so working memory stays focused.
- Open questions: optimal refresh policies and compression strategies.

## Related
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — the pattern that extends working memory
- [[wiki/llm-agents/context-management|Context Management]] — the practice of curating it
- [[wiki/concepts/episodic-memory|Episodic Memory]] — what gets written out when context ends
- [[wiki/concepts/cognitive-load|Cognitive Load]] — the cost of overload
- [[wiki/concepts/attention-mechanisms|Attention Mechanisms]] — what gets selected into it
