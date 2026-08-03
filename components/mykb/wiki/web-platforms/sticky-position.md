---
type: "concept"
title: "position: sticky"
description: "Elements that stick within their scroll container boundaries"
tags: ["css", "layout", "scroll", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# position: sticky

## Summary

position: sticky pins an element to the viewport within its containing block after scrolling past a threshold (top/bottom/left/right), then releases when its container ends. It is the modern approach for headers, table rows, and section labels — with container constraints.

## Details
- Mechanism: sticky is relative-like until the element crosses the declared offset inside its scroll container; then it behaves fixed until the containing block's edge. The containing block is the nearest scrolling ancestor's content box — the sticky element cannot escape its parent's bounds, which both enables "stick within section" and causes "doesn't stick" bugs.
- Concrete example: a table header row sticks via position: sticky; top: 0 inside a scrollable table; a section label sticks while its section scrolls, then yields to the next section. Sticky inside a flex/grid item works only if the item's own box is taller and the container has room to scroll.
- Failure modes: sticky not working when an ancestor has overflow: hidden/auto creating a different scroll container; the parent being exactly the element's height (nothing to stick within); using sticky in a container with no scroll (the page itself must scroll); and sticky + transform ancestors, which change the containing block and break offsets.
- Operational tradeoffs: sticky is cheaper and more semantic than JS scroll listeners; the main cost is the mental model of containing blocks. Test with nested scroll containers (app shells, modals) and remember iOS Safari's historical quirks around sticky in overflow containers.
- RSIS3/mykb relevance: the wiki browser uses sticky column headers in its note table; this note documents the container requirements checked when the loop adds new scroll regions.
- App-shell caveat: sticky inside an app shell with its own scroll container sticks to that container, not the window; verify the scroll parent matches the design intent before building on it.

## Related
- [[wiki/web-platforms/virtual-scrolling|Virtual Scrolling]]
- [[wiki/web-platforms/scroll-behavior|scroll-behavior CSS]]
- [[wiki/web-platforms/scroll-snap|Scroll Snap]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
