# 0002 — Redux Pattern via Zustand

## Context

The frontend holds exactly one client-side store that caches server state
(feed, posts, users, trends) and re-renders subscribed components when that
state changes. The store must never become a second source of truth — the
backend is authoritative, and the store forwards its state to the UI.

## Options considered

- **Pub/sub observables (Angular-style)** — a service exposes observable
  streams; components subscribe and manually manage subscription lifecycles.
- **Redux Toolkit** — the canonical dispatch/reducer implementation, mature
  and widely adopted, with a larger API surface and more boilerplate.
- **Zustand, implementing the Redux pattern by hand** — dispatch-style actions
  produce a single reducer-shaped state update; components subscribe via a
  hook.

## Decision

Use a single Zustand store, structured internally as dispatch -> single
reducer-shaped update -> subscribed components re-render — the Redux pattern,
without pulling in Redux Toolkit.

Pub/sub observables are rejected: that model fits streams of continuous
events (Angular's typical use case) better than it fits a cache of discrete
server-fetched snapshots, and it pushes subscription lifecycle management
into every component, which is exactly the per-component bookkeeping we're
trying to avoid. A Redux-shaped single store, by contrast, matches "cache of
server state" cleanly: one action in, one predictable state shape out, no
per-component subscription teardown.

Zustand over Redux Toolkit: Zustand gives the same dispatch/reducer shape with
far less boilerplate (no providers, no slices ceremony) for a store this small
(four domains: feed, posts, users, trends). Zustand is MIT licensed, so there
is no licensing friction. Accepted risk: Zustand is a smaller, less
battle-tested project than Redux Toolkit and has a smaller maintainer base and
ecosystem of middleware/devtools — acceptable here because the store's shape
is simple and fully specified in this ADR set, so we are not depending on
Zustand's ecosystem for anything beyond the base store.

## Consequences

- All state mutations must go through dispatch-style actions in
  `store/feed_store.ts`; no component may call a Zustand `set` directly from
  outside the store module.
- Only one store exists — new domains (e.g. notifications) extend the same
  store's shape rather than creating a second store.
- If Zustand's maintenance risk materializes (abandonment, breaking API
  churn), the migration path is to Redux Toolkit, since the store already
  follows the same dispatch/reducer shape.
