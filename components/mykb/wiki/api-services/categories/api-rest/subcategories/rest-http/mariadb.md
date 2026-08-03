---
type: "entity"
title: "MariaDB"
description: "MariaDB: an open-source relational database forked from MySQL"
tags: ["entity", "mariadb", "database", "sql", "backend"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# MariaDB

## Summary

MariaDB is an open-source relational database management system forked from MySQL, maintaining SQL compatibility while adding its own storage engines and optimizations. It matters because it is a common drop-in choice for applications that want MySQL semantics without Oracle ownership. Deployment, tuning, and migration decisions dominate its practical use.

## Details

- **Definition** — MariaDB is a server-based relational database using SQL, with pluggable storage engines and broad compatibility with the MySQL wire protocol.
- **History** — The fork preserved MySQL compatibility while diverging in engine defaults, such as using Aria and InnoDB variants for different workloads.
- **Engines** — Storage engines differ in transactional guarantees, compression, and indexing; choosing one per table is part of schema design.
- **Worked example** — An application connects to MariaDB with SQLAlchemy, stores transactional records in an InnoDB-equivalent engine, and reads analytics from a compressed archive table.
- **Common failure modes** — Migrating from MySQL with incompatible syntax or engine assumptions, missing backup and replication setup, and default configuration that underperforms.
- **Practical relevance** — MariaDB appears in many API backends, so connection pooling, query tuning, and backup discipline carry over directly.
- **Variants** — MySQL, PostgreSQL, and embedded SQLite differ in features and deployment; the choice affects migrations and operations.
- **Telemetry note** — The stub mis-tags MariaDB to Android Debug Bridge; the relational-database reading matches the backend context where it was recorded.
- **Backups** — Logical and physical backups differ in restore speed and granularity; regular restore drills verify the backup actually works.
- **Replication** — Replica lag and failover behavior determine how much data loss a failure can cause; monitoring lag is part of operations.
- **Worked example** — A MariaDB instance serves an API behind a connection pool; a slow-query log review leads to an index addition that cuts p95 latency.
- **Migrations** — Schema migrations should run with locking and rollback awareness, especially when tables are large or hot.

## Related

- [[wiki/data-storage/sql-engines|SQL Engines]] — the database family
- [[wiki/data-storage/database-normalization|Database Normalization]] — schema design
- [[wiki/data-storage/database-performance-monitoring|Database Performance Monitoring]] — observing the server
- [[wiki/testing/database-testing|Database Testing]] — testing data layers
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/flask|Flask]] — web framework using it
- [[wiki/data-storage/sqlite-fts5|SQLite FTS5]] — embedded alternative
