---
type: "concept"
title: "Expert Systems"
description: "Classical rule-based systems encoding human expertise in a domain"
tags: ["expert-systems", "rules", "knowledge-base", "classical-ai"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Expert Systems

## Summary
Expert systems encode domain expertise as a knowledge base of rules plus an inference engine (typically forward or backward chaining) to apply them. They matter because they were the first successful applied AI and still define the knowledge-engineering trade-offs. Modern agents reuse the pattern with learned knowledge.

## Details
- Components: knowledge base, inference engine, explanation facility.
- Successes: MYCIN, XCON; limits: brittle, costly to maintain.
- Contrast: LLM agents trade rules for learned, flexible reasoning.
- Open questions: hybrid expert rules with LLM judgment.

## Related
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — rule firing in a loop
- [[wiki/concepts/production-rules|Production Rules]] — the knowledge representation
- [[wiki/concepts/forward-chaining|Forward Chaining]] — the inference engine
- [[wiki/concepts/backward-chaining|Backward Chaining]] — goal-driven inference
- [[wiki/llm-agents/expert-consultation|Expert Consultation]] — the modern specialist pattern
