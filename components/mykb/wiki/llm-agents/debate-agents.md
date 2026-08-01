---
type: "concept"
title: "Debate Agents"
description: "Multiple agents arguing opposing positions to surface the best answer"
tags: ["debate", "multi-agent", "verification", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Debate Agents

## Summary
Debate pits agents against each other: one proposes an answer, another challenges it, and the exchange exposes weaknesses. It matters because adversarial review is stronger than self-review. It is one topology of multi-agent orchestration.

## Details
- Formats: two-agent debate, judge-supervised rounds, multi-round rebuttal.
- Effective for factual questions and code review.
- Cost: several agents and many rounds of tokens.
- Open questions: judging quality and premature consensus.

## Related
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — the coordination context
- [[wiki/llm-agents/expert-consultation|Expert Consultation]] — cooperative vs. adversarial querying
- [[wiki/llm-agents/self-consistency|Self-Consistency]] — agreement-based aggregation
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]] — shared-context debate
- [[wiki/concepts/calibration|Calibration]] — honest confidence in arguments
