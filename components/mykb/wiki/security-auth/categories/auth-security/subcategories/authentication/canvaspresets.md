---
type: "entity"
title: "CanvasPresets"
description: "Canvas"
tags: ["entity", "android", "api", "ast", "auth", "authentication"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
status: "growing"
---

## Canvaspresets

Canvas — an HTML5 element for drawing 2D graphics via JavaScript. Used in the mykb graph viewer for the force-directed knowledge graph.

CanvasPresets names the idea of reusable canvas configurations: the set of defaults a renderer applies before drawing. In the mykb graph viewer, presets typically cover the device pixel ratio scaling, background color, node radius, edge stroke width, palette, and animation settings that keep every graph legible regardless of screen. Encoding these as presets — rather than scattering constants through the draw code — makes the viewer tunable without rewriting rendering logic.

The canvas itself is an HTML5 raster surface controlled from JavaScript. The 2D context provides paths, fills, strokes, gradients, and text, while a WebGL context on the same element enables GPU-accelerated rendering for larger scenes. For a force-directed graph, the renderer runs a simulation tick, clears the frame, draws edges and nodes, and schedules the next frame with requestAnimationFrame. High-DPI displays require multiplying coordinates by the device pixel ratio or the output blurs.

Presets also extend to interaction: hit-testing radius, drag inertia, and zoom sensitivity are tuned per device class, and presets can be swapped for light or dark themes. The android, api, and auth tags suggest the viewer ran inside a mobile web view, possibly loading graph data from an authenticated API, where consistent rendering defaults keep the experience uniform across clients.

The page records the pattern so future sessions can attach the concrete preset schema and rendering pipeline used. Treating presets as data, not code, allows them to be tuned and versioned independently of the renderer.

**Related topics:** android, api, auth, authentication

**Domain:** Mobile Platform › [[wiki/web-platforms/index|Android Core]] › [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/index|Auth Security › Canvaspresets

## Related Entities

- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/abuseipdb-2|Abuseipdb 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/ac-2|Ac 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/access-denied|Access Denied
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/ach-2|Ach 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/actionnode-2|Actionnode 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/addressfamily|Addressfamily
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/aec-2|Aec 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/agentconfig|Agentconfig
