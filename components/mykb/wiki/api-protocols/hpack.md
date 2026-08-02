---
type: "concept"
title: "HPACK"
description: "HTTP/2 header compression"
tags: ["hpack", "http2", "compression", "headers", "protocols"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc7541", "https://httpwg.org/specs/rfc7541.html"]
---

# HPACK

## Summary
HPACK (RFC 7541) is the header compression scheme of HTTP/2: it encodes header names and values as integers into a dynamic table shared between endpoints, using Huffman coding for long values. Since HTTP/1.1 headers repeat on every request, HPACK turns per-request overhead from hundreds of bytes into a few.

## Details
- Mechanism: headers are indexed — static table entries (common fields like :method: GET) cost one integer; dynamic table entries (fields seen recently) cost one integer too.
- Dynamic table: both endpoints maintain a sliding window of recently sent headers; new fields are added with an insertion size control (SETTINGS_HEADER_TABLE_SIZE).
- Huffman coding: optional per-string Huffman encoding shrinks long values (cookies, user agents) further.
- Integer representation: variable-length integers with a continuation-bit scheme, keeping the common cases tiny.
- Security: HPACK tables are per-connection, so compression does not create cross-request CRIME-style oracles the way compression over many requests can — but header values still must not leak secrets into logs.
- QCRAM (RFC 9204) adapts HPACK ideas to QUIC's out-of-order delivery for HTTP/3, replacing the ordering assumptions of HPACK.
- Implementation notes: table size limits, eviction rules, and encoder/decoder state must match exactly or connections break.

## Related
- [[wiki/api-protocols/http2|HTTP/2]] — HPACK is HTTP/2's compression layer
- [[wiki/api-protocols/http3|HTTP/3]] — QCRAM replaces HPACK over QUIC
- [[wiki/api-protocols/http-compression|HTTP Compression]] — body compression vs header compression
- [[wiki/api-protocols/http-headers|HTTP Headers]] — the fields HPACK encodes
- [[wiki/api-protocols/grpc|gRPC]] — gRPC rides HTTP/2 headers
