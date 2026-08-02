---
type: "concept"
title: "Episodic Memory"
description: "Records of specific events and sessions an agent has experienced"
tags: ["episodic-memory", "memory", "sessions", "history"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Episodic_memory", "https://plato.stanford.edu/entries/memory/"]
---

# Episodic Memory

## Summary
Episodic memory stores concrete episodes: what happened, when, and with what outcome. It matters because agents need to recall their own history to learn from it. RSIS3 pulses and mykb session notes are episodic memory in practice.

## Details
- Episodes include context, actions, observations, and outcome.
- Query patterns: 'what did we try last time and why did it fail?'
- Linked to temporal analysis for rising/falling topic detection.
- Open questions: granularity of episodes and retention policy.
- Episodic memory stores specific events with their time, place, and context — the 'what happened when' layer of memory.
- It contrasts with semantic memory: episodic records the episode itself, semantic extracts the general knowledge from many episodes.
- Autobiographical recall and memory consolidation both operate on episodic traces, and episodic memory is what supports mental time travel.
- In agents, episodic memory maps to session logs and pulse records that let the system recall what it did and what resulted.
- **Worked example / comparison** — Worked example — the wiki's session logs are episodic memory: they record that on this date a link-fix pass ran, which files it touched, and what the graph metrics showed afterward.
- For mykb, episodic memory is documented as the event-record layer that semantic-memory and procedural-memory build upon.

## Related
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]]
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]]
- [[wiki/concepts/semantic-memory|Semantic Memory]]
- [[wiki/concepts/declarative-memory|Declarative Memory]]
- [[wiki/concepts/mykb-research-report|Mykb Research Report]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
