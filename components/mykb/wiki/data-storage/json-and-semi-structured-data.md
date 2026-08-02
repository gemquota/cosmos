---
type: "concept"
title: "JSON and Semi-Structured Data"
description: "Storing and querying flexible, schema-less documents"
tags: ["json", "semi-structured", "nosql", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/datatype-json.html", "https://en.wikipedia.org/wiki/JSON"]
---

# JSON and Semi-Structured Data

## Summary

Semi-structured data has shape but no fixed schema, typically represented as JSON.
Modern databases blend relational and JSON querying.
JSON flexibility comes at the cost of schema discipline.
Semi-structured data thrives at ingestion; structure emerges where queries demand it.

## Details

- JSONB in Postgres indexes and queries documents efficiently.
- Document databases (MongoDB) make JSON the native model.
- Warehouses parse JSON for exploration before formal modeling.
- Schema drift is the main risk; validation helps.
- JSONL (newline-delimited) is the standard interchange form.
- Balance flexibility against drift with validation and contracts.
- JSONB-style indexing keeps document queries fast.
- Treat semi-structured data as an interface: validate at the boundary, structure where it matters.

## Related

- [[wiki/data-storage/document-databases|Document Databases]] — JSON-native stores
- [[wiki/data-storage/json-lines-and-ndjson|Json Lines And Ndjson]] — file form
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — drift
- [[wiki/data-storage/document-stores|Document Stores]] — document stores
- [[wiki/data-storage/data-profiling-and-validation|Data Profiling and Validation]] — validation
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

