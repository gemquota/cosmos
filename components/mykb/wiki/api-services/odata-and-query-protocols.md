---
type: "concept"
title: "OData and Query Protocols"
description: "Standardized REST query syntax for data services"
tags: ["odata", "query-protocols", "rest", "api-design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# OData and Query Protocols

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- OData standardizes $filter, $orderby, $top, $skip, $expand over REST resources.
- It shines for enterprise data services with predictable, discoverable queries.
- Implementation cost: query parser, validation, and safe translation to SQL.
- Alternatives: RSQL, JSON:API filters, and vendor DSLs.

## Related

- [[wiki/api-services/api-design-for-data|Api Design For Data]] — API design
- [[wiki/api-services/filtering-and-query-dsls|Filtering And Query Dsls]] — DSL design
- [[wiki/api-services/pagination-and-cursor-patterns|Pagination And Cursor Patterns]] — pagination
- [[wiki/data-storage/sql-engines|SQL Engine Architecture]] — backend translation
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
