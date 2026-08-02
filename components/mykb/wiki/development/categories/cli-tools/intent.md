---
type: "entity"
title: "Intent"

status: "growing"
---


## Intent

Android messaging object for component-to-component communication. Sessions show Intent patterns for starting activities, services, and passing data between components.

An Intent is a passive data structure describing an operation to be performed: it names the component to start, carries extras with the data to pass, and may include flags that change how the target is launched. Explicit intents name a component directly, while implicit intents declare an action and data URI and let the system resolve a matching component through intent filters.

Activities are started with startActivity() or startActivityForResult(), services with startService() or bindService(), and broadcasts are delivered with sendBroadcast() or sendOrderedBroadcast(). Extras travel with the Intent as key-value pairs inside a Bundle, so complex payloads can be passed between components without global state.

Implicit intents enable deep linking: an app can declare intent filters for actions such as VIEW or SEND, and the system presents matching apps to the user. PendingIntents wrap an Intent with a permission grant so that other applications can perform the action on the app's behalf later, which is how notifications and alarms launch tasks. Security considerations include restricting exported components, validating data from implicit intents, and avoiding the leakage of sensitive extras to other apps.

Because intents decouple components, they are central to Android navigation, widget updates, and inter-app communication. The patterns recorded in the [[wiki/web-platforms/index|Cli Tools]] domain show intent distribution and orchestration recurring in agent sessions, from simple activity launches to complex multi-component workflows.

**Related technologies:** cli, ide, queue, terminal

Sessions also record intent-related debugging: logging the action and extras, checking the manifest for missing filters, and verifying that the target package exists before dispatch.

**Domain:** Development Tools › [[wiki/web-platforms/index|Development]] › [[wiki/web-platforms/index|Cli Tools]]

## Related Entities

- [[wiki/development/categories/cli-tools/agentic-context-engineering|Agentic Context Engineering]]
- [[wiki/development/categories/cli-tools/cognitive|Cognitive]]
- [[wiki/development/categories/cli-tools/dev|Dev]]
- [[wiki/development/categories/cli-tools/intent-distribution|Intent Distribution]]
- [[wiki/development/categories/cli-tools/performance|Performance]]
- [[wiki/development/categories/cli-tools/reality|Reality]]
- [[wiki/development/categories/cli-tools/senior-dev|Senior Dev]]
- [[wiki/development/categories/cli-tools/sovereign-orchestrator|Sovereign Orchestrator]]
