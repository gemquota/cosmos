---
type: "concept"
title: "Cognitive Architecture"
description: "The fixed structure of memory, perception, and control that shapes an agent's cognition"
tags: ["cognitive-architecture", "architecture", "cognition", "design"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Cognitive Architecture

## Summary
A cognitive architecture is the overall blueprint of an intelligent system: its memory systems, perception channels, control loops, and how they interact. It matters because architecture determines what behaviors are even possible — an agent cannot exhibit behaviors its architecture has no pathway for. RSIS3's triad — engine, memory, ideation — is a cognitive architecture at ecosystem scale.

## Details
- Components: working memory, long-term memory, perception, action selection, metacognition. Working memory holds the current task state and binds perception to action; long-term memory supplies knowledge and skill; perception maps raw input into the internal representation; action selection decides what to do next; metacognition monitors and modulates the other components. Every serious architecture is a specific arrangement of these pieces with defined interfaces between them.
- Classic examples: SOAR and ACT-R, the two dominant cognitive architectures from cognitive science, both built around production rules over a working memory, with SOAR emphasizing problem-space search and learning from impasses and ACT-R emphasizing subsymbolic activation spreading and skill acquisition. Blackboard architectures coordinate multiple specialist modules through a shared, dynamically updated workspace — a pattern that maps surprisingly well onto agent frameworks where a control loop reads and writes a shared context.
- Trade-offs: modularity vs. integration — modular designs are testable and swappable but pay for coordination; integrated designs are coherent but hard to change. Fixed vs. learned structure — a fixed architecture is predictable and analyzable; learned structure adapts to the task but is opaque and can drift. The history of the field is largely a series of bets on these axes.
- For agentic systems the architecture question is practical: where does memory live, who can write to it, how does a failure in one loop propagate, and what monitors the monitors? These are design decisions, not implementation details.
- RSIS3 relevance: the L1-L3 loop structure, the persistent mykb layer, and the SPACE ideation engine are exactly the perception-action-memory-metacognition division, and its usage practices are the discipline that keeps the components coordinated. Architecture reviews of RSIS3 should ask the same questions asked of SOAR or ACT-R: what behaviors are structurally possible, and which are structurally precluded?

## Related

- [[wiki/agent-systems/agent-loop|Agent Loop]] — the control cycle at the architecture's core
- [[wiki/concepts/executive-function|Executive Function]] — the control layer of the architecture
- [[wiki/concepts/working-memory|Working Memory]] — a standard architectural component
- [[wiki/agent-systems/blackboard-architecture|Blackboard Architecture]] — a classic architecture pattern
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the knowledge system as an architecture
