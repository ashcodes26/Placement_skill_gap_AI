from fastapi import FastAPI

app = FastAPI(title="Placement Skill Gap AI API", version="1.0.0")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/api/health")
def api_health() -> dict[str, str]:
    return {"status": "ok"}
