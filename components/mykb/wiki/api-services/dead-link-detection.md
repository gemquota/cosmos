---
type: "concept"
title: "Dead Link Detection"
description: "Finding external URLs that no longer respond"
tags: ["links", "detection", "maintenance", "references"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dead Link Detection

## Summary
Dead link detection fetches each external URL and classifies the response: live, moved, dead, or ambiguous (bot-blocked, timeout).

## Details
- Ambiguous responses matter — a 403 from a WAF is not a dead source, and a false positive wastes curation time.
- Detection is the sensing layer; link-rot monitoring is the ongoing process that schedules and reacts to it.
- For mykb, dead link detection results feed broken-link reports and the archive-url remediation queue.

## Related
- [[wiki/api-services/link-rot-monitoring|Link-Rot Monitoring]]
- [[wiki/api-protocols/http-status-checks|HTTP Status Checks]]
- [[wiki/dev-tools/broken-link-reports|Broken Link Reports]]
- [[wiki/api-protocols/archive-urls|Archive URLs]]
- [[wiki/api-services/source-monitoring|Source Monitoring]]
- [[wiki/api-protocols/url-formatting|URL Formatting]]
