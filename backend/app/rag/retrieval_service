from app.rag.vector_store import vector_store


class RetrievalService:
    """Retrieve the most relevant chunks from ChromaDB."""

    def search(self, query: str, limit: int = 4):
        return vector_store.search(
            query=query,
            limit=limit,
        )


retrieval_service = RetrievalService()