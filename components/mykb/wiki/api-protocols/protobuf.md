---
type: "concept"
title: "Protocol Buffers"
description: "Language-neutral, binary serialization schema language for typed structured data"
tags: ["protobuf", "serialization", "schemas", "grpc", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Protocol Buffers

## Summary
Protocol Buffers (protobuf) is Google's language-neutral binary serialization format. Messages are defined in `.proto` schemas and compiled into typed classes with compact wire encoding.

## Details
- Field numbers keep wire format stable while fields evolve; `optional`, `repeated`, and `oneof` model structure.
- Backward/forward compatibility comes from unknown-field preservation, complementing API versioning practice.
- Compare with JSON Schema: protobuf is binary and faster, JSON Schema is human-readable and web-native.

## Related
- [[wiki/api-protocols/grpc|gRPC]] — primary consumer of protobuf schemas
- [[wiki/api-protocols/json-schema|JSON Schema]] — text-based schema alternative
- [[wiki/api-protocols/api-versioning|API Versioning]] — schema evolution rules
- [[wiki/api-protocols/message-queues|Message Queues]] — binary payloads on the wire
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — data format trade-offs for the wiki
