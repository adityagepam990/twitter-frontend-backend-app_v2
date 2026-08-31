# Frontend Structure

- Vanilla React 19 + Vite + TypeScript only. No Next.js, no SSR, no routing library.
- The frontend has zero business logic: no filtering, sorting, counting, validation, or ID generation in the browser. If a product rule lives here, move it to a backend service.
- Every `fetch()` call lives under `src/api/`. Nowhere else may call `fetch`.
- Components never import from `src/api/` directly. Components read the Zustand store only.
- Exactly one Zustand store, implemented in the Redux pattern: dispatch-style actions produce a single reducer-shaped update, subscribed components re-render from that.
- The store is a cache of server state. It is never a second source of truth — if the server disagrees, the server wins.
- One component per file, grouped under `components/layout/`, `components/feed/`, or `components/ui/` per the tree in `CLAUDE.md`.
- Types live under `src/types/`, one file per domain entity, never inlined ad hoc across components.
