---
type: "concept"
title: "Instruction Hierarchy"
description: "Ordering instruction sources by authority"
tags: ["instruction-hierarchy", "priorities", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Instruction Hierarchy

## Summary
Instruction hierarchies rank instruction sources: system prompts outrank user prompts, platform rules outrank app rules.

## Details
- Instruction hierarchies rank instruction sources: system prompts outrank user prompts, platform rules outrank app rules.
- Hierarchies mitigate prompt injection and conflicting instructions.
- Enforcement is imperfect but improves robustness.
- RSIS3 relevance: the brief outranks user whims in worker instructions.

## Related
- [[wiki/agent-systems/instruction-following|Instruction Following]] — the behavior
- [[wiki/agent-systems/priority-weights|Priority Weights]] — the weights
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — the threat
- [[wiki/concepts/context-robustness|Context Robustness]] — the property
- [[wiki/agent-systems/scaffold-loops|Scaffold Loops]] — the full treatment of this theme
