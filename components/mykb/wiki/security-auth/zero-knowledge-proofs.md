---
type: "concept"
title: "Zero-Knowledge Proofs"
description: "Cryptographic protocols proving a statement is true without revealing the underlying secret"
tags: ["zkp", "cryptography", "privacy", "proofs"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Zero-knowledge_proof"]
---

# Zero-Knowledge Proofs

## Summary

A zero-knowledge proof (ZKP) lets a prover convince a verifier that a statement is true without disclosing anything beyond the statement's truth — for example, proving age is over 18 without revealing the birthdate. The concept was introduced by Goldwasser, Micali, and Rackoff (1985). ZKP matters because it decouples verification from data exposure: systems can assert credentials, memberships, or computations while keeping the underlying data private. For RSIS3, ZKP techniques are the deep end of privacy-by-design: proving properties of knowledge without leaking the knowledge itself.

## Details

- Properties: completeness (honest prover always convinces), soundness (cheating prover cannot), and zero-knowledge (verifier learns nothing else).
- Families: interactive proofs need a challenge-response exchange; non-interactive (NIZK) forms use a shared reference string or Fiat-Shamir transform — the basis of zk-SNARKs and zk-STARKs.
- Use cases: anonymous credentials (age, membership, licenses), verifiable computation, private payments, and selective disclosure of identity attributes.
- Trade-offs: proof generation cost, trusted setup (some SNARKs), and verification complexity make ZKP expensive where a signed certificate would do.
- Relationship to identity: ZKP-based credentials can complement digital certificates and attribute-based access control by proving attributes without a central verifier seeing raw values.
- For mykb, the pragmatic first use is selective disclosure: proving an identity attribute to a policy without copying the full profile.

## Related

- [[wiki/security-auth/privacy-by-design|Privacy by Design]] — ZKP is a privacy-by-design technique
- [[wiki/security-auth/digital-certificates|Digital Certificates]] — signed attestations ZKP can improve upon
- [[wiki/security-auth/attribute-based-access-control|Attribute-Based Access Control]] — attribute proof without attribute release
- [[wiki/security/zero-trust|Zero Trust Architecture]] — verification without blanket trust
- [[wiki/identity/identity-providers|Identity Providers]] — issuers of verifiable attributes
- [[wiki/memory/provenance|Provenance]] — recording how claims were verified
- [[wiki/identity/jwks|JWKS]] — verification key material in proof systems
- [[wiki/identity/client-certificates|Client Certificates]] — possession-based proof of identity
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — identity claims that can be proven privately
