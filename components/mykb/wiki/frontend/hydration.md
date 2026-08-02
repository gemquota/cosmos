---
type: "concept"
title: "Hydration"
description: "Attaching state and event handling to server-rendered HTML"
tags: [hydration", "rendering", "react", "performance", "ssr"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://react.dev/reference/react-dom/hydrate", "https://nextjs.org/docs/app/building-your-application/rendering"]
---

# Hydration

## Summary
Hydration is the step where a client-side framework takes HTML that was rendered on the server and attaches event listeners, state, and the component tree to it. The browser does not repaint the server markup; instead the framework re-creates its in-memory model in the background and reconciles it with the existing DOM.

## Details
- Serialized state: the server embeds state (typically JSON) in the page so the client can rebuild components without refetching data.
- Double work: the component tree is rendered once on the server and again on the client, which delays interactivity after first paint.
- Interactive wait: until hydration finishes, clicks and typing can be ignored — a cost measured by Time to Interactive.
- Mismatch risks: server and client output must match; differences cause full client re-renders or DOM conflicts.
- Mitigations: streaming SSR, selective hydration, and islands architectures hydrate only interactive regions.
- Modern direction: React 19 supports partial prerendering, while frameworks like Qwik defer hydration to the moment an event fires.

## Related
- [[wiki/frontend/server-side-rendering|Server-Side Rendering]] — produces the HTML hydration attaches to
- [[wiki/frontend/client-side-rendering|Client-Side Rendering]] — the no-hydration alternative
- [[wiki/frontend/islands-architecture|Islands Architecture]] — hydrating only interactive regions
- [[wiki/frontend/virtual-dom|Virtual DOM]] — the reconciliation model hydration relies on
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — interactivity metrics affected by hydration
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — where hydration lives in the stack
