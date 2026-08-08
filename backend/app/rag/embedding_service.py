import logging

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

logger = logging.getLogger(__name__)


class EmbeddingService:
    """
    Generates embeddings for document chunks.
    """

    def __init__(self):
        self.model_name = "sentence-transformers/all-MiniLM-L6-v2"

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            },
        )

    def embed_chunks(
        self,
        chunks: list[Document],
    ) -> list[list[float]]:

        if not chunks:
            return []

        texts = [chunk.page_content for chunk in chunks]

        embeddings = self.embedding_model.embed_documents(texts)

        logger.info(
            "Generated %s embeddings.",
            len(embeddings),
        )

        return embeddings


embedding_service = EmbeddingService()