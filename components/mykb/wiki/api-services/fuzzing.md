---
type: "concept"
title: "Fuzzing"
description: "Automated testing that feeds malformed inputs to find crashes and vulnerabilities"
tags: ["fuzzing", "testing", "security", "automation"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Fuzzing"]
---

# Fuzzing

- Fuzzing drives software with generated, mutated, or malformed inputs to expose crashes, assertion failures, and memory errors.
- Coverage-guided fuzzers (libFuzzer, AFL++, OSS-Fuzz) find real parser and protocol bugs that manual review misses.
- Effective targets: parsers, deserializers, network handlers, and API request validation.
- For mykb: fuzzing API input validation and any binary parsing in the toolchain is cheap, high-yield assurance.

## Related

- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — fuzzing finds parser flaws
- [[wiki/api-services/dast|Dynamic Application Security Testing]] — runtime testing sibling
- [[wiki/api-protocols/json-schema|JSON Schema]] — schema validation as a fuzz oracle
- [[wiki/api-protocols/rest-apis|REST APIs]] — the interfaces under test
- [[wiki/security-auth/token-authentication|Token Authentication]] — fuzzing token parsers and validators
