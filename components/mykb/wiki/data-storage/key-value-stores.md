---
type: "concept"
title: "Key-Value Stores"
description: "Simple get/put stores and their scaling patterns"
tags: ["key-value", "nosql", "redis", "dynamodb"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://redis.io/docs/latest/", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html"]
---

# Key-Value Stores

## Summary
Key-value stores are the simplest data model: a dictionary mapping keys to values, with `get`, `put`, and `delete` as the core operations. Their simplicity enables extreme scalability and low latency — values are found by exact key lookup with no joins or query planning — which makes them the engine of caches, session stores, feature flags, and hot-path data.

## Details
- **Data model** — keys are typically strings or binary; values are opaque blobs or typed structures. Redis values include strings, hashes, lists, sets, and sorted sets; DynamoDB items are attribute maps addressed by partition key.
- **Access patterns** — operations are point lookups by key, optionally with range scans within a partition; there is no cross-key query language, so schema design must encode access paths into keys (e.g., `user:42:orders`).
- **Scaling** — distribution is the differentiator: sharding by key hash or consistent hashing spreads load; DynamoDB partitions by hash key, Redis Cluster uses 16384 slots, and memcached clients hash keys across servers.
- **Consistency choices** — DynamoDB offers eventual, strongly consistent, and conditional writes; Redis is single-threaded per instance so operations are atomic within a key; distributed deployments add the usual CAP trade-offs.
- **Use cases** — caching (Redis, Memcached), session and shopping-cart state, rate limits, leaderboards, configuration, and as the storage under higher-level services; durable variants (RocksDB, LevelDB, DynamoDB) back bigger systems.
- **Trade-offs** — no secondary indexes or joins pushes query logic into the application; the payoff is predictable microsecond-to-millisecond latency and near-linear horizontal scaling.

## Related
- [[wiki/data-storage/document-stores|Document Stores]] — richer, queryable siblings
- [[wiki/data-storage/caching-strategies|Caching Strategies]] — the dominant KV workload
- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — distributing keys across nodes
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — membership for KV clusters
- [[wiki/data-storage/lsm-trees|LSM Trees]] — durable KV storage engines
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — Dynamo-style KV replication
