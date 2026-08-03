---
type: "concept"
title: "Reflexion"
description: "Verbal self-critique that carries lessons into the next attempt"
tags: ["reflexion", "reflection", "self-improvement", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Reflexion

## Summary

Reflexion is a pattern where the agent evaluates its failed attempt in words, stores the lesson, and uses it to retry — the critique, not just the score, drives improvement. It is the lightweight cousin of RSIS3's L2 session loop.

## Details
- Mechanism: the loop is attempt → evaluate → verbalize failure → retry with the lesson: the agent attempts a task, an evaluator (test, environment, human) scores it, the agent reflects in natural language on what went wrong, and the reflection is injected into the next attempt's context; lessons can persist across episodes as episodic memory.
- Concrete example: a coding agent fails a test, reflects that it assumed a dict was ordered in Python < 3.7, and the next attempt fixes the assumption; a math agent missteps, reflects on the formula error, and retries with the corrected reasoning; the reflection library grows, so repeated task classes get solved on the first try.
- Failure modes: reflections that are generic ("I should be more careful") rather than specific and actionable; thrash — the agent over-corrects and breaks what worked; reflection loops without a stop condition burning budget; and lessons that do not persist across sessions (episodic storage needed).
- Operational tradeoffs: reflexion converts failures into training data for the agent at the cost of retry iterations and evaluation infrastructure; the discipline is specific reflections, a bounded retry budget, and persisted lessons tied to task classes.
- RSIS3/mykb relevance: reflexion is the in-agent analog of the L2 loop — the wiki's syntheses capture the durable lessons so the improvement persists beyond the session.
- Reflection quality rubric: require reflections to name the specific error, the correction, and the evidence — generic reflections do not measurably improve retries.
- Persistence format: store lessons as structured notes (task class, failure mode, fix) so they are retrievable at the right moment rather than buried in session history.

## Related
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — the architecture that uses reflexion
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — reflexion at system scale
- [[wiki/concepts/episodic-memory|Episodic Memory]] — where lessons are stored
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — the reasoning it critiques
- [[wiki/concepts/metacognition|Metacognition]] — the underlying ability
