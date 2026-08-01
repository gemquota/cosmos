---
type: "concept"
title: "Deserialization Attacks"
description: "Exploiting unsafe deserialization of untrusted data to execute code or corrupt state"
tags: ["deserialization", "attacks", "rce", "parsers"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data"]
---

# Deserialization Attacks

- Deserialization attacks feed crafted payloads to deserializers that reconstruct objects, leading to code execution, denial of service, or state corruption.
- Risky formats: Java serialization, Python pickle, PHP unserialize, and Ruby Marshal; safe alternatives are JSON/Protobuf with schema validation.
- Prevention: never deserialize untrusted data, use allowlisted classes, integrity checks (signatures), and strict schemas.
- For mykb: agent message passing should prefer schematized formats and reject dynamic deserialization of external payloads.

## Related

- [[wiki/security-auth/command-injection|Command Injection]] — code execution outcome
- [[wiki/api-services/fuzzing|Fuzzing]] — finding parser failures
- [[wiki/api-protocols/json-schema|JSON Schema]] — validated structured exchange
- [[wiki/api-protocols/protobuf|Protocol Buffers]] — schema-first serialization
- [[wiki/security-auth/least-privilege|Least Privilege]] — containing a deserialization exploit
