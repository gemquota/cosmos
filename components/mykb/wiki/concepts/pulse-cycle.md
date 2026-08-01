---
type: "concept"
title: "Pulse Cycle"
description: "9-phase evaluation protocol — the core cognitive loop of RSIS3"
tags: ["pulse", "evaluation", "protocol", "cognitive-loop", "rsis3"]
timestamp: "2026-07-21T10:01:00Z"
---


## Pulse Cycle

# Pulse Cycle

The pulse cycle is RSIS3's 9-phase evaluation protocol. Each cycle evaluates a proposed code mutation against identity, goals, constraints, and tests.

## Phases

| Phase | Purpose |
|-------|---------|
| 1. Context | System state, recent history, active goals |
| 2. Goal Analysis | What are we trying to achieve? |
| 3. Constraint Extraction | What invariants must be preserved? |
| 4. Ambiguity Assessment | Where is the uncertainty? |
| 5. Options | Multiple approaches considered |
| 6. Reasoning | Analysis of each option |
| 7. Evaluation | Scoring against criteria |
| 8. Decision | PASS / HOLD / DISMISS / REFRAME |
| 9. Test Result | Test suite outcome |

## Execution Modes

### Interactive (default)
Human-in-the-loop: phases are prompted via stdin. The agent enters reasoning for each phase.

### Auto (`--auto`)
Headless mode powered by:
- GoalGenerator for phase 2
- RRP state machine (`extract_constraints`) for phase 3
- RRP state machine (`ambiguity_rating_from_text`) for phase 4
- TestRunner or StubScanner for phase 9

### Fast (`--auto --fast`)
Uses StubScanner (AST-based) instead of full test suite for phase 9.
Scans 435 functions in 0.3s.

## Telemetry

Every pulse cycle writes to:
1. **TelemetryWriter** — subconscious observation stream (wiki/telemetry/)
2. **ExperienceMemory** — episodic pulse memory (wiki/pulses/)
3. **Dashboard** — real-time metrics on port 8765

## Temporal Horizon

Pulse cycles have a configurable deadline (`RSIS3_MAX_CYCLE_DURATION`, default 4 hours). If exceeded, the cycle enters HOLD state and must be restarted.

**Domain:** Concepts

## Related

- [[wiki/concepts/mykb-analysis|Mykb Analysis]]
- [[wiki/concepts/mykb-research-report|Mykb Research Report]]
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]]
- [[wiki/concepts/triad-architecture|Triad Architecture]]
- [[wiki/concepts/identity-system|Identity System]]
- [[wiki/concepts/project-lineage|Project Lineage]]


## Relation to Agent Loops

The pulse cycle wraps the [[wiki/agent-systems/agent-loop|agent loop]]: each
phase is a bounded agent loop over reasoning steps, and the whole cycle is one
episode of [[wiki/agent-systems/recursive-self-improvement|recursive
self-improvement]]. Decisions are governed by
[[wiki/agent-systems/constraint-satisfaction|constraint satisfaction]] and
evaluated with the discipline of [[wiki/testing/llm-evaluation|LLM
evaluation]] — golden tests, eval sets, and regression suites map onto phase 9.

## Memory Writes

Pulse outcomes land in [[ops/rsis3-memory-bridge|RSIS3 memory]] as typed
records (pulse, decision, reflection) with full
[[wiki/memory/provenance|provenance]], and are indexed by the
[[wiki/data-storage/knowledge-graph|knowledge graph]] for retrieval in later
cycles.
