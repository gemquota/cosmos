---
type: "entity"
title: "Captcha Detected"
description: "APT (Advanced Package Tool)"
tags: ["entity", "ajax", "api", "ast", "auth", "azure"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
status: "growing"
---

## Captcha Detected

A captcha is a challenge-response test used to tell humans and automated clients apart. When a web client sees a captcha challenge, the flow must pause and hand control back to a human or solver before continuing.

**Related topics:** ajax, api, auth, azure

**Domain:** Web Platforms › [[wiki/web-platforms/index|Frontend]] › [[wiki/web-platforms/index|Frontend Frameworks]] › Captcha Detected

## Overview

"Captcha detected" is the signal an automated web client receives when a site decides the request looks non-human: a login form, a search page, or an API gateway inserts a challenge between the client and the resource. For SPA and AJAX applications, the detection typically arrives as an HTTP response that is not the expected JSON — a challenge page, a 403 with a marker, or a script that renders a widget. The client must recognize this response type early, because treating the challenge body as normal data corrupts the application state and confuses downstream code.

## Detection Signals

Implementations detect captchas by inspecting response headers, status codes, page markers, or widget scripts. A common heuristic is a non-JSON content type where JSON was expected, or the presence of known challenge domains and script names. Rate-limited or repeated failures often precede the challenge, so the client should correlate request frequency with challenge responses. When a challenge is detected, the correct behavior is to stop retrying automatically — a retry loop without human input simply burns requests and can worsen the site's suspicion.

## Handling Strategies

After detection, the flow branches: surface a message for the user, defer to a solving service, or back off until the challenge expires. [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/captcha-blocked|Captcha Blocked]] and [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/captcha-fallback|Captcha Fallback]] record the adjacent states in this session cluster, and [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aliyuncaptcha|AliyunCaptcha]] names one concrete challenge provider. Because the challenge is coupled to authentication, the auth tag on this page points at the identity flow that triggered it; [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ajax|AJAX]] describes the request pattern that carries these interactions.

## Session Context

The session placed captcha detection in the frontend-frameworks branch alongside other SPA entities, and the azure tag suggests the workload ran against Azure-hosted services. Keeping detection logic isolated — a single interceptor that classifies responses — makes the rest of the client robust to whatever challenge style the site deploys.

## Related Entities

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ace-10|Ace 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrains-10|Jetbrains 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/csv-10|Csv 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
