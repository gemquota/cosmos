---
type: "concept"
title: "Real-Time Personalization"
description: "Adapting experiences within seconds of user behavior"
tags: ["personalization", "real-time", "streaming", "serving"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Real-Time Personalization

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Real-time personalization reacts to the latest event: last click, session context, current intent.
- Architecture: event stream, feature store with low-latency lookups, fast model inference.
- Balance freshness against cost and stability; most signals decay quickly.
- Guardrails: fall back to batch/global ranking when online signals are missing.

## Related

- [[wiki/data-storage/personalization-data-flows|Personalization Data Flows]] — data flow
- [[wiki/data-storage/streaming-data-pipelines|Streaming Data Pipelines]] — event path
- [[wiki/data-storage/cache-aside-and-write-through|Cache Aside And Write Through]] — caching features
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
