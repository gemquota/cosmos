---
type: "concept"
title: "Tool Discipline"
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---
description: "Restricting which tools an agent may use, when, and with what permissions"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "agent-safety", "tool-use"]

# Tool Discipline

## Summary
Tool discipline is the practice of tightly controlling which tools an agent can invoke, what arguments are allowed, and what effects are permitted. It matters because tool access is where agent capability becomes real-world impact, and unconstrained access turns small mistakes into large damage. Disciplined tool use bounds blast radius while preserving the agent's usefulness. It is a combination of policy, validation, and observability rather than a single setting.

## Details
- **Definition** — tool discipline covers the allowlist of tools, their parameter constraints, and the policies governing when each may be used.
- **Least privilege** — agents should receive the smallest tool set that can complete their task, added incrementally rather than all at once.
- **Parameter validation** — tools should validate inputs against schemas so an agent cannot smuggle in unexpected paths, flags, or targets.
- **Scoping** — filesystem, network, and command tools should be confined to workspaces and allowlists rather than granted global reach.
- **Approval gates** — high-impact actions, such as external sends or destructive commands, should require explicit human approval.
- **Observation** — logging every tool call with arguments and results makes misuse visible and auditable.
- **Prompt resistance** — tool policies should survive adversarial prompts that try to widen scope through phrasing or indirect instructions.
- **Common failure modes** — over-provisioned tools "just in case", prompts that can be tricked into tool misuse, and tools that silently accept dangerous defaults.
- **Worked example** — a coding agent can edit files only under a workspace, run tests, and read documentation; a deploy command exists but requires approval.
- **Practical relevance** — tool discipline is the difference between a helpful assistant and an unconstrained actor.

## Related
- [[wiki/agent-systems/agent-runtime-security|Agent Runtime Security]] — enforcing boundaries
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — isolating effects
- [[wiki/prompt-engineering/function-calling|Function Calling]] — how tools are invoked
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human checkpoints
- [[wiki/agent-systems/instruction-following|Instruction Following]] — respecting limits
- [[wiki/testing/penetration-testing|Penetration Testing]] — probing tool exposure
