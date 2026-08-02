---
type: "concept"
title: "Screen Readers"
description: "How assistive tech consumes the accessibility tree"
tags: [accessibility", "screen-readers", "a11y", "assistive-tech", "testing"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/fundamentals/accessibility-intro/", "https://developer.mozilla.org/en-US/docs/Learn/Accessibility"]
---

# Screen Readers

## Summary
Screen readers convert the accessibility tree — not the visual page — into speech and Braille output. NVDA, JAWS, VoiceOver, and TalkBack let users navigate by heading, landmark, link, or form control, skipping visual layout entirely. Their behavior is why semantics, text alternatives, and focus management matter.

## Details
- Accessibility tree: browsers derive a semantic tree from HTML and ARIA; only what is exposed there is announced.
- Navigation modes: users jump by headings, landmarks, links, buttons, and tables; linear DOM order often dictates comprehension.
- Virtual cursor: screen reader focus moves independently of visible focus, so aria-hidden and tabindex govern what is reachable.
- Testing reality: each screen reader plus browser pair behaves slightly differently, so test the combinations your users rely on.
- Common failures: unlabeled inputs, missing alt text, heading-order jumps, and dialog focus not being trapped or restored.
- Support: announcements of live regions, form validation messages, and status text shape the experience.

## Related
- [[wiki/frontend/aria|ARIA]] — semantics screen readers consume
- [[wiki/frontend/semantic-html|Semantic HTML]] — native structure announced for free
- [[wiki/frontend/wcag|WCAG]] — criteria defining screen-reader support
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — including screen readers in QA
- [[wiki/frontend/keyboard-navigation|Keyboard Navigation]] — the keyboard-first input model
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — broader assistive technology context
