from pydantic import BaseModel


class DocumentUploadResponse(BaseModel):
    """Response returned after a successful document upload."""

    document_id: str
    original_filename: str
    stored_filename: str
    content_type: str
    size_bytes: int
    status: str