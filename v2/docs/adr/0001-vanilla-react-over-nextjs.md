# 0001 — Vanilla React over Next.js

## Context

Pulse v2 is a single-page home feed where Python owns all business logic and
the browser is a thin renderer of server state. We need a frontend framework
choice for a static, client-rendered UI backed entirely by a FastAPI service.

## Options considered

- **Next.js** — React framework with SSR/SSG, file-based routing, API routes,
  and its own build/deploy model.
- **Vanilla React 19 + Vite + TypeScript** — a client-only SPA, built to
  static assets, with no server-rendering runtime.

## Decision

Use vanilla React 19 with Vite and TypeScript, built to static output hostable
from any web server. Reject Next.js.

Next.js is rejected because it is a heavier container than this app needs and
because it makes you pay for server-side rendering you do not use. Pulse has
exactly one page and no SEO requirement; there is no content that benefits
from being rendered on a server. Next.js would add a Node runtime dependency
for hosting (or lock-in to a specific host's edge/serverless model), a
file-based router we don't need since the app has one route, and an API-routes
layer that would tempt business logic back into JavaScript — the exact
architecture violation this rebuild exists to fix. A Vite-built SPA has none
of that: static files, one entry point, and no server process required to
serve the frontend.

## Consequences

- The frontend must be served as static files; there is no server-side
  render step to fall back on for initial paint — first paint waits on the
  JS bundle and the initial `/api/v1/feed` fetch.
- No built-in routing is available or needed; the app intentionally has no
  router.
- Any future requirement for SEO or server-rendered marketing pages would need
  a separate tool, not a retrofit of this app.
