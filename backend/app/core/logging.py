import logging

from app.core.config import settings


def configure_logging() -> None:
    """Configure application-wide logging."""

    logging.basicConfig(
        level=getattr(logging, settings.log_level, logging.INFO),
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
    )