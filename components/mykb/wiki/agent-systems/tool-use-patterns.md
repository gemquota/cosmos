---
type: "concept"
title: "Tool Use Patterns"
description: "Design patterns for expressing agent actions as discrete, schematized tool calls"
tags: ["tool-use", "function-calling", "agents", "llm", "interaction"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/function-calling"]
---

# Tool Use Patterns

## Summary
Tool use is the mechanism by which an agent turns model output into side effects: declared functions with typed schemas that the model can invoke. It matters because tools are the agent's only reliable channel to the world, and the schema, permission, and error-handling decisions around them dominate real-world agent quality. RSIS3 uses a small, explicit tool surface (exec_command, apply_patch, web_fetch, update_plan) rather than an open-ended action space.

## Details
- **Schema-first**: each tool exposes a name, description, and JSON parameter schema so the model can call it correctly and the runtime can validate calls.
- **Patterns**: single-shot calls, multi-tool sequences, registry-mediated dispatch, and delegated tool sets handed to sub-agents.
- **Guard rails**: permission checks and approval gates sit between model intent and execution; sandboxing limits blast radius.
- Error handling: tool errors are observations, not crashes — they feed the retry logic and the agent loop.
- RSIS3 pattern: exec_command and apply_patch are the workhorses; every call is logged for traceability.
- Worked example: a refactor agent calls grep_search to locate symbols, apply_patch to edit, then exec_command to run tests.

## Related

- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop that consumes tool calls
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — tool results become observations
- [[wiki/llm-agents/tool-registry|Tool Registry]] — centralized discovery and validation of tools
- [[wiki/llm-agents/permission-model|Permission Model]] — authorization around tool execution
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — how tool output feeds the wiki pipeline
