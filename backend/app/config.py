from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Placement Skill Gap AI"
    database_url: str = "sqlite:///./placement_skill_gap.db"
    ai_api_key: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
