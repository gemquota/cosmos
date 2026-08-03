---
type: "concept"
title: "Tool Selection"
description: "Deciding which tool (or whether any tool) an agent should call for the current subgoal"
tags: ["tool-selection", "agents", "tool-calling"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Tool Selection

## Summary
Tool selection is the agent decision of mapping the current goal to the right tool — or to no tool at all. Poor selection is a top source of agent failure: wrong tool, over-eager calling, or tool-shyness; selection quality depends on tool descriptions, schema clarity, and the model's training.

## Details
- Mechanism: the model receives tool schemas with descriptions and picks a call (or none); descriptions should state when to use each tool and what it returns; selection can be single-shot (one decision per step), routed (a router model picks a specialist), or procedural (if-then policies in the system prompt that constrain the choice).
- Concrete example: an agent with exec, apply_patch, and web_fetch tools must choose — edit a file via apply_patch, not exec; a description that says use apply_patch for file edits and exec for commands reduces ambiguity; a router model dispatches a coding subtask to the coding agent; a policy says never call exec before apply_patch for the same file.
- Failure modes: hallucinated tools (calling a tool that does not exist); ambiguous overlap between tools (two tools that both look applicable); loops where the model keeps picking the same wrong tool; tool-shyness where the model reasons instead of calling the obvious tool; selection drift as schemas grow and descriptions stale.
- Tradeoffs: rich descriptions improve selection at the cost of tokens and surface area; the alternative, procedural policies, is deterministic and rigid; the mature pattern is clear, distinct tool descriptions plus policies for the risky boundaries, with selection logged for learning.
- Operational notes: log selection decisions and outcomes, refine descriptions from failures, and eval selection on a held-out task set.
- RSIS3 relevance: the L1 loop's tool registry (exec, apply_patch, web_fetch) is a selection problem mykb can log and learn from — the same loop that improves its own tool choices.

## Related
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — The capability selection depends on
- [[wiki/prompt-engineering/function-calling|Function Calling]] — The API form of tool selection
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — Schemas shape selection quality
- [[wiki/prompt-engineering/agent-state|Agent State]] — Selection decisions live in agent state
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — MCP standardizes tool discovery
