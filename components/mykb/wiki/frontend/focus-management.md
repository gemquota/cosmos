---
type: "concept"
title: "Focus Management"
description: "Focus states, traps, and restoration in dynamic UIs"
tags: [accessibility", "focus", "a11y", "keyboard", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus", "https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex"]
---

# Focus Management

## Summary
Focus management controls where keyboard and assistive-tech focus goes as the UI changes. Opening a dialog moves focus into it; closing restores it to the trigger; route changes move focus to the new heading. Done well, dynamic apps feel continuous; done poorly, users lose their place entirely.

## Details
- Programmatic focus: element.focus() with options such as preventScroll; document.activeElement reveals current focus.
- Modals: trap focus inside the dialog (keyboard listeners or the inert attribute on background content) and return it on close.
- Route changes: SPA navigations should focus the main heading or a sentinel so screen readers announce the new page.
- Reveal on action: focus moves where the user's next action is — after an error, to the failing field; after save, to the confirmation.
- :focus-visible: style focus only for keyboard input, avoiding permanent outlines on mouse users while keeping them for keys.
- Testing: walk every flow with Tab and Shift+Tab; check no focus lands on hidden or inert content.

## Related
- [[wiki/frontend/keyboard-navigation|Keyboard Navigation]] — the tab-order foundation
- [[wiki/frontend/aria|ARIA]] — announcing focus-driven UI changes
- [[wiki/frontend/client-side-routing|Client-Side Routing]] — focus moves on navigation
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — auditing focus behavior
- [[wiki/frontend/wcag|WCAG]] — focus-visible and focus-order criteria
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — the discipline this belongs to
