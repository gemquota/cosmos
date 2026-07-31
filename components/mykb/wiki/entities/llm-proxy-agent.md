---
type: "entity"
title: "LLM Proxy Agent"
description: "The AI coding agent (Codex CLI) acting as the LLM inference layer for RSIS3 in lieu of a production API key"
tags: ["entity", "llm", "proxy", "agent", "codex", "inference"]
timestamp: "2026-07-21T11:05:00Z"
---


## Llm Proxy Agent

# LLM Proxy Agent

## Role
In production, RSIS3 calls an LLM API (e.g., Gemini, OpenAI) for inference during pulse cycles, RRP analysis, code generation, and self-direction. Currently, the project lacks an API key, so **an AI coding agent (Codex CLI) fulfills all LLM calls manually**.

This means the agent:
- Analyzes codebase state (instead of LLM-based analysis)
- Generates implementation plans (instead of LLM-based planning)
- Evaluates outcomes (instead of LLM-based evaluation)
- Writes code patches (instead of LLM-based codegen)
- Answers questions about architecture (instead of LLM-based RRP)

## Implications

### Current (Proxy Mode)
- All cognitive work done by the agent in natural language
- No API costs
- Full human oversight of every decision
- Slower than automated LLM calls
- Knowledge documented in wiki for future automated retrieval

### Future (Production Mode)
- Pulse engine calls LLM API for phase generation
- RRP uses LLM for ambiguity assessment
- Codegen uses LLM for patch generation
- L3 self-direction uses LLM for goal prioritization
- Agent role shifts from executor to supervisor

## Documentation

All analysis, decisions, and knowledge produced by this proxy role are documented in the mykb wiki. This means when the API key is added, the system can retrieve this context via MemoryClient rather than re-discovering everything from scratch.

## Related
- wiki/entities/memory-client.md — The bridge that will serve this knowledge
- wiki/concepts/pulse-cycle.md — Where LLM calls happen in production
- wiki/projects/triad-integration.md — Project tracking

**Domain:** Entities

## Related

- [[wiki/entities/identity-snapshot-0001|Identity Snapshot 0001]]
- [[wiki/entities/memory-client|Memory Client]]
- [[wiki/entities/pulse-engine|Pulse Engine]]
- [[wiki/entities/rrp-state-machine|Rrp State Machine]]
- [[wiki/entities/e2e-test-001|E2E Test 001]]
- [[wiki/entities/e2e-entity|E2E Entity]]
