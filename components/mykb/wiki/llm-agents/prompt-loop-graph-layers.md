---
type: "concept"
title: "Prompt Engineering vs Loop Engineering vs Graph Engineering"
description: "Three units of control, stacked: a prompt controls one response, a loop one agent's cycle, a graph many agents"
tags: ["prompt-engineering", "loop-engineering", "graph-engineering", "context-engineering", "harness-engineering"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering/amp/"]
---

# Prompt Engineering vs Loop Engineering vs Graph Engineering

## Summary
The three terms competing for AI engineering job descriptions are not competing techniques — they are three different units of control, stacked. A prompt controls one model response, a loop controls one agent's behavior cycle, and a graph controls the organization of many agents. Each layer preserves the layer beneath it: a prompt does not disappear when a loop is built around it, it just stops being the thing typed by hand.

## Details
- **The stack** — prompt engineering (instruction for a single call, with labeled sections and minimal-but-sufficient information) → context engineering (what token configuration belongs in the window at all; context is a finite resource) → harness engineering (files, tools, memory, feedback for one agent) → loop engineering (the system that repeatedly observes, acts, verifies, recovers) → graph engineering (the organization of many agents).
- **When the prompt layer breaks** — high volume, multi-step tasks, no human available to grade, and outputs feeding the next step automatically. Prompt engineering does not vanish: Anthropic's multi-agent research writeup reports prompting was the primary lever for fixing coordination failures (early versions spawned 50 subagents for simple queries; the fix was prompting, not topology).
- **Loop primitives** — automations, worktrees, skills, plugins/connectors, sub-agents (maker/checker split), plus state outside the conversation; /loop re-runs on a cadence and /goal runs until a written condition is true with a separate small model checking after each turn.
- **The stop condition is the hard part** — a loop that cannot mechanically distinguish done from stuck does not fail loudly; it keeps spending tokens.
- **Two graphs** — the org graph (stable; who owns what) and the work graph (ephemeral; what needs doing right now, splitting and merging as evidence arrives).
- **LangGraph mechanics** — StateGraph over a state schema; add_node, add_edge, add_conditional_edges, START/END, compile; nodes are plain functions receiving state and returning partial updates; context does not cross a node boundary unless an edge carries it.
- **Choosing the layer** — work the questions in order: does a person read every output? (prompt suffices) → can done be checked by something other than a human? (else no stop condition, only a budget) → does the task fit one agent's context and domain? (build the loop) → do independent branches need to run simultaneously? (graph problem).
- **The operator is the wildcard** — two engineers can build an identical loop and get opposite outcomes; one moves faster on work they understand deeply, the other avoids understanding it. The system cannot tell the difference.
- **Published numbers** — multi-agent research systems: +90.2% on an internal eval but ~15× the tokens of chat, with token spend alone explaining 80% of performance variance.

## Related
- [[wiki/llm-agents/loop-engineering|Loop Engineering]] — the loop layer
- [[wiki/llm-agents/graph-engineering|Graph Engineering]] — the graph layer
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — the context layer
- [[wiki/llm-agents/building-effective-agents|Building Effective Agents]] — workflows vs agents
- [[wiki/llm-agents/langgraph-graph-api|LangGraph Graph API]] — graph mechanics
- [[wiki/llm-agents/loop-specification|Loop Specification]] — the formal artifact
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- MarkTechPost, "Prompt Engineering vs Loop Engineering vs Graph Engineering: What Changes at Each Layer", 2026-07-29 — https://www.marktechpost.com/2026/07/29/prompt-engineering-vs-loop-engineering-vs-graph-engineering/
