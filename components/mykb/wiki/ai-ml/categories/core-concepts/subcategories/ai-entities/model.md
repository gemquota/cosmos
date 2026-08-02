---
type: "entity"
title: "Model"
description: "ViewModel"
tags: ["entity", "api", "ast", "bash", "deployment", "documentation"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---

## Model

ViewModel — an Android architecture component for storing and managing UI-related data across configuration changes. It survives configuration changes such as screen rotation, so the state it holds is not recreated when the Activity or Fragment is recreated.

In the MVVM pattern the ViewModel sits between the View and the data layer. It exposes state through observable holders such as LiveData or StateFlow, and receives UI events from the View, translating them into calls on repositories or use cases. Because it outlives the view, asynchronous work such as network requests and database reads can continue across configuration changes without being cancelled.

A ViewModel's lifetime is scoped to its ViewModelStoreOwner. The owner's ViewModelStore retains instances across recreation and calls onCleared() when the owner is permanently destroyed, which releases resources and cancels work launched in viewModelScope. Best practice is to avoid holding references to Views, Activities, or Fragments inside a ViewModel, since those references can outlive the view and cause memory leaks; state should be exposed as observables and collected by the UI layer.

The saved state module (SavedStateHandle) persists a small amount of state across process death, complementing the in-memory store. Testing a ViewModel is straightforward because it is a plain class: unit tests can construct it directly and verify state transitions without an emulator. Navigation libraries give each destination its own ViewModel scope, and multi-module applications commonly define ViewModels per feature. Together these patterns make ViewModel a core building block of maintainable Android applications, and they appear throughout the [[wiki/web-platforms/index|Android Core]] and [[wiki/web-platforms/index|Api Rest]] domains.

Related patterns such as data binding, lifecycle observers, and repository layering reinforce the same separation of concerns, and code review checklists in the wiki's entity pages routinely call out ViewModel misuse as a common source of leaks and recomposition bugs.

**Domain:** Web Platforms › [[wiki/web-platforms/index|Api Services]] › [[wiki/web-platforms/index|Api Rest]] › Model

## Related Entities

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/aborted|Aborted]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/aegis|Aegis]]
- [[wiki/agent-systems/categories/agents/subcategories/agent-core/agent-active|Agent Active]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/ambiguity-projection-2|Ambiguity Projection 2]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/ambiguity-system|Ambiguity System]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/ambiguity|Ambiguity]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/ap|Ap]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/apex|Apex]]
