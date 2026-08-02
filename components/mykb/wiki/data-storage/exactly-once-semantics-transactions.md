---
type: "concept"
title: "Exactly-Once Semantics and Transactions"
description: "The illusion of processing each record once, end to end"
tags: ["exactly-once", "transactions", "streaming", "flink"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Exactly-Once Semantics and Transactions

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Exactly-once means each record affects state and sinks exactly once despite failures.
- Flink achieves it with checkpointed state plus transactional or idempotent sinks.
- Kafka provides exactly-once within its ecosystem via transactional producers.
- End-to-end exactly-once requires the sink to participate (two-phase or idempotency).

## Related

- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — existing note
- [[wiki/data-storage/two-phase-commit|Two-Phase Commit]] — transactional sinks
- [[wiki/data-storage/processing-guarantees-at-least-once|Processing Guarantees At Least Once]] — baseline guarantee
- [[wiki/data-storage/kafka-transactions-and-atomicity|Kafka Transactions And Atomicity]] — Kafka transactions
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
