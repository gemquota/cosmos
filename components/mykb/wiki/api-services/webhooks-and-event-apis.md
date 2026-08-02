---
type: "concept"
title: "Webhooks and Event APIs"
description: "Delivering events to systems instead of polling"
tags: ["webhooks", "events", "api", "event-driven"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.github.com/en/webhooks", "https://en.wikipedia.org/wiki/Webhook"]
---

# Webhooks and Event APIs

## Summary

Webhooks push events to subscriber endpoints when things happen.
They replace polling, reducing latency and load.
Reliable delivery needs retries, signatures, and idempotency.
Webhooks invert the integration model: consumers register, producers push.

## Details

- Register endpoints; deliver signed HTTP POSTs.
- Retry with backoff; use DLQs for poison events.
- Payloads carry event IDs for deduplication.
- Verify signatures to prevent forgery.
- Event bridges and buses (EventBridge, SNS) scale fan-out.
- Sign every delivery and verify on receipt.
- Provide replay and introspection endpoints for operational sanity.
- Webhooks are the standard push mechanism for modern event-driven integrations.

## Related

- [[wiki/api-services/exactly-once-webhook-delivery|Exactly Once Webhook Delivery]] — delivery
- [[wiki/api-services/api-design-for-data|API Design for Data]] — API design
- [[wiki/infrastructure/eventbridge-and-routing|Eventbridge And Routing]] — routing
- [[wiki/api-services/api-key-management|API Key Management]] — auth
- [[wiki/api-services/retry-strategies-and-backoff-jitter|Retry Strategies And Backoff Jitter]] — retries
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing

