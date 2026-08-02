---
type: "concept"
title: "Context Robustness"
description: "Stable behavior across surrounding context changes"
tags: ["context", "robustness", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Context Robustness

## Summary
Context robustness is stable model behavior when surrounding context shifts: system prompts, conversation history, or retrieved passages.

## Details
- Context robustness is stable model behavior when surrounding context shifts: system prompts, conversation history, or retrieved passages.
- Context sensitivity causes both brilliance and brittleness.
- Testing varies context while holding the core question fixed.
- RSIS3 relevance: retrieval context changes as the graph grows; answers must stay stable.

## Related
- [[wiki/concepts/prompt-robustness|Prompt Robustness]] — the general property
- [[wiki/prompt-engineering/context-windows|Context Windows]] — note
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — the retrieval context
- [[wiki/concepts/distribution-shift-ai|Distribution Shift in AI]] — the broad cause
- [[wiki/concepts/goal-misgeneralization|Goal Misgeneralization]] — the full treatment of this theme
