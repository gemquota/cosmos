---
type: "entity"
title: "BigInt"
description: "Android — mobile development platform, API — service communication interface, Authentication — identity verification"
tags: ["entity", "android", "api", "ast", "auth", "bash"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
status: "growing"
---


## Bigint

BigInt appears in 1 session(s) categorized as API, Mobile, Security, Shell. Related topics: android, api, auth, bash.

**Domain:** Mobile Platform › [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] › [[wiki/web-platforms/supercategories/api-services/categories/api-rest/index|Api Clients › Bigint

## JavaScript BigInt

In JavaScript, `BigInt` is a primitive numeric type for arbitrary-precision integers. The `Number` type is a double-precision float, so integers beyond `Number.MAX_SAFE_INTEGER` (2^53 − 1) lose precision; IDs, timestamps, and hashes frequently exceed that bound. BigInt fixes this with values written as `123n` or produced by `BigInt("...")`.

Key rules:

- Mixing `BigInt` and `Number` in arithmetic throws `TypeError`; convert explicitly first.
- Division truncates toward zero, matching integer semantics.
- Comparisons and bitwise operators work across types, but bitwise operands are cast to BigInt.
- `JSON.stringify` throws on `BigInt` values — use a replacer or serialize as strings.
- Typed-array cousins `BigInt64Array` and `BigUint64Array` store 64-bit integers for binary data.

BigInt is the right tool when exact integer math matters: cryptographic hashing, token and ID generation, and financial calculations where floating-point rounding is unacceptable.

## BigInt in Databases and APIs

The same name appears in PostgreSQL, where `bigint` is an 8-byte signed integer type spanning roughly −9.2×10^18 to +9.2×10^18. APIs that exchange such values must be careful: JSON numbers cannot represent them faithfully, so serializers often emit them as strings. That is why auth and API tooling sessions frequently pair BigInt with payload-formatting concerns — a session categorized under API, Mobile, Security, and Shell could have hit any of these contexts.

## Serialization in Practice

A safe cross-system convention is to treat every large integer as a string at the wire boundary: request and response fields are documented as strings, parsers convert them with BigInt constructors, and arithmetic happens only after conversion. This keeps precision intact across languages and JSON-based APIs, and it is the pattern most SDKs adopt for fields like account IDs and nonces.

## Related Notes

- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — where BigInt executes
- [[wiki/devops-infra/postgresql|PostgreSQL]] — the `bigint` column type

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli

