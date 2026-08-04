---
type: "entity"
title: "AWS DynamoDB"
description: "Serverless key-value and document database with single-digit-millisecond latency at scale"
tags: ["aws", "dynamodb", "nosql", "database", "serverless"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# AWS DynamoDB

## Summary
AWS DynamoDB is a fully managed NoSQL key-value/document store with predictable single-digit-millisecond latency. Tables scale automatically with on-demand or provisioned capacity.

## Details
- Access patterns are designed up front: partition key + sort key + secondary indexes.
- Pay-per-request pricing suits spiky serverless workloads; Global Tables give multi-region writes.
- Contrast with Postgres: DynamoDB trades joins/transactions for scale and ops-free operation.

## Access Pattern Design

DynamoDB rewards thinking about access patterns before the schema exists. Every item is addressed by a partition key, and optionally a sort key, and queries are only efficient when they filter through those keys. Secondary indexes — local or global — are the mechanism for supporting additional query shapes, so the design process is usually: enumerate the queries the application needs, then lay out keys and indexes to serve them, rather than normalizing tables the way a relational design would.

Item collections, single-table designs, and denormalization are common in DynamoDB applications because the query API is limited. Attributes can hold nested documents, and the same table can store several logical entity types distinguished by a type attribute. This is the opposite of the relational instinct, and teams adopting DynamoDB from SQL usually need to unlearn join-first modeling.

## Capacity, Pricing, and Operations

On-demand mode charges per request and absorbs traffic spikes automatically, which suits spiky or unpredictable serverless workloads. Provisioned mode reserves read and write capacity units and requires autoscaling or careful monitoring to avoid throttling. Global Tables replicate writes across regions for low-latency reads and disaster recovery, at the cost of eventual consistency between regions. Backups, point-in-time recovery, and TTL-based expiry of stale items are standard operational features worth enabling from day one.

## Related

- [[wiki/frontend/aws-lambda|AWS Lambda]] — natural compute companion
- [[wiki/frontend/serverless|Serverless]] — managed-state pattern
- [[wiki/devops-infra/sharding|Sharding]] — partition-key design
- [[wiki/devops-infra/postgresql|PostgreSQL]] — relational alternative
- [[wiki/devops-infra/replication|Replication]] — global table durability
- [[wiki/data-storage/entities/mongodb|MongoDB]] — document-store alternative
- [[wiki/devops-infra/load-balancing|Load Balancing]] — capacity and traffic shaping context
