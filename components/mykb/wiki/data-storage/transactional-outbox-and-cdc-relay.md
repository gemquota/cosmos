---
type: "concept"
title: "Transactional Outbox and CDC Relay"
description: "Publishing outbox rows through change data capture"
tags: ["outbox", "cdc", "relay", "event-driven"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Transactional Outbox and CDC Relay

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- CDC (Debezium, Maxwell) reads the outbox table's transaction log and publishes events.
- This removes the poller and gives ordered, low-latency delivery.
- Outbox rows carry a unique event ID for deduplication at consumers.
- Schema and routing metadata in the outbox row shapes the emitted event.

## Related

- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — CDC
- [[wiki/data-storage/outbox-pattern-for-transactions|Outbox Pattern For Transactions]] — outbox basics
- [[wiki/data-storage/debezium-and-cdc-tools|Debezium And Cdc Tools]] — CDC tooling
- [[wiki/api-services/exactly-once-webhook-delivery|Exactly Once Webhook Delivery]] — consumer guarantees
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
