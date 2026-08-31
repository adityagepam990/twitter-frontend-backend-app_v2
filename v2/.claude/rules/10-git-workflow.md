# Git Workflow

- Work only on the current feature branch. Never check out `main`.
- Never run `git merge`, `git push`, or anything that moves or publishes a branch.
- The human runs every git command that changes branches, merges, or pushes.
- You may run read-only git commands (`git status`, `git diff`, `git log`) freely.
- If asked to "ship" or "merge" this work, stop and tell the human to run the git commands themselves.
- Never amend or rewrite commits that are not clearly part of the current uncommitted work.
- Never use `--no-verify`, `--force`, or any flag that skips a safety check.
