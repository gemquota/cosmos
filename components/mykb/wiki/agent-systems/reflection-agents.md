---
type: "concept"
title: "Reflection Agents"
description: "Agents that use memory of past attempts to guide future behavior"
tags: ["reflection", "agents", "memory", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2303.11366", "https://arxiv.org/abs/2303.17651"]
---

# Reflection Agents

## Summary
Reflection agents store and retrieve structured reflections on their own past attempts — what failed, why, and what to change — and use them on the next attempt. Reflexion (2023) demonstrated large gains on coding and decision-making benchmarks with this architecture.

## Details
- **Reflexion loop** — act, evaluate, reflect into a memory buffer, then act again informed by reflections.
- **Key design choices** — what to store (feedback, plans, self-critique), how to retrieve, and when reflection stops.
- **Why it works** — it externalizes learning into retrievable text, so gains persist across runs without retraining.
- **Limits** — reflection quality caps improvement; without external verification, reflections can be confident and wrong.
- **RSIS3 parallel** — pulse outcomes and decision logs are reflections that inform the next planning phase across the triad.

## Related
- [[wiki/agent-systems/self-reflection-loops|Self-Reflection Loops]] — the loop shape
- [[wiki/agent-systems/self-critique|Self-Critique]] — the critique source
- [[wiki/agent-systems/skill-acquisition-loops|Skill Acquisition Loops]] — what reflections accelerate
- [[wiki/concepts/episodic-memory|Episodic Memory]] — the memory substrate
- [[wiki/agent-systems/self-correction|Self-Correction]] — the downstream fix
- [[wiki/memory/memory-retrieval-curves|Memory Retrieval Curves]] — retrieval design
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
- [[wiki/pulses/self-benchmarking|Self-Benchmarking]] — internal benchmarks
