---
type: "entity"
title: "System Instruction Design"
tags: ["prompt", "system-instruction", "role-definition", "guidelines"]
source: ["session-4b35bd59.md", "session-8f62822c.md"]
---

# System Instruction Design

The art and practice of crafting system-level instructions for LLM agents, derived from patterns across 58+ sessions.

## Patterns Observed

### Role Definition
```
You are a [role] that specializes in [domain].
Your primary responsibilities are:
1. [responsibility]
2. [responsibility]
```

### Constraint Listing
```
Rules:
- Never [forbidden action]
- Always [required action]
- When [condition], [expected behavior]
```

### Output Schema
```
When generating [output type], use this format:
- Field: [description]
- Field: [description]
```

## Effective Design Elements

- **Clear hierarchy** — Role → Responsibilities → Constraints → Output
- **Actionable rules** — "Do X" not "Consider doing X"
- **Negative constraints** — What NOT to do is as important as what to do
- **Examples** — Concrete before/after demonstrations
- **Scoped authority** — What the agent can/cannot modify

See also: [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/agents-dot-md|AGENTS.md Pattern]], [[wiki/prompt-engineering/categories/patterns/subcategories/prompt-techniques/iterative-refinement|Iterative Refinement]]
