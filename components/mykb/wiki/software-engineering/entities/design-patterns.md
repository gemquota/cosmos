---
type: "entity"
title: "Design Patterns in the Ecosystem"
tags: ["software", "patterns", "architecture"]
source: ["concepts/", "rsis3/"]
status: "growing"
---

# Design Patterns in the Ecosystem

Key patterns observed across the project ecosystem.

Design patterns are reusable solutions to recurring structural problems, and this repository applies a small, deliberate set of them across its components. Each pattern below names the problem, the structure that solves it, and where it appears in the ecosystem. Patterns are kept explicit because they encode architectural decisions that would otherwise be rediscovered, and restated, in every session.

## Adapter/Bridge Pattern
myrsikb memory bridge adapts between RSIS3's cognitive engine and MyKB's wiki storage.

## State Machine Pattern
RRP implements a formal state machine with phases, events, and transitions.

## Observer/Event Pattern
Pulse engine: pulses generate events → trigger codegen, identity checks, telemetry.

## Factory Pattern
SPACE's LLM provider abstraction uses factory methods for OpenAI/Anthropic/null providers.

## Repository Pattern
MyKB's storage layer wraps persistence behind a repository interface, so RSIS3 reads and writes wiki notes without coupling to the concrete file layout.

## Strategy Pattern
Swappable algorithms — such as retrieval strategies or provider selection — are injected at runtime, letting behavior change without rewriting callers.

## Facade Pattern
The dashboard presents RSIS3, MyKB, and SPACE behind one unified interface, hiding each component's internal complexity from the user.

## Prototype Pattern
Session-derived notes are cloned from templates with fresh frontmatter, preserving structure while allowing each instance to diverge.

Patterns remain useful only when the cost of the abstraction stays below the cost of the duplication it removes; the ecosystem reviews these choices whenever a new component is added. Documented patterns also serve new contributors as a map of where responsibilities live. A pattern that no longer pays for its indirection is retired explicitly, with the rationale recorded, so future sessions do not resurrect it. Consistency in naming and structure is what makes the map legible.

See also: [[wiki/software-engineering/index|Software Engineering]], [[wiki/concepts/triad-architecture|Triad Architecture]], [[wiki/devops-infra/api-gateway-patterns|API Gateway Patterns]], [[wiki/agent-systems/action-observation-loop|Action Observation Loop]]
