---
type: "concept"
title: "Correlation IDs"
description: "IDs attached to logs, metrics, and traces so one request is findable everywhere"
tags: ["logging", "correlation", "observability", "ids"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Correlation IDs

## Summary
A correlation ID ties all log lines, spans, and error reports of one logical unit of work together. Unlike trace IDs they are usually a logging convention first and a tracing construct second.

## Details
- Generate at the edge, propagate in headers or context, and log it in every relevant line.
- Include correlation IDs in user-facing error messages so support can pull the whole story.
- They only work if every hop forwards them — the gap between services is where correlations break.
- mykb relevance: correlation IDs let a user paste an article slug and get every pipeline log for it.

## Related
- [[wiki/dev-tools/distributed-tracing-ids|Distributed Tracing IDs]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/dev-tools/request-tracing|Request Tracing]]
- [[wiki/dev-tools/baggage-propagation|Baggage Propagation]]
- [[wiki/dev-tools/log-aggregators|Log Aggregators]]
