---
type: "entity"
title: "AAR"
description: "AAR"
tags: ["entity", "acronym", "android", "angular", "api", "ast"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---


## Aar

AAR appears in 1 session(s) categorized as API, Frontend, Mobile. Related topics: acronym, android, angular, api.

**Domain:** Mobile Platform › [[wiki/web-platforms/00-index|Android Core]] › [[wiki/web-platforms/00-index|Api Clients › Aar

## What AAR Means

The most common technical referent for AAR is the **Android Archive**: a binary distribution format that bundles an Android library module into a single file consumable by Gradle builds. Unlike an APK, an AAR is not installable; it packages compiled classes, Android resources, a merged `AndroidManifest.xml`, native libraries, and metadata such as `R.txt` and ProGuard rules for the consuming app.

Typical contents of an AAR:

- `classes.jar` — compiled Java or Kotlin bytecode of the library.
- `res/` — resources that get merged into the app's resource table at build time.
- `AndroidManifest.xml` — library manifest declaring components and permissions.
- `lib/` — native `.so` libraries for supported ABIs.
- `R.txt` — the resource IDs the library exposes, used by the consumer.

Gradle consumes AARs through project dependencies or from repositories such as Maven Central, and release AARs are usually processed with R8/ProGuard before publication. The acronym also surfaces in web contexts — for example alongside Angular and generic API client code — so this page keeps all three readings: the Android packaging format, an Angular-related abbreviation, and a generic API term. The tags and session evidence constrain which reading applies in a given note.

## AAR in the Knowledge Base

The page carries the tags acronym, android, angular, api, and ast because the term appeared in sessions spanning mobile, web, and service layers. When a session mentions an AAR, the surrounding evidence — a Gradle task, a dependency block, or an API client import — usually identifies which reading applies; ambiguous mentions stay linked to their transcripts until the referent is confirmed.

## Related Notes

- [[wiki/shell-environment/gradle-builds|Gradle Builds]] — how AAR dependencies are resolved and packaged
- [[wiki/shell-environment/apk-analysis|APK Analysis]] — inspecting the installable counterpart of an AAR

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acs|Acs

