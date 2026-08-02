---
type: "concept"
title: "Client-Side Routing"
description: "History API and URL-driven SPA navigation"
tags: [routing", "spa", "history-api", "javascript", "navigation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/History_API", "https://reactrouter.com/en/main"]
---

# Client-Side Routing

## Summary
Client-side routing swaps page content without full reloads by updating the URL through the History API. pushState changes the address bar, replaceState updates without history entries, and popstate fires on back and forward. Routers match the URL to components, load their code, and manage scroll and focus.

## Details
- History API: pushState and replaceState update the URL without navigating; back and forward trigger popstate.
- Route matching: routers parse the pathname, extract parameters, and render the matching view; hash routing works without server support.
- Code splitting: route-based lazy loading fetches each view's chunk on navigation, keeping the initial bundle small.
- Scroll restoration: SPAs must restore scroll positions per entry and handle anchor links manually.
- Focus management: after navigation, focus should move to the new heading or a sentinel for screen-reader users.
- Server coordination: deep links need fallback rewrites (SPA fallback to index.html) so refresh and share URLs work.

## Related
- [[wiki/frontend/focus-management|Focus Management]] — focus moves on route change
- [[wiki/frontend/code-splitting|Code Splitting]] — loading route chunks on demand
- [[wiki/frontend/hydration|Hydration]] — routing within SSR apps
- [[wiki/web-platforms/web-apis|Web APIs]] — the History API platform
- [[wiki/api-protocols/api-versioning|API Versioning]] — URL design behind routes
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — URL as state
