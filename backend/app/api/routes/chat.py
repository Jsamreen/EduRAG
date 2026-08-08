import logging

from fastapi import APIRouter, HTTPException, status

from app.rag.retrieval_service import retrieval_service

from app.schemas.chat import (
    SearchRequest,
    SearchResponse,
    SearchResult,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post(
    "/search",
    response_model=SearchResponse,
)
def search_documents(
    request: SearchRequest,
) -> SearchResponse:
    """Retrieve relevant document chunks from ChromaDB."""

    try:
        matches = retrieval_service.search(
            query=request.query,
            limit=request.limit,
        )

        results = [
            SearchResult(
                page=document.metadata.get("page", 0),
                score=round(score, 4),
                text=document.page_content,
                document_id=document.metadata.get("document_id", ""),
                document_name=document.metadata.get("document_name", ""),
            )
            for document, score in matches
        ]

        logger.info(
            "Returned %s search results for query: %s",
            len(results),
            request.query,
        )

        return SearchResponse(
            query=request.query,
            results=results,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc