"""Application configuration loaded from environment variables with defaults."""
from functools import lru_cache
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Ignore unknown fields from .env
    )

    api_host: str = "0.0.0.0"
    api_port: int = 8000
    model_server_url: AnyHttpUrl = "http://localhost:9000"
    log_level: str = "INFO"
    
    # Security settings
    max_request_body_size: int = 1_000_000  # 1MB max request body
    model_timeout_seconds: float = 30.0  # Timeout for model server calls
    rate_limit_per_minute: int = 60  # Rate limit: 60 requests per minute per IP


@lru_cache
def get_settings() -> Settings:
    """
    Get the application's Settings object, cached for reuse across the process.
    
    Returns:
        settings (Settings): The cached Settings instance containing configuration
        values (e.g., api_host, api_port, model_server_url, log_level).
    """
    return Settings()
