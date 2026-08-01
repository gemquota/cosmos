---
type: "concept"
title: "AWS DynamoDB"
description: "Serverless key-value and document database with single-digit-millisecond latency at scale"
tags: ["aws", "dynamodb", "nosql", "database", "serverless"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# AWS DynamoDB

## Summary
AWS DynamoDB is a fully managed NoSQL key-value/document store with predictable single-digit-millisecond latency. Tables scale automatically with on-demand or provisioned capacity.

## Details
- Access patterns are designed up front: partition key + sort key + secondary indexes.
- Pay-per-request pricing suits spiky serverless workloads; Global Tables give multi-region writes.
- Contrast with Postgres: DynamoDB trades joins/transactions for scale and ops-free operation.

## Related
- [[wiki/frontend/aws-lambda|AWS Lambda]] — natural compute companion
- [[wiki/frontend/serverless|Serverless]] — managed-state pattern
- [[wiki/devops-infra/sharding|Sharding]] — partition-key design
- [[wiki/devops-infra/postgresql|PostgreSQL]] — relational alternative
- [[wiki/devops-infra/replication|Replication]] — global table durability
