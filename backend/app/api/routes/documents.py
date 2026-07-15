from typing import Annotated

from fastapi import APIRouter, File, UploadFile, status

from app.schemas.document import DocumentUploadResponse
from app.services.document_service import document_service

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    file: Annotated[UploadFile, File(description="University PDF document")],
) -> DocumentUploadResponse:
    """Upload and store a university PDF document."""

    result = await document_service.save_pdf(file)

    return DocumentUploadResponse(**result)