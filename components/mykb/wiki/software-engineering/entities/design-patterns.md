---
type: "entity"
title: "Design Patterns in the Ecosystem"
tags: ["software", "patterns", "architecture"]
source: ["concepts/", "rsis3/"]
---

# Design Patterns in the Ecosystem

Key patterns observed across the project ecosystem.

## Adapter/Bridge Pattern
myrsikb memory bridge adapts between RSIS3's cognitive engine and MyKB's wiki storage.

## State Machine Pattern
RRP implements a formal state machine with phases, events, and transitions.

## Observer/Event Pattern
Pulse engine: pulses generate events → trigger codegen, identity checks, telemetry.

## Factory Pattern
SPACE's LLM provider abstraction uses factory methods for OpenAI/Anthropic/null providers.

See also: [[wiki/software-engineering/index|Software Engineering]], [[wiki/concepts/triad-architecture|Triad Architecture]]
