# API Contract

The API uses `/api` as its base path. JSON is the default request/response format and multipart/form-data is used for file uploads.

Core endpoints:
- GET/POST /api/profile
- POST /api/job/analyze
- POST /api/skill-gap/analyze
- GET /api/roadmap/{student_id}
- POST /api/assessment/submit
- GET /api/dashboard/{student_id}
- POST /api/import/upload
- POST /api/import/preview
- POST /api/import/confirm
- GET /api/import/{job_id}
- GET /api/import/{job_id}/errors
- POST /api/import/{job_id}/retry

The master specification and implementation documents remain authoritative for detailed schemas.
