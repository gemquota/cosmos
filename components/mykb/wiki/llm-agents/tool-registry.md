---
type: "concept"
title: "Tool Registry"
description: "Centralized catalog of available tools with schemas and policies"
tags: ["tool-registry", "tools", "schema", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Tool Registry

## Summary
A tool registry is the authoritative catalog of an agent's available tools: schemas, descriptions, permissions, and status. It matters because a single source of truth prevents schema drift and makes tool discovery safe. Registries enable validation and policy enforcement at call time.

## Details
- Entries: name, description, JSON schema, permissions, rate limits.
- Validation and permission checks consult the registry before execution.
- Registries can be scoped per agent or sub-agent.
- Open questions: dynamic registration of new tools at runtime.

## Related
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — the patterns registries support
- [[wiki/llm-agents/permission-model|Permission Model]] — policies attached to entries
- [[wiki/llm-agents/agent-logs|Agent Logs]] — calls logged against the registry
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop that consumes the registry
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — replay needs stable schemas
