---
type: "entity"
title: "MySQL"
description: "Widely deployed open-source relational database powering many web applications"
tags: ["mysql", "database", "sql", "relational", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# MySQL

## Summary
MySQL is the most widely deployed open-source relational database, the "M" of LAMP. It offers ACID transactions (InnoDB), replication, and broad tooling.

## Details
- InnoDB storage engine provides transactions, row-level locking, and crash recovery.
- Great ecosystem fit: managed offerings (AWS RDS), proxy layers, and ORM support everywhere.
- Compare with PostgreSQL when choosing: MySQL for ubiquity, Postgres for feature depth.

## Related
- [[wiki/devops-infra/postgresql|PostgreSQL]] — main relational alternative
- [[wiki/devops-infra/transactions|Transactions]] — InnoDB guarantees
- [[wiki/devops-infra/replication|Replication]] — read replicas
- [[wiki/devops-infra/backups|Backups]] — operational practice
- [[wiki/devops-infra/database-indexing|Database Indexing]] — query performance
- [[wiki/devops-infra/observability|Observability]] — slow-query and connection monitoring
