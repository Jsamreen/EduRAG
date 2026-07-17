from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class TextChunker:
    """Split extracted PDF text into LangChain Documents."""

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

    def split_pages(
        self,
        document_id: str,
        document_name: str,
        pages: list[dict],
    ) -> list[Document]:
        documents = []

        for page in pages:
            if not page["text"].strip():
                continue

            chunks = self.text_splitter.create_documents(
                texts=[page["text"]],
                metadatas=[
                    {
                        "document_id": document_id,
                        "document_name": document_name,
                        "page": page["page_number"],
                    }
                ],
            )

            documents.extend(chunks)

        return documents


text_chunker = TextChunker()