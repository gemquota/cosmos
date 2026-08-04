---
type: "decision"
title: "decided to use SQLite for the local database because it re"
description: "Decision to use SQLite for the local database: embedded storage with no server setup"
tags: ["decision", "ajax", "alpine", "android", "angular", "ansible"]
timestamp: "2026-07-19T10:08:17.112Z"
---

# Decided to Use SQLite for the Local Database Because It Requires No Server Setup

## Summary

This decision records the choice of SQLite for the local database on the grounds that it requires no server setup. SQLite is an embedded relational database that runs inside the host process and persists to a single file. That makes it a natural fit for local-first applications where installation friction and operational overhead should be near zero.

## Details

- **Embedded database** — SQLite runs as a library inside the application rather than as a separate server process. The program opens a database file directly, so there is no daemon to install, no port to bind, and no connection pool to manage.
- **Zero server setup** — The core rationale of the decision: the database works immediately on first use, removing deployment steps, credentials, and startup ordering problems.
- **File-based persistence** — All tables, indexes, and schema metadata live in one portable file. The file can be copied, backed up, or moved between machines, which simplifies snapshots and disaster recovery.
- **ACID transactions** — SQLite provides atomic, consistent, isolated, and durable transactions with rollback journaling and write-ahead logging modes, giving embedded applications crash safety comparable to server databases.
- **Familiar SQL** — Because it supports standard SQL with indexes, joins, views, triggers, and constraints, teams keep their relational modeling skills without taking on infrastructure.
- **Concurrency model** — Multiple readers can share the database, but only one writer commits at a time; heavy concurrent writes can encounter lock contention.
- **Worked example** — A local knowledge store writes notes through a single connection, flushes a checkpoint file for backup, and serves reads instantly from disk.
- **Failure modes** — Long transactions can block readers, multiple processes can surface 'database is locked', and format migrations must be planned when upgrading versions.
- **Practical relevance** — Embedded storage fits local-first tools, mobile apps, and agent memory layers that must start instantly.
- **Alternatives considered** — Client-server databases offer stronger concurrent-write performance and shared access, at the cost of setup and operations that SQLite removes.
- **Migration path** — A file-based database exports cleanly, so moving to a server database later is a data-export and driver change rather than a rewrite.
- **Tooling** — Command-line clients, backup scripts, and GUI browsers all open the same file, keeping the ecosystem small but complete.

## Related

- [[wiki/decisions/chose-typeorm-because-it-has-the-best-typescript-support|Chose TypeORM Because It Has the Best TypeScript Support]] — sibling database-tooling decision
- [[wiki/decisions/self-hosting|Self-Hosting]] — running infrastructure locally
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — persisting durable state
- [[wiki/decisions/versioning-of-selves|Versioning of Selves]] — state snapshot discipline
- [[wiki/entities/memory-client|Memory Client]] — consumer of the local database
