---
type: "entity"
title: "Alternative Protocols"
description: "Alternative Protocols"
tags: ["entity", "android", "api", "ast", "auth", "aws"]
timestamp: "2026-07-19T22:41:41Z"
status: "growing"
resource: ""
---


## Alternative Protocols

Alternative Protocols appears in 1 session(s) categorized as API, Cloud, Mobile, Security. Related topics: android, api, auth, aws.

**Domain:** Mobile Platform › [[wiki/web-platforms/00-index|Android Core]] › [[wiki/web-platforms/supercategories/api-services/categories/api-rest/00-index|Api Clients › Alternative Protocols

## Overview

"Alternative protocols" refers to communication mechanisms that can stand in for the default HTTP/HTTPS stack in API design. Common options include WebSocket for bidirectional streaming, gRPC for typed, high-throughput RPC over HTTP/2, MQTT for lightweight publish-subscribe messaging on constrained devices, and SSE for one-way server push. Each alternative trades something against plain REST: connection semantics, payload encoding, latency, or power consumption. Teams typically reach for these when request-response polling becomes wasteful, when streaming is intrinsic to the domain, or when clients need strongly typed contracts.

## Details

- WebSocket: persistent full-duplex channel; good for chat, dashboards, and collaborative editing, with its own handshake and reconnection concerns.
- gRPC: Protocol Buffers-based RPC with streaming, deadlines, and first-class code generation; strong fit for internal service-to-service traffic.
- MQTT: broker-based pub/sub with small packets and QoS levels; common in IoT where battery and bandwidth are scarce.
- SSE: unidirectional server push over plain HTTP; simpler than WebSocket when only server-to-client events are needed.

In mobile and cloud settings the choice affects more than the wire format: authentication, proxies, and load balancers must all understand the protocol, and firewalls may block non-HTTP ports. Some architectures layer alternative protocols behind a gateway so clients keep one stable surface while the backend can evolve transport. AWS-oriented stacks, for example, often expose REST or HTTP APIs at the edge while internal services communicate over gRPC or event streams, keeping the public contract simple and the internal fabric fast.

## Related Entities
## Choosing

There is no universal winner: the right protocol follows the workload. Frequent small messages favor MQTT or WebSocket; large typed RPC batches favor gRPC; one-way event feeds favor SSE or a queue-backed transport. The pragmatic default is still HTTP, because it is cacheable, observable, and firewall-friendly — alternatives earn their place when their specific strengths dominate the extra operational complexity.


- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
