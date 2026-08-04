---
type: "entity"
title: "Critical Instructions"
resource: ""
---
description: "Highest-priority rules that agents must follow regardless of task pressure"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "agent-safety", "instructions"]
timestamp: "2026-07-19T22:41:43Z"

# Critical Instructions

## Summary
Critical instructions are the highest-priority rules in an agent's context: constraints that must hold even when the task, tools, or user requests pull the other way. They matter because agents optimize toward the nearest goal, and without explicit inviolable rules they will trade away safety, honesty, or scope. Defining critical instructions clearly is how teams encode boundaries that survive ambiguity.

## Details
- **Definition** — critical instructions are a small set of non-negotiable rules, such as no destructive commands, no secret exfiltration, and no unapproved external effects.
- **Placement** — they belong at the top of the system context, stated positively and specifically, so they dominate later and weaker instructions.
- **Precedence** — when instructions conflict, the hierarchy must be explicit: system rules outrank task instructions, which outrank tool descriptions.
- **Enforcement** — critical instructions need mechanical support: allowlists, sandboxes, and approval gates, because prompt text alone is not a guarantee.
- **Trade-offs** — too many critical rules dilutes attention; a short, prioritized set is more likely to be followed than a long list.
- **Testing** — teams probe critical instructions with adversarial prompts to confirm the agent refuses or escalates rather than complying.
- **Common failure modes** — buried rules, vague wording that invites interpretation, and instructions that contradict each other.
- **Worked example** — an agent's context states it may only write inside a workspace; when asked to modify a file outside, it refuses and asks for an expanded scope.
- **Practical relevance** — critical instructions are the agent equivalent of invariants: cheap to state, costly to violate.

## Related
- [[wiki/agent-systems/instruction-following|Instruction Following]] — how agents follow rules
- [[wiki/agent-systems/instruction-hierarchy|Instruction Hierarchy]] — precedence of rules
- [[wiki/agent-systems/agent-runtime-security|Agent Runtime Security]] — mechanical enforcement
- [[wiki/prompt-engineering/agentic-rails|Agentic Rails]] — constraining agent behavior
- [[wiki/agent-systems/covert-reasoning|Covert Reasoning]] — when instructions are hidden
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human checkpoints
