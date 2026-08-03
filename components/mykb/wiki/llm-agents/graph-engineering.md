---
type: "concept"
title: "Graph Engineering"
description: "Designing multi-agent organizations as programmable graphs — org graph vs work graph, nodes/edges/state, governance"
tags: ["graph-engineering", "multi-agent", "orchestration", "org-graph", "work-graph", "langgraph"]
timestamp: "2026-08-03T12:00:00Z"
status: "growing"
source: ["https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026", "https://www.truefoundry.com/blog/graph-engineering-enterprise-guide", "https://www.aibuilderclub.com/blog/graph-engineering-guide-2026"]
---

# Graph Engineering

## Summary
Graph engineering is the design and operation of a multi-agent system as an explicit graph: which nodes exist (agents, deterministic functions, routers, joins, human checkpoints), which transitions are permitted, and how runtime work graphs form and mutate. The term crystallized around Peter Steinberger's July 18, 2026 question — "Are we still talking loops or did we shift to graphs yet?" — and names the layer above loop engineering: loops make agent behavior programmable; graphs make agent organizations programmable.

## Details
- **Two graphs at once** — the org graph is stable (long-lived agents with named roles, zone ownership, preserved context, edges that change only on redeploy) and answers *who*; the work graph is ephemeral (task nodes that split, merge, cancel, and reorder as evidence arrives) and answers *what, right now*.
- **What a loop is vs a graph** — a loop is a single agent's behavioral contract (trigger → act → verify → retry → exit); a graph is an organization of agents where each node runs its own loop and edges define data flow, dependencies, and failure routing. A single loop is the smallest graph — one node with an edge back to itself.
- **Dynamic agent orgs** — graphs can rewrite themselves mid-run: spawn a new node when scope expands, collapse a merger when branches converge, route to a fallback on unrecoverable failure, reorder edges when priorities shift.
- **Not knowledge graphs** — this is not GraphRAG or entity-relationship modeling; knowledge graphs structure what a system *knows*, graph engineering structures who the system *is*.
- **Not a new capability** — LangGraph, AutoGen, and Google ADK did graph orchestration before the label existed; what is new is shared vocabulary for node/edge/state decisions frameworks always forced.
- **Not a default** — most tasks are one job with one verifier (a loop); reaching for a graph first buys a distributed-systems problem. Loops are forgiving; graphs force you to model the workflow explicitly, including failure modes.
- **Mechanics** — in LangGraph a StateGraph is declared over a state schema; nodes register with add_node, edges wire with add_edge/add_conditional_edges, START/END marked, then compile. Context does not cross a node boundary unless an edge carries it — that is the entire failure mode.
- **Enterprise concerns** — governance needs resolved identity per node ("the graph did it" is not an audit answer), tool-level registry permissions, guardrail hooks, and propagated graph_id/run_id/node_id identifiers; cost control must budget fan-out, retries, and dynamic subtasks explicitly.
- **Patterns** — advisor-orchestrator (one planner + many workers, ~92% quality at ~63% price on SWE-bench Pro) and zone defense (long-lived specialists owning auth/data/API/frontend zones with no context bleed).

## Related
- [[wiki/llm-agents/loop-engineering|Loop Engineering]] — the layer below
- [[wiki/llm-agents/prompt-loop-graph-layers|Prompt vs Loop vs Graph]] — the full stack
- [[wiki/llm-agents/multi-agent-research-systems|Multi-Agent Research Systems]] — production org graph
- [[wiki/llm-agents/langgraph-graph-api|LangGraph Graph API]] — the reference implementation
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — orchestrator patterns
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — node-level delegation
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — synthesis

## Sources
- explainx.ai, "Graph Engineering: Wire Multi-Agent Orgs After Loops", 2026-07-18 — https://explainx.ai/blog/graph-engineering-ai-agents-multi-agent-organizations-2026
- TrueFoundry, "Graph Engineering for Multi-Agent Systems: Architecture, Governance, and Observability", 2026-07-20 — https://www.truefoundry.com/blog/graph-engineering-enterprise-guide
- AI Builder Club, "Graph Engineering Guide (2026)" — https://www.aibuilderclub.com/blog/graph-engineering-guide-2026
