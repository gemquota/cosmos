---
type: "entity"
title: "ADC"
description: "BroadcastReceiver"
tags: ["entity", "acronym", "android", "api", "ast", "auth"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
status: "growing"
---

## Adc

BroadcastReceiver — an Android component for listening to system-wide broadcast messages. Receivers are registered either statically in the manifest or dynamically at runtime with registerReceiver().

When a broadcast arrives, onReceive() runs on the main thread and must return quickly; long-running work should be delegated to a service or a coroutine, or use goAsync() to keep the process alive while an asynchronous operation completes. Ordered broadcasts pass a result to each receiver in sequence, and abortBroadcast() can stop delivery to later receivers.

Modern Android restricts implicit broadcasts for background receivers to reduce battery and privacy abuse; manifest-registered receivers are allowed mainly for system broadcasts such as BOOT_COMPLETED and connectivity changes. A receiver exported without a permission can be triggered by any app, so developers should protect receivers with signature permissions or set exported="false" when the receiver is only used internally. Process-local alternatives such as LiveData or Flow avoid process-wide exposure entirely.

Receivers are commonly used to react to network state changes, package installation events, alarms, and messages from the system UI. Combined with the NotificationManager, they enable apps to update notifications or refresh content in the background. Because receiver lifetimes are short, careful registration in onStart() and onStop(), or the use of lifecycle-aware helpers, prevents leaks. These patterns appear throughout the [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] domain alongside other API concepts such as those catalogued under [[wiki/web-platforms/supercategories/api-services/categories/api-rest/index|Api Clients]].

Because broadcast handling is inherently asynchronous and system-driven, sessions emphasize logging the action received, guarding against null extras, and testing both the manifest-declared and runtime-registered paths.

Testing receivers typically means sending a broadcast in an instrumented test, asserting that the expected side effect occurred, and checking that receivers do not outlive the component that registered them.

**Domain:** Mobile Platform › [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] › [[wiki/web-platforms/supercategories/api-services/categories/api-rest/index|Api Clients › Adc

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
