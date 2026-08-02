---
type: "concept"
title: "Data Contracts"
description: "Agreed schemas and SLAs between producers and consumers"
tags: ["data-contracts", "governance", "schema", "sla"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.datamesh-architecture.com/", "https://docs.getdbt.com/docs/build/contracts"]
---

# Data Contracts

## Summary
A data contract is a written agreement between a producer and its consumers: the schema, the semantics, the freshness SLA, and the quality guarantees. It turns implicit assumptions into versioned, testable promises so producers can change safely and consumers can trust the data.

## Details
- **What it contains** — field names, types, nullability, key constraints, value vocabularies, update frequency, retention, and ownership contact; machine-readable formats (JSON schema, YAML) let tooling enforce it.
- **Why contracts emerged** — schema-on-read lakes and internal microservices drifted until every consumer re-implemented validation; a contract centralizes the rules and makes breaking changes visible and gated.
- **Enforcement** — CI runs contract checks against sample data; production pipelines validate payloads at the boundary; dbt model contracts fail builds when schema or data type changes.
- **Versioning** — contracts follow semantic versioning; major changes require consumer migration windows (expand-contract), while minor additions are backward compatible.
- **Culture** — contracts work when producers and consumers share the review loop; a registry (data catalog) plus a change process matters more than any tool.
- **Relationship to quality** — data-quality checks implement the contract's terms; data observability monitors whether the SLA is being met in production.

## Related
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — the change process contracts govern
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — enforcing contract terms
- [[wiki/data-storage/data-observability|Data Observability]] — SLA monitoring
- [[wiki/data-storage/schema-on-read|Schema-on-Read vs Schema-on-Write]] — the boundary contracts formalize
- [[wiki/data-storage/expand-contract-migrations|Expand-Contract Migrations]] — contract-safe rollout
