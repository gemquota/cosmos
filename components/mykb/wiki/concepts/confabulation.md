---
type: "concept"
title: "Confabulation"
description: "Producing plausible but fabricated explanations without intent to deceive"
tags: ["confabulation", "hallucination", "memory", "reasoning"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Confabulation

## Summary
Confabulation is when an agent generates a coherent, confident account that does not match reality — often filling memory gaps after the fact. It differs from deliberate lying because the agent believes the account. In LLM agents it overlaps with hallucination and is a key evaluation target.

## Details
- Common after context loss or when recall fails: the model fills the gap smoothly.
- Dangerous in agent logs: fabricated 'what happened' corrupts learning.
- Mitigation: grounding claims in retrieved evidence and traceable records.
- Open questions: distinguishing confabulated memory from creative synthesis.

## Related
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — reflection can catch confabulation
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — the mitigation toolkit
- [[wiki/concepts/calibration|Calibration]] — confabulated claims are overconfident
- [[wiki/concepts/episodic-memory|Episodic Memory]] — the memory being confabulated
- [[wiki/concepts/metacognition|Metacognition]] — monitoring for invented content
