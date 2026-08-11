import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

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


# ----------------------------------------------
# CORS
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------
# API Routes
# ---------------------------------------------------------

app.include_router(
    api_router,
    prefix=settings.api_prefix,
)


# --------------------------------------------------
# Startup
# ---------------------------------------------------------

@app.on_event("startup")
def startup_event() -> None:
    logger.info(
        "%s version %s started in %s mode",
        settings.app_name,
        settings.app_version,
        settings.app_env,
    )


# ---------------------------------------------------------
# React Frontend

frontend_directory = Path("/app/frontend_dist")

if frontend_directory.exists():
    app.mount(
        "/",
        StaticFiles(
            directory=frontend_directory,
            html=True,
        ),
        name="frontend",
    )