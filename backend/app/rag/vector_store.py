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

        self.db.add_documents(documents)

        logger.info(
            "Stored %s chunks in ChromaDB.",
            len(documents),
        )


vector_store = VectorStore()