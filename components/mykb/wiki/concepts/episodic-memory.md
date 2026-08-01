---
type: "concept"
title: "Episodic Memory"
description: "Records of specific events and sessions an agent has experienced"
tags: ["episodic-memory", "memory", "sessions", "history"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Episodic Memory

## Summary
Episodic memory stores concrete episodes: what happened, when, and with what outcome. It matters because agents need to recall their own history to learn from it. RSIS3 pulses and mykb session notes are episodic memory in practice.

## Details
- Episodes include context, actions, observations, and outcome.
- Query patterns: 'what did we try last time and why did it fail?'
- Linked to temporal analysis for rising/falling topic detection.
- Open questions: granularity of episodes and retention policy.

## Related
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — the architecture that uses it
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]] — continuity depends on episode recall
- [[wiki/concepts/semantic-memory|Semantic Memory]] — abstractions distilled from episodes
- [[wiki/concepts/declarative-memory|Declarative Memory]] — the superclass it belongs to
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — how the wiki stores episodic notes
