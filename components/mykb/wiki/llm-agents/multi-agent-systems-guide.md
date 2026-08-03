---
type: "concept"
title: "How and When to Build Multi-Agent Systems"
description: "LangChain's synthesis of the Cognition and Anthropic posts: context engineering is critical, read-systems beat write-systems"
tags: ["multi-agent", "context-engineering", "langgraph", "durable-execution", "observability"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://blog.langchain.com/how-and-when-to-build-multi-agent-systems/"]
---

# How and When to Build Multi-Agent Systems

## Summary
Harrison Chase's June 2025 post reconciles the seemingly opposite titles "Don't Build Multi-Agents" (Cognition) and "How we built our multi-agent research system" (Anthropic): both are right because they optimize different task shapes. The post draws two shared insights — context engineering is critical, and multi-agent systems that primarily read are easier than those that write — then maps them to LangGraph and LangSmith.

## Details
- **Context engineering is critical** — the hardest part of multi-agent (or single-agent) applications is communicating context to the models; Cognition's toy examples show subagents make context delivery harder, while Anthropic's long-horizon conversation management (summarizing completed phases into external memory, spawning fresh subagents with clean contexts) is context engineering in practice.
- **Read vs write** — read actions parallelize naturally; write actions face the dual challenge of communicating context between agents and merging outputs coherently. Conflicting read results are reconcilable; conflicting write results produce incompatible artifacts. Anthropic's research system is mostly read; Cognition's coding system is mostly write — hence the different conclusions.
- **Frameworks must expose context** — you need full control over what is passed to the LLM and the order of steps; LangGraph is positioned as a low-level orchestration framework with no hidden prompts and no enforced cognitive architectures.
- **Durable execution** — agents are stateful and errors compound; restarts are expensive, so long-running agents need durable execution that resumes from where the error occurred.
- **Observability** — non-deterministic agent decisions make debugging hard ("not finding obvious information" needs tracing of queries, sources, and tool failures); production tracing is the fix.
- **Evaluation** — start small (~20 datapoints), use LLM-as-judge to automate scoring, and keep human testing; these map to LangSmith datasets, server-side judges, and annotation queues.
- **When multi-agent works** — breadth-first queries, heavy parallelization, information exceeding single context windows, and interfacing with numerous complex tools; not for shared-context domains, many inter-agent dependencies, or mostly sequential coding.

## Related
- [[wiki/llm-agents/dont-build-multi-agents|Don't Build Multi-Agents]] — the read/write contrast
- [[wiki/llm-agents/multi-agent-research-systems|Multi-Agent Research Systems]] — Anthropic's system
- [[wiki/llm-agents/langgraph-graph-api|LangGraph Graph API]] — the orchestration layer
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — the shared insight
- [[wiki/llm-agents/graph-engineering|Graph Engineering]] — topology as the design object
- [[wiki/llm-agents/agent-logs|Agent Logs]] — tracing and observability
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- LangChain (Harrison Chase), "How and when to build multi-agent systems", 2025-06-16 — https://blog.langchain.com/how-and-when-to-build-multi-agent-systems/
