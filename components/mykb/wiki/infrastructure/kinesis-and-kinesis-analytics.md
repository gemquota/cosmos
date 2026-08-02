---
type: "concept"
title: "Kinesis and Kinesis Analytics"
description: "AWS streaming ingestion with SQL-based stream analytics"
tags: ["kinesis", "aws", "streaming", "analytics"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Kinesis and Kinesis Analytics

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Kinesis Data Streams ingests sharded records with retention up to 365 days.
- Kinesis Data Firehose delivers to S3, Redshift, and OpenSearch with batching.
- Kinesis Data Analytics runs Flink SQL applications over streams.
- Shard count determines throughput; scaling adds or splits shards.

## Related

- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — platform landscape
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — analytics engines
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — Firehose destinations
- [[wiki/data-storage/sharding-and-partitioning-revisited|Sharding And Partitioning Revisited]] — shard model
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
