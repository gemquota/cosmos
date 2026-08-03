---
type: "concept"
title: "Insecure Deserialization"
description: "Attacker-controlled serialized data that triggers code execution on load"
tags: ["security", "deserialization", "attacks", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Insecure Deserialization

## Summary
Insecure deserialization happens when an application rebuilds objects from attacker-controlled serialized data, and the deserialization process itself — not the resulting object — executes dangerous code. Java, PHP, Python, and .NET all have real-world gadget-chain exploits.

## Details
Serialization converts objects to bytes (Java ObjectInputStream, PHP unserialize, Python pickle, .NET BinaryFormatter); deserialization rebuilds them. Many formats invoke code during reconstruction: custom readObject methods, __wakeup/__destruct hooks, reduce functions, and property setters. An attacker who can supply the byte stream can chain these hooks — gadget chains — into arbitrary code execution, file writes, or SSRF, even when the final object type looks harmless.

The mechanism: the danger is polymorphic deserialization. A library reads the stream's declared class and constructs it, running its lifecycle hooks with attacker-controlled fields. Classic chains (Java Commons Collections, PHP Laravel RCE, Python pickle's __reduce__) compose small "gadget" classes into a full exploit. JSON is not immune either when libraries support magic fields (JSON.net TypeNameHandling, Java polymorphic Jackson) that let the payload name the class to instantiate.

Concrete example: an API accepts a Java-serialized session object in a cookie. The server deserializes it with ObjectInputStream to restore the session. An attacker crafts a stream whose first object is a gadget chain that, when deserialized, executes Runtime.exec to download and run a shell — a single HTTP request becomes remote code execution. The fix is not validating the resulting object but refusing to deserialize untrusted streams at all.

Failure modes: allowlists of safe classes that are incomplete (the gadget classes are rarely the ones listed); libraries that enable polymorphic typing by default; signed cookies with a static secret (signature forgery via leaked key); and nested deserialization inside file uploads, cache keys, or queue messages. Even "safe" formats become unsafe when the application wires attacker input into a deserializer.

Operational tradeoffs: the durable fix is to stop deserializing untrusted data: use JSON with plain data classes (no polymorphic typing), or a signed and encrypted container when opaque state is required. Where native deserialization is unavoidable, sandbox the process, use strict class allowlists, and treat the format as hostile input. Detection focuses on logs of unusual deserialization class names and unexpected subprocess activity.

RSIS3/mykb relevance: the wiki's ingestion tooling should never unpickle or ObjectInputStream-unserialize untrusted artifacts; documenting the no-native-deserialization rule gives RSIS3's checks a hard line to enforce.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/file-upload-security|File Upload Security]] — related coverage in the same cluster
- [[wiki/api-protocols/zip-slip|Zip Slip]] — related coverage in the same cluster
- [[wiki/api-protocols/cache-poisoning|Cache Poisoning]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
