---
type: "concept"
title: "Full-Stack Development"
description: "Owning the whole product: client, server, data, and deployment"
tags: ["full-stack", "development", "end-to-end", "ownership"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Full-stack_developer", "https://en.wikipedia.org/wiki/Web_application"]
---

# Full-Stack Development

## Summary
Full-stack development means working across the entire product — frontend, backend, data, and operations — with the judgment to know when to go deep. It is a breadth role that shines in small teams and prototypes, where context spans the whole system.

## Details
- A full-stack engineer reads the whole stack: HTTP, APIs, databases, caches, and deployment pipelines.
- The value is end-to-end ownership: features ship without handoffs, and debugging spans layers naturally.
- The risk is the jack-of-all-trades trap: shallow everywhere instead of deliberately deep where it matters.
- Full-stack is a team shape too: product engineers own slices vertically, with specialists for the hard layers.
- Security and data correctness are the full-stack engineer's silent responsibilities — breadth means no one else is looking.
- For the mykb bundle, the curator-tooling owner is effectively full-stack: scripts, storage, CI, and the reading interface.
- Worked example — a full-stack wiki feature: add a tag filter in the UI, a query parameter in the API, an index in the store, and a cache header in the CDN config — one PR, one owner.

Worked example — a full-stack wiki feature: add a tag filter in the UI, a query parameter in the API, an index in the store, and a cache header in the CDN config — one PR, one owner.

## Related
- [[wiki/compositions/frontend-architecture|Frontend Architecture]]
- [[wiki/compositions/backend-architecture-patterns|Backend Architecture Patterns]]
- [[wiki/compositions/api-design-best-practices|API Design Best Practices]]
- [[wiki/compositions/database-migrations|Database Migrations]]
- [[wiki/tooling/platform-engineering|Platform Engineering]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/compositions/query-optimization|Query Optimization]]
- [[wiki/compositions/explain-analyze|EXPLAIN ANALYZE]]
- [[wiki/api-protocols/rest-apis|REST APIs]]
- [[wiki/api-protocols/graphql|GraphQL]]
