---
type: "concept"
title: "Tool Calling"
description: "The general capability of an LLM to request invocations of external tools during a conversation"
tags: ["tool-calling", "agents", "llm", "function-calling"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://docs.anthropic.com/en/docs/build-with-claude/tool-use"]
---

# Tool Calling

## Summary
Tool calling (or tool use) is the model's ability to emit structured requests to external functions — search, code execution, APIs — mid-conversation, with results returned as new messages. It turns a text-only model into an agent core that can observe and act.

## Details
- Anthropic's tool-use docs describe the pattern: define tools with input schemas, let the model decide when to call them, stop execution at the tool boundary, and feed results back.
- Tool calls are model-issued but host-executed, so safety, rate limits, and permissions live in the host layer.
- Interleaving: a single assistant turn can contain text plus several tool calls, and the conversation alternates until the model produces a final answer.
- Common tool families for RSIS3-style agents: filesystem, shell, web fetch, search, and memory/wiki read-write.
- Failure modes: missing required arguments, hallucinated tool names, loops, and tool-result bloat — all mitigated by schema strictness and token budgets.
- Tool calling is the execution layer beneath prompt chaining and agent loops: chains decide the stage, tools execute the action.

## Related
- [[wiki/prompt-engineering/function-calling|Function Calling]] — The OpenAI-branded form of the same capability
- [[wiki/prompt-engineering/tool-selection|Tool Selection]] — Choosing the right tool for the current goal
- [[wiki/prompt-engineering/agent-state|Agent State]] — Tool results mutate the conversation state
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — Standard interface for tool servers
- [[wiki/ml-frameworks/streaming-responses|Streaming Responses]] — Tool-call events stream to the client incrementally
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — Schemas the model uses to emit valid calls
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Tool outcomes are captured into wiki sources
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Tool outcomes enrich the wiki graph
