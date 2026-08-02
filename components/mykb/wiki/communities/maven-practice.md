---
type: "concept"
title: "Maven Practice"
description: "The declarative JVM build tool built around the standard directory layout"
tags: ["maven", "builds", "jvm", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Maven Practice

## Summary
Maven builds JVM projects from a declarative pom.xml: standard lifecycle phases, plugins, and dependency resolution from repositories. Its convention-over-configuration makes projects predictable, at the cost of flexibility.

## Details
- Lifecycle phases (validate, compile, test, package, deploy) standardize the build story.
- Dependency mediation and plugin versions are the classic pain points — pin both.
- Maven Central is the reference repository; mirrors and checksums harden resolution.
- mykb relevance: the wiki Java services build with Maven and pinned plugin versions.

## Related
- [[wiki/communities/gradle-practice|Gradle Practice]]
- [[wiki/dev-tools/build-systems|Build Systems]]
- [[wiki/dev-tools/dependency-management|Dependency Management]]
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
