---
type: "concept"
title: "MIME Types"
description: "Content-Type values that declare how a body should be interpreted"
tags: ["http", "mime", "standards", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# MIME Types

## Summary
MIME types (media types) are the Content-Type values — application/json, text/html, image/png — that tell receivers how to interpret a body. Correct declaration is a correctness and security issue: the wrong type corrupts parsing and re-enables sniffing.

## Details
A media type is type/subtype (plus optional parameters like charset): application/json, text/html; charset=utf-8, multipart/form-data; boundary=... . The registry (IANA) assigns them; experimental or vendor types use the x- and vnd. prefixes (application/vnd.api+json). The sender declares what the bytes mean; the receiver must not guess beyond the declaration.

The mechanism: on the response side, the browser and intermediaries use Content-Type for parsing, rendering, and caching decisions; a text/html response executes markup, an image/png response renders an image. On the request side, Content-Type tells the server how to parse the body — application/json vs form-encoded are different parsers. Mismatches fail in two ways: data corruption (parsing JSON as form data) and security (declaring text/plain but bytes that get sniffed as HTML).

Concrete example: an API returns application/json but with a body that is actually a JSON string containing an HTML fragment. Fine — the client renders it as data. But the same API, misconfigured to return text/html for user content, lets a browser render the fragment as live HTML — stored XSS. Conversely, a client posting JSON with Content-Type: text/plain makes the server skip JSON parsing, hitting a 400 or mis-binding parameters.

Failure modes: missing Content-Type (receivers sniff or default, both risky); charset omitted on text types (mojibake and encoding-bypass filters); claiming application/json for non-JSON bodies; and multipart boundaries that conflict with content. Also, some servers echo Content-Type from client input into responses, letting attackers choose the render mode for their payload.

Operational tradeoffs: the discipline is declare-always and declare-correctly: every response sets an explicit, accurate Content-Type with charset where applicable; every request parser validates the declared type and rejects unknown ones (415). Combine with nosniff so browsers never upgrade the declared type. The OpenAPI spec should pin response content types per operation so generated clients and gateways agree.

RSIS3/mykb relevance: the wiki's APIs should pin content types in their contracts; documenting the declaration rule keeps RSIS3's client code from guessing and the security checks from missing sniffing risk.

## Related
- [[wiki/api-protocols/http-fundamentals|HTTP Fundamentals]] — related coverage in the same cluster
- [[wiki/api-protocols/charset-encodings|Charset Encodings]] — related coverage in the same cluster
- [[wiki/api-protocols/mime-types|MIME Types]] — related coverage in the same cluster
- [[wiki/api-protocols/charset-encodings|Charset Encodings]] — related coverage in the same cluster
- [[wiki/api-protocols/content-negotiation|Content Negotiation]] — related coverage in the same cluster
- [[wiki/api-protocols/http-compression|HTTP Compression]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
