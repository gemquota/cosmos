---
type: "concept"
title: "User-Agent Parsing"
description: "Extracting browser and device signals from the User-Agent string"
tags: ["user-agent", "device", "web", "detection"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# User-Agent Parsing

## Summary

User-agent parsing extracts browser, OS, and device from the UA string — a free-form, spoofable, ever-changing field. It is acceptable for analytics and content negotiation only when treated as unreliable and paired with better signals.

## Details
- Mechanism: the UA string is a token soup (Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 ...); parsers match regexes against known product tokens. Client Hints (Sec-CH-UA family) are the structured alternative, sent only when the server opts in, and are more stable than parsing.
- Concrete example: analytics segmenting sessions by browser family (Chrome vs Safari) via UA works for cohorts, but serving different HTML based on UA breaks when bots, spoofers, or new engines appear; layout decisions belong to feature detection and viewport, not UA.
- Failure modes: regex rot as vendors change token order or add versions; spoofed/bot UAs polluting cohorts; missing new engine versions breaking detection; and the classic wrong inference ("Safari" token in every browser, "Chrome" in Edge) that misclassifies real users.
- Operational tradeoffs: for server-side choice, prefer Client Hints with UA fallback; for client-side, use feature detection and navigator properties (userAgentData where available); keep parser datasets versioned and re-test quarterly against a fresh UA corpus.
- RSIS3/mykb relevance: the wiki analytics tags sessions from userAgentData with UA fallback, and this note records the parse corpus the loop refreshes.
- Privacy note: UA and hints are fingerprinting signals; minimize retention, especially for cross-site analytics, and consider aggregating instead of storing raw strings.
- Bot handling: detect bots separately (crawler lists, behavior) from human cohorts so analytics and rate limits do not misfire on either group.
- Structured alternative: prefer navigator.userAgentData and Client Hints where available, falling back to parsing; structured fields change less often than the UA token soup.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/device-detection|Device Detection]]
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]]
- [[wiki/web-platforms/device-detection|Device Detection]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
- [[wiki/web-platforms/web-standards|Web Standards]]
