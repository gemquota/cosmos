---
type: "concept"
title: "DynamoDB and PartiQL"
description: "AWS serverless key-value/document store with SQL-like PartiQL access"
tags: ["dynamodb", "partiql", "aws", "nosql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# DynamoDB and PartiQL

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- DynamoDB is a fully managed key-value and document database with single-digit-millisecond latency.
- Design centers on primary keys: partition key and optional sort key determine access patterns.
- PartiQL adds SQL-like syntax over items, complementing the classic API operations.
- GSIs, on-demand capacity, and DAX caching support scaling; hot keys and scans are the classic pitfalls.

## Related

- [[wiki/data-storage/key-value-stores|Key-Value Stores]] — key-value fundamentals
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — distribution under the hood
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning And Zone Maps]] — querying by key
- [[wiki/data-storage/hot-and-cold-data-tiering|Hot And Cold Data Tiering]] — capacity planning
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
