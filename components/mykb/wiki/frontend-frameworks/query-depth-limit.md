---
type: "concept"
title: "Query Depth Limits"
description: "Capping query nesting to blunt GraphQL DoS"
tags: ["graphql", "security", "queries", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Query Depth Limits

## Summary
Query depth limits cap how deeply a GraphQL document may nest selections — `query { user { friends { posts { comments { ... } } } } }` — so a small document cannot trigger exponentially deep resolver chains. They are the simplest line of defense against GraphQL DoS, and they are usually combined with cost analysis and persisted queries because depth alone misses wide and expensive queries.

## Details
- Mechanism: after parsing, the server walks the selection set and computes the maximum nesting depth of fields; a document whose depth exceeds the limit (commonly 8-12) is rejected before execution. Depth correlates with worst-case work because each level multiplies the number of resolvers that can run — a chain of lists 12 levels deep can expand combinatorially, while a 4-level query is bounded by the data. Depth limits are cheap, deterministic, and schema-independent, which is why every GraphQL security middleware ships one by default.
- Concrete examples: a public API rejects a 15-level nested introspection probe; a gateway applies a depth limit of 10 while the schema's deepest legitimate query is 6, leaving headroom; an admin tool that legitimately needs deep traversal is exempted per-role. The limit is usually configurable per operation type (queries deeper than mutations) and enforced alongside an introspection toggle, since introspection documents are extremely deep and are a common probe vector.
- Failure modes: depth limits alone fail against wide queries — `{ a: f1, b: f2, ... 500 top-level fields }` has depth 1 but runs 500 resolvers, and aliases multiply the same field's executions without increasing depth. They also misclassify deep-but-cheap queries (deep singleton chains, like a 20-level config object, are harmless) and shallow-but-expensive ones (a breadth-2 query that fans out across millions of rows). Overly aggressive limits break legitimate clients; too-loose limits let real attacks through.
- Operational tradeoffs: the layered answer is depth limits (blunt nesting) plus complexity scoring (per-field weights that charge aliases, list multipliers, and expensive resolvers) plus persisted queries (allowlist) plus timeouts. Cost analysis is more accurate but needs maintenance as the schema evolves — every expensive field must be weighted. The practice: start with a depth limit and persisted queries, add complexity scoring when profiling shows wide queries slipping through, and tune limits from the deepest real query plus margin rather than guesswork.
- RSIS3/mykb relevance: agent-generated GraphQL queries (RSIS3 tools probing the knowledge graph) are exactly the population that needs depth and cost budgets — bounded by the same allowlist-plus-cost discipline so an agent's exploration cannot exhaust the daemon, mirroring RSIS3's resource budgets for loops.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]]
- [[wiki/frontend-frameworks/graphql-aliases|GraphQL Aliases]]
- [[wiki/frontend-frameworks/graphql-variables|GraphQL Variables]]
- [[wiki/frontend-frameworks/graphql-directives|GraphQL Directives]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]]
- [[wiki/api-protocols/graphql-security|GraphQL Security]]
