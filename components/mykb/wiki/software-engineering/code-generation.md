---
type: "concept"
title: "Code Generation"
description: "Producing source code automatically from models, schemas, or LLM prompts"
tags: ["codegen", "automation", "llm", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Code Generation

## Summary
Code generation creates code from higher-level descriptions: schemas to SDKs, OpenAPI specs to clients, and prompts to functions via LLMs. It removes boilerplate and keeps artifacts in sync with their source of truth.

## Details
- Deterministic generators (OpenAPI, protobuf) produce stable, reviewable output.
- LLM-based generation is probabilistic; it needs tests and review to be safe.
- RSIS3 relevance: mykb articles are partly generated knowledge artifacts — generation with provenance.

## Related
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — generators turn domain models into code
- [[wiki/llm-agents/code-generation-agents|Code Generation Agents]] — LLM-driven generation at agent scale
- [[wiki/api-protocols/openapi|OpenAPI]] — contract-first generation of clients and servers
- [[wiki/software-engineering/project-scaffolding|Project Scaffolding]] — scaffolding is code generation for whole projects
