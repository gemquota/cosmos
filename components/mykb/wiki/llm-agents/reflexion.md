---
type: "concept"
title: "Reflexion"
description: "Verbal self-critique that carries lessons into the next attempt"
tags: ["reflexion", "reflection", "self-improvement", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Reflexion

## Summary
Reflexion is a pattern where the agent evaluates its failed attempt in words, stores the lesson, and uses it to retry. It matters because the critique, not just the score, drives improvement. It is the lightweight cousin of RSIS3's L2 session loop.

## Details
- Loop: attempt → evaluate → verbalize failure → retry with the lesson.
- Lessons can persist across episodes as episodic memory.
- Works for code, math, and interactive tasks.
- Open questions: when reflection loops converge or thrash.

## Related
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — the architecture that uses reflexion
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — reflexion at system scale
- [[wiki/concepts/episodic-memory|Episodic Memory]] — where lessons are stored
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — the reasoning it critiques
- [[wiki/concepts/metacognition|Metacognition]] — the underlying ability
