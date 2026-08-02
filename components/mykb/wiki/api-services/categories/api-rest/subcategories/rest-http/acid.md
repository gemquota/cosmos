---
type: "entity"
title: "ACID"
description: "Android — mobile development platform, Angular — TypeScript web framework, API — service communication interface"
tags: ["entity", "acronym", "android", "angular", "api", "ast"]
timestamp: "2026-07-19T22:41:41Z"
status: "growing"
resource: ""
---

## Acid

ACID — Atomicity, Consistency, Isolation, Durability. A set of database transaction properties.

**Related topics:** android, angular, api

**Domain:** Mobile Platform › [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] › [[wiki/web-platforms/supercategories/api-services/categories/api-rest/index|Api Clients › Acid

## Overview

ACID describes the guarantees a database transaction should provide. Atomicity means a transaction's operations are all-or-nothing: if any statement fails, the whole transaction rolls back to its starting state. Consistency means a transaction moves the database from one valid state to another, preserving constraints such as foreign keys, unique indexes, and check constraints. Isolation controls how concurrent transactions see each other's intermediate work. Durability guarantees that committed changes survive crashes and restarts, usually through write-ahead logs.

## Details

The four properties trade off against each other and against performance. Atomicity is typically implemented with an undo log or rollback segments, durability with a redo or write-ahead log, and isolation with locks or multi-version concurrency control. Strict isolation — full serializability — can collapse throughput under contention, so databases offer weaker levels such as read committed, which admits non-repeatable reads but is often the practical default. Choosing the right combination is application-specific: financial ledgers favor durability and atomicity, while analytics workloads may relax isolation for speed. ACID is one axis of the CAP and PACELC trade-offs; distributed systems that sacrifice strong consistency typically relax isolation or atomicity to stay available. Related concepts include [[wiki/devops-infra/isolation-levels|Isolation Levels]], [[wiki/devops-infra/transactions|Database Transactions]], and [[wiki/devops-infra/acid|ACID]] as applied in operational infrastructure.

## Related Entities
## In Practice

Real databases implement ACID to different degrees. PostgreSQL, MySQL, and SQLite all support transactions with BEGIN and COMMIT, but their default isolation levels and locking behaviors differ. Distributed stores such as DynamoDB and MongoDB relax the letter of ACID, offering per-item or per-document atomicity and tunable consistency instead. Applications bridge the gap with application-level techniques: idempotent operations, optimistic concurrency checks, and compensating workflows. Understanding which ACID guarantees a system actually provides is essential before designing around them, because assuming strong atomicity or isolation where none exists leads to subtle data-integrity bugs.


- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acs|Acs
