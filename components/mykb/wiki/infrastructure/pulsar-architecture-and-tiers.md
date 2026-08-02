---
type: "concept"
title: "Pulsar Architecture and Tiered Storage"
description: "Segment-based broker/storage separation with unbounded retention"
tags: ["pulsar", "event-streaming", "tiered-storage", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pulsar Architecture and Tiered Storage

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Pulsar brokers serve topics while BookKeeper persists segments; the two scale independently.
- Tiered storage offloads old segments to S3/GCS, enabling unbounded retention cheaply.
- Multi-tenancy with namespaces and quotas isolates teams on one cluster.
- Function-style processing and IO connectors round out the platform.

## Related

- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — platform landscape
- [[wiki/data-storage/object-storage|Object Storage]] — tiered storage target
- [[wiki/infrastructure/kafka-vs-pulsar-vs-redpanda|Kafka Vs Pulsar Vs Redpanda]] — comparison context
- [[wiki/data-storage/compaction-and-retention-kafka|Compaction And Retention Kafka]] — retention tradeoffs
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
