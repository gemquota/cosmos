---
type: "concept"
title: "Dropdowns in Practice"
description: "Select menus and comboboxes: native selects, custom menus, search, and keyboard behavior"
tags: ["dropdowns", "select", "combobox", "ux", "accessibility"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/ARIA/apg/patterns/combobox/", "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select"]
---
# Dropdowns in Practice

## Summary
Dropdowns present a choice from a set. Native `<select>` is accessible and mobile-friendly; custom comboboxes add search, grouping, and multi-select but must re-implement keyboard and ARIA behavior. Prefer native until the requirements justify custom.

## Details
- **Native select** — free accessibility, mobile pickers, and form integration; limited styling and no search.
- **Combobox pattern** — ARIA combobox/listbox roles, typing to filter, Arrow keys to move, Enter to select, Esc to close.
- **Keyboard** — focus stays on the trigger; the listbox manages its own key handling; announce selections.
- **Search and multi-select** — filtering and tags add complexity; empty states and "no results" handling matter.
- **Worked example** — the mykb filter bar uses a native select for simple filters and a searchable combobox for tag selection.
- **Relevance** — RSIS3's form generators should default to native selects and reach for comboboxes deliberately.

## Related
- [[wiki/web-platforms/pointer-events-css|pointer-events CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/z-index-management|Z-Index Management]] — adjacent concept in this wiki
- [[wiki/web-platforms/stacking-contexts|Stacking Contexts]] — adjacent concept in this wiki
- [[wiki/web-platforms/touch-action-css|touch-action CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
