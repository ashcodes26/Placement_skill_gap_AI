# Placement Skill Gap AI

AI-powered platform for identifying placement skill gaps and generating evidence-based learning plans.

## Development model

This repository uses an issue → branch → pull request → CI verification → merge workflow.

### Feature completion rule

A feature is **Done** only when:

1. The implementation is complete.
2. Automated tests covering the feature pass.
3. Build/type/lint checks pass where applicable.
4. Integration/API checks pass where applicable.
5. The pull request is reviewed and merged.
6. The corresponding GitHub Issue acceptance criteria are satisfied.

A card should not be moved to **Done** merely because code was written.

## Recommended project workflow

Backlog → Todo → In Progress → Review → Testing → Done

Use GitHub Issues for individual work items and GitHub Projects for planning and status tracking.

## Branch convention

- `main` — stable, reviewed code
- `feature/<short-name>` — new features
- `fix/<short-name>` — bug fixes
- `chore/<short-name>` — maintenance

## Pull request rule

Every PR should reference its issue (for example: `Closes #12`) and describe:
- What changed
- How it was tested
- Any known limitations

## Quality gate

CI should be the source of truth for automated verification. Human review remains required for product behavior, UX, security-sensitive changes, and acceptance criteria that cannot be reliably tested automatically.
