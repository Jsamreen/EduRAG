from pydantic import BaseModel, Field


class ExtractedPage(BaseModel):
    """Text extracted from one page of a PDF."""

    page_number: int = Field(
        ...,
        description="Human-readable page number starting from 1",
    )
    text: str
    character_count: int


class DocumentUploadResponse(BaseModel):
    """Response returned after a successful document upload."""

    document_id: str
    original_filename: str
    stored_filename: str
    content_type: str
    size_bytes: int
    status: str


class DocumentExtractionResponse(BaseModel):
    """Response returned after extracting text from a PDF."""

    document_id: str
    original_filename: str
    total_pages: int
    pages_with_text: int
    total_characters: int
    status: str
    pages: list[ExtractedPage]