# Architecture

## Core modules

### Frontend
Responsible for user experience, dashboard views, forms, client-side validation and API consumption.

### Backend
Responsible for authentication, user/profile data, placement/job data, API contracts, orchestration and persistence.

### ML
Responsible for resume/skill extraction, skill normalization, skill-gap computation, recommendation ranking and model evaluation.

### Data
Contains synthetic/sample data used for development and testing. Production/private data must remain outside the repository.

## AI Skill-Gap pipeline

```
Resume / Profile
      ↓
Document parsing
      ↓
Skill extraction
      ↓
Skill normalization
      ↓
Target-role requirements
      ↓
Skill-gap computation
      ↓
Gap prioritization
      ↓
Learning recommendations
      ↓
Personalized roadmap
```

Each stage should have deterministic tests and clear input/output contracts.
