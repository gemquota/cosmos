---
type: "entity"
title: "Ajax"
status: "growing"
---


## Ajax

Asynchronous JavaScript and XML — technique for making asynchronous HTTP requests from web pages without full page reloads. Sessions show fetch API and XMLHttpRequest patterns.

**Related technologies:** ajax, android, api

**Domain:** Web Platforms › [[wiki/web-platforms/supercategories/frontend/index|Frontend]] › [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/index|Frontend Frameworks]] › Ajax

## Overview

Ajax (Asynchronous JavaScript and XML) is the technique of making asynchronous HTTP requests from a web page so that data can be fetched and rendered without a full page reload. Although the name references XML, modern practice sends and receives JSON. The pattern underpins single-page applications, which is why the page sits under Frontend › Frontend Frameworks › Ajax-Spa.

## Mechanics

Early implementations used the XMLHttpRequest object with callback handlers; the modern equivalent is the Fetch API, which returns promises and integrates cleanly with async/await. Either way the request runs in the background while the page stays interactive, and the response updates only the relevant part of the DOM. AbortController and timeout wrappers give callers control over long or failed requests.

## Patterns

Common Ajax patterns include loading indicators tied to in-flight requests, optimistic updates that apply changes before the server confirms them, and automatic retries with backoff for transient failures. Error handling distinguishes network failures from HTTP error statuses, and idempotency keys prevent duplicate side effects on retry. Caching headers and conditional requests (ETag, If-None-Match) reduce redundant payloads.

## In the SPA Context

In single-page applications, Ajax calls are typically centralized in an API client layer so that auth tokens, error normalization, and base URLs live in one place. State management updates from request results, and navigation happens client-side without reloads. The related entities in this branch — such as the fetch and request-warning records — capture the concrete cases sessions encountered.

## Related Entities

- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ace-10|Ace 10]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrains-10|Jetbrains 10]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/csv-10|Csv 10]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/web-platforms/supercategories/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
