# Implement Feature

Checklist for adding a new feature to Pulse v2. Follow in order; do not skip steps.

1. **Name the files first.** Before writing any code, list every file the feature touches using `<feature>_<layer>.py` (backend) or the component/type/api naming in `CLAUDE.md`. Confirm none of the forbidden catch-all filenames appear.
2. **Work bottom-up.**
   - `repositories/engines/*` (or extend the existing engine) — the data shape.
   - `repositories/<feature>_repository.py` — the abstract interface, if new.
   - `repositories/provider.py` — wire the engine, if the feature needs a new one.
   - `services/<feature>_service.py` — pure Python business logic, domain exceptions only.
   - `schemas/<feature>_schema.py` and `models/<feature>_model.py` — request/response and domain shapes.
   - `api/v1/routes/<feature>_routes.py` — the endpoint, translating domain exceptions to HTTP.
   - `api/v1/router.py` — mount the new route.
   - Frontend, if needed: `src/types/`, then `src/api/`, then `store/feed_store.ts` actions, then components — never the reverse.
3. **Add the test.** Backend: a `tests/` case proving the service logic and, if a new repository/engine was added, a test proving the swap in `provider.py` still returns identical results across engines. Frontend: no new business logic exists to test — if you find yourself testing browser-side logic, that logic is misplaced.
4. **Run the test.** Ask before running `pytest`/`npm test` if it hasn't been explicitly approved for this session; report the result.
5. **Stop.** Do not refactor neighboring files, do not add speculative options, do not start the next feature.
