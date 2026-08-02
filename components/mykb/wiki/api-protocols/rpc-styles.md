---
type: "concept"
title: "RPC Styles"
description: "Taxonomy of RPC styles and their trade-offs"
tags: ["rpc", "api-styles", "architecture", "rest", "grpc"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Remote_procedure_call", "https://www.martinfowler.com/articles/richardsonMaturityModel.html"]
---

# RPC Styles

## Summary
Remote procedure call is the oldest API style: a client calls a function that executes on a server. The styles form a spectrum — classic RPC (CORBA, SOAP), modern RPC (gRPC, Thrift), REST, and GraphQL — differing in contract strictness, coupling, caching, and tooling.

## Details
- Classic RPC: CORBA, XML-RPC, SOAP — binary or XML contracts with rigid stubs; powerful but notorious for versioning pain and heavyweight toolchains.
- Modern RPC: gRPC (protobuf over HTTP/2), Apache Thrift, and Cap'n Proto — codegen from IDL, strong typing, streaming, and rich error models.
- REST: resources + HTTP verbs + status codes; loose, cacheable, and interoperable, but action semantics are implicit and contracts are documents, not code.
- GraphQL: a query language where clients shape responses; flexible reads, but caching and backend control get harder.
- Trade-offs: strict IDL gives compile-time safety and fast wire formats, at the cost of versioning rigidity; REST trades safety for longevity and ubiquity.
- Hybrid reality: most systems are polyglot — gRPC internally, REST at the edge, GraphQL for client-driven surfaces (see BFF).
- Choosing: match contract stability to team size and change rate; the IDL is a contract you will live with for years.

## Related
- [[wiki/api-protocols/grpc|gRPC]] — the flagship modern RPC framework
- [[wiki/api-protocols/rest-apis|REST APIs]] — the resource-oriented alternative
- [[wiki/api-protocols/graphql|GraphQL]] — the query-language alternative
- [[wiki/api-protocols/json-rpc|JSON-RPC]] — the minimal JSON RPC standard
- [[wiki/api-protocols/rest-maturity-model|REST Maturity Model]] — level 0 is RPC-style HTTP
