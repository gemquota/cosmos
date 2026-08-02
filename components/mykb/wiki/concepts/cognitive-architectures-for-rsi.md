---
type: "concept"
title: "Cognitive Architectures for RSI"
description: "System designs that support recursive self-improvement"
tags: ["cognitive-architecture", "rsi", "agents", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Cognitive_architecture", "https://en.wikipedia.org/wiki/Soar_(cognitive_architecture)"]
---

# Cognitive Architectures for RSI

## Summary
Cognitive architectures for RSI are blueprints — memory systems, reflection layers, practice gates, and control loops — that let a system improve itself safely. Classic architectures (Soar, ACT-R, LIDA) inform modern stacks where a base agent loop is wrapped in meta-cognitive layers.

## Details
- **Classic lineage** — Soar's problem spaces and ACT-R's modules inspired layered, inspectable agent designs.
- **RSI-relevant components** — a stable identity/self-model, episodic memory, a reflection phase, and external evaluators.
- **Modern instantiations** — the triad architecture (RSIS3 + mykb + myrsikb) is a concrete example: cognition, memory, and interface separated by contracts.
- **Safety by construction** — architecture fixes what can change (scaffold) and what cannot (evaluator), bounding self-improvement.
- **Open questions** — how much of improvement should live in weights vs scaffold vs knowledge base.

## Related
- [[wiki/agent-systems/self-modeling|Self-Modeling]] — the self-model component
- [[wiki/agent-systems/reflection-agents|Reflection Agents]] — the reflection component
- [[wiki/concepts/memory-hierarchy|Memory Hierarchy]] — the memory component
- [[wiki/concepts/control-protocols|Control Protocols]] — the constraint component
- [[wiki/concepts/cognitive-architecture|Cognitive Architecture]] — existing concept
- [[wiki/concepts/triad-architecture|Triad Architecture]] — concrete architecture
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-model scores
- [[wiki/pulses/capability-probes|Capability Probes]] — capability tracking
