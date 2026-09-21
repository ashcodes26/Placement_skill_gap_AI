# Placement Skill Gap AI — Project Structure

## Repository structure

```
Placement_skill_gap_AI/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── feature-verification.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   └── tests/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── features/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── lib/
│   └── tests/
├── ml/
│   ├── preprocessing/
│   ├── skill_extraction/
│   ├── gap_analysis/
│   ├── recommendation/
│   ├── evaluation/
│   └── tests/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── docs/
│   ├── PROJECT_STRUCTURE.md
│   ├── DEFINITION_OF_DONE.md
│   ├── ARCHITECTURE.md
│   └── API.md
├── tests/
│   └── e2e/
├── scripts/
├── .env.example
├── docker-compose.yml
└── README.md
```

## Architectural boundaries

- **frontend**: UI and client-side state only.
- **backend**: authentication, API, persistence, orchestration and business rules.
- **ml**: model/data-processing logic; expose stable service interfaces to the backend.
- **data**: development/sample datasets only; never commit secrets or private user data.
- **tests**: end-to-end tests spanning the running application.

## Feature flow

```
User
  → Frontend
  → Backend API
  → ML services
  → Database / external sources
  → Backend response
  → Frontend
```

Every production feature should have an issue, implementation branch, tests, PR, and CI verification.
