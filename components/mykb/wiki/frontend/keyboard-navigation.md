---
type: "concept"
title: "Keyboard Navigation"
description: "Tab order, focusability, and full keyboard operability"
tags: [accessibility", "keyboard", "focus", "a11y", "wcag"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/Accessibility/Keyboard-navigable_JavaScript_widgets", "https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html"]
---

# Keyboard Navigation

## Summary
Keyboard navigation means every function works without a pointer: users tab between focusable elements, activate with Enter or Space, and operate custom widgets with arrow keys. The browser exposes tab order, and developers control it with tabindex, roving tabindex, and skip links. Keyboard operability is a WCAG 2.2 Level A requirement.

## Details
- Tab order: the DOM order of focusable elements determines Tab sequence; tabindex="0" adds elements, tabindex="-1" allows scripted focus.
- Positive tabindex: values above 0 create manual ordering that usually fights the DOM and should be avoided.
- Roving tabindex: composite widgets keep one tab stop and move it with arrow keys, the pattern for menus and tablists.
- Visible focus: a clear :focus-visible indicator is required for AA conformance and essential for orientation.
- Skip links: a "skip to content" link lets keyboard users bypass repeated navigation landmarks.
- Traps: modals must trap focus and restore it on close; focus should never wander into hidden content.

## Related
- [[wiki/frontend/focus-management|Focus Management]] — programmatic focus control
- [[wiki/frontend/aria|ARIA]] — widget semantics that pair with arrow-key patterns
- [[wiki/frontend/wcag|WCAG]] — the keyboard-operable criteria
- [[wiki/frontend/semantic-html|Semantic HTML]] — native elements are keyboard-ready
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — verifying keyboard flows
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — the wider discipline
