# Pulse v2

## North Star

Pulse is a single-page Twitter/X-style home feed. Python owns all business
logic — filtering, sorting, counting, validation, ID generation; the browser
only renders state handed to it by the store. This is a full rebuild of a v1
whose architecture was rejected in review (business logic leaked into the
frontend, storage was not swappable, files were untraceable to features). A
change is "done" when: it respects the layering contract below, the
architecture audit reports `VIOLATIONS: 0`, relevant tests pass, and no file
outside `v2/` was touched.

## Where files sit

```
v2/backend/
  main.py                  app factory, CORS, router mount. zero endpoints.
  core/config.py
  api/v1/router.py         aggregates feature routers
  api/v1/routes/           health_routes.py feed_routes.py post_routes.py
                           user_routes.py trend_routes.py
  schemas/                 post_schema.py user_schema.py trend_schema.py
  models/                  post_model.py user_model.py trend_model.py
  services/                feed_service.py post_service.py user_service.py
                           trend_service.py
  repositories/
    provider.py            ONLY file importing engines
    post_repository.py     abstract base
    user_repository.py
    trend_repository.py
    engines/memory/        memory_post_repository.py ...
    engines/jsonfile/      jsonfile_post_repository.py ...
    seed/                  post_seed.py user_seed.py trend_seed.py
  tests/
v2/frontend/src/
  api/                     client.ts feed_api.ts post_api.ts user_api.ts
                           trend_api.ts   (the only fetch() in the app)
  types/                   post.ts user.ts trend.ts
  store/feed_store.ts      one store, Redux pattern
  components/layout/       AppLayout LeftSidebar RightSidebar
  components/feed/         FeedColumn FeedTabs ComposeBox PostCard PostActions
  components/ui/           Avatar FollowButton IconButton
  styles/                  _tokens.scss _mixins.scss globals.scss
v2/docs/adr/
```

## API surface (`/api/v1`)

| Method | Path                    | Purpose                          |
|--------|-------------------------|-----------------------------------|
| GET    | /api/v1/health          | Liveness check                   |
| GET    | /api/v1/feed            | Ranked/ordered feed for home page |
| GET    | /api/v1/posts/{id}      | Fetch a single post              |
| POST   | /api/v1/posts           | Create a post                    |
| POST   | /api/v1/posts/{id}/like | Like/unlike a post                |
| POST   | /api/v1/posts/{id}/repost | Repost/unrepost a post         |
| GET    | /api/v1/users/{id}      | Fetch a user profile             |
| POST   | /api/v1/users/{id}/follow | Follow/unfollow a user         |
| GET    | /api/v1/trends          | Trending topics list             |

## Dev and test commands (human-run)

- `uvicorn backend.main:app --reload` — start the API (human-run; do not launch)
- `npm run dev` — start the frontend (human-run; do not launch)
- `pytest v2/backend/tests` — run backend tests (human-run; you may report the command, do not invoke without asking)
- `npm run build` — production static build (human-run)

## Definition of done

1. Files added/changed follow the tree above; no forbidden filenames introduced.
2. Layering respected: routes -> services -> repositories -> engines, no skips, no upward calls.
3. `/.claude/commands/review-architecture.md` audit run and ends `VIOLATIONS: 0`.
4. A test exists and passes for the changed behavior (repository swap, new endpoint, new service rule).
5. No new dependency added without asking first.
6. Still on the current feature branch; nothing pushed or merged.

## Cost discipline

- Prefer targeted reads (the exact file you need) over repo-wide exploration.
- Never open more than 6 files in one task without being explicitly told to.
- Do not re-read files you already have open in context.
- Stop when the current phase's goal is met — do not polish, refactor, or expand scope unasked.

## Invariants

- Colours, fonts, spacing, radii, breakpoints exist only in `_tokens.scss`.
- `fetch(` exists only under `src/api/`; components read the store, never `src/api/` directly.
- `from fastapi` never appears in `services/` or `repositories/`.
- Only `repositories/provider.py` imports a storage engine.
- Every backend path is under `/api/v1`; unversioned paths 404.
- No file named `models.py`, `schemas.py`, `routes.py`, `utils.py`, `helpers.py`, `common.py`, or `mock_data.py`.
- One Zustand store only, Redux pattern (dispatch -> reducer-shaped update -> subscribe).
- Raw `@media` only inside `_mixins.scss`; everywhere else uses `respond-to()`.
- Never merge to main, never checkout main, never push — human runs branch-moving git commands.
- `main.py` contains only the app factory, CORS, and router mount — zero endpoints.
