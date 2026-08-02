---
type: "concept"
title: "Protocol Buffers"
description: "Compact, typed binary serialization with schema evolution rules, used by gRPC"
tags: ["protobuf", "serialization", "grpc", "schemas", "binary"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://protobuf.dev/", "https://protobuf.dev/programming-guides/encoding/"]
---
# Protocol Buffers

## Summary
Protocol Buffers serialize structured data as compact binary using field tags and wire types. A .proto schema defines messages, fields are numbered, and generated code handles encoding in any language. Field numbers and rules like reserved and optional enable compatible evolution.

## Details
- **Encoding** — varints, length-delimited, and fixed-width wire types; field numbers (not names) travel on the wire, so they are immutable once released.
- **Schema evolution** — add fields with new numbers, never reuse or change types of released numbers; `reserved` protects numbers from accidental reuse.
- **Typed codegen** — protoc and plugins emit strongly typed classes, reducing runtime reflection and parsing bugs.
- **Compared with JSON** — smaller, faster, schema-checked, but not human-readable; JSON interop requires converters.
- **Worked example** — a memory service stores pulse entries as protobuf messages, with field 1 reserved for future schema migration.
- **Relevance** — RSIS3's typed tool contracts can use protobuf where payload sizes and schema strictness matter.

## Related
- [[wiki/api-protocols/rest-vs-grpc|REST vs gRPC]] — adjacent concept in this wiki
- [[wiki/api-protocols/insecure-deserialization|Insecure Deserialization]] — adjacent concept in this wiki
- [[wiki/api-protocols/client-libraries|API Client Libraries]] — adjacent concept in this wiki
- [[wiki/api-protocols/m2m-tokens|Machine-to-Machine Tokens]] — adjacent concept in this wiki
- [[wiki/api-protocols/protobuf|Protocol Buffers]] — existing coverage
- [[wiki/api-protocols/grpc|gRPC]] — existing coverage
- [[wiki/api-protocols/content-negotiation|Content Negotiation]] — existing coverage
