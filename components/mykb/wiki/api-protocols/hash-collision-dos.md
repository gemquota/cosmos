---
type: "concept"
title: "Hash Collision DoS"
description: "Crafting inputs whose hashes collide to degrade hash tables to O(n)"
tags: ["security", "dos", "algorithms", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Hash Collision DoS

## Summary
Hash collision denial of service crafts many inputs that hash to the same bucket in a hash table, degrading expected O(1) lookups to O(n) per operation. The classic target is a web framework's form-parameter map, where one HTTP request becomes a CPU bomb.

## Details
Hash tables are fast on average because keys spread across buckets. If an attacker can predict the hash function and submit many keys that collide, every insert and lookup degenerates into a linked-list scan: a request with a few thousand colliding parameter names costs quadratic time. The 2011-2012 wave of web-framework vulnerabilities (Ruby on Rails, PHP, Java) was exactly this: crafted POST parameter names triggered massive CPU use per request.

The mechanism: older frameworks used predictable hash functions (often with a constant seed, or none at all) so an attacker could compute colliding strings offline. The fixes are randomized hash seeds per process (attacker can't predict the seed), cryptographic or SipHash-based string hashing, and hard caps on parameter counts and sizes. Modern runtimes do all three, but the attack still applies to custom hash-based data structures, caches, and any code that hashes attacker-controlled keys.

Concrete example: a JSON API parses user-supplied objects into language dictionaries. If the runtime uses a fixed-seed hash, an attacker sends {"aaa":1, "bbb":1, ...} with thousands of colliding keys; each insert scans a growing chain, and a single request pins a core. With a per-process random seed or SipHash, the collision set computed offline no longer collides, and with a parameter cap the request is rejected outright.

Failure modes: seeds that are fixed per release or predictable from process id defeat randomization; hash functions with weak mixing (trivial multiplicative constants) can still be attacked even when seeded; and limits that count bytes but not keys allow many tiny colliding keys. Caches with attacker-controlled keys (user ids, URLs) are a quieter version of the same problem.

Operational tradeoffs: randomized seeding costs nothing at runtime and is the standard defense, at the cost of making hash order non-deterministic across processes (minor for most apps); key-count caps can break legitimate bulk endpoints, so they need documented, tunable values. Defense in depth: keep hash tables out of the hot path for attacker-controlled keys, cap request sizes, and rate-limit parsing-heavy endpoints.

RSIS3/mykb relevance: any wiki tooling that parses untrusted payloads into maps should note the runtime's hash seeding; documenting the defense lets RSIS3 check dependency and runtime configuration.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/regex-dos|ReDoS Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/decompression-bombs|Decompression Bombs]] — related coverage in the same cluster
- [[wiki/api-protocols/billion-laughs|Billion Laughs]] — related coverage in the same cluster
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/backpressure|Backpressure]] — related coverage in the same cluster
