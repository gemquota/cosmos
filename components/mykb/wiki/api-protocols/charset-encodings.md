---
type: "concept"
title: "Charset Encodings"
description: "Character encodings such as UTF-8, UTF-16, and Latin-1 used in text payloads"
tags: ["encoding", "http", "i18n", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Charset Encodings

## Summary
Character-set encodings map bytes to characters, and mismatches between what a client sends and a server decodes corrupt data or open injection holes. UTF-8 is the safe default; everything else needs explicit declaration.

## Details
Every text payload has an encoding: UTF-8, UTF-16, ISO-8859-1, Windows-1252, Shift_JIS, and so on. HTTP carries this in Content-Type (text/html; charset=utf-8) and in the BOM or XML declaration for files; JSON is defined as UTF-8 per RFC 8259; HTML and XML have their own meta-declaration mechanisms. When sender and receiver disagree, bytes get misinterpreted — mojibake at best, injection or bypass at worst.

The mechanism: decoders interpret byte sequences according to the declared or assumed charset. Ambiguity is the danger: some encodings are multi-byte with overlapping byte values, and sequences that are invalid in one charset can be valid in another. Attackers exploit this with mixed-encoding payloads to smuggle characters past filters that normalized in one encoding while the parser later decodes in another — the classic encoding bypass in WAFs.

Concrete example: an API accepts user comments, sanitizes for the string "<script>" in UTF-8, and stores UTF-8 — fine. But if a proxy or database column is latin-1 and the client sends UTF-8 bytes, the stored text round-trips as mojibake and a cleverly encoded payload can survive a filter that only knows one encoding. JSON responses that omit charset on a server defaulting to something non-UTF-8 corrupt every non-ASCII character.

Failure modes: missing charset declarations let receivers guess, and guesses differ (Windows-1252 versus ISO-8859-1 for the 0x80-0x9F range); UTF-7 tricks (decoded by old browsers) and UTF-16 BOM injection bypass naive filters; and mixed encodings in the same pipeline — form to middleware to database to template — corrupt or inject at the last hop. Half-width and full-width homoglyph attacks are a separate but related normalization problem.

Operational tradeoffs: standardizing on UTF-8 everywhere (transport, storage, templating) eliminates most of the class; where legacy encodings are unavoidable, declare them explicitly at every boundary and convert at the edge, never deep in the stack. Validation should operate on decoded characters, not raw bytes, and responses should always set charset. A test suite with non-ASCII, emoji, and byte-invalid inputs catches the failures that docs won't.

RSIS3/mykb relevance: the wiki stores Markdown with frontmatter; a standing rule that all mykb files are UTF-8 and all APIs declare charset prevents silent corruption during RSIS3 consolidation writes.

## Related
- [[wiki/api-protocols/http-fundamentals|HTTP Fundamentals]]
- [[wiki/api-protocols/mime-types|MIME Types]]
- [[wiki/api-protocols/content-negotiation|Content Negotiation]]
- [[wiki/api-protocols/http-compression|HTTP Compression]]
- [[wiki/api-protocols/http-headers|HTTP Headers]]
