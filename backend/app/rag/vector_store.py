import logging

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.rag.embedding_service import embedding_service

logger = logging.getLogger(__name__)


class VectorStore:
    """
    Handles storing and retrieving document chunks
    from ChromaDB.
    """

    def __init__(self):
        self.db = Chroma(
            collection_name="edu_rag",
            embedding_function=embedding_service.embedding_model,
            persist_directory="chroma_db",
        )

    def add_documents(
        self,
        documents: list[Document],
    ) -> None:

        if not documents:
            return

        document_id = documents[0].metadata.get("document_id")

        if document_id:
            self.db.delete(
                where={
                    "document_id": document_id
                }
            )

            logger.info(
                "Removed existing chunks for document %s",
                document_id,
            )

        self.db.add_documents(documents)

        logger.info(
            "Stored %s chunks in ChromaDB.",
            len(documents),
        )

    def search(
        self,
        query: str,
        limit: int = 4,
    ) -> list[tuple[Document, float]]:
        """Return the most relevant chunks and their relevance scores."""

        cleaned_query = query.strip()

        if not cleaned_query:
            raise ValueError(
                "Search query cannot be empty."
            )

        results = (
            self.db
            .similarity_search_with_relevance_scores(
                query=cleaned_query,
                k=limit,
            )
        )

        logger.info(
            "Retrieved %s chunks for query: %s",
            len(results),
            cleaned_query,
        )

        return results

vector_store = VectorStore()
