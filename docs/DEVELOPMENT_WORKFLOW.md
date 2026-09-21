# Development and Feature Verification Workflow

## 1. Issue creation

Every meaningful feature starts as a GitHub Issue with:
- goal
- scope
- acceptance criteria
- automated verification plan

## 2. Implementation

Create a branch from `main`:

```
feature/<short-name>
```

Implement the feature and add tests at the same time.

## 3. Pull request

Open a PR and link it to the issue.

The PR must explain what changed and how it was verified.

## 4. Automated verification

GitHub Actions should run the repository's applicable checks, such as:
- dependency installation
- linting
- type checking
- unit tests
- integration/API tests
- end-to-end tests
- production build

The exact commands should be defined once the application stack is established.

## 5. Completion signal

A feature is considered technically verified only when all required CI checks pass.

A feature is considered complete only after:
- CI passes
- acceptance criteria are satisfied
- required review is complete
- the PR is merged

## 6. Project tracking

Use GitHub Projects to show the lifecycle:

**Backlog → Todo → In Progress → Review → Testing → Done**

The Project is the management layer. The repository contains the implementation, tests, and CI configuration.

## 7. AI-assisted development

AI-generated code must follow the same verification process as human-written code. Generated code is not evidence of completion; passing tests and satisfied acceptance criteria are.
