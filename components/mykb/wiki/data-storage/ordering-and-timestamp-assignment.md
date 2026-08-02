---
type: "concept"
title: "Ordering and Timestamp Assignment"
description: "Where and how events get their timestamps"
tags: ["timestamps", "ordering", "event-time", "streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Ordering and Timestamp Assignment

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Timestamps come from sources (device, server), extractors, or processing engines.
- Assignment strategy affects event-time processing and window correctness.
- Watermarks and late-data policies rely on trustworthy timestamp assignment.
- Monitor clock skew: sources with wrong clocks corrupt ordering.

## Related

- [[wiki/data-storage/stream-windowing|Stream Windowing]] — windows use timestamps
- [[wiki/data-storage/event-time-vs-processing-time|Event Time Vs Processing Time]] — time domains
- [[wiki/data-storage/logical-clocks-and-timestamps|Logical Clocks And Timestamps]] — clock theory
- [[wiki/data-storage/hybrid-logical-clocks-and-true-time|Hybrid Logical Clocks And True Time]] — hybrid clocks
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
