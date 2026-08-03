---
type: "concept"
title: "Concept Mapping"
description: "Diagram that links concepts with labeled relations to expose a domain's structure"
tags: ["concept-map", "diagram", "knowledge-representation", "relations"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Concept Mapping

## Summary
Concept mapping goes beyond mind maps by labeling the edges: 'spaced repetition *increases* retention'. It externalizes the relational structure of a topic and makes gaps visible. Where a mind map shows association, a concept map shows a claim — and claims are what a knowledge base should record.

## Details
- **Parts** — concept nodes, labeled directed edges, and cross-links between branches; propositions are node-edge-node triples. A map of "forgetting" might contain: retrieval practice *strengthens* memory traces; interference *weakens* traces; sleep *consolidates* traces — each edge is a testable proposition.
- **Use** — assessment, learning design, and planning; the labels force precision about how ideas connect. In planning, a concept map of a system's dependencies exposes which nodes have many outgoing edges (drivers) and which are leaves (leaf consequences), guiding where to intervene.
- **Concrete example** — mapping the RSIS3 loop architecture as a concept map yields edges like "L1 *generates* telemetry" and "telemetry *feeds* L2", and the map immediately reveals a missing edge when a loop's output is not consumed anywhere — a structural gap a prose description would hide.
- **Failure modes** — unlabeled edges that degrade into a mind map; maps that grow so dense they become unreadable hairballs; edge labels that disagree with the source material (the map then asserts something the notes do not); and mapping for its own sake, producing diagrams nobody updates after the source notes change.
- **Tradeoffs** — hand-drawn maps are excellent for one-off sense-making and teaching, but they rot: every note change requires redrawing. Machine-readable graphs (typed links in a knowledge base) update by construction and scale, at the cost of a less expressive canvas for visual reasoning.
- **Agent relevance** — a concept map is a hand-drawn knowledge graph; mykb's typed links (`cites`, `extends`) automate what concept mapping does by hand, and graph views render the result.
- **RSIS3/mykb relevance** — concept maps are the natural diagram form for the triple-store structures this wiki maintains; keeping the labeled-edge discipline in mind makes both hand-drawn and automated maps more truthful.

## Related
- [[wiki/memory/mind-mapping|Mind Mapping]] — the looser, unlabeled visual cousin
- [[wiki/memory/ontology-design|Ontology Design]] — labeled relations are the ontology instinct
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the machine-readable form of a concept map
- [[wiki/memory/graph-notes|Graph Notes]] — tools that render notes as concept maps
- [[wiki/concepts/triad-architecture|Triad Architecture]] — mykb's graph engine realizes concept maps
