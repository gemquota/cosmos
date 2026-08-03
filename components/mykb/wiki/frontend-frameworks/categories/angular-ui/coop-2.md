---
type: "entity"
title: "COOP"
description: "Acronym referenced in session 019ed74e"
tags: ["acronym", "android", "angular", "api", "ast", "auth", "aws", "bootstrap", "entity"]
timestamp: "2026-07-19T22:41:39Z"
status: "growing"
resource: ""
---


## Coop 2

COOP appears in 3 session(s) categorized as API, Cloud, Frontend, Mobile, Security. Related topics: acronym, android, angular, api, auth, aws, bootstrap.

**Domain:** Mobile Platform › [[wiki/web-platforms/00-index|Android Core]] › [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/00-index|Angular Ui

## Overview

COOP is an acronym with a well-known web-platform expansion: Cross-Origin-Opener-Policy. COOP is an HTTP response header that lets a document opt out of sharing its browsing context group with other origins, isolating it from cross-origin windows opened via `window.open` or target links. It is part of the same security family as Cross-Origin-Embedder-Policy (COEP) and Cross-Origin-Resource-Policy (CORP), and it defends against cross-origin information leaks such as window references and certain side-channel attacks.

## Details

- Header values: `same-origin` restricts the context group to same-origin documents; `same-origin-allow-popups` permits some popups; `unsafe-none` opts out.
- Effects: with COOP set, the page gets a fresh browsing context group, so malicious cross-origin pages cannot retain a reference to the opener window.
- Pairing: COOP is often combined with COEP to enable features like `SharedArrayBuffer`, which require cross-origin isolation.
- Debugging: mismatched COOP/COEP settings show up in the console; popups that lose opener references are the visible symptom.
- Cloud and mobile: headers are configured at the edge or origin — AWS-backed stacks set them via proxies, CDNs, or server responses, and mobile webviews inherit the same browser enforcement.

In sessions covering API, frontend, and security, COOP typically appears when hardening a web app: setting the header in infrastructure, testing popup flows, and verifying isolation in the browser. The acronym can also mean Cooperative Operation or Collaboration Protocol in other contexts, but under frontend and security tags the Cross-Origin-Opener-Policy reading is the operative one.

## Related Entities

- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/aim-2|Aim 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/autonomous-iterative-mode-2|Autonomous Iterative Mode 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/avg-age-2|Avg Age 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/avg-energy-2|Avg Energy 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/batch-2|Batch 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/dna-10|Dna 10
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/harmonica-explorer-2|Harmonica Explorer 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/hidpi-2|Hidpi 2
