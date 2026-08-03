---
type: "concept"
title: "Sparse Fieldsets"
description: "Letting clients select which fields a response includes"
tags: ["api", "http", "design", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Sparse Fieldsets

## Summary
Sparse fieldsets let a client request only the fields it actually needs, typically through a `fields` query parameter such as `GET /users/42?fields=id,name,email`. They cut payload size, rendering work, and bandwidth on mobile, and they turn a fat resource representation into a projection the client controls.

## Details
- Mechanism: the server parses the `fields` list, validates each name against the resource schema, and serializes only the requested subset of the object. Unlisted fields are omitted entirely, which changes both the payload and its shape, so clients must treat the response as a projection rather than assuming a fixed schema. Nested projections need a consistent notation, for example `fields=user(id,name),posts(id,title)`, and some APIs accept comma-separated dotted paths like `fields=id,name,author.id`.
- Concrete examples: a mobile feed endpoint that returns 50KB of user objects per item can drop to a few KB with `fields=id,name,avatar`; an admin dashboard listing 10,000 rows fetches only the columns its table renders; a partner integration that needs just `order.id` and `order.status` avoids pulling full line-item details. GraphQL solves the same problem structurally, which is why sparse fieldsets are sometimes called the REST analog of GraphQL selection sets.
- Failure modes: unknown field names are the classic trap — servers that silently ignore them return a partial projection and clients break confusingly, while servers that reject them force clients to track schema versions. Renaming a field breaks every projection that referenced it, so field names are part of the API contract and need deprecation discipline. Recursive or deeply nested projections can amplify, not shrink, a response, and `fields=*` or unbounded lists defeat the purpose.
- Operational tradeoffs: implementing fieldsets adds schema introspection and validation code, but the payoff is real: smaller payloads mean lower egress cost, faster mobile rendering, and less work for intermediary caches. The tradeoffs are complexity in the serializer, cache-key divergence (each projection is a different response, so caching must include the fields parameter), and the temptation to let default responses stay fat while only select clients project. A common compromise is sensible defaults plus fieldsets for heavy resources and list endpoints.
- RSIS3/mykb relevance: the same projection discipline applies to MyKB's knowledge graph and search APIs — letting dashboard views request only the fields they render (titles, links, timestamps) keeps graph queries fast as the wiki grows, mirroring RSIS3's principle of reading only what each loop needs.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]]
- [[wiki/api-protocols/api-pagination|API Pagination]]
- [[wiki/api-protocols/api-filtering|API Filtering]]
- [[wiki/api-protocols/api-sorting|API Sorting]]
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]]
- [[wiki/api-protocols/offset-pagination|Offset Pagination]]
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]]
