# Backend Structure

- Layering is strict: routes -> services -> repositories -> engines. A layer calls only the layer directly beneath it, never skips, never calls upward.
- Services are pure Python. Never import `fastapi` inside `services/` or `repositories/`.
- Services raise domain exceptions. Routes translate exceptions to HTTP responses.
- Only `repositories/provider.py` may import a storage engine. Every other file talks to an abstract repository interface.
- Swapping the storage engine (memory -> jsonfile -> postgres) must be a one-file change in `provider.py`, proven by a test.
- Every endpoint path starts with `/api/v1`. A route without that prefix is a bug.
- `main.py` holds only the app factory, CORS setup, and router mounting. No `@app.` route decorators there.
- One feature per file, named `<feature>_<layer>.py` (e.g. `post_service.py`, `user_repository.py`).
- Never create a file named `models.py`, `schemas.py`, `routes.py`, `utils.py`, `helpers.py`, `common.py`, or `mock_data.py`.
- Seed data lives under `repositories/seed/`, one file per feature, never inline in a repository or service.
