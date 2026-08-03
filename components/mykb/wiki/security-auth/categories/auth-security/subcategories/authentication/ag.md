---
type: "entity"
title: "AG"
description: "Fragment"
tags: ["entity", "acronym", "api", "ast", "auth", "authentication"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---

## Ag

Fragment — a reusable portion of the Android UI within an Activity. Sessions show Fragment lifecycle and dynamic UI patterns.

A Fragment encapsulates a piece of UI and its behavior so that it can be combined with other fragments inside an Activity. Fragments have their own lifecycle, can be added, removed, and replaced at runtime, and allow a single screen to adapt across device sizes, such as showing a list and a detail pane side by side on tablets.

The Fragment lifecycle mirrors the Activity lifecycle, with callbacks from onAttach() and onCreate() through onStart() and onResume(), and back down through onPause(), onStop(), onDestroyView(), and onDetach(). Because the view can be destroyed and recreated while the Fragment survives, data should be held in the Fragment or its ViewModel, not in view references.

Fragment transactions are performed on the FragmentManager: a transaction adds, removes, replaces, or hides fragments, and can be added to the back stack so that the system back button reverses the change. Transitions and animations can be attached to the transaction for smooth navigation.

Fragments communicate with their host Activity and each other through shared ViewModels, callbacks, or the FragmentResult API, rather than holding direct references, which keeps them reusable and testable. The Fragment entry in the [[wiki/web-platforms/00-index|Auth Security]] domain accompanies other Android patterns recorded in sessions, where dynamic UI and lifecycle discipline recur across projects.

The entry records Fragment patterns as they appeared in sessions, including the common mistake of holding an Activity reference from a long-lived Fragment, which is avoided with scoped ViewModels.

Navigation components model destinations and arguments, which simplifies the same transactions the wiki records while keeping state restoration explicit.

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Security Auth]] › [[wiki/web-platforms/00-index|Auth Security]] › Ag

## Related Entities

- [[wiki/security-auth/categories/auth-security/subcategories/authentication/ab|Ab]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/automatic-10|Automatic 10]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/fov-2|Fov 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/selective-chaos|Selective Chaos]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/rubenverborgh|Rubenverborgh]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/sim-speed|Sim Speed]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/missing-content|Missing Content]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/searchtext|Searchtext]]
