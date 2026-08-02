---
type: "concept"
title: "Exactly-Once Processing"
description: "The strongest delivery guarantee in stream processing"
tags: ["exactly-once", "streaming", "guarantees", "transactions"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/documentation/", "https://en.wikipedia.org/wiki/Stream_processing"]
---

# Exactly-Once Processing

## Summary

Exactly-once means each record affects results exactly once despite failures and retries.
It is achieved through idempotency, transactional sinks, or checkpointed state.
End-to-end exactly-once requires every hop to cooperate.
Exactly-once is a system property, not a magic switch; every component must participate.

## Details

- Kafka provides exactly-once within its ecosystem via transactional producers.
- Flink achieves it with checkpointed state and transactional/2PC sinks.
- Idempotent writes make at-least-once behave like exactly-once.
- Genuine end-to-end guarantees need source and sink participation.
- Cost: latency and coordination overhead versus at-least-once.
- Prefer idempotent sinks over complex protocols where possible.
- Document which guarantee applies at each hop.
- Choose guarantees per hop and prove them with tests; a vague 'exactly once' claim is a liability.

## Related

- [[wiki/data-storage/processing-guarantees-at-least-once|Processing Guarantees At Least Once]] — baseline
- [[wiki/data-storage/kafka-transactions-and-atomicity|Kafka Transactions And Atomicity]] — Kafka transactions
- [[wiki/data-storage/idempotent-writes-and-upserts|Idempotent Writes And Upserts]] — idempotency
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — existing note
- [[wiki/data-storage/checkpointing-and-recovery-flink|Checkpointing And Recovery Flink]] — Flink checkpoints
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

