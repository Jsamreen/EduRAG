import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application configuration loaded from environment variables."""

    app_name: str = os.getenv("APP_NAME", "EduRAG API")
    app_version: str = os.getenv("APP_VERSION", "0.1.0")
    app_env: str = os.getenv("APP_ENV", "development")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    api_prefix: str = os.getenv("API_PREFIX", "/api/v1")
    log_level: str = os.getenv("LOG_LEVEL", "INFO").upper()


settings = Settings()