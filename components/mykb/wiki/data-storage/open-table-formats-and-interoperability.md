---
type: "concept"
title: "Open Table Formats and Interoperability"
description: "Delta, Iceberg, and Hudi as portable, spec-driven lakehouse formats"
tags: ["open-table-formats", "interoperability", "lakehouse", "specs"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Open Table Formats and Interoperability

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Open formats decouple table semantics from any single engine, avoiding vendor lock-in.
- Iceberg's spec, Delta's protocol, and Hudi's timeline each define metadata and commits.
- Interoperability projects (Uniform tables, XTable) let engines read each other's tables.
- Real interop requires catalog agreements, not just file-format compatibility.

## Related

- [[wiki/data-storage/open-table-formats|Open Table Formats]] — existing note
- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — lakehouse context
- [[wiki/data-storage/uniform-tables-and-format-agnostic-engines|Uniform Tables And Format Agnostic Engines]] — interop mechanism
- [[wiki/data-storage/table-format-comparisons|Table Format Comparisons]] — format comparison
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
