---
type: "concept"
title: "Protocol Buffers"
description: "Language-neutral, binary serialization schema language for typed structured data"
tags: ["protobuf", "serialization", "schemas", "grpc", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://protobuf.dev/overview/", "https://protobuf.dev/programming-guides/proto3/"]
---

# Protocol Buffers

## Summary
Protocol Buffers (protobuf) is Google's language-neutral binary serialization format. Messages are defined in `.proto` schemas and compiled into typed classes with compact wire encoding.

## Details
- Field numbers keep wire format stable while fields evolve; `optional`, `repeated`, and `oneof` model structure.
- Backward/forward compatibility comes from unknown-field preservation, complementing API versioning practice.
- Compare with JSON Schema: protobuf is binary and faster, JSON Schema is human-readable and web-native.
- Protocol Buffers is a language-neutral, platform-neutral serialization format: messages are defined in .proto files and compiled into efficient binary encodings.
- Encoding uses tag-length-value framing with varints, which keeps small integers compact and allows schema evolution via field numbers.
- Field numbers are the contract: renaming or reordering fields breaks wire compatibility, while adding new fields with new numbers stays backward-compatible.
- Generated code provides type safety and reflection, and the binary format is dramatically smaller and faster to parse than JSON.
- **Worked example / comparison** — Worked example — a message with an int32 field uses one byte for common values; adding field 4 later does not break clients that only know fields 1-3.
- For mykb, protobuf is documented as the IDL and wire format behind gRPC services.

## Related
- [[wiki/api-protocols/grpc|gRPC]]
- [[wiki/api-protocols/json-schema|JSON Schema]]
- [[wiki/api-protocols/api-versioning|API Versioning]]
- [[wiki/api-protocols/message-queues|Message Queues]]
- [[wiki/concepts/mykb-analysis|Mykb Analysis]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/markdown-linting|Markdown Linting]]
- [[wiki/concepts/explainers|Explainers]]
