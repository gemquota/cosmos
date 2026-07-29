---
type: "concept"
title: "RSIS3 Project Lineage"
description: "Full evolutionary history from iterative agent swarm attempts through RRP, rsirrp, rsis, rsirrp2, rsirrpb, rsis2, to rsis3"
tags: ["lineage", "history", "rsis3", "rrp", "agent-swarm", "evolution"]
timestamp: "2026-07-21T11:00:00Z"
---


## Project Lineage

# RSIS3 Project Lineage

## Origin
The project began with iterative experiments in coordinated agent swarms. The core insight was that agents needed a structured protocol for recursive refinement — leading to the Recursive Refinement Protocol (RRP).

## Evolution

```
Agent Swarm Experiments
    │
    ▼
RRP (Recursive Refinement Protocol)
    │
    ├──→ rsirrp (first RRP implementation)
    │         │
    │         ├──→ rsis (first self-improving system)
    │         │
    │         ├──→ rsirrp2 (RRP v2, branched)
    │         │      │
    │         │      ├── rsirrp (original branch)
    │         │      └── rsirrp2 (fork)
    │         │           │
    │         │           └── (fork merged back)
    │         │
    │         ▼
    │    rsirrpb (merged RRP base)
    │         │
    │         └── merged with rsis ──→ rsis2
    │                                    │
    │                                    └── recreated from scratch
    │                                         based on both codebases
    │                                         │
    │                                         ▼
    │                                      rsis3 (current)
    │
    └──→ ACE (Autonomous Cognitive Engine)
              │
              └── Sibling/predecessor iteration of the coordinated
                  agent swarm concept. Different architectural
                  approach: event-sourced causality, Lamport clocks,
                  sandboxed execution, sovereign panic recovery.
```

### Key Branch Points

1. **RRP → rsirrp** — First implementation of the Recursive Refinement Protocol as a standalone system
2. **rsirrp → rsis** — Added recursive self-improvement on top of the RRP core
3. **rsirrp/rsirrp2 fork** — Brief divergence in RRP implementation approaches before merging
4. **rsirrpb + rsis → rsis2** — Merged refinement protocol with self-improvement
5. **rsis2 → rsis3** — Complete rewrite from scratch based on lessons from both codebases
6. **RRP → ACE** — Alternative architecture: event-sourced, sandboxed, with sovereign panic recovery

### Relationship to ACE

ACE (Autonomous Cognitive Engine) is a sibling project that diverged from the same RRP/swarm origins. While RSIS3 focused on clean separation of cognition (RSIS3) and memory (mykb) with test-gated mutation, ACE pursued a mathematically rigorous event-sourced architecture with Lamport clocks, sandboxed execution, and sovereign panic recovery. Both projects explored autonomous self-improvement but with fundamentally different safety philosophies:

- **RSIS3**: Test-verified behavior — "if tests pass, the change is good"
- **ACE**: Mathematically-proven state — "if hash chains are unbroken, the state is consistent"

**Domain:** Concepts

## Related

- [[wiki/concepts/mykb-analysis|Mykb Analysis]]
- [[wiki/concepts/mykb-research-report|Mykb Research Report]]
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]]
- [[wiki/concepts/triad-architecture|Triad Architecture]]
- [[wiki/concepts/pulse-cycle|Pulse Cycle]]
- [[wiki/concepts/identity-system|Identity System]]
