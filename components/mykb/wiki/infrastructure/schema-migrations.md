---
type: "concept"
title: "Schema Migrations"
description: "Versioned, reversible changes to database schemas that ship safely alongside application deploys"
tags: ["schema", "migrations", "databases", "deployments"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Schema Migrations

## Summary
Schema migrations change database structure in versioned, ordered steps that apply once and roll back deliberately. They are where deployments and data meet — and where most release risk lives.

## Details
- Expand-and-contract: add columns/backfill first, deploy code, then drop old columns — keeps old and new code compatible.
- Migrations must be idempotent and ordered; locks and long-running DDL need planning.
- Blue-green and canary deploys force migrations that work with two code versions at once.
- Open question: how to test migrations against production-sized data.

## Related
- [[wiki/infrastructure/blue-green-deployments|Blue-Green Deployments]] — two versions share one schema
- [[wiki/devops-infra/release-versioning|Release Versioning]] — paired with release versions
- [[wiki/devops-infra/postgresql|PostgreSQL]] — common migration target
- [[wiki/devops-infra/mysql|MySQL]] — common migration target
