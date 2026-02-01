from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    DB_URL: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()