---
type: "concept"
title: "LangGraph Graph API"
description: "State, nodes, and edges in LangGraph: message-passing super-steps, StateGraph, schemas, and reducers"
tags: ["langgraph", "graph-api", "stategraph", "state", "nodes", "edges", "reducers"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://docs.langchain.com/oss/python/langgraph/graph-api"]
---

# LangGraph Graph API

## Summary
LangGraph models agent workflows as graphs defined by three components: state (the shared data structure snapshot), nodes (functions that read state, do work, and return updates), and edges (functions deciding which node runs next). Nodes and edges are plain functions — they can contain an LLM or ordinary code. The reference implementation behind graph engineering's vocabulary, the Graph API shows how message passing turns a graph into a general program.

## Details
- **Message passing and super-steps** — inspired by Google's Pregel, execution proceeds in discrete super-steps: nodes active in the same super-step run in parallel, sequential nodes belong to separate super-steps; a node activates when it receives a message on an incoming channel, runs, and the graph halts when all nodes are inactive and no messages are in transit.
- **StateGraph** — the main class, parameterized by a user-defined state object; you define state, add nodes and edges, then compile (structural checks like orphaned nodes plus runtime args like checkpointers and breakpoints).
- **State schema** — TypedDict is the documented default; dataclasses give default values; Pydantic BaseModel adds recursive validation but is less performant. `create_agent` does not support Pydantic state.
- **Multiple schemas** — an internal schema holds all channels; explicit input and output schemas are subsets constraining what invoke accepts/returns; nodes can declare additional private channels. Private channels are hidden from invoke but visible when streaming with stream_mode="values" unless output_keys restrict them.
- **Reducers** — each state key has an independent binary reducer (left = accumulated current value, right = latest node update); the default is override, but Annotated types can compose (e.g., append) updates across nodes.
- **The failure mode in one line** — context does not cross a node boundary unless an edge carries it; missing edges produce downstream agents acting without needed information.

## Related
- [[wiki/llm-agents/graph-engineering|Graph Engineering]] — the discipline this implements
- [[wiki/llm-agents/prompt-loop-graph-layers|Prompt vs Loop vs Graph]] — the stack
- [[wiki/llm-agents/multi-agent-systems-guide|How and When to Build Multi-Agent Systems]] — the framework's rationale
- [[wiki/llm-agents/multi-agent-research-systems|Multi-Agent Research Systems]] — production usage
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — workflow-level patterns
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- LangChain docs, "Graph API overview" — https://docs.langchain.com/oss/python/langgraph/graph-api
