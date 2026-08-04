---
type: "entity"
title: "NotImplementedError"
description: "An exception raised when a required method or feature is not implemented"
tags: ["entity", "exceptions", "python", "abstract", "errors"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

# NotImplementedError

## Summary

NotImplementedError is a Python exception raised when code reaches a method or feature that should exist but has not been implemented — the classic body of an abstract method in a base class. It matters because it turns missing implementations from silent wrong behavior into loud, localized failures. Raising it marks a contract: subclasses must provide the behavior.

## Details

- **Definition** — Raising NotImplementedError signals that a method has no usable implementation, typically in an abstract base or a stub.
- **Abstract methods** — Base classes raise it so subclasses that forget to implement fail at call time with a clear message.
- **Distinction** — It differs from NotImplemented, a special value used for operator dispatch, and from NotImplementedError in other languages' idioms.
- **Worked example** — A base Repository defines fetch as raising NotImplementedError; a new storage backend that omits fetch fails loudly in tests instead of returning wrong data.
- **Common failure modes** — Raising it from methods that should have real defaults, catching it broadly and swallowing the signal, and using it where a more specific error fits.
- **Practical relevance** — Interface enforcement without language-level abstract classes relies on this pattern; type checkers can also declare the contract.
- **Testing** — Tests can assert that unimplemented branches raise, documenting the contract and preventing accidental silent fallthrough.
- **Telemetry note** — Recorded among backend and tooling tags, consistent with scaffolding and plugin-development sessions.
- **Documentation** — The raised message should name the expected behavior and the subclass that must implement it, turning the error into documentation.
- **Alternatives** — Abstract base classes, protocols, and type stubs give static enforcement where the runtime exception is only a backstop.
- **Worked example** — A plugin system defines an interface; an unregistered plugin raises NotImplementedError with the plugin name, and the loader surfaces a clear configuration error.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/exception-2|Exception]] — the exception family
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/errorcode|ErrorCode]] — coding the failure
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/pycompileerror|PyCompileError]] — compile-time sibling
- [[wiki/testing/api-testing|API Testing]] — asserting contract failures
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/codegenengine-2|CodegenEngine]] — generating stub implementations
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/notimplementederror-2|NotImplementedError]] — the pattern itself
