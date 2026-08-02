---
type: "concept"
title: "Google Pub/Sub"
description: "Serverless, globally available event ingestion with at-least-once delivery"
tags: ["pubsub", "gcp", "messaging", "event-streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Google Pub/Sub

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Pub/Sub decouples publishers and subscribers with pull and push subscriptions.
- It is serverless: no brokers to manage, with global namespaces and regional endpoints.
- Ordering is best-effort unless ordered-delivery keys are used; exactly-once is via idempotent consumers.
- Dataflow, Cloud Functions, and BigQuery subscriptions make it GCP's event backbone.

## Related

- [[wiki/data-storage/message-queues|Message Queues]] — queue semantics
- [[wiki/infrastructure/eventbridge-and-routing|Eventbridge And Routing]] — routing comparison
- [[wiki/api-services/exactly-once-webhook-delivery|Exactly Once Webhook Delivery]] — delivery guarantees
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — platform landscape
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
