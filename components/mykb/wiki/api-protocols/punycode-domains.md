---
type: "concept"
title: "Punycode Domains"
description: "Internationalized domain names encoded as ASCII for DNS"
tags: ["dns", "url", "i18n", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Punycode Domains

## Summary
Punycode (RFC 3492) encodes internationalized domain names (IDNs) into the ASCII form DNS requires — xn-- prefix. It is how non-ASCII domains work, and it is also the substrate for homograph phishing, where lookalike characters in different scripts impersonate trusted domains.

## Details
DNS labels are ASCII by convention, so internationalized domains are converted: the U-label (e.g., 例え.jp) becomes the A-label (xn--r8jz45g.jp). Browsers convert between them for display and lookup. The conversion is specified by IDNA (RFC 5890), which also defines validation — but the display of the U-label is where the security surface lives.

The mechanism: homograph attacks exploit characters that look identical across scripts — Cyrillic а (U+0430) vs Latin a (U+0061), Greek ο vs Latin o. A domain like paypaI.com using the Cyrillic I is registered by an attacker and displays nearly identically. Browsers mitigate with mixed-script detection (confusables detection, showing punycode instead of the pretty form for suspicious labels), but the mitigations have gaps and the attacks persist, especially in email and QR codes.

Concrete example: an attacker registers xn--80ak6aa92e.com, which displays as аррle.com using Cyrillic characters. A phishing email links there; the user sees apple.com in the status bar or rendered text and enters credentials. The defense is user-side (browser punycode display for mixed scripts) and org-side (training, email gateway lookalike detection, and DMARC/DKIM so the spoof can't come from the real domain).

Failure modes: full-width or confusable Unicode in other contexts (usernames, subdomains, email local parts) bypassing exact-string allowlists; zero-width characters and other invisible codepoints making domains render oddly; and normalization gaps where NFC/NFKC forms of the same label differ across systems, breaking equality checks in allowlists.

Operational tradeoffs: the safe baseline is treating any non-ASCII domain as untrusted until verified: allowlist exact A-labels in security-sensitive code, avoid string comparison on U-labels without normalization, and rely on browser IDN display rules rather than your own. For email, strict DMARC and sender allowlists blunt the spoofing vector. When internationalized domains are a product requirement, test the confusable set for your most-phished domains.

RSIS3/mykb relevance: the wiki's link-checker should normalize and flag homograph-like domains; documenting the A-label/U-label rule gives RSIS3's URL vetting a concrete test.

## Related
- [[wiki/api-protocols/http-fundamentals|HTTP Fundamentals]]
- [[wiki/api-protocols/url-structure|URL Structure]]
- [[wiki/api-protocols/uri-vs-url|URI vs URL]]
- [[wiki/api-protocols/percent-encoding|Percent-Encoding]]
- [[wiki/api-protocols/http-methods|HTTP Methods]]
- [[wiki/api-protocols/http-headers|HTTP Headers]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
