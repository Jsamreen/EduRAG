from typing import Annotated

from fastapi import APIRouter, File, UploadFile, status

from app.services.document_service import document_service

from app.schemas.document import (
    DocumentExtractionResponse,
    DocumentUploadResponse,
)
from app.services.pdf_extraction_service import pdf_extraction_service

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

@router.post(
    "/{document_id}/extract",
    response_model=DocumentExtractionResponse,
)
def extract_document_text(
    document_id: str,
) -> DocumentExtractionResponse:
    """Extract page-level text from an uploaded PDF."""

    document_path = document_service.get_document_path(document_id)

    extraction = pdf_extraction_service.extract_text(document_path)

    return DocumentExtractionResponse(
        document_id=document_id,
        original_filename=document_path.name,
        total_pages=extraction["total_pages"],
        pages_with_text=extraction["pages_with_text"],
        total_characters=extraction["total_characters"],
        status="extracted",
        pages=extraction["pages"],
    )