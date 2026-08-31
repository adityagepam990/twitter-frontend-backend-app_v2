# Verification — 27 Aug architecture review

Evidence that each point raised in the 27 Aug review of the v1 architecture,
and each invariant it produced in `v2/CLAUDE.md`, is addressed in v2. The grep
commands below are the exact checks in `.claude/commands/review-architecture.md`,
re-run on 2026-08-31 with a result of `VIOLATIONS: 0`.

| Review point | Evidence |
|---|---|
| Business logic leaked into the frontend (v1 rejection reason) | `backend/services/feed_service.py:11` owns tab filtering/ranking (`get_feed(tab)`). `grep -rn "\.sort(\|\.filter(\|Math\.random\|crypto\.randomUUID" v2/frontend/src` returns one hit, `components/ui/Avatar.tsx:12`, which strips blank tokens while deriving initials from a display name for rendering — presentation only, not a product rule (no counting, ordering, or ID-generation logic in the frontend). |
| Storage was not swappable (v1 rejection reason) | `backend/repositories/provider.py` is the single file that imports `engines.*` and switches on `settings.ENGINE` (`memory` \| `jsonfile`); proven by `backend/tests/test_storage_swap.py::test_only_provider_imports_storage_engines` (AST-walks every `.py` file, asserts none but `provider.py` imports `repositories.engines`) and the cross-engine contract tests `test_post_repository_contract_matches_across_engines`, `test_user_repository_contract_matches_across_engines`, `test_trend_repository_contract_matches_across_engines`. |
| Files were untraceable to features (v1 rejection reason) | One-feature-per-file naming (`<feature>_<layer>.py`) per `backend/api/v1/routes/`, `backend/services/`, `backend/repositories/`, `backend/schemas/`, `backend/models/`; mirrored on the frontend by `components/feed/`, `components/layout/`, `components/ui/` — matches the tree in `v2/CLAUDE.md`. |
| Hex colours only in `_tokens.scss` | `grep -rniE "#[0-9a-f]{3,8}\b" v2/frontend/src --include=*.scss --include=*.tsx --include=*.ts \| grep -v "_tokens.scss"` → clean. All 9 hex literals live in `frontend/src/styles/_tokens.scss:4-16`. |
| `fetch()` only under `src/api/` | `grep -rn "fetch(" v2/frontend/src --include=*.ts --include=*.tsx \| grep -v "src/api/"` → clean. Sole call site: `frontend/src/api/client.ts:21`. |
| `fastapi` never imported in `services/` or `repositories/` | `grep -rn "from fastapi\|import fastapi" v2/backend/services v2/backend/repositories` → clean. |
| `main.py` holds zero endpoint decorators | `grep -n "@app\.\|@router\." v2/backend/main.py` → clean. `backend/main.py` contains only `create_app()`, CORS setup, and `app.include_router(api_v1_router)`. |
| Only `provider.py` imports a storage engine | `grep -rln "engines\." v2/backend/repositories \| grep -v "provider.py"` → clean. Enforced further by `test_only_provider_imports_storage_engines`. |
| No forbidden catch-all filenames | `find v2 -type f \( -name "models.py" -o -name "schemas.py" -o -name "routes.py" -o -name "utils.py" -o -name "helpers.py" -o -name "common.py" -o -name "mock_data.py" \)` → no matches. |
| Raw `@media` only inside `_mixins.scss` | `grep -rn "@media" v2/frontend/src --include=*.scss \| grep -v "_mixins.scss"` → clean. The 3 raw `@media` blocks live in `frontend/src/styles/_mixins.scss:6,10,14`, wrapped by `respond-to()`. |
| No inline `style={{` in `.tsx` | `grep -rn "style={{" v2/frontend/src --include=*.tsx` → clean. |
| Every backend path under `/api/v1`; unversioned paths 404 | `grep -rn "@router\.\(get\|post\|put\|delete\|patch\)(" v2/backend/api \| grep -v "/api/v1"` → clean (prefix moved from the aggregating `APIRouter(prefix=...)` in `api/v1/router.py` onto each route decorator, e.g. `api/v1/routes/health_routes.py:6`, so the literal path string carries the version). Runtime behaviour proven by `backend/tests/test_health_routes.py::test_unversioned_health_is_404` and `::test_unversioned_feed_is_404`. |
| One Zustand store, Redux pattern | Single store file `frontend/src/store/feed_store.ts`; `find v2/frontend/src -iname "*store*"` returns only that file. |
| Layering: routes -> services -> repositories -> engines, no skips | Route files (`api/v1/routes/*.py`) import only from `services/*`; `services/*.py` import only from `repositories/*` (abstract interfaces) plus `models/*`; only `repositories/provider.py` reaches into `repositories/engines/*` — confirmed by the "fastapi never in services/repositories" and "only provider.py imports engines" checks above, which would fail if a layer were skipped. |

## Audit result

All 9 `/review-architecture` checks re-run clean on 2026-08-31:

```
VIOLATIONS: 0
```

## Test run

```
$ pytest v2/backend/tests
......................                                                   [100%]
22 passed, 1 warning in 0.86s
```

## Production build

```
$ npm run build
dist/index.html                   0.39 kB │ gzip:  0.26 kB
dist/assets/index-ClZc3_7n.css     7.48 kB │ gzip:  1.95 kB
dist/assets/index-eKV9AiXo.js    214.34 kB │ gzip: 66.91 kB
built in 4.05s
```
