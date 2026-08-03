---
type: "concept"
title: "Correlation IDs"
description: "IDs attached to logs, metrics, and traces so one request is findable everywhere"
tags: ["logging", "correlation", "observability", "ids"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Correlation IDs

## Summary
A correlation ID ties all log lines, spans, and error reports of one logical unit of work together. Unlike trace IDs it is usually a logging convention first and a tracing construct second — a human-readable handle that makes one request findable across every system that touched it.

## Details
- Mechanism: the ID is generated at the edge (ingress, scheduler, job runner), propagated in headers or context through every hop, and logged in every relevant line; it appears in error responses so users and support share the same handle; aggregators filter on it to reconstruct the full story.
- Concrete example: a user reports a failed article import with ID abc123; support greps the log aggregator for abc123 and sees the ingestion, transformation, and publishing steps in order — including the error at the third stage; the same ID threads through metrics and traces for deeper investigation.
- Failure modes: propagation gaps — a hop that does not forward the header breaks the chain, and the correlation silently dies at the service boundary; IDs regenerated per service instead of forwarded, so each system has its own story; IDs not logged on error paths, defeating the purpose; high-cardinality or PII-bearing IDs leaking user data into logs.
- Tradeoffs: correlation IDs are nearly free (one header and log field) but only as good as the propagation discipline; the alternative, timestamp-based reconstruction, fails under concurrency; the mature pattern is generate-once, forward-always, log-everywhere, with the ID in user-facing errors.
- Operational notes: validate propagation in tests, add the ID to every log line and alert, and enforce a standard header name.
- RSIS3 relevance: correlation IDs let a user paste an article slug and get every pipeline log for it — the same traceability RSIS3 wants for each loop iteration.

## Related
- [[wiki/dev-tools/distributed-tracing-ids|Distributed Tracing IDs]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/dev-tools/baggage-propagation|Baggage Propagation]]
- [[wiki/dev-tools/log-aggregators|Log Aggregators]]
