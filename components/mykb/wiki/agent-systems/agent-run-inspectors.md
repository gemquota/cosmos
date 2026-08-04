---
type: "concept"
title: "Agent Run Inspectors"
description: "Tools to inspect a completed or in-flight agent run step by step"
tags: ["run-inspectors", "agents", "debugging", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Agent Run Inspectors

## Summary
Agent run inspectors are tools that examine a completed or in-flight agent run step by step, showing inputs, outputs, and tool calls. They matter because agent behavior is opaque by default, and debugging requires looking inside the loop rather than at final results. Inspection is the interface between a running agent and the humans who must trust it. Inspection is what makes agent behavior reviewable rather than mysterious.

## Details
- **Definition** — a run inspector presents an agent run as a navigable sequence of steps, each with its prompt, tool call, observation, and result.
- **Granularity** — inspectors support multiple levels, from high-level stage summaries down to individual token-level or tool-response details.
- **Live and replay** — inspectors work on in-flight runs for intervention and on recorded runs via deterministic-replay for post-mortem analysis.
- **Worked example** — an inspector shows a research agent making three redundant web calls; the team spots the loop and adds a deduplication step.
- **Value** — inspectors accelerate root-cause analysis by making wasted calls, repeated errors, and context bloat visible instead of hidden.
- **Integration** — inspectors consume agent-logs-and-audits data and feed session-replay-agents for whole-session analysis.
- **Failure modes** — missing step metadata, non-deterministic replays, and overwhelming detail all undermine inspection usefulness.
- **Practical relevance** — run inspection is the debugging counterpart to trace visualization and a required capability for accountable agent operations.
- **Context views** — inspectors should show the context each step saw, since context drift causes many failures.
- **Search** — filtering steps by tool, status, or time makes large runs navigable.
- **Annotation** — teams should be able to mark steps with notes for later analysis.
- **Failure example** — an inspector that hides tool arguments cannot show why a harmful call was made.

## Related
- [[wiki/agent-systems/agent-trace-visualization|Agent Trace Visualization]] — the visual layer over run data
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — replaying runs for inspection
- [[wiki/agent-systems/session-replay-agents|Session Replay for Agents]] — session-level analysis
- [[wiki/agent-systems/agent-logs-and-audits|Agent Logs and Audits]] — the underlying record
- [[wiki/prompt-engineering/prompt-debugging|Prompt Debugging]] — prompt-level inspection
