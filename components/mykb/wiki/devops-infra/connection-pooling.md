---
type: "concept"
title: "Connection Pooling"
description: "Reusing database connections across requests to amortize handshake cost and bound concurrency"
tags: ["connection-pooling", "database", "performance", "sql", "devops"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Connection Pooling

## Summary
Connection pooling keeps a set of open database connections for reuse, avoiding per-request handshake overhead and capping database load. PgBouncer and per-app pools are standard.

## Details
- Tune pool size: too few stalls, too many overload the DB; rule-of-thumb math beats guesses.
- Timeouts release connections stuck on slow queries; health checks prune dead ones.
- Serverless and edge workloads need poolers or managed proxies (RDS Proxy) due to short-lived instances.

## Related
- [[wiki/devops-infra/postgresql|PostgreSQL]] — pooler ecosystem
- [[wiki/api-protocols/timeouts|Timeouts]] — free stuck connections
- [[wiki/frontend/serverless|Serverless]] — short-lived runtimes need pooling
- [[wiki/devops-infra/observability|Observability]] — pool metrics
- [[wiki/devops-infra/replication|Replication]] — pool to read replicas
