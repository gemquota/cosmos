---
type: "entity"
title: "Pulse Engine"
description: "9-phase evaluation protocol coordinator — RSIS3's core cognitive loop"
tags: ["pulse", "evaluation", "protocol", "rsis3", "engine"]
timestamp: "2026-07-21T10:06:00Z"
---


## Pulse Engine

# Pulse Engine

**Source:** `rsis3/src/tools/pulse_engine.py`

The pulse engine orchestrates the 9-phase evaluation cycle. Key integrations:

### TelemetryWriter
Rate-limited subconscious observation stream. Channels include `pulse_cycle`, `scheduler_cycle`, `layer_scores`.

### RRP State Machine
Uses `extract_constraints()` and `ambiguity_rating_from_text()` from the RRP engine for auto-mode phases.

### StubScanner (--fast mode)
AST-based scanner checks 435 functions in 0.3s. Reports implementation ratio.

### ExperimentManager (auto-mode)
Records pulse outcomes to open experiments. Auto-concludes when effect size > 0.3.

### ExecutivePlanner
Plans created with episodic context from ExperienceMemory. Past similar pulses inform the first step.

**Domain:** Entities

## Related

- [[wiki/entities/identity-snapshot-0001|Identity Snapshot 0001]]
- [[wiki/entities/memory-client|Memory Client]]
- [[wiki/entities/rrp-state-machine|Rrp State Machine]]
- [[wiki/entities/llm-proxy-agent|Llm Proxy Agent]]
- [[wiki/entities/e2e-test-001|E2E Test 001]]
- [[wiki/entities/e2e-entity|E2E Entity]]
