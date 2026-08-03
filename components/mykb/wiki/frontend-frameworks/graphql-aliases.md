---
type: "concept"
title: "GraphQL Aliases"
description: "Renaming fields in responses to disambiguate queries"
tags: ["graphql", "queries", "aliases", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# GraphQL Aliases

## Summary
GraphQL aliases let a client rename a field in the response by writing `aliasName: fieldName(args)`. Their primary job is disambiguation: fetching the same field twice with different arguments is impossible without aliases, because GraphQL responses key results by field name. Aliases are a small but foundational part of the query language.

## Details
- Mechanism: in a query like `{ today: weather(city: "NYC") { temp }, weekend: weather(city: "LA") { temp } }`, the response is keyed under `today` and `weekend` rather than `weather`, so two executions of the same field can coexist. The server executes each aliased field independently and returns the results under the alias; nested selections work the same way. Aliases do not change execution semantics — the resolver runs once per alias — they only rename the response key.
- Concrete examples: a dashboard fetches `thisWeek` and `lastWeek` revenue in one query; a chat UI fetches the latest message and the unread count for two conversations; a compare screen renders two products' prices side by side. Aliases are also used to fetch the same connection with different filters (featured vs. recent) and to disambiguate fields when a client-side cache keys responses by field path.
- Failure modes: the main failure is cost amplification — aliases let one query execute an expensive field many times (`{ a: slowField, b: slowField, c: slowField }` runs the resolver three times), which interacts badly with naive query-cost analysis that charges per unique field rather than per execution. Depth and breadth limits must account for aliases, or a single query can multiply work behind a small-looking document. Confusingly named aliases also hurt readability and make persisted-query reviews harder.
- Operational tradeoffs: aliases are client-side syntax with server-side cost consequences, so the server's security and cost controls (query depth, complexity scoring, time limits) must treat each alias as a separate execution. The countermeasure is cost analysis that counts resolver executions, plus complexity budgets per query; some gateways also cap the number of aliased fields per operation. For clients, aliases enable compact queries, but the same result is often achievable with GraphQL variables and a loop, at the cost of more round trips.
- RSIS3/mykb relevance: MyKB's graph queries compare metrics across time windows — a natural alias use case; the operational lesson is that any query-cost discipline in the daemon's API must count aliased executions, mirroring RSIS3's rule that resource budgets are enforced at the point of actual work.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]]
- [[wiki/frontend-frameworks/graphql-variables|GraphQL Variables]]
- [[wiki/frontend-frameworks/graphql-directives|GraphQL Directives]]
- [[wiki/frontend-frameworks/graphql-batching|GraphQL Batching]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]]
- [[wiki/api-protocols/graphql-security|GraphQL Security]]
