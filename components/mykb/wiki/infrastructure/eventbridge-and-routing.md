---
type: "concept"
title: "EventBridge and Event Routing"
description: "AWS's event bus with content-based routing, filtering, and targets"
tags: ["eventbridge", "aws", "event-routing", "eda"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# EventBridge and Event Routing

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- EventBridge routes events from sources to targets via rules with content-based filters.
- Schemas, schema registries, and archive/replay improve event governance.
- It supports scheduled rules, API destinations, and cross-account buses.
- Compared to SNS: richer filtering, schema tooling, and target integration catalog.

## Related

- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — event-driven context
- [[wiki/infrastructure/sqs-and-sns-fanout|Sqs And Sns Fanout]] — simpler fanout alternative
- [[wiki/api-services/webhooks-and-event-apis|Webhooks And Event Apis]] — HTTP targets
- [[wiki/data-storage/schema-registry-and-evolution|Schema Registry And Evolution]] — schema governance for events
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
