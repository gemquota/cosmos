---
type: "concept"
title: "File Upload UIs"
description: "Uploading files well: drag-drop, progress, validation, previews, and resumability"
tags: ["file-upload", "forms", "ux", "progress", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/File_API", "https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/progress_event"]
---
# File Upload UIs

## Summary
File upload UX spans selection (input, drag-and-drop), validation, progress, previews, and failure handling. Native `<input type="file">` gives the picker; drag-and-drop and progress bars need APIs. Large uploads benefit from chunking and resumability.

## Details
- **Selection** — accept, multiple, and capture attributes; drag-and-drop layers FileList handling on top.
- **Validation** — client-side checks (type, size, count) before upload; server re-validates everything.
- **Progress** — XHR progress events or fetch streams report percentages; paused/resume needs chunked uploads.
- **Previews** — object URLs preview images/video before upload; revoke them to avoid leaks.
- **Worked example** — the mykb wiki importer accepts markdown drops, validates size, shows per-file progress, and retries failed chunks.
- **Relevance** — uploads are a common surface in RSIS3's acquisition tools, so the pattern belongs in the UI library.
- **Security layers** — files are untrusted input: cap size, validate type and magic bytes, scan for malware, store outside executable paths, and serve from a sandboxed origin.

## Related
- [[wiki/api-protocols/file-upload-security|File Upload Security]] — adjacent concept in this wiki
- [[wiki/api-protocols/zip-slip|Zip Slip]] — adjacent concept in this wiki
- [[wiki/web-platforms/stored-xss|Stored XSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/path-normalization|Path Normalization]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — existing coverage
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
