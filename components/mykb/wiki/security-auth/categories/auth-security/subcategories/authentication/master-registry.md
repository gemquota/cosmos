---
type: "entity"
title: "Master Registry"
resource: ""
---
description: "A single authoritative store that records entities, versions, and their locations"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "registry", "metadata"]
timestamp: "2026-07-19T22:41:42Z"

# Master Registry

## Summary
A master registry is the single authoritative store that records what entities exist, which versions are current, and where they can be found. It matters because distributed systems fragment knowledge across services, and fragmented knowledge produces drift and confusion. One trusted registry turns "ask around" into "look it up", giving every consumer the same current answer.

## Details
- **Definition** — a master registry maps stable identifiers to current metadata: location, version, owner, and status.
- **Single source of truth** — writes go through the registry so every consumer reads the same current record instead of cached assumptions.
- **Versioning** — registering each version with its release state lets consumers pin, upgrade, and audit changes deliberately.
- **Lifecycle states** — records track active, deprecated, and retired states so consumers can plan migrations instead of discovering removals.
- **Discovery** — services and agents query the registry to find the right endpoint or artifact, replacing hard-coded addresses.
- **Consistency** — the registry must reconcile concurrent updates and handle partitions, or its authority erodes.
- **Access control** — registries hold sensitive metadata, so read and write permissions must be scoped and audited.
- **Common failure modes** — stale registrations, multiple unofficial registries, and records that drift from reality because cleanup is manual.
- **Worked example** — a model registry records each model version with its artifact path and status; a deployment pipeline promotes a version by updating its state, and consumers discover the new canonical path.
- **Practical relevance** — a master registry is the backbone of reproducible deployment and trustworthy metadata in any ecosystem.

## Related
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — registry for models
- [[wiki/data-storage/data-catalogs-and-metadata|Data Catalogs and Metadata]] — cataloging assets
- [[wiki/data-storage/metastore-and-catalog-iceberg|Metastore and Catalog]] — table registries
- [[wiki/api-protocols/api-versioning|API Versioning]] — versioned contracts
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — versioned agents
- [[wiki/tooling/environment-management|Environment Management]] — environment-scoped registries
