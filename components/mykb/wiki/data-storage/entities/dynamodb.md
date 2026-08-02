---
type: "entity"
title: "DynamoDB"
description: "Amazon DynamoDB"
tags: ["entity", "android", "angular", "api", "ast", "auth"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---

## Dynamodb

Amazon DynamoDB — a fully managed NoSQL key-value and document database.

**Related topics:** android, angular, api, auth

**Domain:** Mobile Platform › [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] › [[wiki/web-platforms/supercategories/api-services/categories/api-rest/index|Api Clients › Dynamodb

## Overview

Amazon DynamoDB is a fully managed NoSQL database that stores items as key-value or document structures. The service replicates data across multiple availability zones, scales throughput by partition, and exposes a low-latency API, which makes it a common backend for mobile and web applications. Sessions referencing DynamoDB alongside Android, Angular, API, and auth tags reflect that typical pattern: a client application calls an API, and the API layer reads and writes DynamoDB tables behind authentication.

## Data Model

A table holds items, each identified by a primary key that is either a single partition key or a partition key plus a sort key. Items are schemaless — attributes can differ from row to row — so the access patterns, not a fixed schema, drive table design. This means modeling is a matter of deciding which queries must be fast: a global secondary index can serve an alternate query path, but every index consumes write capacity, and denormalization is usually preferred over joins because the service has no relational join operation.

## Access Patterns

DynamoDB is used through a small set of operations: GetItem, PutItem, UpdateItem, DeleteItem, and Query, with Scan available as a last resort because it reads the whole table. [[wiki/devops-infra/connection-pooling|connection pooling]] and retry logic belong in the client, while capacity planning — on-demand versus provisioned — decides how cost and throttling behave under load. [[wiki/data-storage/entities/cache|cache]] layers such as DynamoDB Accelerator or external caches reduce read cost for hot keys, and the [[wiki/infrastructure/categories/aws/index|AWS]] tree documents the surrounding account and IAM setup.

## Operations

Operational concerns include backups, point-in-time recovery, and table export, all managed through the AWS console, CLI, or SDK. Monitoring watches throttled requests, consumed capacity, and error rates. Because the service handles replication and failover internally, teams mostly worry about key design, index cost, and hot partitions rather than servers. For relational needs, [[wiki/data-storage/entities/database-schema-audit|database schema audit]] and [[wiki/data-storage/entities/mongodb|MongoDB]] offer contrast: schema-on-write versus schema-on-read, and join support versus key-value lookup.

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
