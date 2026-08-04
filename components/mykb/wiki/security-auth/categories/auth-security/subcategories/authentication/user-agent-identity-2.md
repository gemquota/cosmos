---
type: "concept"
title: "User Agent Identity"
resource: ""
---
description: "How clients identify themselves through user-agent strings and device signals"
tags: ["android", "api", "ast", "auth", "authentication", "entity", "user-agent", "identity"]
timestamp: "2026-07-19T22:41:43Z"

# User Agent Identity

## Summary
User agent identity is how a client describes itself to a server: the user-agent header, device hints, and related signals such as language and platform. It matters because servers use these signals for rendering, analytics, and abuse detection. The signals are self-reported, so they must be treated as untrusted and validated, never as proof of identity.

## Details
- **Definition** — the user-agent string identifies the browser, engine, OS, and version of the requesting client.
- **Parsing** — user-agent strings are notoriously varied; robust parsing uses suffix and pattern rules rather than exact matches.
- **Self-reported** — clients can lie, so security decisions must never rest on user-agent values alone.
- **Feature detection** — modern practice prefers testing capabilities directly instead of inferring them from the user-agent string.
- **Analytics** — platform and version signals feed dashboards and compatibility decisions when collected with consent.
- **Bot detection** — user agents help flag automation, but sophisticated bots forge headers, so other signals are needed.
- **Common failure modes** — brittle string matching, blocking real users based on stale agent lists, and trusting agent data for security.
- **Worked example** — a site serves different markup for mobile and desktop based on the user agent, while authorization relies on session tokens, never the header.
- **Practical relevance** — treating user agent identity as advisory keeps experiences compatible without compromising security.

- **Client hints** — structured hints supplement the user-agent string with device and viewport data when the client opts in.
- **Reduction** — browsers are freezing or reducing user-agent detail, pushing sites toward feature detection.
- **Logging** — storing user-agent data responsibly matters for privacy, so minimize what is retained.
## Related
- [[wiki/web-platforms/browser-engines|Browser Engines]] — what agents describe
- [[wiki/security/zero-trust|Zero Trust]] — never trust headers
- [[wiki/testing/security-testing|Security Testing]] — spoofed headers
- [[wiki/identity/session-management|Session Management]] — real identity source
- [[wiki/testing/penetration-testing|Penetration Testing]] — header forgery
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring on the Web]] — client telemetry
