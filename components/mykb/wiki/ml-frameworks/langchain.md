---
type: "concept"
title: "LangChain"
description: "A framework for composing LLM applications: chains, agents, retrieval, and integrations"
tags: ["langchain", "llm", "framework", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# LangChain

## Summary

LangChain is a framework for building LLM applications: chains, agents, retrievers, memory, and integrations, plus LangGraph for stateful graph workflows. It accelerates prototyping and standardizes components — and its abstractions can obscure what is actually happening.

## Details
- Mechanism: components compose: models (provider-agnostic), prompts (templates), retrievers (vector stores), tools, memory (conversation state), and chains/agents that orchestrate them; LangGraph models agent flows as explicit state machines with nodes and edges, enabling loops, branching, and human-in-the-loop checkpoints.
- Concrete example: a RAG chain: load docs → split → embed → retrieve → prompt → model; an agent with tools: model decides tool calls, executes, loops; a LangGraph workflow adds a review node where a human approves before final output.
- Failure modes: abstraction leakage — upgrades and version mismatches break chains; hidden defaults (which model, which prompt) making behavior mysterious; over-abstraction that hides costs and calls (fewer layers = clearer telemetry); and framework lock-in when logic lives in proprietary abstractions.
- Operational tradeoffs: LangChain trades a learning curve and abstraction risk for velocity and ecosystem breadth; the discipline is keeping the core logic framework-light (plain functions + explicit control flow), using the framework for integration plumbing, and pinning versions.
- RSIS3/mykb relevance: the wiki's prototypes may use LangChain for plumbing, but the loop's production paths keep core logic explicit and framework-independent.
- Telemetry: instrument every chain/agent step (prompt, model call, tool result, cost) at your own layer; framework-internal tracing is convenient but your schema must own the events.
- Migration risk: framework majors restructure APIs; isolate framework usage behind small adapters so a major upgrade is a plumbing change, not a rewrite.

## Related
- [[wiki/ml-frameworks/llamaindex|LlamaIndex]] — The retrieval-focused sibling framework
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — The pattern chains implement
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — The RAG pattern LangChain standardizes
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Agent tool loops in the framework
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — MCP integration in LangChain
