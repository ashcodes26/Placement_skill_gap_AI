# Definition of Done

A feature is complete only when all applicable gates pass.

## Required gates

- [ ] Acceptance criteria in the GitHub Issue are satisfied.
- [ ] Implementation is committed on a feature/fix branch.
- [ ] Unit tests pass.
- [ ] Integration/API tests pass where applicable.
- [ ] Frontend build/type checks pass where applicable.
- [ ] ML evaluation/regression checks pass where applicable.
- [ ] Lint/format checks pass where configured.
- [ ] No secrets or credentials are committed.
- [ ] Pull request is reviewed.
- [ ] Pull request is merged into `main`.

## Verification status

Use these states:

- **NOT_STARTED** — no implementation evidence.
- **IN_PROGRESS** — implementation exists but verification is incomplete.
- **VERIFIED** — automated checks and acceptance criteria passed.
- **BLOCKED** — a required check failed or evidence is missing.

CI is responsible for automated verification. Human review is required for product behavior and acceptance criteria that cannot be reliably automated.
