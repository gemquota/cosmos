---
type: "concept"
title: "Tool Selection"
description: "Deciding which tool (or whether any tool) an agent should call for the current subgoal"
tags: ["tool-selection", "agents", "tool-calling"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Tool Selection

## Summary
Tool selection is the agent decision of mapping the current goal to the right tool — or to no tool at all. Poor selection is a top source of agent failure: wrong tool, over-eager calling, or tool-shyness.

## Details
- Selection quality depends on tool descriptions, schema clarity, and the model's training; descriptions should state when to use each tool.
- Common patterns: single-shot selection, router models, and procedural if-then policies in the system prompt.
- Failures: hallucinated tools, ambiguous overlap between tools, and loops where the model keeps picking the same wrong tool.
- RSIS3 relevance: the L1 loop's tool registry (exec, apply_patch, web_fetch) is a selection problem mykb can log and learn from.

## Related
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — The capability selection depends on
- [[wiki/prompt-engineering/function-calling|Function Calling]] — The API form of tool selection
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — Schemas shape selection quality
- [[wiki/prompt-engineering/agent-state|Agent State]] — Selection decisions live in agent state
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — MCP standardizes tool discovery
