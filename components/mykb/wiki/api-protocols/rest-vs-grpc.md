---
type: "concept"
title: "REST vs gRPC"
description: "JSON-over-HTTP versus typed binary contracts over HTTP/2"
tags: ["api", "rest", "grpc", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# REST vs gRPC

## Summary
JSON-over-HTTP versus typed binary contracts over HTTP/2. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- REST speaks JSON over HTTP/1.1; gRPC speaks protobuf over HTTP/2
- gRPC offers streaming and strong contracts; REST offers tooling and cacheability
- Open question — how do browsers consume gRPC-web pragmatically?

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-vs-rpc|REST vs RPC]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-vs-graphql|REST vs GraphQL]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-vs-grpc|REST vs gRPC]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-apis|REST APIs]] — related coverage in the same cluster
- [[wiki/api-protocols/rpc-styles|RPC Styles]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql|GraphQL]] — related coverage in the same cluster
