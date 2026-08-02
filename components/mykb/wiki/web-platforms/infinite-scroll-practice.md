---
type: "concept"
title: "Infinite Scroll in Practice"
description: "Loading more content as the user approaches the bottom, with pagination and stability caveats"
tags: ["infinite-scroll", "pagination", "performance", "ux", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API", "https://developer.mozilla.org/en-US/docs/Web/API/fetch"]
---
# Infinite Scroll in Practice

## Summary
Infinite scroll appends content as the user nears the end, triggered by IntersectionObserver sentinels. It feels seamless but hides navigation state: no deep links, hard to know position, and layout-shift risk. The pattern pairs with cursor pagination and needs explicit loading/error/empty states.

## Details
- **Trigger** — a sentinel element observed with IntersectionObserver fires a fetch when visible; rootMargin preloads ahead.
- **Pagination** — cursor-based page tokens avoid offset drift as new items arrive; dedupe on merge.
- **Stability** — reserve space for appended items (no CLS), keep scroll position on navigation, and avoid appending above the viewport.
- **Fallbacks** — provide "load more" buttons and pagination links for accessibility and shareability.
- **Worked example** — the mykb search results page appends cursor-paginated cards with a sentinel and a fallback button.
- **Relevance** — RSIS3's long result sets (logs, search) benefit from the same stable-append pattern.

## Related
- [[wiki/api-protocols/api-pagination|API Pagination]] — adjacent concept in this wiki
- [[wiki/api-protocols/api-filtering|API Filtering]] — adjacent concept in this wiki
- [[wiki/api-protocols/api-sorting|API Sorting]] — adjacent concept in this wiki
- [[wiki/api-protocols/sparse-fieldsets|Sparse Fieldsets]] — adjacent concept in this wiki
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — existing coverage
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
