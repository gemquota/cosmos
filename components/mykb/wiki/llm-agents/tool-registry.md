---
type: "concept"
title: "Tool Registry"
description: "Centralized catalog of available tools with schemas and policies"
tags: ["tool-registry", "tools", "schema", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Tool Registry

## Summary

A tool registry is the catalog of functions an agent may call: schemas, descriptions, permissions, and lifecycle metadata. It is the interface between the model's intent and the system's capabilities — and the primary attack surface for agent systems.

## Details
- Mechanism: the registry stores each tool's JSON schema (name, parameters, description), its implementation binding, permission requirements, cost/rate metadata, and version; the agent's context includes tool schemas for function calling; the runtime validates arguments against schemas, enforces permissions, and logs every invocation before executing.
- Concrete example: a wiki agent's registry lists search_notes, read_note, write_note (write-scoped), and graph_query with schemas that constrain paths; function-calling models select tools by description, so schema quality — clear names, precise descriptions, strict parameter types — determines routing accuracy.
- Failure modes: ambiguous or overlapping tool descriptions causing misrouting; schemas too loose (free-form strings where enums belong) allowing invalid calls; registry drift — tools removed but still advertised; and tools without permission metadata sneaking past policy checks.
- Operational tradeoffs: a registry centralizes tool governance (discoverability, versioning, permissions) at the cost of schema maintenance; the discipline is schema-first design, permission metadata per tool, invocation logging, and versioning so prompts and runtimes stay in sync.
- RSIS3/mykb relevance: the wiki's tool registry is the single source of truth for agent capabilities, and the loop's permission model reads from the same metadata.
- Schema quality practice: descriptions should state the tool's purpose, the meaning of each parameter, and common failure conditions; the model routes on these words.
- Registry testing: fuzz-call tools with adversarial arguments to verify schema enforcement and permission checks, since the registry is the attack surface.

## Related
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — the patterns registries support
- [[wiki/llm-agents/permission-model|Permission Model]] — policies attached to entries
- [[wiki/llm-agents/agent-logs|Agent Logs]] — calls logged against the registry
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop that consumes the registry
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — replay needs stable schemas
