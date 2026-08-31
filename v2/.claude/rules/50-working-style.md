# Working Style

- Do not perform unrequested refactors. Fix or build what was asked, nothing adjacent.
- Do not add a new dependency (npm or pip) without asking the human first.
- Do not build speculative abstractions for hypothetical future needs. Solve the problem in front of you.
- Stop at the phase boundary. When the requested change is complete and tested, stop — do not continue polishing, expanding scope, or starting the next feature unasked.
- Prefer the smallest diff that satisfies the architecture contract in `CLAUDE.md`.
- If a requested change would violate the architecture contract, say so and propose a compliant alternative instead of silently working around it.
