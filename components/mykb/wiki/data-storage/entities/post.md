---
type: "entity"
title: "POST"
description: "PostgreSQL"
tags: ["entity", "acronym", "android", "api", "ast", "aws"]
timestamp: "2026-07-19T22:41:42Z"
status: "growing"
resource: ""
---

## Post

PostgreSQL — a powerful, open-source relational database. Sessions show schema design, migrations, JSON queries, and indexing.

**Related topics:** android, api, aws

**Domain:** Mobile Platform › [[wiki/web-platforms/index|Android Core]] › [[wiki/web-platforms/index|Api Clients › Post

## Overview

PostgreSQL is an open-source relational database management system known for standards compliance, extensibility, and robustness. It stores data in tables with strict typing and constraints, and it supports SQL plus advanced features: JSON and JSONB columns, full-text search, window functions, common table expressions, and user-defined types. PostgreSQL's write-ahead logging provides crash safety and enables point-in-time recovery, while its concurrency control allows many readers and writers to proceed without blocking each other unnecessarily.

## Details

- Schema design: tables, foreign keys, check constraints, and indexes encode the data model; migrations alter the schema in versioned steps.
- JSON: JSONB stores parsed JSON with indexing via GIN, letting relational and document-style data coexist in one database.
- Indexing: B-tree, hash, GIN, GiST, and BRIN indexes serve different query shapes; `EXPLAIN ANALYZE` reveals which plan the planner chose.
- Sessions: typical work includes writing queries, tuning indexes, and running migrations against local and remote instances.
- Operations: `psql` is the standard shell client; connection pooling and backups are part of production hygiene.

Because the entity is tagged with the acronym POST, it also inherits the HTTP meaning — the POST method for creating resources — but its description pins the referent to PostgreSQL, the database. In API work, the two senses meet: a POST endpoint frequently writes rows into PostgreSQL, and schema, migration, and indexing decisions directly shape API latency and correctness. Related systems include [[wiki/data-storage/entities/mysql|MySQL]], [[wiki/data-storage/entities/mongodb|MongoDB]], and [[wiki/data-storage/entities/dynamodb|DynamoDB]], each with different trade-offs in consistency, scaling, and operations.

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
