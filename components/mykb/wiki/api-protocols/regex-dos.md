---
type: "concept"
title: "ReDoS Attacks"
description: "Catastrophic backtracking in regular expressions that freezes a CPU"
tags: ["security", "regex", "dos", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# ReDoS Attacks

## Summary
Regular expression denial of service (ReDoS) exploits catastrophic backtracking: a pattern like (a+)+ applied to a carefully crafted input like aaaaa...! takes exponential time, freezing the CPU. One request can pin a core for minutes.

## Details
Most regex engines backtrack to find matches. Patterns with nested quantifiers — (a+)+, (a|a)*, (.*)* — create exponentially many ways to fail: when the input nearly matches but fails at the end, the engine tries every split of the string among the quantifiers. The classic example: (a+)+$ against a^n b (or a^n !) explores 2^n paths. Inputs of a few dozen characters are enough to stall a process.

The mechanism: the attacker sends a long, near-matching input to any endpoint whose validation regex is vulnerable — email, username, id, log-line parsing. The engine burns CPU; with concurrent requests, all cores saturate and the service stalls. The vulnerable regex is usually written innocently for validation and never load-tested with adversarial input. Linear-time engines (RE2, Rust regex) and atomic groups or possessive quantifiers eliminate backtracking.

Concrete example: an API validates usernames with ^([a-z]+)+$ and rejects on the first invalid character. The attacker sends a 30-character string of a's followed by '9' — no match, but the engine tries 2^30 paths before giving up. The validation endpoint becomes a CPU bomb. Switching to ^[a-z]+$ (linear) or RE2 fixes it; so does a length cap before regex evaluation.

Failure modes: every endpoint that runs a user-influenced regex against user-controlled input is a candidate — including third-party libraries that parse with regex; patterns with nested quantifiers or alternation overlap (a|aa)*; and engines without backtracking limits that can't be configured. Timeout-based mitigations (regex timeouts) help but can still leak CPU before the kill.

Operational tradeoffs: the durable fix is avoiding backtracking-prone patterns and using linear-time engines for untrusted input; where backtracking engines are required, add length caps, explicit timeouts, and load tests with pathological inputs. Reviews should flag nested quantifiers and overlapping alternations as defects. ReDoS is a correctness bug as much as a security bug: the pattern is doing exponentially more work than intended.

RSIS3/mykb relevance: the wiki's validation and parsing code should audit regexes for backtracking; documenting the linear-time rule gives RSIS3's checks a concrete pattern list to grep for.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/decompression-bombs|Decompression Bombs]]
- [[wiki/api-protocols/billion-laughs|Billion Laughs]]
- [[wiki/api-protocols/entity-expansion|Entity Expansion]]
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/api-protocols/backpressure|Backpressure]]
