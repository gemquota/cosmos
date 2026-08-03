---
type: "concept"
title: "DynamoDB and PartiQL"
description: "AWS serverless key-value/document store with SQL-like PartiQL access"
tags: ["dynamodb", "partiql", "aws", "nosql"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# DynamoDB and PartiQL

## Summary

DynamoDB is AWS's fully managed key-value and document database, built for single-digit-millisecond access at any scale — it was the service that made "serverless database" concrete, with no provisioning, automatic scaling, and multi-region replication. PartiQL is the SQL-compatible query language layered on top, letting developers use familiar SQL syntax instead of only the low-level API operations.

## Details

- DynamoDB is a fully managed key-value and document database with single-digit-millisecond latency. The architecture: items are distributed across partitions by consistent hashing of the partition key, and each partition holds a contiguous range of sort-key values. Reads and writes hit exactly one partition (the one holding the item's key), which is why access latency is flat regardless of table size — the system never scans; it routes by key. The consistency model: eventually consistent by default, strongly consistent on request (at the cost of availability and throughput), and transactions for multi-item atomicity.
- Design centers on primary keys: partition key and optional sort key determine access patterns. The partition key decides which partition an item lands on; the sort key orders items within a partition and enables range queries. The design rule is brutal: DynamoDB only serves access patterns that go through the key structure — "fetch item by ID", "fetch range of items with same ID ordered by timestamp" — and everything else (secondary lookups, aggregates, joins) requires extra machinery: global secondary indexes (GSIs) maintain alternative key views, and scans (which read the whole table) are the anti-pattern to avoid. The design discipline is to model for the queries first, because the key structure is nearly immutable after creation.
- PartiQL adds SQL-like syntax over items, complementing the classic API operations. PartiQL lets you write `SELECT * FROM table WHERE pk = ? AND sk BETWEEN ? AND ?` — translated into the same key-based operations under the hood — which lowers the learning curve and makes the access patterns explicit. The caveat: PartiQL is syntax, not a query engine — it does not change what DynamoDB can do; a PartiQL query that would need a scan still scans.
- GSIs, on-demand capacity, and DAX caching support scaling; hot keys and scans are the classic pitfalls. GSIs trade storage and write cost for alternative read paths; on-demand capacity auto-scales (at a premium vs provisioned); DAX (a managed cache) absorbs hot read workloads. The classic failures: hot keys (one key absorbing disproportionate traffic, overwhelming its partition), scans that grow with table size, and GSI throttling when the base table's writes exceed the index's capacity.
- For mykb: the node anchors the AWS NoSQL branch — key-value stores, consistent hashing, and partition-pruning concepts connect to this concrete implementation.

## Related

- [[wiki/data-storage/key-value-stores|Key-Value Stores]] — key-value fundamentals
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — distribution under the hood
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning And Zone Maps]] — querying by key
- [[wiki/data-storage/hot-and-cold-data-tiering|Hot And Cold Data Tiering]] — capacity planning
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
