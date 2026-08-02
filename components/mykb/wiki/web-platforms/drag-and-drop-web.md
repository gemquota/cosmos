---
type: "concept"
title: "Drag and Drop on the Web"
description: "HTML5 drag and drop, pointer-event alternatives, and accessible reordering"
tags: ["drag-drop", "dnd", "web", "api", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API", "https://html.spec.whatwg.org/multipage/dnd.html"]
---
# Drag and Drop on the Web

## Summary
HTML drag and drop moves elements between sources and targets using dragstart/dragover/drop events and a dataTransfer payload. It is powerful but finicky: touch support is absent, and keyboard access requires explicit handling. Pointer-event-based implementations cover touch and stylus.

## Details
- **Events** — dragstart sets data and effects; dragover must preventDefault to allow drop; drop reads data and mutates the model.
- **dataTransfer** — carries types and data; setData/getData scope formats; files arrive via dataTransfer.files.
- **Touch gap** — mobile browsers ignore HTML5 DnD; pointer-event or library-based (dnd-kit) solutions unify input.
- **Accessibility** — provide keyboard reordering (move up/down buttons) and ARIA roles for drag handles.
- **Worked example** — the mykb dashboard's column editor reorders cards with pointer-based DnD plus keyboard buttons.
- **Relevance** — agent-driven UI builders need DnD semantics that work across input types.
- **Files and dataTransfer** — dropping OS files exposes them via dataTransfer.files; dropEffect and effectAllowed negotiate move versus copy, and dragenter/dragleave must pair to avoid flicker.

## Related
- [[wiki/web-platforms/touch-action-css|touch-action CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/pointer-events-css|pointer-events CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/scroll-behavior|scroll-behavior CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/scroll-snap|Scroll Snap]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
