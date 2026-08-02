---
type: "concept"
title: "Fuzz Testing"
description: "Feeding malformed and random inputs to expose crashes and robustness bugs"
tags: ["fuzzing", "testing", "security", "robustness"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://llvm.org/docs/LibFuzzer.html", "https://aflplus.plus/"]
---

# Fuzz Testing

## Summary
Fuzzing feeds programs large volumes of malformed, random, or mutated inputs to expose crashes, hangs, memory errors, and robustness bugs. It complements tests because it explores input spaces no one thought to write by hand.

## Details
- Engines: libFuzzer and AFL++ for native code; OSS-Fuzz runs continuous fuzzing at scale.
- Coverage-guided fuzzing mutates inputs that reach new code paths, making exploration efficient.
- Targets: parsers, decoders, network stacks, compilers, and anything processing untrusted input.
- Fuzzing has found thousands of real CVEs in image parsers, TLS stacks, and browsers.
- Integrate as a CI job with a seed corpus and crash triage; each crash becomes a regression test.
- Managed languages fuzz at FFI boundaries and interpreters, for example Jazzer for Java.
- Use sanitizers, ASan and UBSan, to turn silent corruption into reported failures.

## Related
- [[wiki/testing/security-testing|Security Testing]] — fuzzing is a core security technique
- [[wiki/testing/negative-testing|Negative Testing]] — malformed input handling
- [[wiki/testing/property-based-testing|Property-Based Testing]] — generated inputs with invariants
- [[wiki/testing/grammar-based-testing|Grammar-Based Testing]] — structure-aware input generation
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — where fuzzing findings surface
- [[wiki/testing/regression-testing|Regression Testing]] — crash repros become regression tests
