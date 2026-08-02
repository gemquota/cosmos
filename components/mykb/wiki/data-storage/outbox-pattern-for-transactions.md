---
type: "concept"
title: "Outbox Pattern for Transactions"
description: "Reliably publishing events from a database transaction"
tags: ["outbox", "events", "transactions", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Outbox Pattern for Transactions

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- The outbox pattern writes events into a table in the same transaction as the business change.
- A relay (CDC or poller) publishes outbox rows to the message bus.
- It guarantees events are not lost when the business write commits.
- Combine with idempotent consumers and deduplication for exactly-once delivery.

## Related

- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — problem context
- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — relay mechanism
- [[wiki/data-storage/transactional-outbox-and-cdc-relay|Transactional Outbox And Cdc Relay]] — outbox + CDC
- [[wiki/api-services/exactly-once-webhook-delivery|Exactly Once Webhook Delivery]] — delivery guarantees
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
