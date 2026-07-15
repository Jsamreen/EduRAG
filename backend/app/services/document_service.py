import logging
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile, status

from app.core.config import settings

logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = {".pdf"}
ALLOWED_CONTENT_TYPES = {"application/pdf"}


class DocumentService:
    """Handle document validation and local file storage."""

    def __init__(self) -> None:
        self.upload_directory = settings.upload_directory
        self.upload_directory.mkdir(parents=True, exist_ok=True)

    async def save_pdf(self, file: UploadFile) -> dict[str, object]:
        """Validate and save an uploaded PDF document."""

        original_filename = file.filename or "unnamed.pdf"
        extension = Path(original_filename).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only PDF files are supported.",
            )

        if file.content_type not in ALLOWED_CONTENT_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The uploaded file must have the application/pdf content type.",
            )

        document_id = str(uuid4())
        stored_filename = f"{document_id}.pdf"
        destination = self.upload_directory / stored_filename

        size_bytes = 0

        try:
            with destination.open("wb") as output_file:
                while chunk := await file.read(1024 * 1024):
                    size_bytes += len(chunk)

                    if size_bytes > settings.max_file_size_bytes:
                        output_file.close()
                        destination.unlink(missing_ok=True)

                        raise HTTPException(
                            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                            detail=(
                                "File exceeds the maximum allowed size of "
                                f"{settings.max_file_size_mb} MB."
                            ),
                        )

                    output_file.write(chunk)

        except HTTPException:
            raise

        except OSError as exc:
            logger.exception(
                "Failed to save uploaded file: %s",
                original_filename,
            )

            destination.unlink(missing_ok=True)

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="The document could not be saved.",
            ) from exc

        finally:
            await file.close()

        logger.info(
            "Saved document '%s' as '%s' (%s bytes)",
            original_filename,
            stored_filename,
            size_bytes,
        )

        return {
            "document_id": document_id,
            "original_filename": original_filename,
            "stored_filename": stored_filename,
            "content_type": file.content_type or "application/pdf",
            "size_bytes": size_bytes,
            "status": "uploaded",
        }


document_service = DocumentService()