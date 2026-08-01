---
type: "concept"
title: "Mobile Security Hardening"
description: "Defense-in-depth for mobile apps guided by OWASP MASVS: storage, transport, code, and runtime"
tags: ["mobile", "security", "hardening", "masvs", "tamper"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://mas.owasp.org/MASVS/"]
---

# Mobile Security Hardening

## Summary

Mobile security hardening applies defense-in-depth across storage, transport, code, and runtime, guided by OWASP MASVS verification levels. Key areas are secure local storage, TLS everywhere, code obfuscation, root and jailbreak detection, and dependency hygiene. MASVS gives teams a graded checklist instead of vibes.

## Details

- Secure storage: Android Keystore and EncryptedSharedPreferences, iOS Keychain; never plaintext keys or tokens.
- Transport: TLS with certificate pinning for sensitive APIs, rejecting cleartext traffic by default.
- Code protection: R8/ProGuard shrinking and obfuscation, tamper detection, and release-only build hygiene.
- Runtime environment: detect rooted or jailbroken devices and respond proportionately to risk.
- Supply chain: scan dependencies, produce SBOMs, and sign artifacts from CI.
- MASVS L1 (standard) through L3 (advanced) let you pick verification depth by data sensitivity; threat-model first.
- RSIS3 relevance: a companion app holding API keys should target at least MASVS L1 plus secure storage.

## Related

- [[wiki/mobile-platform/jailbreak-detection|Jailbreak Detection]] — iOS runtime-risk detection
- [[wiki/mobile-platform/rooted-device-detection|Rooted Device Detection]] — Android runtime-risk detection
- [[wiki/android-core/r8-obfuscation|R8 Obfuscation]] — default Android code protection pipeline
- [[wiki/android-core/proguard-rules|Proguard Rules]] — rule files that keep obfuscation safe
- [[wiki/security/tls|TLS]] — transport security baseline
- [[wiki/security/secrets-management|Secrets Management]] — vault-grade handling of mobile secrets
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — dependency and build integrity
