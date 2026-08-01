---
type: "concept"
title: "Attention Mechanisms"
description: "Selection processes that decide what information an agent focuses on"
tags: ["attention", "selection", "cognition", "context"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Attention Mechanisms

## Summary
Attention mechanisms allocate processing and context to the most relevant information, whether in the model's internal computation or the agent's retrieval choices. They matter because selection determines what the agent actually considers. Attention is what keeps context manageable.

## Details
- Internal: transformer attention weights select relevant tokens.
- External: agent-level attention chooses which files, memories, and tools to consult.
- RSIS3 relevance: retrieval selection and prompt construction are attention policies.
- Open questions: aligning agent-level attention with task relevance.

## Related
- [[wiki/llm-agents/context-management|Context Management]] — the practice of focusing attention
- [[wiki/concepts/working-memory|Working Memory]] — the selected set attention fills
- [[wiki/concepts/perception-loop|Perception Loop]] — attention applied at perception time
- [[wiki/concepts/cognitive-load|Cognitive Load]] — attention as load reduction
- [[wiki/concepts/metacognition|Metacognition]] — attending to one's own process
