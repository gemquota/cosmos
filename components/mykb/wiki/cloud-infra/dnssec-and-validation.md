---
type: "concept"
title: "DNSSEC & Validation"
description: "Authenticating DNS answers with signed zone records and chain-of-trust validation"
tags: ["dns", "dnssec", "security", "validation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# DNSSEC & Validation

## Summary

DNSSEC cryptographically signs DNS records so resolvers can verify answers came from the authoritative source — defeating spoofing, cache poisoning, and some hijacking. Validation is the resolver-side check; deployment is the signing and key management on the authoritative side.

## Details
- Mechanism: the zone owner signs records with a zone-signing key (ZSK), signs the ZSK with a key-signing key (KSK), and publishes DS records at the parent for a chain of trust; validating resolvers walk the chain to the root. Algorithms (RSASHA256, ECDSA P-256, Ed25519) and key rollovers must be planned; signatures expire, so re-signing must happen before validity lapses.
- Concrete example: an attacker forges a DNS answer for example.com; a validating resolver detects the bad signature and returns SERVFAIL, so the client never reaches the fake site. A broken key rollover (DS mismatch) takes the whole domain down for validators — the classic DNSSEC outage — so staging and monitoring rollovers is mandatory.
- Failure modes: expired signatures after a signing pipeline stops (silent SERVFAILs for validators); KSK rollover errors causing denial-of-service on the domain; unsigned delegation gaps (a child zone without DS breaks validation for it); and resolvers not validating at all, making DNSSEC invisible to the user.
- Operational tradeoffs: DNSSEC defends the resolution path but adds operational complexity (key management, rollover runbooks, signing latency); the root and TLDs are signed, so validation is deployable today. Combine with DoH/DoT (which protects the last mile) for end-to-end answer integrity.
- RSIS3/mykb relevance: the wiki's domains are signed with automated key rollover; this note records the DS publication and rollover procedure the loop's DNS automation follows.
- Rollover rehearsal: practice KSK rollover in a staging domain before the real one; the first rollover should not happen during a production emergency.
- Validation monitoring: track the percentage of validating resolvers for your zones; the metric tells you how much of the internet actually verifies your signatures.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
