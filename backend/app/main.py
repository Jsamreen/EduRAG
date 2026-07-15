import logging

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    description="AI-powered university knowledge assistant using RAG",
    version=settings.app_version,
    debug=settings.debug,
)

app.include_router(
    api_router,
    prefix=settings.api_prefix,
)


@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    """Return basic application information."""

    return {
        "message": "Welcome to EduRAG API",
        "environment": settings.app_env,
        "documentation": "/docs",
    }


@app.on_event("startup")
def startup_event() -> None:
    logger.info(
        "%s version %s started in %s mode",
        settings.app_name,
        settings.app_version,
        settings.app_env,
    )