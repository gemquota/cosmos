---
type: "concept"
title: "AWS MSK and Managed Kafka"
description: "Fully managed Apache Kafka clusters on AWS"
tags: ["msk", "kafka", "aws", "managed"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# AWS MSK and Managed Kafka

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- MSK provisions and operates Kafka brokers and ZooKeeper (or KRaft) nodes.
- It integrates with IAM, CloudWatch, and Glue Schema Registry for governance.
- MSK Serverless removes capacity planning with on-demand scaling.
- You still design topics, partitions, and replication factor; AWS handles the machinery.

## Related

- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — managed Kafka context
- [[wiki/infrastructure/kafka-vs-pulsar-vs-redpanda|Kafka Vs Pulsar Vs Redpanda]] — alternative platforms
- [[wiki/infrastructure/confluent-cloud-and-schema-registry|Confluent Cloud And Schema Registry]] — managed alternative with schema tools
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
