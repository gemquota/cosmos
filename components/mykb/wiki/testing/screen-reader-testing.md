---
type: "concept"
title: "Screen Reader Testing"
description: "Testing with VoiceOver, NVDA, and other assistive technology"
tags: ["screen-reader", "accessibility", "testing", "assistive-technology"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://webaim.org/techniques/screenreader/", "https://www.w3.org/WAI/standards-guidelines/at/"]
---

# Screen Reader Testing

## Summary
Screen reader testing validates that assistive technology users can navigate and operate the product: announcing content, reading forms, and interacting with dynamic regions. It is the highest-fidelity accessibility check available.

## Details
- Screen readers: NVDA on Windows, VoiceOver on macOS and iOS, TalkBack on Android, and JAWS.
- Verify labels are announced, heading structure reads sensibly, and live regions update.
- Test dialog focus management, alt text, and form error announcements.
- Script the same user journeys as automated tests, but operate by keyboard and screen reader.
- Use accessibility trees and roles to reason about announcements.
- Run real screen readers locally or in device farms; keep a structured checklist.
- Pair with automated axe checks for coverage and screen reader tests for behavior.

## Related
- [[wiki/testing/accessibility-testing|Accessibility Testing]] — the umbrella discipline
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — ARIA and semantics behind announcements
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — screen readers on mobile OSes
- [[wiki/testing/ui-testing|UI Testing]] — keyboard and focus verification
- [[wiki/testing/manual-testing|Manual Testing]] — human execution of screen reader passes
- [[wiki/testing/compatibility-testing|Compatibility Testing]] — screen reader and browser matrices
