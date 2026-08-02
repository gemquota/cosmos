---
type: "concept"
title: "Agent Orchestration Frameworks"
description: "Software platforms for defining, running, and monitoring agent workflows"
tags: ["agents", "orchestration", "frameworks", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/langchain-ai/langgraph", "https://arxiv.org/abs/2304.03442"]
---

# Agent Orchestration Frameworks

## Summary
Agent orchestration frameworks provide the runtime for agent workflows: state management, tool invocation, retries, and human-in-the-loop hooks. They abstract the plumbing so developers express agents as graphs or declarative workflows. Choosing a framework is a bet on its state model, ecosystem, and debugging story.

## Details
- **Graph-based** — LangGraph models workflows as stateful graphs with explicit nodes, edges, and checkpoints, enabling human interrupts and time travel.
- **Code-first** — AutoGen and CrewAI express agents as Python objects and crews with roles and tasks; DSPy focuses on optimizing prompts programmatically.
- **Protocol-based** — the Model Context Protocol standardizes how agents connect to tools and data servers across implementations.
- **Worked example** — a graph with nodes fetch → analyze → draft → review and an edge that pauses for human approval before publish.
- **Selection criteria** — checkpointing, replay, observability, streaming, and the cost of vendor lock-in.
- **mykb relevance** — orchestration choices affect how RSIS3-like recursion, memory writes, and approval gates get implemented.

## Related
- [[wiki/ml-frameworks/langgraph-llamaindex|LangGraph and LlamaIndex]] — graph runtime and data framework
- [[wiki/ml-frameworks/dspy-autogen-crewai|DSPy, AutoGen, and CrewAI]] — code-first orchestration libraries
- [[wiki/ml-frameworks/langchain-framework|LangChain Framework]] — the ecosystem most frameworks build on
- [[wiki/agent-systems/multi-agent-systems|Multi-Agent Systems]] — what orchestration frameworks run
- [[wiki/agent-systems/agent-pipelines|Agent Pipelines]] — linear multi-stage orchestration
- [[wiki/agent-systems/agent-templates|Agent Templates]] — related concept in this cluster
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/concepts/triad-architecture|Triad Architecture]] — the RSIS3/mykb architecture it serves
