from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[3] / ".env",
        env_file_encoding="utf-8",
    )

    MONGO_DB_URL: str
    MONGO_DB_NAME: str
    OPENAI_MODEL: str
    OPENAI_API_KEY: str
    OPENAI_MODELS: str = "gpt-4o-mini,gpt-4o"  # comma-separated list for a model picker; override in .env


settings = Settings()
